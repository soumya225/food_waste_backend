import numpy as np
import math
from scipy.optimize import linprog
import food_item

class Day:
    minProtein = -100
    minFat = -50
    minCarb = -300
    
    
    def __init__(self, items):
        self.items = items

    def makeObjectiveArray(self):
        length = len(self.items)
        c = np.zeros(length)
        for i in range(length):
            c[i] = self.items[i].daysToExpiry
        print(c)
        return c

    def makeInequalityConstraintsLHS(self):
        length = len(self.items)
        A_ub = np.zeros((3, length))
        for i in range(length):
            A_ub[0,i] = self.items[i].protein * -1
            A_ub[1,i] = self.items[i].fat * -1
            A_ub[2,i] = self.items[i].carb * -1
        print(A_ub)
        return A_ub

    def makeBounds(self):
        bounds = []
        for i in range(len(self.items)):
            bounds.append((0,self.items[i].quantity))
        print(bounds)
        return bounds


    def solve(self):
        c = self.makeObjectiveArray()
        A_ub = self.makeInequalityConstraintsLHS()
        b_ub = np.array([self.minProtein, self.minFat, self.minCarb])

        bounds = self.makeBounds()
        self.result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds)

        print(self.result);

        x = self.result.x

        solution = {}
        for i in range(len(x)):
            solution[self.items[i].name] = round(x[i])

        return solution
        




#day = Day([food_item.FoodItem("Beans", 10, 2, 0, 20, 15),
#           food_item.FoodItem("Rice", 2, 1, 15, 20, 20),
#           food_item.FoodItem("Avocado", 2, 5, 5, 20, 20),
#           food_item.FoodItem("Bread", 4, 0, 10, 30, 7)])
#day.solve()
