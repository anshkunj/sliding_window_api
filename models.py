# models.py
from pydantic import BaseModel
class Array_input(BaseModel) :
	arr : list[int]
	k : int
class array_input(BaseModel) :
	arr : list[int]