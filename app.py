from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# HTML template for the calculator
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask Calculator</title>
</head>
<body>
    <h1>Flask Calculator</h1>
    <form action="/" method="post">
        <label for="num1">Enter first number:</label><br>
        <input type="text" id="num1" name="num1" required><br><br>
        <label for="num2">Enter second number:</label><br>
        <input type="text" id="num2" name="num2" required><br><br>
        <label for="operation">Choose an operation:</label><br>
        <select id="operation" name="operation" required>
            <option value="add">Add</option>
            <option value="subtract">Subtract</option>
            <option value="multiply">Multiply</option>
            <option value="divide">Divide</option>
        </select><br><br>
        <button type="submit">Calculate</button>
    </form>
    <br>
    {% if result is not none %}
        <h3>Result: {{ result }}</h3>
    {% endif %}
    {% if error is not none %}
        <h3 style="color: red;">Error: {{ error }}</h3>
    {% endif %}
</body>
</html>
"""


# Calculator route
@app.route("/", methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        try:
            # getting form data
            operation = request.form.get("operation")
            num1 = float(request.form.get("num1"))
            num2 = float(request.form.get("num2"))

            # perform the calculation
            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 == 0:
                    return render_template_string(
                        html_template,
                        error="Division by zero is not allowed",
                        result=None,
                    )
                result = num1 / num2
            else:
                return render_template_string(
                    html_template, error="Invalid operation", result=None
                )

            # Render the result in the template
            return render_template_string(html_template, result=result, error=None)
        except ValueError:
            return render_template_string(
                html_template,
                error="Invalid input. Please enter numeric values.",
                result=None,
            )
    return render_template_string(html_template, result=None, error=None)


if __name__ == "__main__":
    app.run("0.0.0.0", port=80, debug=True)
