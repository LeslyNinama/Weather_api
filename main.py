import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

variable = pd.read_csv("data/stations.txt", skiprows=17)
data_d = variable.loc[:, ['STAID', 'STANAME                                 ']]
@app.route("/")
def home():
    df = pd.read_csv("data/stations.txt", skiprows=20)
    return render_template("home.html", data=data_d.to_html())

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = f"data/TG_STAID{station.zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"]==date]["   TG"].squeeze()/10
    return {"Station": station,
            "Date": date,
            "Temperature": temperature}
@app.route("/api/v1/<station>")
def all_data(station):
    filename = f"data/TG_STAID{station.zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(orient="records")
    return result

@app.route("/api/v1/annual/<station>/<year>")
def all_year(station, year):
    filename = f"data/TG_STAID{station.zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df.loc[df["    DATE"].str.startswith(f"{year}")].to_dict(orient="records")
    return result


if __name__ == "__main__":
    app.run(debug=True)

