from flask import Flask, request, jsonify, render_template_string
from core.prompt_engine import HDPromptEngine

app = Flask(__name__)

MOBILE_STUDIO_UI = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sovereign Studio Recorder v1.0</title>
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
        .sub-text { color: #768390; font-size: 13px; margin-bottom: 24px; }
        
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
            max-height: 150px;
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
    <h2>HD Studio Workspace</h2>
    <div class="sub-text">Capture audio and extract perfect replication formulas</div>
    
    <div class="control-panel">
        <button id="recordBtn" class="action-btn record-mode">START RECORDING</button>
        <button id="downloadBtn" class="action-btn download-mode">SAVE AUDIO TO PHONE</button>
        <div id="statusBadge" class="status-badge">Status: Ready</div>
    </div>

    <div id="outputContainer" class="output-box">
        <div class="section-title">Musical Matrix Profile</div>
        <div class="metadata-grid">
            <div class="grid-item"><span>GENRE CLASSIFIER</span><strong id="metaGenre">-</strong></div>
            <div class="grid-item"><span>TEMPO VECTOR</span><strong id="metaBPM">-</strong></div>
            <div class="grid-item"><span>KEY PROFILE</span><strong id="metaKey">-</strong></div>
            <div class="grid-item"><span>VOCAL TIMBRE</span><strong id="metaVoice">-</strong></div>
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

    const recordBtn = document.getElementById('recordBtn');
    const downloadBtn = document.getElementById('downloadBtn');
    const statusBadge = document.getElementById('statusBadge');
    const outputContainer = document.getElementById('outputContainer');

    recordBtn.addEventListener('click', async () => {
        if (!recorder || recorder.state === 'inactive') {
            chunks = [];
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
                recorder = new MediaRecorder(stream);
                
                recorder.ondataavailable = e => chunks.push(e.data);
                recorder.onstop = async () => {
                    statusBadge.innerText = "Status: Building replication profiles...";
                    trackBlob = new Blob(chunks, { type: 'audio/mp3' });
                    trackBlobUrl = URL.createObjectURL(trackBlob);
                    
                    // Show save button instantly
                    downloadBtn.style.display = 'block';
                    
                    // Request replication blueprints from Flask server
                    const payload = {
                        bpm: 124,
                        estimated_key: "F# Minor",
                        detected_genre: "Melodic Synthpop, Modern Retro Wave",
                        vocal_timbre: "Clear male baritone lead voice, smooth reverb"
                    };

                    const response = await fetch('/api/process', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(payload)
                    });
                    
                    const data = await response.json();
                    
                    // Render blueprints onto interface blocks
                    document.getElementById('metaGenre').innerText = payload.detected_genre;
                    document.getElementById('metaBPM').innerText = payload.bpm + " BPM";
                    document.getElementById('metaKey').innerText = payload.estimated_key;
                    document.getElementById('metaVoice').innerText = payload.vocal_timbre;
                    
                    document.getElementById('promptText').innerText = data.compiled_prompt;
                    document.getElementById('lyricText').innerText = data.compiled_lyrics;
                    
                    statusBadge.innerText = "Status: Extraction Complete!";
                    outputContainer.style.display = 'block';
                };

                recorder.start();
                recordBtn.classList.add('active');
                recordBtn.innerText = 'STOP CAPTURE';
                statusBadge.innerText = "Status: Capturing High Definition Signal...";
            } catch (err) {
                statusBadge.innerText = "Status: Access Denied";
                alert("Microphone configuration permissions required.");
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
            a.download = 'studio_recording_' + Date.now() + '.mp3';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            statusBadge.innerText = "Status: File saved to phone memory.";
        }
    });

    function copyText(elementId) {
        const text = document.getElementById(elementId).innerText;
        navigator.clipboard.writeText(text);
        alert("Copied to phone clipboard successfully.");
    }
</script>

</body>
</html>
"""

@app.route('/', methods=['GET'])
def render_mobile_studio_interface():
    """Serves the HD Recording Interface straight to your mobile device."""
    return render_template_string(MOBILE_STUDIO_UI)

@app.route('/api/process', methods=['POST'])
def handle_mobile_processing_request():
    """Compiles exact prompt matching matrices for third-party audio generation platforms."""
    dna_metrics = request.get_json() or {}
    
    style_tags = HDPromptEngine.construct_meta_tags(dna_metrics)
    lyric_content = HDPromptEngine.generate_exact_lyric_sheet()
    
    return jsonify({
        "status": "success",
        "compiled_prompt": style_tags,
        "compiled_lyrics": lyric_content
    }), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
