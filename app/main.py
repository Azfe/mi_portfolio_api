from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.infrastructure.database import connect_to_mongo, close_mongo_connection
from app.api.routes.work_experience_route import router as work_experience_router
from app.api.routes.education_route import router as education_router
from app.api.routes.profile import router as profile
from app.api.routes.skills import router as skills
from app.api.routes.experiences import router as experiences
from app.api.routes.cv import router as cv

# Crear aplicación FastAPI
app = FastAPI(
    title=settings.api_title,
    version=settings.api_version,
    description="API para gestionar portfolio y CV"
)

# Configurar CORS (para permitir requests desde el frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar los dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Eventos de inicio y cierre
@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()

# Ruta raíz
@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Portfolio API",
        "version": settings.api_version,
        "docs": "/docs"
    }


# Incluir rutas
app.include_router(work_experience_router, prefix="/api/v1")
app.include_router(education_router, prefix="/api/v1")

#Routes Issue #14: Añadir modulos profile, skills, experiences, cv
app.include_router(profile, prefix="/api/v1")
app.include_router(skills, prefix="/api/v1")
app.include_router(experiences, prefix="/api/v1")
app.include_router(cv, prefix="/api/v1")