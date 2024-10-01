from pydantic import BaseModel
from typing import Optional, List, Dict
from datetime import datetime


class Dhuvas(BaseModel):
    id: Optional[str] = None
    day: Optional[int] = None
    month: Optional[int] = None
    year: Optional[int] = None
    detail: Optional[str] = None
    source: Optional[str] = None


class PaymentVoucher(BaseModel):
    pvNum: int
    businessArea: int
    agency: str
    vendor: str
    date: datetime
    notes: str
    currency: str
    exchangeRate: float
    # numOfInvoice: int
    invoiceDetails: List[Dict[str, str | datetime | int | List[Dict[str, int | str]]]]
    preparedBy: Dict[str, str]
    verifiedBy: Dict[str, Optional[str]]
    authorisedByOne: Dict[str, Optional[str]]
    authorisedByTwo: Dict[str, Optional[str]]

    poNum: Optional[str] = None
    paymentMethod: str
    parkedDate: Optional[datetime]
    postingDate: Optional[datetime]
    clearingDoc: Dict[str, str | datetime | None]
    transferNum: Optional[str] = None
