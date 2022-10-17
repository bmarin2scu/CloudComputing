from flask import Flask, render_template
import requests
import json
import os

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def get_meal():
   response = requests.get('http://' + str(os.environ.get("API_HOST")) + ':' + str(os.environ.get("API_PORT")) + "/" + str(os.environ.get("API_ENDPOINT")))
   response = response.content
   response = json.loads(response)
   meal = response['Meal']
   price = response['Price']
   return render_template('yummy.html', meal = meal, price = price)

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=str(os.environ.get("CONSUMER_PORT")), debug=True)