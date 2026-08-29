from datetime import date
from utils import add, subtract, multiply, divide
print("Name: Fatihatun Nazat")
print("Today's date:", date.today())
print("Arithmetic operations :")
print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
try:
    print("Division:", divide(10, 2))
except ValueError as e:
    print("Error:", e)
try:
    print("Division:", divide(10, 0))
except ValueError as e:
    print("Error:", e)