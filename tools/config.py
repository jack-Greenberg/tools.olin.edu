"""
Configurations
"""
import os


class BaseConfig(object):
    TEMPLATES_AUTO_RELOAD = False
    JWT_TOKEN_LOCATION = ["cookies"]
    JWT_ACCESS_COOKIE_PATH = "/api/"
    JWT_COOKIE_CSRF_PROTECT = False
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    ENV = "development"
    SECRET_KEY = "dev"
    SESSION_COOKIE_SAMESITE = "lax"


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    ENV = "production"
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", os.urandom(16))
    SESSION_COOKIE_SAMESITE = "strict"


DATABASE_CONFIG = {
    "drivername": "postgresql",
    "host": os.getenv("POSTGRES_HOST", "tools-db"),
    "port": "5432",
    "username": os.getenv("POSTGRES_USER", "tools"),
    "password": os.getenv("POSTGRES_PASSWORD", "development"),
    "database": os.getenv("POSTGRES_DB", "tools"),
}

AZURE_APPLICATION_ID = os.getenv("AZURE_APPLICATION_ID", "")
AZURE_TENANT_ID = os.getenv("AZURE_TENANT_ID", "")
AZURE_CLIENT_SECRET = os.getenv("AZURE_CLIENT_SECRET", "")
AZURE_AUTHORITY = (
    ("https://login.microsoftonline.com/" + AZURE_TENANT_ID) if AZURE_TENANT_ID else ""
)
AZURE_ENABLED = all(
    [AZURE_APPLICATION_ID, AZURE_TENANT_ID, AZURE_CLIENT_SECRET, AZURE_AUTHORITY]
)
