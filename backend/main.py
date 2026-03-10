from fastapi import FastAPI

app = FastAPI()

satellites = {}
debris = {}

@app.get("/")
def home():
    return {"message": "Autonomous Constellation Manager Running"}

@app.post("/api/telemetry")
def telemetry(data: dict):

    objects = data["objects"]

    for obj in objects:

        obj_id = obj["id"]
        obj_type = obj["type"]

        r = [
            obj["r"]["x"],
            obj["r"]["y"],
            obj["r"]["z"]
        ]

        v = [
            obj["v"]["x"],
            obj["v"]["y"],
            obj["v"]["z"]
        ]

        if obj_type == "SATELLITE":
            satellites[obj_id] = {
                "r": r,
                "v": v
            }

        else:
            debris[obj_id] = {
                "r": r,
                "v": v
            } 
    
    return {
        "status": "ACK",
        "processes_count": len(objects)
    }