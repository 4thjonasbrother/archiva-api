from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from AssetRegisterReader import AssetRegister
import traceback

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://10.12.29.68:3001",
    "http://10.12.29.68:3001",
    "https://10.12.29.68:3000",
    "http://10.12.29.68:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

asset_register = AssetRegister()

@app.get("/")
async def root():
    return {"start": "Welcome to Archiva API", "last_updated": "20/08/2024 09:32"}

@app.get("/assets")
async def assets():
    _assets = asset_register.read_assets_json_file()
    return _assets

@app.get("/asset/{asset_num}")
async def asset(asset_num: str):
    _assets = asset_register.read_assets_json_file()
    for each_asset in _assets:
        if asset_num == each_asset["asset_number"]:
            return each_asset
    return {
                "asset_number": "",
                "sap_number": "",
                "name": "",
                "present_location": "",
                "condition": ""
            }

@app.get("/update_assets")
async def update_assets():
    try:
        asset_register.export_to_json()
        return {"success": True, "message": "Successfully updated assets data"}
    except Exception:
        return {"success": False, "message": traceback.print_exc()}
    
