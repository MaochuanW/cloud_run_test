import os
import string
from flask import Flask, request
import psycopg2
app = Flask(__name__) 

@app.route('/City_Pred2022') #python decorator 
def City_pred2022(): #function that app.route decorator references
    connection = psycopg2.connect(host='spatialdb.gisandbox.org', database='wang8837', user='wang8837')
    cursor = connection.cursor()
    cursor.execute("SELECT json_build_object('type', 'FeatureCollection', 'features', json_agg(features.feature)::jsonb)"
            "FROM (SELECT jsonb_build_object('type', 'Feature', 'geometry', ST_AsGeoJSON(shape)::jsonb, 'properties', jsonb_build_object('gid', gid, 'city_name', city_name, 'population', population, 'pred_mc', pred_mc, 'pred_g', pred_g, 'pred_h', pred_h))::jsonb As feature FROM city_pred2022) features;")
    returns =cursor.fetchall()
    connection.close()
    return returns[0][0]




if __name__ == "__main__":
    app.run(
      debug=True, #shows errors 
      host='0.0.0.0', #tells app to run exposed to outside world
      port=int(os.environ.get("PORT", 8080))) #port = '5000'
