from fastapi import APIRouter, Depends
from ..schemas.planner import MacroInput, MacroSuggestion
from ..services import planner as planner_service
from .auth import get_current_user

router = APIRouter(prefix="/planner", tags=["planner"])


@router.post("/macros", response_model=MacroSuggestion)
def macros(data: MacroInput, user=Depends(get_current_user)):
    bmr = planner_service.calc_bmr_msj(
        weight_kg=data.weight_kg, height_cm=data.height_cm, age=data.age, sex=data.sex
    )
    tdee = planner_service.estimate_tdee(bmr, data.activity_level)
    return planner_service.suggest_macros_guardrailed(data, bmr, tdee)
