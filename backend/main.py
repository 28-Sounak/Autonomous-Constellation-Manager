from fastapi import FastAPI
from telemetry_handler import process_telemetry
from collision_detection import detect_collisions

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Autonomous Constellation Manager Running"}

@app.post("/api/telemetry")
def telemetry(data: dict):

    count = process_telemetry(data)
    
    return {
        "status": "ACK",
        "processes_count": count
    }

@app.get("/api/collisions")
def collisions():

    alerts = detect_collisions()

    return {"collision_alrerts": alerts}