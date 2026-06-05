import os
from pydantic_settings import BaseSettings

class SystemConfig(BaseSettings):
    """System-wide configurations for HD audio execution."""
    PROJECT_NAME: str = "HD-Music-Replicator"
    OUTPUT_SAMPLE_RATE: int = 44100  # CD Quality HD Audio Standard
    CHANNELS: int = 2               # Stereo Quality
    
    # Storage Paths
    BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
    INPUT_DIR: str = os.path.join(BASE_DIR, "data/input")
    OUTPUT_DIR: str = os.path.join(BASE_DIR, "data/output")
    
    # Model Configs
    DEMUCS_MODEL: str = "htdemucs"  # Hybrid Transformer Demucs for HD separation
    
    # External Audio Generation API (Suno/Udio Bridge Configuration)
    GENERATION_API_URL: str = "https://api.suno.ai/v1/generate"
    API_KEY: str = os.getenv("MUSIC_API_KEY", "your_secure_fallback_key")

    class Config:
        env_file = ".env"

config = SystemConfig()

# Create directories autonomously if missing
for path in [config.INPUT_DIR, config.OUTPUT_DIR]:
    os.makedirs(path, exist_ok=True)
