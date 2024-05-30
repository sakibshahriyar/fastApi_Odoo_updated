from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.models.odoo import fetch_purchase_orders, fetch_purchase_order_by_id, create_purchase_order, update_purchase_order, delete_purchase_order
from app.schemas.purchase import PurchaseOrder

router = APIRouter(
    prefix="/purchases",
    tags=["purchases"]
)

@router.get("/", response_class=JSONResponse)
async def read_purchase_orders():
    purchase_orders = fetch_purchase_orders()
    return JSONResponse(content=purchase_orders)

@router.get("/{order_id}", response_class=JSONResponse)
async def get_purchase_order_by_id(order_id: int):
    order = fetch_purchase_order_by_id(order_id)
    if order:
        return JSONResponse(content=order)
    else:
        raise HTTPException(status_code=404, detail="Purchase order not found")

@router.post("/", response_class=JSONResponse)
async def create_purchase_order_endpoint(order: PurchaseOrder):
    order_id = create_purchase_order(order.name, order.partner_id, order.amount_total)
    return {"message": "Purchase order created", "order_id": order_id}

@router.put("/{order_id}", response_class=JSONResponse)
async def update_purchase_order_endpoint(order_id: int, order: PurchaseOrder):
    update_purchase_order(order_id, order.name, order.partner_id, order.amount_total)
    return {"message": "Purchase order updated"}

@router.delete("/{order_id}", response_class=JSONResponse)
async def delete_purchase_order_endpoint(order_id: int):
    delete_purchase_order(order_id)
    return {"message": "Purchase order deleted"}
