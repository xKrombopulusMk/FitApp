from pydantic import BaseModel


class MacroInput(BaseModel):
    weight_kg: float
    height_cm: float
    age: int
    sex: str
    activity_level: float
    goal: str


class MacroSuggestion(BaseModel):
    calories: int
    protein_g: float
    carbs_g: float
    fat_g: float
    fiber_g: float
