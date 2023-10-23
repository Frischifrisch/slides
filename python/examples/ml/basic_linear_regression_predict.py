from joblib import load
import sys

if len(sys.argv) < 2:
    exit(f"Usage: {sys.argv[0]} Xes")

input_values = [[float(val)] for val in sys.argv[1:]]
model = load('linear.joblib')
print(model.predict(input_values))
