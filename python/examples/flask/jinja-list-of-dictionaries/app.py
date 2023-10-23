from flask import Flask, render_template
import csv
app = Flask(__name__)

@app.route("/")
def main():
    planets = read_csv_file('planets.csv')

    return render_template('main.html',
        title     = "Planets",
        planets   = planets,
    )

def read_csv_file(filename):
    planets = []
    with open(filename) as fh:
        rd = csv.DictReader(fh, delimiter=',')
        planets.extend(iter(rd))
    return planets
