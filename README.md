# Machine-Learning-for-Meal-Planning

This project analyzes the **cost-efficiency of common food items** in the United States by evaluating their **macronutrient content relative to price**. It's part of a broader effort to make nutrition **more affordable and accessible**, especially for students and individuals on a budget.

## Project Goals

- Convert USDA food price data into **standardized cost per gram**
- Merge with USDA nutrition databases to extract **protein, carb, and fat content**
- Rank food items by **macronutrient per dollar**
- Support future expansion into **personalized, cost-optimized meal planning**

## Data Sources

- `items_with_cost.csv` — Consumer food prices (with unit information like "per lb", "per oz")
- `food.csv` — USDA FoodData Central metadata with `fdc_id`
- `nutrient.csv` — Nutrient definitions and units (e.g., protein, fat, energy)
- `food_nutrient.csv` — Links each food item (`fdc_id`) to its nutrient contents

## Key Features

- **Unit normalization**: Converts price per lb or oz to **price per gram**
- **Nutrient merging**: Matches USDA food items with their macronutrient profiles
- **Cost-efficiency computation**: Calculates metrics like **grams of protein per dollar**
- **Ready for ML**: Cleaned dataset can feed into machine learning pipelines for optimization

## Visit A Demo:
  https://machine-learning-for-meal-planning.onrender.com/
