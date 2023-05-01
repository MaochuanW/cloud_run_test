from flask import Flask, request
import os
import psycopg2

# Set Up Flask App
app = Flask(__name__)

# Define Routes
@app.route("/")
def home():
    return "GIS 5572 - Final - Maochuan Wang"

@app.route("/City_Pred2022", methods=['GET'])
def city_pred2022():
    connection = psycopg2.connect(
        host='35.223.186.20',
        database='postgres',
        user='postgres',
        password='139571wang'
    )
    cursor = connection.cursor()
    cursor.execute("""
        SELECT JSON_AGG(
            json_build_object(
                'type', 'Feature',
                'geometry', ST_AsGeoJSON(geom),
                'properties', jsonb_build_object(
                    'city_name', city_name,
                    'population', population,
                    'pred_mc', pred_mc,
                    'pred_g', pred_g,
                    'pred_h', pred_h
                )
            )
        )
        FROM city_pred2022;
    """)

    results = cursor.fetchall()
    connection.close()
    return results[0][0]

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
