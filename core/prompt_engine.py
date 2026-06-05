class HDPromptEngine:
    """Builds the generation prompt parameters and lyrics for the AI music engine."""

    @staticmethod
    def construct_meta_tags(dna_metrics: dict) -> str:
        """Creates high-density metadata strings optimized for engine tag inputs."""
        return f"{dna_metrics['detected_genre']}, {dna_metrics['bpm']} BPM, Key of {dna_metrics['estimated_key']}, pristine studio mix, high fidelity recording quality, 44kHz, clear mastering"

    @staticmethod
    def generate_exact_lyric_sheet() -> str:
        """
        Provides structural prompt lyric blocks injected into the target engine.
        Uses clear structural markers ([Verse], [Chorus]) to anchor long-term memory tracking.
        """
        return (
            "[Instrumental Intro]\n"
            "[Synthesizer build-up, rhythmic drum synchronization]\n\n"
            "[Verse 1]\n"
            "Signals moving through the midnight screen,\n"
            "A clean spectrum that you've never seen.\n"
            "No static talking, no sirens in the dark,\n"
            "Just pure frequency hitting the mark.\n\n"
            "[Pre-Chorus]\n"
            "Isolate the rhythm, wash the noise away,\n"
            "We hold the master record at the end of day.\n\n"
            "[Chorus]\n"
            "Replicate the sound, track it line by line,\n"
            "Sovereign engines moving through the space of time.\n"
            "Perfect cadence, heavy beats alive,\n"
            "Sustaining the frequency in twenty-twenty-six we thrive.\n\n"
            "[Outro]\n"
            "Fading out pristine.\n"
            "[Fade to End]\n"
            "[End]"
        )
