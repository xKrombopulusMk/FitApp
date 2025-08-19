from dataclasses import dataclass

@dataclass
class Summary:
    xp: int
    badges: list[str]
    quests: list[str]


def daily_checkin(habits: dict) -> Summary:
    xp = 0
    if habits.get("sleep_ok"):
        xp += 10
    if habits.get("water_ok"):
        xp += 5
    if habits.get("workout_ok"):
        xp += 15
    if habits.get("fiber_ok"):
        xp += 10
    return Summary(xp=xp, badges=[], quests=[])
