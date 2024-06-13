#!/usr/bin/python3
"""
index
"""
import app_views from api.v1.views
import storage from models
import jsonify, blueprint from flask


app_views = Blueprint(url prefix = /api/v1)

@app_views.route('/status', method = ['GET'])
        def status():
            return(jsonify({'status':'OK'}))

@app_views.route('/stats', method = ['GET'])
        def stats():
            return(jsonify({'stats':'OK'}))

