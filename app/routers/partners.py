from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.models.odoo import fetch_odoo_data, fetch_partner_by_id, create_partner, update_partner, delete_partner
from app.schemas.partner import Partner

router = APIRouter(
    prefix="/partners",
    tags=["partners"]
)

@router.get("/", response_class=JSONResponse)
async def read_odoo_data_json():
    odoo_data = fetch_odoo_data()
    return JSONResponse(content=odoo_data)

@router.get("/{partner_id}", response_class=JSONResponse)
async def get_partner_by_id(partner_id: int):
    partner = fetch_partner_by_id(partner_id)
    if partner:
        return JSONResponse(content=partner)
    else:
        raise HTTPException(status_code=404, detail="Partner not found")

@router.post("/", response_class=JSONResponse)
async def create_partner_endpoint(partner: Partner):
    partner_id = create_partner(partner.name, partner.email, partner.phone)
    return {"message": "Partner created", "partner_id": partner_id}

@router.put("/{partner_id}", response_class=JSONResponse)
async def update_partner_endpoint(partner_id: int, partner: Partner):
    update_partner(partner_id, partner.name, partner.email, partner.phone)
    return {"message": "Partner updated"}

@router.delete("/{partner_id}", response_class=JSONResponse)
async def delete_partner_endpoint(partner_id: int):
    delete_partner(partner_id)
    return {"message": "Partner deleted"}
