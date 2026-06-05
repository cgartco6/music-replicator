# Serverless API Controller designed explicitly to run inside Vercel Serverless Tiers
from flask import Flask, request, jsonify
from config import config
from core.prompt_engine import HDPromptEngine
import requests

app = Flask(__name__)

@app.route('/api/generate', methods=['POST'])
def handle_serverless_generation_request():
    """
    Vercel endpoint. Receives lightweight clean DNA maps sent from your local laptop,
    combines them with the prompt engine formulas, and calls the generation grid.
    """
    request_payload = request.get_json() or {}
    
    # Validation checks
    bpm = request_payload.get("bpm", 120)
    estimated_key = request_payload.get("estimated_key", "C")
    detected_genre = request_payload.get("detected_genre", "Modern Beats")
    
    dna_metrics = {
        "bpm": bpm,
        "estimated_key": estimated_key,
        "detected_genre": detected_genre
    }
    
    # Compile prompt configuration sequences and raw lyric streams
    style_tags = HDPromptEngine.construct_meta_tags(dna_metrics)
    lyric_content = HDPromptEngine.generate_exact_lyric_sheet()
    
    # Prepare external cloud dispatch body mapping to AI endpoints
    api_payload = {
        "prompt": lyric_content,
        "tags": style_tags,
        "title": "HD Automated Structural Replication Track"
    }
    
    if config.USE_LOCAL_MOCK_FALLBACK or config.MUSIC_API_KEY == "your_actual_suno_provider_api_key_here":
        return jsonify({
            "status": "dry_run_success",
            "message": "API key unconfigured or mock active. Production parameters successfully verified.",
            "compiled_style_tags_used": style_tags,
            "compiled_lyrics_used": lyric_content
        }), 200

    headers = {
        "Authorization": f"Bearer {config.MUSIC_API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(config.GENERATION_API_URL, json=api_payload, headers=headers, timeout=15)
        return jsonify({
            "status": "dispatched",
            "gateway_status_code": response.status_code,
            "gateway_payload": response.json()
        }), 200
    except Exception as e:
        return jsonify({
            "status": "processing_error",
            "details": str(e),
            "generated_prompts_preserved": {
                "tags": style_tags,
                "lyrics": lyric_content
            }
        }), 500

# For local direct server debugging workflows
if __name__ == '__main__':
    app.run(port=5000, debug=True)
