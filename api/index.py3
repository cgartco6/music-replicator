from flask import Flask, request, jsonify
from config import config
from core.prompt_engine import HDPromptEngine
import requests

# Essential definition instance named 'app' for serverless execution routing
app = Flask(__name__)

@app.route('/api/generate', methods=['POST'])
def handle_serverless_generation_request():
    request_payload = request.get_json() or {}
    
    bpm = request_payload.get("bpm", 120)
    estimated_key = request_payload.get("estimated_key", "C")
    detected_genre = request_payload.get("detected_genre", "Modern Beats")
    
    dna_metrics = {
        "bpm": bpm,
        "estimated_key": estimated_key,
        "detected_genre": detected_genre
    }
    
    style_tags = HDPromptEngine.construct_meta_tags(dna_metrics)
    lyric_content = HDPromptEngine.generate_exact_lyric_sheet()
    
    return jsonify({
        "status": "dry_run_success",
        "message": "Engine running smoothly. Serverless framework online.",
        "compiled_style_tags_used": style_tags,
        "compiled_lyrics_used": lyric_content
    }), 200

@app.route('/', methods=['GET'])
def handle_root_fallback():
    """Handles base URL queries directly to provide a validation checkpoint."""
    return jsonify({
        "status": "online",
        "system": "HD-Music-Replicator-Gateway",
        "active_endpoint": "/api/generate"
    }), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
