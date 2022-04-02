# Butler food schedule API

To use the API, a POST request has to be sent to https://food-expiry-tracker.herokuapp.com/schedule with a JSON array as body. 
An example request body is presented below:
</br>
[
    {
        "name": "Carrot",
        "protein": 2,
        "fat": 2,
        "carb": 6,
        "quantity": 30,
        "daysToExpiry": 6
    },
    {
        "name": "Potato",
        "protein": 4,
        "fat": 6,
        "carb": 15,
        "quantity": 10,
        "daysToExpiry": 9
    },
    {
        "name": "Beans",
        "protein": 20,
        "fat": 15,
        "carb": 4,
        "quantity": 15,
        "daysToExpiry": 20
    },
    {
        "name": "Avocado",
        "protein": 5,
        "fat": 10,
        "carb": 6,
        "quantity": 5,
        "daysToExpiry": 2
    }
]

Note that the Flutter application that uses this API can be found at https://github.com/soumya225/food_waste/


