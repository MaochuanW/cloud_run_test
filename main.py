import os
from flask import Flask, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

@app.route('/City_Pred2022')
def City_pred2022():
    with psycopg2.connect(host='spatialdb.gisandbox.org', database='wang8837', user='wang8837') as connection:
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("SELECT json_build_object('type', 'FeatureCollection', 'features', json_agg(features.feature)::jsonb)"
                           "FROM (SELECT jsonb_build_object('type', 'Feature', 'geometry', ST_AsGeoJSON(geom)::jsonb, 'properties', jsonb_build_object('gid', gid, 'city_name', city_name, 'population', population, 'pred_mc', pred_mc, 'pred_g', pred_g, 'pred_h', pred_h))::jsonb As feature FROM city_pred2022) features;")
            result = cursor.fetchone()
            return jsonify(result)

if __name__ == "__main__":
    app.run(
        debug=True,
        host='0.0.0.0',
        port=int(os.environ.get("PORT", 8080))
    )
