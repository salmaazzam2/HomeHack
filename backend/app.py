from flask import Flask, jsonify
from processing import load_data

app = Flask(__name__)

@app.route('/data')
def get_all_data():
    df = load_data()
    return jsonify(df.to_dict(orient="records"))

@app.route('/filter/<column>/<value>')
def filter_dynamic(column, value):
    df = load_data()
    filtered_df = smart_filter(df, column, value)
    return jsonify(filtered_df.to_dict(orient="records"))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

