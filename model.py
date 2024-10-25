# models.py
from pydantic import BaseModel

class DataInput(BaseModel):
    """
    Data model for the input data to the prediction endpoint.

    Attributes:
        hour_of_day (int): The hour of the day (0-23).
        day_of_week (int): The day of the week (0-6, where 0 is Sunday).
        day_of_year (int): The day of the year (1-365 or 1-366 for leap years).
    """
    hour_of_day: int
    day_of_week: int
    day_of_year: int
