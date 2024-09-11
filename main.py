from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from AssetRegisterReader import AssetRegister
from DB import ArchivaDB
from schema import Dhuvas
import traceback

app = FastAPI(
    title="ArchivaAPI"
)

DB = ArchivaDB()

origins = [
    "http://localhost:3000",
    "https://10.12.29.68:3001",
    "http://10.12.29.68:3001",
    "https://10.12.29.68:3000",
    "http://10.12.29.68:3000",
    "http://10.12.29.70:3000",
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
    return {"start": "Welcome to Archiva API", "last_updated": "29/08/2024 09:32"}

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
    
@app.get("/dhuvas")
async def dhuvas():
    try:
        result = DB.get_dhuvas()
        return {"success": True, "result": result}
    except Exception:
        return {"success": False, "result": traceback.print_exc()}
    

@app.post("/dhuvas/add/")
async def add_dhuvas(dhuvas: Dhuvas):
    try:
        DB.add_dhuvas(
            day=dhuvas.day,
            month=dhuvas.month,
            year=dhuvas.year,
            detail=dhuvas.detail,
            source=dhuvas.source
        )
        return {"success": True, "message": "Successfully added dhuvas!"}
    except Exception:
        return {"success": False, "message": traceback.print_exc()}

@app.post("/dhuvas/remove/")
async def remove_dhuvas(dhuvas: Dhuvas):
    try:
        DB.remove_dhuvas(dhuvasId = dhuvas.id)
        return {"success": True, "message": "Successfully removed dhuvas!"}
    except Exception:
        return {"success": False, "message": traceback.print_exc()}

@app.get("/racks/")
async def racks():
    return DB.get_racks()

@app.get("/racks/{rackRoute}")
async def get_rack(rackRoute: str):
    return DB.get_rack(rackRoute)