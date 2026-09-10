from datetime import datetime

from sqlmodel import Field, SQLModel


class EventRequest(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    text: str
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Event(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    date: datetime
    duration_minutes: int
