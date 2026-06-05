import os
import sys
import requests
from core.isolator import HDIsolationEngine
from core.analyzer import HDAnalysisEngine

def process_and_export_to_cloud(target_filename: str, vercel_url: str = "http://127.0.0.1:5000/api/generate"):
    """
    Runs locally on your laptop to execute heavy processing tasks, then
    sends clean data maps up to the cloud endpoint.
    """
    from config import config
    input_file_path = os.path.join(config.INPUT_DIR, target_filename)
    
    if not os.path.exists(input_path := input_file_path):
        print(f"[-] Missing input audio file asset target: {input_path}")
        return

    # 1. Clean environmental sounds locally using your laptop hardware
    isolator = HDIsolationEngine()
    stems = isolator.strip_environment_noise(input_path)
    
    # 2. Analyze the clean instrumental profile data
    analyzer = HDAnalysisEngine()
    dna_metrics = analyzer.extract_musical_dna(stems["no_vocals"])
    
    print("[*] Processing Complete. Forwarding clean musical structures to the Cloud Gateway Server...")
    
    # 3. Offload clean metadata metrics to the serverless web server endpoint
    try:
        response = requests.post(vercel_url, json=dna_metrics, timeout=30)
        print(f"[+] Serverless Response Status ({response.status_code}):")
        print(response.text)
    except Exception as e:
        print(f"[-] Failed to sync data directly to server endpoint: {e}")

if __name__ == "__main__":
    # Create dummy testing handle if executing infrastructure check without a pre-existing track file
    test_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/input/recorded_song.wav")
    if not os.path.exists(test_file):
        print("[*] Base target 'data/input/recorded_song.wav' not found. Please add a wav audio file to run local tests.")
    else:
        # Swap out with live deployed production Vercel app domain routes once pushed to git
        process_and_export_to_cloud("recorded_song.wav", vercel_url="http://127.0.0.1:5000/api/generate")
