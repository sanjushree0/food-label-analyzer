

from flask import Flask, request, jsonify
from flask_cors import CORS
import easyocr
import base64
import os
import time

app = Flask(__name__)
CORS(app)

# Initialize EasyOCR model (PyTorch engine, bypasses all Intel MKL bugs!)
print("Initializing EasyOCR Engine...")
reader = easyocr.Reader(['en'])
print("EasyOCR Initialized successfully!")

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "service": "easyocr"}), 200

@app.route('/ocr', methods=['POST'])
def process_ocr():
    try:
        data = request.json
        if not data or 'image' not in data:
            return jsonify({"error": "No base64 image provided"}), 400
            
        base64_img = data['image']
        
        # Strip potential data URI prefix
        if "," in base64_img:
            base64_img = base64_img.split(",")[1]
            
        file_path = f"tmp_upload_{int(time.time())}.jpg"
        
        # Save temp image for analysis
        with open(file_path, "wb") as fh:
            fh.write(base64.b64decode(base64_img))
            
        # Run PyTorch inference
        result = reader.readtext(file_path)
        
        # Cleanup temp file
        if os.path.exists(file_path):
            os.remove(file_path)
            
        # Extract purely the text from the EasyOCR output
        # Result format: [([[x, y]...], 'text', confidence), ...]
        extracted_lines = []
        if result:
            for line in result:
                text = line[1]
                extracted_lines.append(text)
                
        # Join lines with newlines so the Javascript NLP can parse it properly
        final_text = "\n".join(extracted_lines)
        
        return jsonify({
            "success": True,
            "text": final_text
        }), 200
        
    except Exception as e:
        print(f"OCR Error: {str(e)}")
        # Cleanup on fail
        if 'file_path' in locals() and os.path.exists(file_path):
            os.remove(file_path)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Force port 5001 as required by the backend
    app.run(host='0.0.0.0', port=5001, debug=False)
