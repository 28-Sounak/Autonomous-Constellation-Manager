satellites = {}
debris = {}

def process_telemetry(data):

    obj_id = data['satellite_id']

    r = [data["x"], data["y"], data["z"]]

    satellites[obj_id] = {

        "r": r,
        "velocity": data["velocity"]
    }
    
    return len(satellites)

    '''objects = data['objects']

    for obj in objects:

        obj_id = obj['id']
        obj_type = obj['type']

        r = [obj["r"]["x"], obj["r"]["y"], obj["r"]["z"]]
        v = [obj["v"]["x"], obj["v"]["y"], obj["v"]["z"]]

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
        
        return len(objects)'''