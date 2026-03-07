import pandas as pd

class MovieRecommender:

    def __init__(self, rules_df):
        self.rules = rules_df

    # Recommend movies
    def recommend(self, movie):

        df = self.rules[self.rules["Movie1"].str.lower() == movie.lower()]

        if df.empty:
            return "Movie not found"

        df = df.sort_values(by="Lift", ascending=False)

        df = df.drop_duplicates(subset=["Movie2"])

        return df[["Movie2","Confidence","Lift"]].head(10)


    # Relation between two movies
    def relation(self, movie1, movie2):

        df = self.rules[
            (self.rules["Movie1"].str.lower() == movie1.lower()) &
            (self.rules["Movie2"].str.lower() == movie2.lower())
        ]

        if df.empty:
            return "No strong relation found"

        best = df.sort_values(by="Lift", ascending=False).iloc[0]

        return {
            "Support": best["Support"],
            "Confidence": best["Confidence"],
            "Lift": best["Lift"]
        }