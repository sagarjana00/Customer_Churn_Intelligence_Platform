import pandas as pd


def predict_customer(model, preprocessor, input_df):
    """
    Predict churn and churn probability for a customer.

    Parameters
    ----------
    model : trained ML model
        Loaded churn prediction model.

    preprocessor : fitted preprocessor
        Preprocessor used during model training.

    input_df : pandas.DataFrame
        Customer information in the original feature format.

    Returns
    -------
    prediction : int
        0 = No churn
        1 = Churn

    probability : float
        Probability of churn.
    """

    required_features = list(preprocessor.feature_names_in_)

    missing_features = [
        feature
        for feature in required_features
        if feature not in input_df.columns
    ]

    if missing_features:
        raise ValueError(
            f"Missing required features: {missing_features}"
        )

    input_df = input_df[required_features].copy()

    processed_input = preprocessor.transform(input_df)

    prediction = model.predict(processed_input)[0]

    probability = model.predict_proba(
        processed_input
    )[0][1]

    return prediction, probability