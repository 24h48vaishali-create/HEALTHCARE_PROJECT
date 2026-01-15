from flask import jsonify
import database 

def configure_routes(app):
    @app.route('/api/cases/<mode>')
    def get_cases(mode):
        return jsonify(database.emergency_cases if mode=='emergency' else database.non_emergency_cases)
    
    @app.route('/api/hospitals')
    def get_hospitals():
        return jsonify(database.hospitals)