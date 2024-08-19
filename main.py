from fastapi import FastAPI
from AssetRegisterReader import AssetRegister
import traceback

app = FastAPI()
asset_register = AssetRegister()

@app.get("/")
async def root():
    return {"start": "Welcome to Archiva API", "last_updated": "19/08/2024 11:35"}

@app.get("/assets")
async def assets():
    assets = asset_register.read_assets_json_file()
    return assets

@app.get("/update_assets")
async def update_assets():
    try:
        asset_register.export_to_json()
        return {"success": True, "message": "Successfully updated assets data"}
    except Exception:
        return {"success": False, "message": traceback.print_exc()}
    
