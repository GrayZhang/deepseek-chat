from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

DEEPSEEK_API_URL = 'https://api.deepseek.com/your-endpoint'  # 请替换为实际的 DeepSeek API URL

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    # 调用 DeepSeek API
    response = requests.post(DEEPSEEK_API_URL, json={'message': user_message})
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
