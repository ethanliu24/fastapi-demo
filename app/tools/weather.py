from pydantic import BaseModel, Field
from langchain_core.tools import tool

class SearchInput(BaseModel):
    location:str = Field(description="The city and state, e.g., San Francisco")
    date:str = Field(description="the forecasting date for when to get the weather format (yyyy-mm-dd)")

@tool("get_weather_forecast", args_schema=SearchInput, return_direct=True)
def get_weather_forecast(location: str, date: str):
    """
    Retrieves the weather using Open-Meteo API for a given location (city) and a date (yyyy-mm-dd).
    Returns a float the represents temperature in Celsius.
    Format your response like this:
    "The weather at `location` on `date` (in format such as May 5, 2020) is `temperature`C"
    """
    return 30
