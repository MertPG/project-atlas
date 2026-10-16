
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from project_utils import calculate_weekly_hours

app = FastAPI(
    title="Project Atlas API",
    description="Haftalık çalışma saati hesaplama servisi",
    version="1.0.0",
)


class WeeklyHoursRequest(BaseModel):
    hours_per_day: float = Field(ge=0, description="Günlük çalışma saati")
    days_per_week: int = Field(ge=0, le=7, description="Haftalık çalışma günü")

class WeeklyHoursResponse(BaseModel):
    hours_per_day: float
    days_per_week: int
    total_hours: float


@app.get("/")
def home():
    return {
        "message": "Project Atlas API çalışıyor!",
        "docs": "/docs",
    }


@app.post(
    "/calculate-weekly-hours",
    response_model=WeeklyHoursResponse,
)
def calculate_hours(request: WeeklyHoursRequest):
    try:
        total_hours = calculate_weekly_hours(
            request.hours_per_day,
            request.days_per_week,
        )
        return {
            "hours_per_day": request.hours_per_day,
            "days_per_week": request.days_per_week,
            "total_hours": total_hours,
        }
    except (TypeError, ValueError) as error:
        raise HTTPException(status_code=400, detail=str(error))
