from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.openapi.docs import get_swagger_ui_html
from app.routers import partners, purchases
from fastapi.openapi.utils import get_openapi

app = FastAPI()

app.include_router(partners.router)
app.include_router(purchases.router)

# Add documentation routes
@app.get("/docs", response_class=HTMLResponse)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="API Docs")

@app.get("/openapi.json")
async def get_open_api_endpoint():
    return JSONResponse(get_openapi(title="Your API", version="1.0", routes=app.routes))
