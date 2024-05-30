from pydantic import BaseModel

class PurchaseOrder(BaseModel):
    name: str
    partner_id: int
    amount_total: float
