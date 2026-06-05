import librosa
import numpy as np
from config import config

class HDAnalysisEngine:
    """Analyzes isolated audio matrix arrays to reverse engineer core song signatures."""

    def __init__(self):
        self.sr = config.OUTPUT_SAMPLE_RATE

    def extract_musical_dna(self, audio_file_path: str) -> dict:
        """Extracts exact musical properties needed for absolute target tracking duplication."""
        print(f"[*] Analyzing Clean Signal Data: {audio_file_path}")
        
        y, sr = librosa.load(audio_file_path, sr=self.sr)
        
        # 1. Determine Precise Target Tempo Vector
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
        computed_bpm = float(tempo[0]) if isinstance(tempo, np.ndarray) else float(tempo)
        
        # 2. Extract Exact Musical Key Signature Configurations
        chroma = librosa.feature.chroma_stft(y=y, sr=sr)
        mean_chroma = np.mean(chroma, axis=1)
        notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        estimated_key = notes[int(np.argmax(mean_chroma))]
        
        # 3. Analyze Harmonic vs Percussive Power Multipliers
        harmonic, percussive = librosa.effects.hpss(y)
        harmonic_energy = float(np.sum(harmonic ** 2))
        percussive_energy = float(np.sum(percussive ** 2))
        
        # Determine stylistic tracking archetypes
        if percussive_energy > (harmonic_energy * 1.3):
            detected_genre = "Electronic Dance Music, Synthwave, Modern Heavy Beats"
        elif percussive_energy > harmonic_energy:
            detected_genre = "Rhythmic Pop, Modern Funk, Upbeat Grooves"
        else:
            detected_genre = "Acoustic Ballad, Symphonic, Cinematic Orchestral Melody"

        return {
            "bpm": int(round(computed_bpm)),
            "estimated_key": estimated_key,
            "detected_genre": detected_genre,
            "sample_rate": sr
        }
