from fastapi import APIRouter, Depends
from sqlmodel import Session

from backend.schemas import NewRequest, PlanTimeRequest
from db.database import get_session
from db.models import Event, EventRequest

router = APIRouter()


@router.get("/health")
async def health_check():
    return {"status": "ok"}


@router.post("/new_request")
async def new_request(payload: NewRequest, session: Session = Depends(get_session)):
    event_request = EventRequest(text=payload.text)
    session.add(event_request)
    session.commit()
    session.refresh(event_request)
    # TODO: pass payload.text to an LLM to extract event fields
    return {"id": event_request.id, "received": event_request.text}


@router.post("/plan_time")
async def plan_time(payload: PlanTimeRequest, session: Session = Depends(get_session)):
    event = Event(
        name=payload.name,
        date=payload.date,
        duration_minutes=payload.duration_minutes,
    )
    session.add(event)
    session.commit()
    session.refresh(event)
    return event