from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from time import time
from typing import Dict

from .routers import auth, users, measurements, planner

app = FastAPI(title="AppFit")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# rate limit simples por IP
_RATE_LIMIT: Dict[str, float] = {}
_LIMIT_WINDOW = 1.0
_LIMIT_COUNT = 60

@app.middleware("http")
async def rate_limit(request: Request, call_next):
    ip = request.client.host if request.client else "anon"
    window = int(time() / _LIMIT_WINDOW)
    key = f"{ip}:{window}"
    count = _RATE_LIMIT.get(key, 0) + 1
    _RATE_LIMIT[key] = count
    if count > _LIMIT_COUNT:
        return Response("Too Many Requests", status_code=429)
    return await call_next(request)

app.include_router(auth.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1")
app.include_router(measurements.router, prefix="/api/v1")
app.include_router(planner.router, prefix="/api/v1")

@app.get("/healthz")
def healthz():
    return {"status": "ok"}
