from pyscript import display, document

# --- PART 1: Variable Declarations & Data Types ---

# 1. Variable with letters only
name = "Christopher Francis P. De Vera"  # Type: str

# 2. Variable with letters only
age = 15  # Type: int

# 3. Variable with letters and digits
height = 165.5  # Type: float

# 4. List variable representing countries to visit
countries = ["China", "Japan", "France", "Germany", "Switzerland"]  # Type: list

# 5. Student status boolean variable
student_type = False  # Type: bool

# 6. Dictionary variable with required keys
my_info = {
    "color": "Purple",
    "car_brand": "Toyota",
    "shoe_size": "8 us",
    "best_friend": "Carlos Ezikiel B. Boromeo",
}  # Type: dict

# 7. Set variable with favorite fruits
favorite_fruits = {"avocado", "banana", "mango", "apple", "watermelon"}  # Type: set

# 8. Tuple variable with seven days of the week
days_of_week = (
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
)  # Type: tuple
display(f"My Name is {name}", target="name")
display(f"I am {age} years old.", target="age")
display(f"My Height is {height} cm.", target="height")
display(f"Countries I want to visit: {', '.join(countries)}", target="countries")
display(f"Am I a New Student?: {'New Student' if student_type else 'Not a New Student'}", target="student_type")
display(f"My Favorite Color is: {my_info['color']}", target="color")
display(f"My Favorite Car Brand is: {my_info['car_brand']}", target="car_brand")
display(f"My Shoe Size is: {my_info['shoe_size']}", target="shoe_size")
display(f"My Best Friend is: {my_info['best_friend']}", target="best_friend")
display(f"My Favorite Fruits are: {', '.join(favorite_fruits)}", target="fruits")
display(f"Days I'm Available are: {', '.join(days_of_week)}", target="days")

# --- PART 2: Python Numbers Calculator --- 

# 1. Function to perform calculations based on user input
def solve(e):
    e.preventDefault()  # Prevent form submission and page reload
    number1 = float(document.getElementById("num1").value)
    number2 = float(document.getElementById("num2").value)
    Desired_Output = document.getElementById("operation").value

 # 2. Perform the desired operation based on user selection   
    if Desired_Output == "+":
        result = number1 + number2
    elif Desired_Output == "-":
        result = number1 - number2
    elif Desired_Output == "×":
        result = number1 * number2
    elif Desired_Output == "÷":
        result = number1 / number2

# 3. Display the result in the output div
    display(f"{number1} {Desired_Output} {number2} = {result}", target="output")
