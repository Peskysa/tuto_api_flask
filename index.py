"""API didáctica local. SPDX-License-Identifier: AGPL-3.0-only."""
import math
from flask import Flask, jsonify, request

def create_app():
    app = Flask(__name__)
    app.config.update(MAX_CONTENT_LENGTH=4096, TRUSTED_HOSTS=['localhost', '127.0.0.1'])
    @app.get('/')
    def home():
        return '<h1>Hello, Pescaa!</h1><p>API de ejemplo de Marco Pescador. Consulta /health y POST /api/sumar.</p>'
    @app.get('/health')
    def health():
        return jsonify(status='ok', version='2.0.0')
    @app.post('/api/sumar')
    def sumar():
        if not request.is_json:
            return jsonify(error='Envía un objeto JSON.'), 415
        data = request.get_json(silent=True)
        if not isinstance(data, dict) or set(data) != {'a', 'b'}:
            return jsonify(error='Se requieren exactamente a y b.'), 400
        values = [data['a'], data['b']]
        try:
            valid = all(type(n) in (int, float) and math.isfinite(n) for n in values)
            total = sum(values) if valid else math.inf
            valid = valid and math.isfinite(total)
        except (TypeError, OverflowError):
            valid = False
        if not valid:
            return jsonify(error='Usa dos números finitos, sin booleanos.'), 400
        return jsonify(resultado=total)
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify(error='Petición no válida.'), 400
    @app.errorhandler(413)
    def too_large(error):
        return jsonify(error='Límite de petición: 4 KB.'), 413
    @app.after_request
    def headers(response):
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['Cache-Control'] = 'no-store'
        return response
    return app

app = create_app()
if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=False)
