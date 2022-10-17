from flask import Flask, request 
import random
import json
import os
app = Flask(__name__)

@app.route('/meal_rec')
def meal_pick():
    meals = [
    {'Meal': 'ramen',
     'Price': '$14'},
    {'Meal': 'fish and chips',
     'Price': '$15'},
    {'Meal': 'soup and sandwich',
     'Price': '$11'},
    {'Meal': 'chicken and waffles',
     'Price': '$18'},
    {'Meal': 'chilaquiles',
     'Price': '$15'},
    {'Meal': 'hamburger',
     'Price': '$11'},
    {'Meal': 'pizza',
     'Price': '$16'},
    {'Meal': 'chicken and rice',
     'Price': '$12'},
    {'Meal': 'sushi',
     'Price': '$38'},
   {'Meal': 'steak',
     'Price': '$88'},
   {'Meal': 'bangers and mash',
     'Price': '$15'},
   {'Meal': 'banh mi',
     'Price': '$9'},
   {'Meal': 'pho',
     'Price': '$14'},
   {'Meal': 'beef noodle soup',
     'Price': '$14'},
    {'Meal': 'lobster',
     'Price': '$88'},]
    meal_picked = random.choice(meals)
    return json.dumps(meal_picked)

if __name__ == '__main__':
    app.run(host="0.0.0.0")