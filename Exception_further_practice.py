# Raising Custom Exceptions
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above")
    return "Access granted"


try:
    print(check_age(16))
except ValueError as e:
    print(f"Exception: {e}")
    




# Custom Exception Class
class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom exception!")
except CustomError as e:
    print(f"Caught an exception: {e}")
    



# Real time usage of Exception Class (Check age)
class CustomAgeException(Exception):
    """ Custom Exception for Invalid age """
    def __init__(self,age,message="Age must be 18 or above to register."):
        self.age=age
        self.message=message
        super().__init__(f"{message} Given age: {age}")

def register_user(age):
    if age < 18:
        raise CustomAgeException(age)
    return "User registered successfully!"

try:
    print(register_user(20))
    print(register_user(16))
except CustomAgeException as e:
    print(f"Registration Error: {e}")
