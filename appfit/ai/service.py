from fastapi import FastAPI
from pydantic import BaseModel
import os
from .meal_rules import default_week_plan, default_coach_tips

app = FastAPI(title="AppFit AI")


class PlanRequest(BaseModel):
    profile: dict


class CoachRequest(BaseModel):
    context: dict


@app.post("/ai/plan")
def plan(req: PlanRequest):
    return default_week_plan()


@app.post("/ai/coach")
def coach(req: CoachRequest):
    return {"tips": default_coach_tips()}
