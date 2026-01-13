# models.py
from pydantic import BaseModel
from tying import List
class Array_input(BaseModel) :
	arr : List[int]
	k : int
class array_input(BaseModel) :
	arr : List[int]