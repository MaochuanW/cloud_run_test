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

@app.route("/City_Pred_2021June")
def city_pred_2021June():
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
    city_pred_0
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

@app.route("/City_Pred_2021July")
def city_pred_2023July():
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
    city_pred_1
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

@app.route("/City_Pred_2021August")
def city_pred_August():
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
    city_pred_2
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

@app.route("/City_Pred_2021September")
def city_Pred_2023sep():
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
    city_pred_3
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

@app.route("/Stinkbug_Priority")
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
    stinkbug_priority
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
