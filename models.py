from typing import List
from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class HomeRequest(BaseModel):

    budget: float = Field(
        gt=0
    )

    room_type: str = "Living Room"

    style: str = "Modern"

    items: List[str] = []

    notes: Optional[str] = ""


class PartyRequest(BaseModel):

    budget: float = Field(
        gt=0
    )

    guests: int = Field(
        gt=0,
        le=10000
    )

    event_type: str = "Birthday"

    venue: str = "Home"

    city: str = ""

    notes: Optional[str] = ""


class JewelryRequest(BaseModel):

    budget: float = Field(
        gt=0
    )

    occasion: str = "Wedding"

    style: str = "Elegant"

    metal: str = "Any"

    notes: Optional[str] = ""