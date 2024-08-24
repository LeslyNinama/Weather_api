import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

variable = pd.read_csv("data_small/stations.txt", skiprows=20)
data_d = variable.loc[:, ['STAID', 'STANAME                                 ']]
@app.route("/")
def home():
   # df = pd.read_csv("data_small/stations.txt", skiprows=20)
    return render_template("home.html", data=data_d.to_html())

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = f"data_small/TG_STAID{station.zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"]==date]["   TG"].squeeze()/10
    return {"Station": station,
            "Date": date,
            "Temperature": temperature}
if __name__ == "__main__":
    app.run(debug=True)

