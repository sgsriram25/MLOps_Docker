from flask import Flask, request, render_template
import joblib
import pandas as pd
import os

app = Flask(__name__, template_folder="templates")

# Load model and encoders
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "artifacts"))
model_path = os.path.join(base_dir, "model.pkl")
encoders_path = os.path.join(base_dir, "encoders.pkl")

model = joblib.load(model_path)
encoders = joblib.load(encoders_path)

feature_columns = ["buying", "maint", "doors", "persons", "lug_boot", "safety"]

# Add after loading encoders
for col, le in encoders.items():
    print(f"{col}: {list(le.classes_)}")

# Friendly labels
friendly_labels = {
    "unacc": "Unacceptable Car",
    "acc": "Acceptable Car",
    "good": "Good Car",
    "vgood": "Very Good Car"
}

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    form_data = {}
    if request.method == "POST":
        try:
            input_dict = {}
            for col in feature_columns:
                value = request.form[col].strip()
                le = encoders[col]
                if value not in le.classes_:
                    raise ValueError(f"Invalid input for {col}: {value}")
                input_dict[col] = le.transform([value])[0]
                form_data[col] = value  # keep the selection

            input_df = pd.DataFrame([input_dict])
            pred = model.predict(input_df)[0]
            raw_label = encoders["class"].inverse_transform([pred])[0]
            prediction = friendly_labels.get(raw_label, raw_label)

            # Debug
            print(f"Encoded input: {input_dict}")
            print(f"Raw prediction: {pred}")
            print(f"Final prediction: {prediction}")

        except Exception as e:
            prediction = f"Error: {str(e)}"
            import traceback
            print(traceback.format_exc())

    # Dynamically generate dropdown options from encoders
    dropdown_options = {col: encoders[col].classes_ for col in feature_columns}

    return render_template(
        "predict.html",
        prediction=prediction,
        form_data=form_data,
        dropdown_options=dropdown_options
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)