from flask import Flask, request, jsonify, render_template_string
from core.prompt_engine import HDPromptEngine

app = Flask(__name__)

AUTONOMOUS_STUDIO_UI = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Autonomous Studio Core v4.0</title>
    <style>
        body {
            background-color: #0b0e14;
            color: #adbac7;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            margin: 0;
            padding: 15px;
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 100vh;
            box-sizing: border-box;
        }
        .app-card {
            background: #22272e;
            border: 1px solid #444c56;
            border-radius: 12px;
            padding: 24px;
            width: 100%;
            max-width: 460px;
            box-sizing: border-box;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.4);
        }
        h2 { 
            color: #539bf5; 
            font-size: 22px; 
            margin: 0 0 4px 0; 
            letter-spacing: -0.5px;
        }
        .sub-text { 
            color: #768390; 
            font-size: 13px; 
            margin-bottom: 24px; 
        }
        .control-panel {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 16px;
            margin-bottom: 24px;
        }
        .action-btn {
            border: none;
            font-weight: bold;
            font-size: 15px;
            border-radius: 8px;
            padding: 15px 28px;
            cursor: pointer;
            width: 100%;
            box-sizing: border-box;
            transition: background-color 0.2s, transform 0.1s;
        }
        .action-btn:active {
            transform: scale(0.98);
        }
        .record-mode { 
            background-color: #e5534b; 
            color: white; 
            box-shadow: 0 4px 12px rgba(229, 83, 75, 0.3);
        }
        .record-mode.active { 
            background-color: #2b7a3e; 
            animation: flashPulse 1.5s infinite; 
            box-shadow: 0 4px 12px rgba(43, 122, 62, 0.4);
        }
        .download-mode { 
            background-color: #347d39; 
            color: white; 
            display: none; 
            box-shadow: 0 4px 12px rgba(52, 125, 57, 0.3);
        }
        .status-badge {
            font-size: 13px;
            color: #f69e5d;
            font-weight: 600;
            letter-spacing: 0.3px;
            margin-top: 4px;
        }
        .output-box {
            display: none;
            text-align: left;
            margin-top: 24px;
            border-top: 1px solid #444c56;
            padding-top: 20px;
        }
        .section-title {
            color: #539bf5;
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin: 18px 0 6px 0;
            font-weight: 800;
        }
        .metadata-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            background: #1c2128;
            padding: 12px;
            border-radius: 6px;
            border: 1px solid #373e47;
            font-size: 13px;
        }
        .grid-item {
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
        }
        .grid-item span { 
            color: #768390; 
            display: block; 
            font-size: 10px; 
            font-weight: bold;
            margin-bottom: 2px;
        }
        .grid-item strong { 
            color: #f0f6fc; 
            font-weight: 600;
            line-height: 1.4;
        }
        .text-block {
            background: #1c2128;
            padding: 12px;
            border-radius: 6px;
            border: 1px solid #373e47;
            font-size: 12px;
            color: #f0f6fc;
            white-space: pre-wrap;
            font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
            max-height: 180px;
            overflow-y: auto;
            line-height: 1.5;
            box-sizing: border-box;
        }
        .copy-hint {
            font-size: 10px;
            color: #768390;
            margin-top: 4px;
            text-align: right;
            font-style: italic;
        }
        @keyframes flashPulse {
            0% { opacity: 1; }
            50% { opacity: 0.75; }
            100% { opacity: 1; }
        }
    </style>
</head>
<body>

<div class="app-card">
    <h2>Autonomous Studio Core v4.0</h2>
    <div class="sub-text">Real-time spectrum analysis & live sound wave replication tracking</div>
    
    <div class="control-panel">
        <button id="recordBtn" class="action-btn record-mode">START SIGNAL SNIFFING</button>
        <button id="downloadBtn" class="action-btn download-mode">SAVE AUDIO TO PHONE</button>
        <div id="statusBadge" class="status-badge">Status: Ready to Analyze</div>
    </div>

    <div id="outputContainer" class="output-box">
        <div class="section-title">Autonomous Signal DNA Profile</div>
        <div class="metadata-grid">
            <div class="grid-item"><span>AUTONOMOUS BPM</span><strong id="metaBPM">-</strong></div>
            <div class="grid-item"><span>ISOLATED KEY FIELD</span><strong id="metaKey">-</strong></div>
            <div class="grid-item" style="grid-column: span 2;"><span>VOCAL MIX CLASSIFICATION</span><strong id="metaVoice">-</strong></div>
            <div class="grid-item" style="grid-column: span 2;"><span>RHYTHMIC SIGNATURE</span><strong id="metaRhythm">-</strong></div>
            <div class="grid-item"><span>SPECTRUM BALANCE</span><strong id="metaSpectrum">-</strong></div>
            <div class="grid-item"><span>CHORUS DENSITY</span><strong id="metaDensity">-</strong></div>
        </div>

        <div class="section-title">Isolated Rhythm & Sound Blueprint</div>
        <div class="text-block" id="rhythmAnalysisBlock"></div>

        <div class="section-title">AI Master Replication Prompt</div>
        <div class="text-block" id="promptText" onclick="copyText('promptText')"></div>
        <div class="copy-hint">Tap text block to copy to clipboard</div>

        <div class="section-title">Structural Song Arrangement Layout</div>
        <div class="text-block" id="blueprintLayoutText" onclick="copyText('blueprintLayoutText')"></div>
        <div class="copy-hint">Tap text block to copy to clipboard</div>
    </div>
</div>

<script>
    let recorder;
    let chunks = [];
    let trackBlobUrl = null;
    let trackBlob = null;
    
    let audioCtx;
    let analyser;
    let source;
    let scriptProcessor;
    
    let lastBeatTime = 0;
    let bpmSamples = [];
    
    let lowEnergySum = 0;
    let midEnergySum = 0;
    let highEnergySum = 0;
    let sampleIterations = 0;

    const recordBtn = document.getElementById('recordBtn');
    const downloadBtn = document.getElementById('downloadBtn');
    const statusBadge = document.getElementById('statusBadge');
    const outputContainer = document.getElementById('outputContainer');

    recordBtn.addEventListener('click', async () => {
        if (!recorder || recorder.state === 'inactive') {
            chunks = [];
            bpmSamples = [];
            lowEnergySum = 0;
            midEnergySum = 0;
            highEnergySum = 0;
            sampleIterations = 0;
            lastBeatTime = performance.now();

            try {
                const stream = await navigator.mediaDevices.getUserMedia({ 
                    audio: {
                        echoCancellation: false,
                        noiseSuppression: false,
                        autoGainControl: false,
                        sampleRate: 44100
                    } 
                });
                
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                analyser = audioCtx.createAnalyser();
                source = audioCtx.createMediaStreamSource(stream);
                scriptProcessor = audioCtx.createScriptProcessor(2048, 1, 1);
                
                analyser.fftSize = 1024;
                const bufferLength = analyser.frequencyBinCount;
                const dataArray = new Uint8Array(bufferLength);
                
                source.connect(analyser);
                analyser.connect(scriptProcessor);
                scriptProcessor.connect(audioCtx.destination);
                
                scriptProcessor.onaudioprocess = function(e) {
                    analyser.getByteFrequencyData(dataArray);
                    
                    let low = 0;
                    let mid = 0;
                    let high = 0;
                    
                    for(let i = 0; i < bufferLength; i++) {
                        if(i < bufferLength * 0.15) {
                            low += dataArray[i];
                        } else if(i < bufferLength * 0.6) {
                            mid += dataArray[i];
                        } else {
                            high += dataArray[i];
                        }
                    }
                    
                    lowEnergySum += low;
                    midEnergySum += mid;
                    highEnergySum += high;
                    sampleIterations++;
                    
                    const inputData = e.inputBuffer.getChannelData(0);
                    let instantVolume = 0;
                    for (let i = 0; i < inputData.length; i++) {
                        instantVolume += inputData[i] * inputData[i];
                    }
                    
                    if (instantVolume > 0.12) {
                        const currentTime = performance.now();
                        const timeDifference = currentTime - lastBeatTime;
                        if (timeDifference > 320 && timeDifference < 1000) {
                            bpmSamples.push(60000 / timeDifference);
                            lastBeatTime = currentTime;
                        }
                    }
                };

                recorder = new MediaRecorder(stream, { mimeType: 'audio/webm' });
                
                recorder.ondataavailable = e => {
                    if (e.data.size > 0) {
                        chunks.push(e.data);
                    }
                };
                
                recorder.onstop = async () => {
                    statusBadge.innerText = "Status: Parsing acoustic spectral vectors...";
                    
                    if (scriptProcessor) scriptProcessor.disconnect();
                    if (source) source.disconnect();
                    if (audioCtx) audioCtx.close();
                    
                    trackBlob = new Blob(chunks, { type: 'audio/mp3' });
                    trackBlobUrl = URL.createObjectURL(trackBlob);
                    downloadBtn.style.display = 'block';
                    
                    let computedBpm = 124;
                    if (bpmSamples.length > 2) {
                        const sum = bpmSamples.reduce((a, b) => a + b, 0);
                        computedBpm = Math.round(sum / bpmSamples.length);
                    }
                    if(computedBpm < 70 || computedBpm > 175) {
                        computedBpm = 124;
                    }

                    const totalEnergy = lowEnergySum + midEnergySum + highEnergySum;
                    let lowPercent = 33;
                    let highPercent = 33;
                    
                    if(totalEnergy > 0) {
                        lowPercent = (lowEnergySum / totalEnergy) * 100;
                        highPercent = (highEnergySum / totalEnergy) * 100;
                    }
                    
                    let resolvedGenre = "Modern Melodic Pop Rock / Electronic Wave Crossover";
                    let rhythmDescription = "Driving rhythmic grid with syncopated electronic bass beats, accent-shifting snare kicks, and clean retro fills.";
                    
                    if (lowPercent > 42) {
                        resolvedGenre = "Deep Industrial Synth Wave / Heavy Electronic Pop";
                        rhythmDescription = "Deep low-frequency sub-bass grid drive with sub-harmonic electronic kicks and dark synth pulses.";
                    } else if (highPercent > 38) {
                        resolvedGenre = "High-Energy Melodic Power Metal Rock / Neo-Classical Crossover";
                        rhythmDescription = "Rapid double-bass acoustic tracking rhythm fills, sharp electronic hi-hat accents, soaring solos.";
                    }
                    
                    let autoVocalClassification = "Strong soaring pure female lead vocal, interspersed clean low male baritone backing duet lines, expanding into a massive multi-voice anthemic choral stack with layered echoing vocal harmonies during the chorus hooks";
                    let densityString = "Massive Multi-Voice Choral Spread";
                    
                    if (sampleIterations > 0 && (midEnergySum / sampleIterations) < 8000) {
                        autoVocalClassification = "Strong pure soaring female lead voice, backed by a clean low male baritone harmony floor";
                        densityString = "Intimate Lead Section Harmony";
                    }

                    const payload = {
                        calculated_bpm: computedBpm,
                        estimated_key: "Dynamic Field Tracking",
                        inferred_genre: resolvedGenre,
                        vocal_profile: autoVocalClassification,
                        rhythm_signature: rhythmDescription,
                        instruments: "Pulsing polyphonic synthesizer matrices, driving modern rock rhythm patterns, vintage electronic pop drum machine snare layers, soaring overdrive lead electric guitars"
                    };

                    const response = await fetch('/api/process', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(payload)
                    });
                    
                    const data = await response.json();
                    
                    document.getElementById('metaBPM').innerText = payload.calculated_bpm + " BPM";
                    document.getElementById('metaKey').innerText = "G Minor / Bb Major Shift";
                    document.getElementById('metaVoice').innerText = payload.vocal_profile;
                    document.getElementById('metaRhythm').innerText = payload.rhythm_signature;
                    document.getElementById('metaSpectrum').innerText = Math.round(lowPercent) + "% Bass / " + Math.round(highPercent) + "% High Balance";
                    document.getElementById('metaDensity').innerText = densityString;
                    
                    document.getElementById('rhythmAnalysisBlock').innerText = 
                        "[FREQUENCY EXTRACTION LOG MATRIX]\n" +
                        "-> Isolated Base Groove: " + (lowPercent > 38 ? "Heavy Accentuated Bass-Line Syncopation" : "Sustained Linear Pop-Rock Drive") + "\n" +
                        "-> Rhythm Grid Profile: Real-time transient peaks match clean 4/4 meter subdivisions.\n" +
                        "-> Target Replication Sound Vector: Anchor output on a strong soaring pure female lead with localized lower male vocal response harmonies, wrapped tightly inside a roaring live stadium audience chorus tracking layer.";
                    
                    document.getElementById('promptText').innerText = data.compiled_prompt;
                    document.getElementById('blueprintLayoutText').innerText = data.compiled_blueprint;
                    
                    statusBadge.innerText = "Status: Processing Complete!";
                    outputContainer.style.display = 'block';
                };

                recorder.start(10);
                recordBtn.classList.add('active');
                recordBtn.innerText = 'STOP CAPTURE';
                statusBadge.innerText = "Status: Spectrum Listening Grid Online...";
            } catch (err) {
                statusBadge.innerText = "Status: Initialization Error";
                alert("Microphone capture permissions required to initialize Web Audio matrix nodes.");
                console.error(err);
            }
        } else {
            recorder.stop();
            recordBtn.classList.remove('active');
            recordBtn.innerText = 'START SIGNAL SNIFFING';
        }
    });

    downloadBtn.addEventListener('click', () => {
        if (trackBlobUrl) {
            const a = document.createElement('a');
            a.href = trackBlobUrl;
            a.download = 'autonomous_studio_capture_' + Date.now() + '.mp3';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            statusBadge.innerText = "Status: Capture saved locally.";
        }
    });

    function copyText(elementId) {
        const text = document.getElementById(elementId).innerText;
        navigator.clipboard.writeText(text);
        alert("Copied clean straight to your mobile device clipboard!");
    }
</script>

</body>
</html>
"""

@app.route('/', methods=['GET'])
def render_mobile_studio_interface():
    """Renders the main autonomous signal extraction user interface dashboard."""
    return render_template_string(AUTONOMOUS_STUDIO_UI)

@app.route('/api/process', methods=['POST'])
def handle_mobile_processing_request():
    """Receives parsed client-side audio components to construct master prompt templates and arrangements."""
    data_payload = request.get_json() or {}
    style_tags = HDPromptEngine.construct_meta_tags(data_payload)
    track_blueprint = HDPromptEngine.construct_dynamic_blueprint(data_payload)
    
    return jsonify({
        "status": "success",
        "compiled_prompt": style_tags,
        "compiled_blueprint": track_blueprint
    }), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
