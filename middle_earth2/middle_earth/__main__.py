from fastapi import FastAPI
from uvicorn import run
from fastapi.staticfiles import StaticFiles

from middle_earth.config import DefaultSettings
from middle_earth.config.utils import get_settings
from middle_earth.endpoints import list_of_routes
from middle_earth.front_endpoints import list_of_routes as front_list_of_routes


def bind_routes(application: FastAPI, setting: DefaultSettings) -> None:
    """
    Bind all routes to application.
    """
    for route in list_of_routes:
        application.include_router(route, prefix=setting.PATH_PREFIX)
    for route in front_list_of_routes:
        application.include_router(route, prefix=setting.PATH_PREFIX)


def get_app() -> FastAPI:
    """
    Creates application and all dependable objects.
    """
    description = "Wiki for Tolkien's world"

    tags_metadata = [
        {
            "name": "Middle-Earth",
            "description": "Wiki for Tolkien's world",
        },
        {
            "name": "Health check",
            "description": "API health check.",
        },
    ]

    application = FastAPI(
        title="Middle-Earth",
        description=description,
        docs_url="/swagger",
        openapi_url="/openapi",
        version="1.0.0",
        openapi_tags=tags_metadata,
    )
    settings = get_settings()
    bind_routes(application, settings)
    application.state.settings = settings
    return application


app = get_app()
app.mount('/static', StaticFiles(directory='static'), 'static')


if __name__ == "__main__":  # pragma: no cover
    settings_for_application = get_settings()
    run(
        "middle_earth.__main__:app",
        host='localhost',
        port=settings_for_application.APP_PORT,
        reload=True,
        reload_dirs=["middle_earth"],
        log_level="debug",
    )
