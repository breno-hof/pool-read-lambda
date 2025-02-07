from aws_lambda_powertools.event_handler import APIGatewayHttpResolver
from use_cases.get_pool_use_case import GetPoolUseCase
from use_cases.list_pools_use_case import ListPoolsUseCase

app = APIGatewayHttpResolver()

@app.get("/pools/<pool_id>")
def get_pool(pool_id: str):
    return GetPoolUseCase.get_pool_by_id(pool_id)

@app.get("/pools")
def get_all_pools():
    return ListPoolsUseCase.get_all_pools()

def lambda_handler(event, context):
    return app.resolve(event, context)