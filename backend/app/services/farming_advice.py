def get_farming_advice(crop: str) -> dict:
    crop = crop.lower().strip()

    if not crop:
        return{
            "success": False,
            "message": "Crop name cannot be empty."
        }

    farming_data = {
        "wheat": {
            "crop": "Wheat",
            "advice": "Monitor soil moisture, use balanced fertilization, and inspect regularly for rust diseases."
        },
        "rice": {
            "crop": "Rice",
            "advice": "Maintain appropriate water levels, monitor weeds, and inspect for common rice pests."
        },
        "maize": {
            "crop": "Maize",
            "advice": "Ensure proper soil drainage, monitor crop growth, and inspect for fall armyworm."
        },
        "potato": {
            "crop": "Potato",
            "advice": "Use healthy seed tubers, maintain suitable soil moisture, and monitor for late blight."
        }
    }

    if crop in farming_data:
        return {
            "success": True,
            "data": farming_data[crop]
        }

    return {
        "success": False,
        "message": "Crop information is not available yet."
    }
