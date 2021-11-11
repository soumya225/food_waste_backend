from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask import request
import pandas as pd
import ast
import food_item as f
import day as d

app = Flask(__name__)
api = Api(app)

class Schedule(Resource):
    def post(self):
        print(request.json)

        json = request.json #list of food items
        food_items = []

        for i in range(len(json)):
            food_items.append(f.FoodItem(
                json[i]["name"],
                json[i]["protein"],
                json[i]["fat"],
                json[i]["carb"],
                json[i]["quantity"],
                json[i]["daysToExpiry"]))

        day = d.Day(food_items)
        solution = day.solve()
        
        return solution, 200
    

api.add_resource(Schedule, '/schedule') 

if __name__ == '__main__':
    app.run()
