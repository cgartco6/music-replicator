class HDPromptEngine:
    """Advanced prompt alignment layer for fluid, autonomous audio-to-audio replication matching."""

    @staticmethod
    def construct_meta_tags(dna_metrics: dict) -> str:
        """
        Compiles real-time extracted mathematical audio metrics and performance constraints
        into an explicitly descriptive string engineered for third-party generative music models.
        """
        base_genre = dna_metrics.get('inferred_genre', 'Modern Electronic Rock Crossover')
        calculated_tempo = dna_metrics.get('calculated_bpm', 124)
        pattern_signature = dna_metrics.get('rhythm_signature', 'Driving syncopated transient grid')
        vocal_matrix = dna_metrics.get('vocal_profile', 'Layered vocal arrangement')
        instrumentation_layer = dna_metrics.get('instruments', 'Layered instrumentation matrix')
        
        compiled_tags = (
            f"Genre Profile: {base_genre}, "
            f"Tempo: {calculated_tempo} BPM, "
            f"Rhythm Pattern: {pattern_signature}, "
            f"Vocal Architecture: {vocal_matrix}, "
            f"Instrument Breakdown: {instrumentation_layer}, "
            f"Live Ambience Layer: massive stadium crowd singing along in perfect unison, live stadium rock concert energy, large arena acoustic room decay, wide field echoing cheering and roaring, heavy group ambient noise tracking, "
            f"Acoustic Spacing: ultra-wide stereo sound fields, modern electronic synth lines layered with heavy stadium rock rhythm configurations, physical mixing console warmth, tape saturation emulator, "
            f"Production Tier: 44.1kHz high-fidelity studio master output tracking, radio edit ready, commercial streaming audio master quality"
        )
        return compiled_tags

    @staticmethod
    def construct_dynamic_blueprint(dna_metrics: dict) -> str:
        """
        Analyses the processed real-time metrics to programmatically assemble a highly detailed
        structural arrangement layout, complete with performance prompts for generative engines.
        """
        base_genre = dna_metrics.get('inferred_genre', 'Modern Electronic Rock Crossover')
        calculated_tempo = dna_metrics.get('calculated_bpm', 124)
        vocal_setup = dna_metrics.get('vocal_profile', 'Dual vocal interaction')
        
        blueprint_document = (
            f"[SYSTEM METRIC ALIGNMENT]\n"
            f"-> Target Tracking Engine Speed: {calculated_tempo} BPM\n"
            f"-> Extracted Audio DNA: {base_genre}\n"
            f"-> Configured Vocal Split Matrix: {vocal_setup}\n\n"
            f"[TRACK ARRANGEMENT BLUEPRINT]\n\n"
            f"[Instrumental Intro]\n"
            f"[Atmospheric entry, pulsing synth bass rhythm grid activates, electronic hi-hat subdivisions crisp, live room ambiance present]\n\n"
            f"[Verse 1]\n"
            f"[Strong pure soaring female lead voice enters, front-and-center vocal mix setting, dry compression, clean intelligibility]\n"
            f"-> Line 1: (Input raw lyrics layer 1 here for vocal synchronization)\n"
            f"-> Line 2: (Input raw lyrics layer 2 here for vocal synchronization)\n"
            f"-> Line 3: (Input raw lyrics layer 3 here for vocal synchronization)\n"
            f"-> Line 4: (Input raw lyrics layer 4 here for vocal synchronization)\n\n"
            f"[Pre-Chorus]\n"
            f"[Vocal dynamic modification: Main female lead voice layered with subtle low male baritone harmony underneath, deep floor support, instrumental build-up, snare fills increasing velocity]\n"
            f"-> Line 5: (Input raw tracking pre-chorus lyrics here)\n"
            f"-> Line 6: (Input raw tracking pre-chorus lyrics here)\n\n"
            f"[Chorus]\n"
            f"[Vocal explosion matrix: Main soaring female lead voice expands immediately into a massive multi-voice anthemic choral stack, full stadium group harmony overlay, massive stadium crowd singing along, roaring cheering echoes in wide background fields, walls of heavy synthesizers and melodic overdrive guitars driving the rhythm section]\n"
            f"-> Main Hook: (Input main dynamic chorus theme lines here)\n"
            f"-> Main Hook: (Input main dynamic chorus theme lines here)\n"
            f"-> Echo Tag: [Full crowd backing group echoes call-and-response variants]\n\n"
            f"[Verse 2]\n"
            f"[Instrumentation drops down back to pulsing electronic synth line baseline drive, crisp rock snares keeping pace, female lead solo returns to clean intimate space configuration]\n"
            f"-> Line 7: (Input verse 2 lyrics tracking block)\n"
            f"-> Line 8: (Input verse 2 lyrics tracking block)\n\n"
            f"[Pre-Chorus]\n"
            f"[Bring back the dual harmony mix: Female lead carrying melodic arc, lower clean male vocals anchoring the cadence intervals, instrumentation picking up energy]\n\n"
            f"[Chorus]\n"
            f"[Maximum energy execution, full vocal choir stacking layer, soaring lead vocals panning wide left and right, stadium crowd chorus tracking in high volume, screaming polyphonic synthesizers blending with heavy rock driving instrumentation grid]\n\n"
            f"[Bridge]\n"
            f"[Dynamic breakdown: Rhythm tracking drops completely to sub-bass pulses and ambient electric guitar washes, clean clear solo female vocal building step-by-step from quiet delivery up to full power soaring registration, building dramatic intensity, background crowd chanting rhythmic pulses]\n\n"
            f"[Chorus]\n"
            f"[Grand finale chorus entry, peak performance density, multi-vocal harmonic saturation, wall-of-sound production engineering mixing, crowd cheering roaring soaring high]\n\n"
            f"[Outro]\n"
            f"[Main rhythm section elements exit sequentially, synthesizer tracking patterns slowly fade, spacious delay on trailing vocals, lingering arena crowd ambiance and low applause trailing into silent vacuum field]\n"
            f"[Fade out completely]\n"
            f"[End Instrument Tracking Session]"
        )
        return blueprint_document
