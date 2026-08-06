import pandas as pd


def predict_customer(model, preprocessor, input_df):
    processed_input = preprocessor.transform(input_df)

    prediction = model.predict(processed_input)[0]
    probability = model.predict_proba(processed_input)[0][1]

    return prediction, probability