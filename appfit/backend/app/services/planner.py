from dataclasses import dataclass

@dataclass
class MacroResult:
    calories: int
    protein_g: float
    carbs_g: float
    fat_g: float
    fiber_g: float


def calc_bmr_msj(weight_kg: float, height_cm: float, age: int, sex: str) -> float:
    if sex.lower() == "male":
        return 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    return 10 * weight_kg + 6.25 * height_cm - 5 * age - 161


def estimate_tdee(bmr: float, activity_level: float) -> float:
    return bmr * activity_level


def suggest_macros_guardrailed(data, bmr: float, tdee: float) -> MacroResult:
    calories = max(int(tdee), int(bmr))
    protein = max(0.8 * data.weight_kg, 0.8 * data.weight_kg)
    carbs = (calories * 0.5) / 4
    fat = (calories * 0.25) / 9
    fiber = 25.0
    if calories < bmr:
        calories = int(bmr)
    return MacroResult(
        calories=calories,
        protein_g=round(protein, 1),
        carbs_g=round(carbs, 1),
        fat_g=round(fat, 1),
        fiber_g=fiber,
    )


def weekly_meal_plan(macros: MacroResult) -> dict:
    meals = []
    for day in range(7):
        meals.append(
            {
                "day": day,
                "meals": [
                    {"name": "Café", "cal": macros.calories * 0.3},
                    {"name": "Almoço", "cal": macros.calories * 0.4},
                    {"name": "Jantar", "cal": macros.calories * 0.3},
                ],
            }
        )
    return {"week": meals}
