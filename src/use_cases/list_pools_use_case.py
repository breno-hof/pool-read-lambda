from models.pool_model import PoolModel, MaterialEnum, HeatingTypeEnum, MaintenanceFrequencyEnum
from pydantic import ValidationError

# Simulando um banco de dados fake (DynamoDB ou outro)
FAKE_DB = {
    "12345": {
        "pool_id": "12345",
        "name": "Luxury Pool",
        "location": "California",
        "volume": 5000.0,
        "material": "tile",
        "heating_type": "solar",
        "maintenance_frequency": "weekly",
        "notes": ["Clean filter", "Check chlorine levels"]
    },
    "": {
        "pool_id": "12345",
        "name": "Luxury Pool",
        "location": "California",
        "volume": 5000.0,
        "material": "tile",
        "heating_type": "solar",
        "maintenance_frequency": "weekly",
        "notes": ["Clean filter", "Check chlorine levels"]
    },
}

class ListPoolsUseCase:
    
    @staticmethod
    def get_all_pools():
        pool_list = []

        for _, pool_data in FAKE_DB.items():
            try:
                pool = PoolModel(**pool_data)  # Validação automática
                pool_list.append(pool.model_dump())

            except ValidationError as e:
                return {"error": str(e)}, 500

        return { "data": pool_list }, 200  # Retorna JSON válido
