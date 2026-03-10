satellites = {}
debris = {}

def process_telemetry(data):
    
    objects = data['objects']

    for obj in objects:

        obj_id = obj['id']
        obj_type = obj['type']

        r = [obj["r"]["x"], obj["r"]["y"], obj["r"]["z"]]
        v = [obj["v"]["x"], obj["v"]["y"], obj["v"]["z"]]

        if obj_type == "SATELLITE":
            satellited[obj_id] = {
                "r": r,
                "v": v
            }
        
        else:
            debris[obj_id] = {
                "r": r,
                "v": v
            }
        
        return len(objects)