from flask import Flask, render_template, request
import pickle
import pandas as pd

from model.recommender import MovieRecommender

app = Flask(__name__)

# load model
model = pickle.load(open("movie_model.pkl","rb"))

# create sorted movie list
movies = set(model.rules["Movie1"]).union(set(model.rules["Movie2"]))
movie_list = sorted(movies, key=str.lower)


@app.route("/", methods=["GET","POST"])
def index():

    result = None
    relation = None
    message = None

    if request.method == "POST":

        movie1 = request.form.get("movie1")
        movie2 = request.form.get("movie2")

        # single movie recommendation
        if movie1 and not movie2:

            res = model.recommend(movie1)

            if isinstance(res,str):
                message = res
            else:
                result = res.to_dict(orient="records")


        # two movie relation
        elif movie1 and movie2:

            rel = model.relation(movie1,movie2)

            if isinstance(rel,str):
                message = rel
            else:
                relation = rel


    return render_template(
        "index.html",
        movies=movie_list,
        result=result,
        relation=relation,
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)