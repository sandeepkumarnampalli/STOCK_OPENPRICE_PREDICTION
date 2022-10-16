from flask import Flask,render_template,request
app = Flask(__name__)

#initialize ml model
from joblib import dump, load
# load the saved model
stock_app = load('escorts_prediction.joblib')

@app.route('/', methods=['POST', 'GET'])
def home():
    home_page = '<html><h1>STOCK OPEN PRICE PREDICTION APPLICATION</h1><body><a href="/stock_data.html">Click here to get your Stock Open Price Prediction</a></html>'
    return home_page


@app.route('/stock_data.html', methods=['POST', 'GET'])
def predict_stock():
    cl = 0
    nif = 0
    stock_open = 'NA'
    if request.method == 'POST':
        cl = float(request.form['close'])
        nif = float(request.form['nifty'])
        print(cl, nif)
        # step 5 -- predicting outcome with new data
        stock_open = stock_app.predict([[cl, nif]])

    return render_template('stock_data.html', cl=cl, nif=nif, stock_open=stock_open)


if __name__ == '__main__':
    app.run(debug=True)