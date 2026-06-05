import os
from pydantic_settings import BaseSettings

class SystemConfig(BaseSettings):
    """System configuration parameters mapped to serverless and local runtimes."""
    PROJECT_NAME: str = "HD-Music-Replicator"
    OUTPUT_SAMPLE_RATE: int = 44100
    CHANNELS: int = 2
    
    BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
    INPUT_DIR: str = os.path.join(BASE_DIR, "data/input")
    OUTPUT_DIR: str = os.path.join(BASE_DIR, "data/output")
    
    DEMUCS_MODEL: str = "htdemucs"
    GENERATION_API_URL: str = "https://api.crazyrouter.com/suno/submit/music"
    MUSIC_API_KEY: str = "your_actual_suno_provider_api_key_here"
    USE_LOCAL_MOCK_FALLBACK: bool = False

    class Config:
        env_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
        env_file_encoding = 'utf-8'
        extra = "ignore"

config = SystemConfig()

# Autonomously establish directories if operating on local hardware nodes
if not os.environ.get("VERCEL"):
    for path in [config.INPUT_DIR, config.OUTPUT_DIR]:
        os.makedirs(path, exist_ok=True)
