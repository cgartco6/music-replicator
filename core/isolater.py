import os
import subprocess
from config import config

class HDIsolationEngine:
    """Isolates high-definition musical assets from environmental ambient pollution."""
    
    def __init__(self):
        self.model = config.DEMUCS_MODEL

    def strip_environment_noise(self, input_file_path: str) -> dict:
        """Runs heavy-lifting localized stem separations to drop barks, chatter, and horns."""
        print(f"[*] Initializing local HD Audio Isolation processing for: {os.path.basename(input_file_path)}")
        
        cmd = [
            "demucs",
            "-n", self.model,
            "--two-stems", "vocals",
            "-o", config.OUTPUT_DIR,
            input_file_path
        ]
        
        try:
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            base_name = os.path.splitext(os.path.basename(input_file_path))[0]
            model_output_dir = os.path.join(config.OUTPUT_DIR, self.model, base_name)
            
            stems = {
                "vocals": os.path.join(model_output_dir, "vocals.wav"),
                "no_vocals": os.path.join(model_output_dir, "no_vocals.wav")
            }
            return stems
        except subprocess.CalledProcessError as e:
            print(f"[-] Critical failure during source isolation step: {e.stderr.decode()}")
            raise RuntimeError("Demucs processing failure. Ensure FFMPEG toolchains are locally active.")
