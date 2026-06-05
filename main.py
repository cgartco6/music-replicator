import os
import sys
from core.isolator import HDIsolationEngine
from core.analyzer import HDAnalysisEngine
from core.replicator import HDReplicationEngine
from config import config

def execute_system_pipeline(target_filename: str):
    """Orchestrates isolation, extraction, analysis, and replication processing."""
    
    input_path = os.path.join(config.INPUT_DIR, target_filename)
    
    if not os.path.exists(input_path):
        print(f"[-] Error: Target file not found at location: {input_path}")
        print("[*] Please place your raw input recording inside the 'data/input/' directory directory.")
        sys.exit(1)
        
    print("\n=== STARTING SYSTEM SEPARATION & REPLICATION PIPELINE ===")
    
    # Phase 1: Environment Scrubber & Isolated Stem Separation Engine
    isolation_unit = HDIsolationEngine()
    isolated_stems = isolation_unit.strip_environment_noise(input_path)
    
    # Pull out the primary cleaned track (preferring non-vocal instrument core or master blend for context tracking)
    target_clean_track = isolated_stems.get("no_vocals") or isolated_stems.get("other")
    
    # Phase 2: Structural High-Definition Musical DNA Extraction
    analysis_unit = HDAnalysisEngine()
    dna_metrics = analysis_unit.extract_musical_dna(target_clean_track)
    
    # Print clean terminal analytics readouts
    print("\n" + "="*40)
    print("      EXTRACTED MUSIC DNA MATRIX       ")
    print("="*40)
    for key, value in dna_metrics.items():
        print(f" {key.upper().replace('_', ' ')} : {value}")
    print("="*40 + "\n")
    
    # Phase 3: Generative Studio Recreation Vector Deployment
    replication_unit = HDReplicationEngine()
    recreation_result = replication_unit.trigger_replication_pipeline(
        dna_metrics=dna_metrics, 
        prompt_override="High definition, professional studio mastering grade, no environmental noise."
    )
    
    print("\n=== REPLICATION PIPELINE WORKFLOW COMPLETE ===")
    print(f"[+] Output logs and isolated audio stems safely written to: {config.OUTPUT_DIR}")

if __name__ == "__main__":
    # To run: Place your noisy file (e.g., 'recorded_song.wav') in data/input/ and pass its name here
    # For testing execution, we ensure sample file handles gracefully
    execute_system_pipeline("recorded_song.wav")
