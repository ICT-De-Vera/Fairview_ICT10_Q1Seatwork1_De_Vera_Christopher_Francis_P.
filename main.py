from js import document, parseFloat



name="Christopher Francis P. De Vera"
age=15
height=165.5
countries = ["China", "Japan", "France", "Germany", "Switzerland"]
student_type = False
dictionary = {
    "color": "white",
    "car_brand": "Toyota",
    "shoe_size": "8 us",
    "best_friend": "Carlos Ezikiel B. Boromeo",
}
fruits = {"avocado", "banana", "mango", "apple", "watermelon"}
days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")


def display():
    """Put the stored values into elements with matching IDs in index.html."""
    values = {
        "name": name,
        "age": age,
        "height": height,
        "countries": ", ".join(countries),
        "student_type": student_type,
        "color": dictionary["color"],
        "car_brand": dictionary["car_brand"],
        "shoe_size": dictionary["shoe_size"],
        "best_friend": dictionary["best_friend"],
        "fruits": ", ".join(sorted(fruits)),
        "days": ", ".join(days),
    }
    for element_id, value in values.items():
        element = document.getElementById(element_id)
        if element:
            element.innerText = str(value)


def calculate(event):
    event.preventDefault()
    num1 = parseFloat(document.getElementById("num1").value)
    num2 = parseFloat(document.getElementById("num2").value)
    operation = document.getElementById("operation").value
    calculation_result = None
    if operation == "add":
        calculation_result = num1 + num2
    elif operation == "subtract":
        calculation_result = num1 - num2
    elif operation == "multiply":
        calculation_result = num1 * num2
    elif operation == "divide":
        calculation_result = "Cannot divide by zero" if num2 == 0 else num1 / num2
    else:
        calculation_result = "Invalid operation"
    document.getElementById("result").innerText = "Result: " + str(calculation_result)



calculator_form = document.getElementById("calculator-form")
calculator_form.addEventListener("submit", calculate)
display()

