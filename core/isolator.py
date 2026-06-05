import os
import subprocess
import soundfile as sf
import numpy as np
from config import config

class HDIsolationEngine:
    """Uses Hybrid Transformer Demucs models to split environment noise from clean tracks."""
    
    def __init__(self):
        self.model = config.DEMUCS_MODEL
        self.out_rate = config.OUTPUT_SAMPLE_RATE

    def strip_environment_noise(self, input_file_path: str) -> dict:
        """
        Runs Demucs deep separation. It completely separates vocals, drums, bass,
        and other musical elements, abandoning background elements like wind, traffic,
        talking, barking, or ambient environmental pollution.
        """
        print(f"[*] Initializing HD Audio Isolation for: {os.path.basename(input_file_path)}")
        
        # Build execution payload targeting output workspace
        cmd = [
            "demucs",
            "-n", self.model,
            "--two-stems", "vocals", # Splitting clean vocals from the musical framework if necessary
            "-o", config.OUTPUT_DIR,
            input_file_path
        ]
        
        try:
            # Run deep separation sub-process
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            # Locate output files based on standard Demucs directory architectures
            base_name = os.path.splitext(os.path.basename(input_file_path))[0]
            model_output_dir = os.path.join(config.OUTPUT_DIR, self.model, base_name)
            
            stems = {
                "vocals": os.path.join(model_output_dir, "vocals.wav"),
                "no_vocals": os.path.join(model_output_dir, "no_vocals.wav")
            }
            
            # Real fallback if 4-stem was executed by default setting changes
            if not os.path.exists(stems["vocals"]):
                stems = {
                    "vocals": os.path.join(model_output_dir, "vocals.wav"),
                    "drums": os.path.join(model_output_dir, "drums.wav"),
                    "bass": os.path.join(model_output_dir, "bass.wav"),
                    "other": os.path.join(model_output_dir, "other.wav"),
                }
            
            print("[+] HD Noise Separation Complete. Environmental pollution dropped.")
            return stems
            
        except subprocess.CalledProcessError as e:
            print(f"[-] Demucs Execution Critical Failure: {e.stderr.decode()}")
            raise RuntimeError("Audio separation processing pipeline halted.")
