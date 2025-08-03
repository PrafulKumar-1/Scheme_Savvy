from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Application settings are defined here.
    Pydantic automatically reads environment variables or from a .env file.
    """
    APP_NAME: str = "SchemeSavvy API"
    API_V1_STR: str = "/api/v1"

    class Config:
        # This tells Pydantic to look for a .env file if it exists.
        env_file = ".env"

# Create a single instance of the settings to be used throughout the app.
settings = Settings()