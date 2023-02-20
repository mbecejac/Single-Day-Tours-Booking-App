import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from app.db.database import Base, engine
from app.tours.routes import bus_carrier_router, tour_application_router, tour_router
from app.users.routes import customer_router, employee_router, language_router, tour_guide_router, user_router

Base.metadata.create_all(bind=engine)


def init_app():
    app = FastAPI()
    app.include_router(user_router)
    app.include_router(employee_router)
    app.include_router(language_router)
    app.include_router(tour_guide_router)
    app.include_router(customer_router)
    app.include_router(bus_carrier_router)
    app.include_router(tour_router)
    app.include_router(tour_application_router)

    return app


app = init_app()


@app.get("/", include_in_schema=False)
def hello_world():
    return RedirectResponse("/docs")


if __name__ == "__main__":
    uvicorn.run(app)
