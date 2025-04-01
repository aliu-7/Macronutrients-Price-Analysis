from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the dataset
df = pd.read_csv("price_macros.csv")

@app.route("/")
def index():
    # Get top 5 cheapest items by price per kg
    cheapest_items = df.nsmallest(5, "Price per 100g")

    def best_macro_price(macro, min_macro=50):
        df_filtered = df[df["Item"] != "Coffee, 100%, ground roast"]  # Exclude coffee from macro leaderboards

        # Use different thresholds: 50g for carbs, 20g for protein and fats
        if macro in ["Protein (g)", "Fat (g)"]:
            min_macro = 20

        # Only keep foods that have at least the required grams per 100g
        df_filtered = df_filtered[df_filtered[macro] >= min_macro]

        # Calculate macro per dollar for display purposes
        df_filtered["macro_per_dollar"] = df_filtered[macro] / (df_filtered["Price per 100g"] * 10)  # Price per kg

        # Rank by price per kilogram (cheapest first)
        return df_filtered.nsmallest(3, "Price per 100g")[["Item", macro, "macro_per_dollar"]]

    best_protein = best_macro_price("Protein (g)")
    best_carbs = best_macro_price("Carbohydrates (g)")
    best_fats = best_macro_price("Fat (g)")

    # Get all food items for the "All Food Items" section
    all_food_items = df["Item"].tolist()

    return render_template(
        "index.html",
        cheapest_items=cheapest_items.to_dict(orient="records"),
        best_protein=best_protein.to_dict(orient="records"),
        best_carbs=best_carbs.to_dict(orient="records"),
        best_fats=best_fats.to_dict(orient="records"),
        all_food_items=all_food_items  # Sending all items
    )

@app.route("/get_food_items")
def get_food_items():
    food_items = df["Item"].tolist()
    return jsonify(food_items)

@app.route("/item/<item_name>")
def item_page(item_name):
    item_data = df[df["Item"] == item_name].to_dict(orient="records")
    if not item_data:
        return "Item not found", 404
    return render_template("item.html", item=item_data[0])

if __name__ == "__main__":
    app.run(debug=True)
