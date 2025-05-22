from flask import Flask, jsonify

app = Flask(__name__)

Mobile = [
    "Apple",
    "Samsung",
    "Google Pixel",
    "Oneplus",
    "Realme",
    "Motorola",
    "Vivo",
    "Oppo",
    "Redmi",
    "POCO"
]

@app.route('/mobile', methods=['GET'])
def get_anime():
    print("GET /anime request received")
    return jsonify(Mobile)

if __name__ == '__main__':
    print("Starting Flask server on http://0.0.0.0:3000")
    app.run(host='0.0.0.0', port=3000, debug=True)