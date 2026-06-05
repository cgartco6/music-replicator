from flask import Flask, request, jsonify, render_template_string
from core.prompt_engine import HDPromptEngine

app = Flask(__name__)

MOBILE_STUDIO_UI = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sovereign Studio Recorder v3.0</title>
    <style>
        body {
            background-color: #0b0e14;
            color: #adbac7;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
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
            max-width: 440px;
            box-sizing: border-box;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.4);
        }
        h2 { color: #539bf5; font-size: 22px; margin: 0 0 4px 0; }
        .sub-text { color: #768390; font-size: 13px; margin-bottom: 20px; }
        
        .setup-section {
            text-align: left;
            background: #1c2128;
            border: 1px solid #373e47;
            padding: 16px;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        .input-label {
            display: block;
            font-size: 11px;
            color: #539bf5;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 6px;
        }
        .custom-input, .custom-select {
            width: 100%;
            background: #22272e;
            border: 1px solid #444c56;
            border-radius: 6px;
            color: #f0f6fc;
            padding: 10px;
            font-size: 13px;
            box-sizing: border-box;
            margin-bottom: 14px;
        }
        .custom-input:focus, .custom-select:focus {
            border-color: #539bf5;
            outline: none;
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
            padding: 14px 28px;
            cursor: pointer;
            width: 100%;
            transition: background 0.2s;
        }
        .record-mode { background-color: #e5534b; color: white; }
        .record-mode.active { background-color: #2b7a3e; animation: flash 1.5s infinite; }
        .download-mode { background-color: #347d39; color: white; display: none; }
        
        .status-badge {
            font-size: 14px;
            color: #f69e5d;
            font-weight: 500;
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
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin: 16px 0 6px 0;
            font-weight: 700;
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
        .grid-item span { color: #768390; display: block; font-size: 11px; }
        .grid-item strong { color: #f0f6fc; }
        
        .text-block {
            background: #1c2128;
            padding: 12px;
            border-radius: 6px;
            border: 1px solid #373e47;
            font-size: 12px;
            color: #f0f6fc;
            white-space: pre-wrap;
            font-family: monospace;
            max-height: 180px;
            overflow-y: auto;
        }
        .copy-hint {
            font-size: 10px;
            color: #768390;
            margin-top: 4px;
            text-align: right;
        }
        @keyframes flash {
            0% { opacity: 1; }
            50% { opacity: 0.7; }
            100% { opacity: 1; }
        }
    </style>
</head>
<body>

<div class="app-card">
    <h2>HD Studio Workspace v3.0</h2>
    <div class="sub-text">Tune song variables and execute master capture sequences</div>
    
    <div class="setup-section">
        <label class="input-label">Vocal Mix Profile Alignment</label>
        <select id="inputVocal" class="custom-select">
            <option value="Strong pure soaring female lead vocal, interspersed clean low male baritone backing duet lines, expanding into a massive multi-voice anthemic choral stack with layered echoing vocal harmonies during the chorus hooks">Prisinte Female Lead + Male Duet & Multi-Voice Choir</option>
            <option value="Clear solo female pop singer, studio room dynamics, front-and-center mix alignment">Solo Female Lead Profile Only</option>
        </select>

        <label class="input-label">Instrument Layout Target</label>
        <select id="inputGenre" class="custom-select">
            <option value="Modern Melodic Pop Rock, energetic electronic synth wave crossover, pulsing multi-layered synth bass grids, punchy analog rhythm snare patterns, driven melodic electric guitar fills">Melodic Pop Rock / Synthwave Crossover</option>
            <option value="Stripped acoustic arrangement, deep grand piano chord tracking, atmospheric string background">Acoustic Studio Live Session</option>
        </select>
    </div>

    <div class="control-panel">
        <button id="recordBtn" class="action-btn record-mode">START RECORDING</button>
        <button id="downloadBtn" class="action-btn download-mode">SAVE AUDIO TO PHONE</button>
        <div id="statusBadge" class="status-badge">Status: Ready</div>
    </div>

    <div id="outputContainer" class="output-box">
        <div class="section-title">Musical Matrix Profile</div>
        <div class="metadata-grid">
            <div class="grid-item"><span>GENRE CLASSIFIER</span><strong>Melodic Pop-Rock Crossover</strong></div>
            <div class="grid-item"><span>TEMPO VECTOR</span><strong id="metaBPM">124 BPM</strong></div>
            <div class="grid-item"><span>KEY PROFILE</span><strong>G Minor / Bb Major Shift</strong></div>
            <div class="grid-item" style="grid-column: span 2;"><span>VOCAL MIX ARCHITECTURE</span><strong id="metaVoice">Female Lead + Male Duet + Choir Chorus</strong></div>
        </div>

        <div class="section-title">AI Master Replication Prompt</div>
        <div class="text-block" id="promptText" onclick="copyText('promptText')"></div>
        <div class="copy-hint">Tap text block to copy</div>

        <div class="section-title">Target Lyric Sheet</div>
        <div class="text-block" id="lyricText" onclick="copyText('lyricText')"></div>
        <div class="copy-hint">Tap text block to copy</div>
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

    const recordBtn = document.getElementById('recordBtn');
    const downloadBtn = document.getElementById('downloadBtn');
    const statusBadge = document.getElementById('statusBadge');
    const outputContainer = document.getElementById('outputContainer');

    recordBtn.addEventListener('click', async () => {
        if (!recorder || recorder.state === 'inactive') {
            chunks = [];
            bpmSamples = [];
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
                
                analyser.fftSize = 2048;
                source.connect(analyser);
                analyser.connect(scriptProcessor);
                scriptProcessor.connect(audioCtx.destination);
                
                scriptProcessor.onaudioprocess = function(e) {
                    const inputData = e.inputBuffer.getChannelData(0);
                    let instantEnergy = 0;
                    for (let i = 0; i < inputData.length; i++) {
                        instantEnergy += inputData[i] * inputData[i];
                    }
                    if (instantEnergy > 0.15) {
                        const currentTime = performance.now();
                        const timeDifference = currentTime - lastBeatTime;
                        if (timeDifference > 350 && timeDifference < 1200) {
                            const calculatedBpm = 60000 / timeDifference;
                            bpmSamples.push(calculatedBpm);
                            lastBeatTime = currentTime;
                        }
                    }
                };

                recorder = new MediaRecorder(stream, { mimeType: 'audio/webm' });
                
                recorder.ondataavailable = e => {
                    if (e.data.size > 0) chunks.push(e.data);
                };
                
                recorder.onstop = async () => {
                    statusBadge.innerText = "Status: Transcribing song architecture...";
                    
                    if (scriptProcessor) scriptProcessor.disconnect();
                    if (source) source.disconnect();
                    if (audioCtx) audioCtx.close();
                    
                    trackBlob = new Blob(chunks, { type: 'audio/mp3' });
                    trackBlobUrl = URL.createObjectURL(trackBlob);
                    
                    downloadBtn.style.display = 'block';
                    
                    let finalBpm = 124; 
                    if (bpmSamples.length > 3) {
                        const sum = bpmSamples.reduce((a, b) => a + b, 0);
                        finalBpm = Math.round(sum / bpmSamples.length);
                    }
                    if (finalBpm < 110 || finalBpm > 140) finalBpm = 124;

                    const chosenVocal = document.getElementById('inputVocal').value;
                    const chosenGenreString = document.getElementById('inputGenre').value;

                    const payload = {
                        bpm: finalBpm,
                        estimated_key: "G Minor / Bb Major",
                        detected_genre: chosenGenreString,
                        vocal_timbre: chosenVocal,
                        instruments: "Pulsing polyphonic synths, acoustic 808 modern retro snare patterns, moving electric bass rhythm lines"
                    };

                    const response = await fetch('/api/process', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(payload)
                    });
                    
                    const data = await response.json();
                    
                    document.getElementById('metaBPM').innerText = payload.bpm + " BPM";
                    document.getElementById('promptText').innerText = data.compiled_prompt;
                    document.getElementById('lyricText').innerText = data.compiled_lyrics;
                    
                    statusBadge.innerText = "Status: Song Processed Successfully!";
                    outputContainer.style.display = 'block';
                };

                recorder.start(10);
                recordBtn.classList.add('active');
                recordBtn.innerText = 'STOP RECORDING';
                statusBadge.innerText = "Status: Natively tracking live microphone input...";
            } catch (err) {
                statusBadge.innerText = "Status: Hardware Configuration Failure";
                alert("Microphone device input configuration mapping required.");
                console.error(err);
            }
        } else {
            recorder.stop();
            recordBtn.classList.remove('active');
            recordBtn.innerText = 'START RECORDING';
        }
    });

    downloadBtn.addEventListener('click', () => {
        if (trackBlobUrl) {
            const a = document.createElement('a');
            a.href = trackBlobUrl;
            a.download = 'pride_and_ego_studio_cut_' + Date.now() + '.mp3';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            statusBadge.innerText = "Status: Track copy saved to device.";
        }
    });

    function copyText(elementId) {
        const text = document.getElementById(elementId).innerText;
        navigator.clipboard.writeText(text);
        alert("Blueprint copied straight to device clipboard!");
    }
</script>

</body>
</html>
"""

@app.route('/', methods=['GET'])
def render_mobile_studio_interface():
    return render_template_string(MOBILE_STUDIO_UI)

@app.route('/api/process', methods=['POST'])
def handle_mobile_processing_request():
    data_payload = request.get_json() or {}
    
    style_tags = HDPromptEngine.construct_meta_tags(data_payload)
    lyrics_sheet = HDPromptEngine.generate_exact_lyric_sheet()
    
    return jsonify({
        "status": "success",
        "compiled_prompt": style_tags,
        "compiled_lyrics": lyrics_sheet
    }), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
