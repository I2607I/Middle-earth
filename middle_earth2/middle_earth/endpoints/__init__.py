from middle_earth.endpoints.health_check import api_router as health_check_router
from middle_earth.endpoints.main import api_router as character_router


list_of_routes = [
    health_check_router,
    character_router
]


__all__ = [
    "list_of_routes",
]
