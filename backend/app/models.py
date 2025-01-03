from pydantic import BaseModel
from typing import Any, Optional
from datetime import datetime

class BusinessCreate(BaseModel):
    business_name: str

class BusinessOut(BaseModel):
    id: Optional[str]
    business_name: Optional[str]
    registration_date: Optional[str]
    state_of_formation: Optional[str]
    principals: Optional[Any]
    contact_info: Optional[Any]
    scraped_at: Optional[datetime]
