from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/bmi', methods=['POST'])
def calculate_bmi():
    data = request.get_json()
    height_cm = data.get('height')
    weight_kg = data.get('weight')

    if not height_cm or not weight_kg:
        return jsonify({"error": "Invalid input"}), 400

    height_m = height_cm / 100
    bmi = round(weight_kg / (height_m ** 2), 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 24.9:
        category = "Normal"
    elif bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    return jsonify({"bmi": bmi, "category": category})


@app.route('/daily-calories', methods=['POST'])
def daily_calories():
    data = request.get_json()
    age = data.get('age')
    weight = data.get('weight')
    height = data.get('height')
    gender = data.get('gender')
    activity = data.get('activity', 'sedentary')

    if not age or not weight or not height or not gender:
        return jsonify({"error": "Invalid input"}), 400

    if gender == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    activity_factors = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
        "very active": 1.9
    }

    calories = round(bmr * activity_factors.get(activity, 1.2), 2)

    return jsonify({"recommended_calories": calories})


@app.route('/diet-suggestion', methods=['POST'])
def diet_suggestion():
    data = request.get_json()
    goal = data.get('goal', 'maintain')

    suggestions = {
        "lose": "Try a calorie deficit of 500 calories per day. Focus on high-protein, low-carb meals.",
        "gain": "Add 300-500 calories per day. Focus on protein and healthy fats.",
        "maintain": "Eat balanced meals with vegetables, lean protein, and whole grains."
    }

    return jsonify({"suggestion": suggestions.get(goal, suggestions['maintain'])})


@app.route('/health-check', methods=['POST'])
def health_check():
    data = request.get_json()
    age = data.get('age')
    weight = data.get('weight')

    if not age or not weight:
        return jsonify({"error": "Invalid input"}), 400

    result = "Good" if age < 50 and 45 <= weight <= 90 else "Consider consulting a doctor."

    return jsonify({"status": result})


@app.route('/exercise-recommendation', methods=['GET'])
def exercise_recommendation():
    exercises = [
        "30-minute walk",
        "15-minute light jog",
        "10-minute stretching",
        "20 squats, 15 pushups, 10 sit-ups",
        "Dance to 3 of your favorite songs"
    ]
    return jsonify({"exercises": exercises})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)