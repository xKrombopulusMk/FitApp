import os
import httpx

import os
import httpx

CLIENT_ID = os.getenv("STRAVA_CLIENT_ID", "")
CLIENT_SECRET = os.getenv("STRAVA_CLIENT_SECRET", "")
REDIRECT_URI = os.getenv("STRAVA_REDIRECT_URI", "")


def get_authorize_url() -> str:
    return (
        "https://www.strava.com/oauth/authorize?client_id="
        f"{CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}&scope=activity:read"
    )


def exchange_token(code: str) -> dict:
    return {"access_token": "stub", "refresh_token": "stub"}


def fetch_activities(token: str) -> list[dict]:
    return []
