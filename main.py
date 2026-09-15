import math
import result
import pyscript
import document
import display
import parseFloat
import event
import getElementById
import addEventListener
import preventDefault3



name="Christopher Francis P. De Vera"
age=15
height=165.5
list=["China", "Japan", "France", "Germany", "Switzerland"]
student_type="False"
dictionary={color: "white", car_brand: "Toyota",shoe_size: "8 us", best_friend: "Carlos Ezikiel B. Boromeo"} # 
set={avocado, banana, mango, apple, watermelon}
tuple=(Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday)
def calculate(event):
    event.preventDefault()
    num1 = parseFloat(document.getElementById("num1").value)
    num2 = parseFloat(document.getElementById("num2").value)
    operation = document.getElementById("operation").value
    let result
    if (operation === "add") {
        result = num1 + num2
    } else if (operation === "subtract") {
        result = num1 - num2
    } else if (operation === "multiply") {
        result = num1 * num2
    } else if (operation === "divide") {
        result = num1 / num2
    }
    document.getElementById("result").innerText = "Result: " + result



calculator_form = document.getElementById("calculator-form")
calculator_form.addEventListener("submit", calculate)

