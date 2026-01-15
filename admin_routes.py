from flask import jsonify, request, session
import database
from datetime import datetime

def configure_admin_routes(app):
    @app.route('/api/admin/login', methods=['POST'])
    def login():
        data = request.json
        if data.get('user') == "admin" and data.get('pass') == "123":
            return jsonify({"status": "ok"})
        return jsonify({"status": "fail"}), 401

    @app.route('/api/admin/data')
    def admin_data():
        return jsonify(database.hospitals[0])

    @app.route('/api/admin/update', methods=['POST'])
    def admin_update():
        data = request.json
        h = database.hospitals[0]
        # Update all fields
        h['doctor'] = data.get('doctor')
        h['specialty'] = data.get('specialty')
        h['icu_beds'] = int(data.get('icu_beds'))
        h['amb_available'] = data.get('amb_status') == 'true'
        h['lat'] = data.get('lat')
        h['lng'] = data.get('lng')
        h['updated_at'] = datetime.now() # Resets the "Last Updated" timer
        return jsonify({"status": "success"})