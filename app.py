from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import uvicorn

from model import DataInput
from utils import get_forecast


app = FastAPI()

@app.post("/predict")
def predict(data: DataInput):
    """
    Predict the output based on input features.

    Args:
        data (DataInput): The input data containing hour, day of week, and day of year.

    Returns:
        dict: A dictionary containing the prediction result.
    """
    try:
        input_data = data.dict()
        prediction = float(get_forecast(input_data))
        return JSONResponse(
            content={"prediction": prediction, "message": "Model has predicted successfully"},
            status_code=status.HTTP_200_OK
        )

    except Exception as e:
        return JSONResponse(
            content={"error": str(e), "message": "Prediction failed"},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
