import pandas as pd
import joblib
from datetime import datetime, timedelta


def get_forecast(input_dict):
    """
    Get forecasted values using a pre-trained model.

    This function loads a pre-trained XGBoost model and uses it to 
    predict values based on the input data provided. It transforms the 
    input data into a suitable format, creating features required by 
    the model for making predictions.

    Args:
        data (dict or pd.DataFrame): Input data containing 'hour_of_day' 
        'day_of_week', and 'day_of_year' keys/columns.

    Returns:
        np.ndarray: An array of predicted values based on the input data.
    """
    loaded_model = joblib.load('energy_consumption_forcaster.pkl')
    data = {key: [value] for key, value in input_dict.items()}
    input_df = pd.DataFrame(data)

    predictions = loaded_model.predict(input_df)
    return predictions[0]
