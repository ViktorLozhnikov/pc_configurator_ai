from flask import Flask, jsonify, request, render_template
from compatibility import check_compatibility
from ai_build import chat_with_ai
from database import load_components
from flask import send_from_directory
import json
import os

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )

# Головна сторінка
@app.route('/')
def home():
    return render_template('index.html')

# Чат із AI
@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        if not user_message:
            return jsonify({"error": "Message is required"}), 400
        reply = chat_with_ai(user_message)
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/components', methods=['GET'])
def components():
    try:
        category = request.args.get('category')
        if not category:
            return jsonify({"error": "Category is required"}), 400
        components = load_components()
        return jsonify(components.get(category, []))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/builds', methods=['GET'])
def get_builds():
    try:
        # Зчитуємо дані з файлу ready_builds.json
        with open('backend/ready_builds.json', 'r', encoding='utf-8') as file:
            builds = json.load(file)
        return jsonify(builds["builds"])  # Повертаємо тільки список збірок
    except FileNotFoundError:
        return jsonify({"error": "Файл ready_builds.json не знайдено"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
   
@app.route('/compatibility', methods=['POST'])
def compatibility():
    try:
        data = request.json
        app.logger.debug(f"Received data: {data}")  # Логування отриманих даних
        components = data.get("components", {})
        if not components:
            raise ValueError("No components provided.")
        app.logger.debug(f"Components to check: {components}")
        compatibility = check_compatibility(components)
        app.logger.debug(f"Compatibility result: {compatibility}")
        return jsonify(compatibility)
    except Exception as e:
        app.logger.error(f"Error in compatibility check: {e}")
        return jsonify({"error": str(e)}), 500

app.logger.debug(f"Received data: {components}")

if __name__ == '__main__':
    app.run(debug=True)
