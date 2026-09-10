from datetime import datetime

from pydantic import BaseModel


class NewRequest(BaseModel):
    text: str


class PlanTimeRequest(BaseModel):
    name: str
    date: datetime
    duration_minutes: int
