from flask import Flask, render_template, request
# import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pik', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        age = request.form['age']
        exp = request.form['exp']

    input_arr = [[age, exp]]
    prediction = model.predict(input_arr)
    return render_template('predict.html', output=f'💵 ${float(prediction):0.2f}')


if __name__ == "__main__":
    app.run(debug=True)
