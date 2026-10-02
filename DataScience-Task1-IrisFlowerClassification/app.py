import gradio as gr
import joblib
import pandas as pd


# Load trained KNN model
model = joblib.load("iris_flower_classifier.pkl")


# Iris species
species = {
    0: "Setosa",
    1: "Versicolor",
    2: "Virginica"
}


def predict_iris(sepal_length, sepal_width, petal_length, petal_width):

    input_data = pd.DataFrame(
        [[
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        ]],
        columns=[
            "sepal length (cm)",
            "sepal width (cm)",
            "petal length (cm)",
            "petal width (cm)"
        ]
    )

    prediction = model.predict(input_data)
    probabilities = model.predict_proba(input_data)[0]

    predicted_species = species[prediction[0]]

    probability_output = {
        species[i]: float(probabilities[i])
        for i in range(3)
    }

    return predicted_species, probability_output


# Create Gradio interface
demo = gr.Interface(
    fn=predict_iris,
    inputs=[
        gr.Number(
            label="Sepal Length (cm)",
            value=5.1
        ),
        gr.Number(
            label="Sepal Width (cm)",
            value=3.5
        ),
        gr.Number(
            label="Petal Length (cm)",
            value=1.4
        ),
        gr.Number(
            label="Petal Width (cm)",
            value=0.2
        )
    ],
    outputs=[
        gr.Textbox(label="Predicted Iris Species"),
        gr.Label(label="Prediction Probabilities")
    ],
    title="🌸 Iris Flower Classification",
    description=(
        "Enter the sepal and petal measurements to predict "
        "the Iris flower species using a tuned KNN model."
    ),
    examples=[
        [5.1, 3.5, 1.4, 0.2],
        [6.0, 2.9, 4.5, 1.5],
        [6.5, 3.0, 5.2, 2.0]
    ]
)


if __name__ == "__main__":
    demo.launch()