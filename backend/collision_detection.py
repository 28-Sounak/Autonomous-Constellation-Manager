import math
from telemetry_handler import satellites, debris

def detect_collisions():

    alerts = []

    for sat_id, sat in satellites.items():

        for deb_id, deb in debris.items():

            dx = sat["r"][0] - deb["r"][0]
            dy = sat["r"][1] - deb["r"][1]
            dz = sat["r"][2] - deb["r"][2]

            distance = math.sqrt(dx*dx + dy*dy + dz*dz)

            if distance < 50:
                alerts.append({
                    "satellite": sat_id,
                    "debris": deb_id,
                    "distance": distance
                })

    return alerts