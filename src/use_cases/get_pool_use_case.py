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
    }
}

class GetPoolUseCase:
    
    @staticmethod
    def get_pool_by_id(pool_id: str):
        if pool_id not in FAKE_DB:
            return {"error": "Pool not found"}, 404
        
        try:
            pool_data = FAKE_DB[pool_id]
            pool = PoolModel(**pool_data)  # Validação automática
            return { "data": pool.model_dump() }, 200  # Retorna JSON válido
        
        except ValidationError as e:
            return {"error": str(e)}, 500
        