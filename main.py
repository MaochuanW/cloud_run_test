from flask import Flask, request
import os
import psycopg2
import string

# Set Up Flask App
app = Flask(__name__)

# Define Routes
@app.route("/")
def home():
    return "GIS 5572 - Final - Maochuan Wang"

@app.route("/City_Pred2022")
def city_pred2022():
    connection = psycopg2.connect(
        host='spatialdb.gisandbox.org',
        database='wang8837',
        user='wang8837',
        password='student'
    )
    cursor = connection.cursor()
    cursor.execute("""
        WITH data AS (
  SELECT
    city_name,
    population,
    pred_mc,
    pred_g,
    pred_h,
    ST_AsGeoJSON(geom)::json AS geometry
  FROM
    city_pred2022
)

SELECT json_build_object(
  'type', 'FeatureCollection',
  'features', json_agg(
    json_build_object(
      'type', 'Feature',
      'geometry', geometry,
      'properties', json_build_object(
        'city_name', city_name,
        'population', population,
        'pred_mc', pred_mc,
        'pred_g', pred_g,
        'pred_h', pred_h
      )
    )
  )
) AS geojson
FROM data;

    """)

    results = cursor.fetchall()
    connection.close()
    return results[0][0]

@app.route("/City_Pred2023")
def city_pred2023():
    connection = psycopg2.connect(
        host='spatialdb.gisandbox.org',
        database='wang8837',
        user='wang8837',
        password='student'
    )
    cursor = connection.cursor()
    cursor.execute("""
        WITH data AS (
  SELECT
    city_name,
    population,
    pred_mc,
    pred_g,
    pred_h,
    ST_AsGeoJSON(geom)::json AS geometry
  FROM
    city_pred2023
)

SELECT json_build_object(
  'type', 'FeatureCollection',
  'features', json_agg(
    json_build_object(
      'type', 'Feature',
      'geometry', geometry,
      'properties', json_build_object(
        'city_name', city_name,
        'population', population,
        'pred_mc', pred_mc,
        'pred_g', pred_g,
        'pred_h', pred_h
      )
    )
  )
) AS geojson
FROM data;

    """)

    results = cursor.fetchall()
    connection.close()
    return results[0][0]

@app.route("/City_Pred2024")
def city_pred2024():
    connection = psycopg2.connect(
        host='spatialdb.gisandbox.org',
        database='wang8837',
        user='wang8837',
        password='student'
    )
    cursor = connection.cursor()
    cursor.execute("""
        WITH data AS (
  SELECT
    city_name,
    population,
    pred_mc,
    pred_g,
    pred_h,
    ST_AsGeoJSON(geom)::json AS geometry
  FROM
    city_pred2024
)

SELECT json_build_object(
  'type', 'FeatureCollection',
  'features', json_agg(
    json_build_object(
      'type', 'Feature',
      'geometry', geometry,
      'properties', json_build_object(
        'city_name', city_name,
        'population', population,
        'pred_mc', pred_mc,
        'pred_g', pred_g,
        'pred_h', pred_h
      )
    )
  )
) AS geojson
FROM data;

    """)

    results = cursor.fetchall()
    connection.close()
    return results[0][0]

@app.route("/City_Sim")
def city_sim():
    connection = psycopg2.connect(
        host='spatialdb.gisandbox.org',
        database='wang8837',
        user='wang8837',
        password='student'
    )
    cursor = connection.cursor()
    cursor.execute("""
        WITH data AS (
  SELECT
    city_name,
    population,
    sim_mc,
    sim_g,
    sim_h,
    ST_AsGeoJSON(geom)::json AS geometry
  FROM
    city_sim
)

SELECT json_build_object(
  'type', 'FeatureCollection',
  'features', json_agg(
    json_build_object(
      'type', 'Feature',
      'geometry', geometry,
      'properties', json_build_object(
        'city_name', city_name,
        'population', population,
        'sim_mc', sim_mc,
        'sim_g', sim_g,
        'sim_h', sim_h
      )
    )
  )
) AS geojson
FROM data;

    """)

    results = cursor.fetchall()
    connection.close()
    return results[0][0]

@app.route("/final_stinkbug")
def final_stinkbug():
    connection = psycopg2.connect(
        host='spatialdb.gisandbox.org',
        database='wang8837',
        user='wang8837',
        password='student'
    )
    cursor = connection.cursor()
    cursor.execute("""
        WITH data AS (
  SELECT
    city_name,
    population,
    priority,
    ST_AsGeoJSON(geom)::json AS geometry
  FROM
    final_stinkbug
)

SELECT json_build_object(
  'type', 'FeatureCollection',
  'features', json_agg(
    json_build_object(
      'type', 'Feature',
      'geometry', geometry,
      'properties', json_build_object(
        'city_name', city_name,
        'population', population,
        'priority', priority
      )
    )
  )
) AS geojson
FROM data;

    """)

    results = cursor.fetchall()
    connection.close()
    return results[0][0]

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
