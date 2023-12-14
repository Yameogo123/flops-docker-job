from pydantic import BaseModel
from typing import List, Any


class User(BaseModel):
    username: str 
    password: str


class Iris(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class Diabete(BaseModel):
    Pregnancies: float
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: float


class DataFrame(BaseModel):
    index: List[int]
    columns: List[str]
    data: List[List[Any]]