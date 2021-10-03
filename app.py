from flask import Flask, request
from flask_cors import CORS
import turicreate as tc

app = Flask(__name__)
CORS(app)

@app.route('/recomendaciones', methods=['POST'])
def recomendaciones():

        json_data = request.json

        data = tc.SFrame({'user_id': json_data["users"],
              	'item_id': json_data["places"],
              	'rating': json_data["ratings"]})

        m = tc.factorization_recommender.create(data, target='rating')

        recommendations = m.recommend([json_data["user"]])

        datos = []
        
        for i in recommendations:
                datos.append(i["item_id"])

        return {"data":datos}   

if __name__ == '__main__':
    app.run
