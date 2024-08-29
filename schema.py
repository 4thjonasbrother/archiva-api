from pydantic import BaseModel
from typing import Optional


class Dhuvas(BaseModel):
    id: Optional[str] = None
    day: Optional[int] = None
    month: Optional[int] = None
    year: Optional[int] = None
    detail: Optional[str] = None
    source: Optional[str] = None