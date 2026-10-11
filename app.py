
from flask import Flask, request

app = Flask(__name__)


def calculate_result(mark1, mark2, mark3):
    total = mark1 + mark2 + mark3
    average = total / 3

    if average >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    return total, average, result


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        mark1 = float(request.form["mark1"])
        mark2 = float(request.form["mark2"])
        mark3 = float(request.form["mark3"])

        total, average, result = calculate_result(
            mark1, mark2, mark3
        )

        return (
            f"<h2>Student Result</h2>"
            f"<p>Name: {name}</p>"
            f"<p>Total: {total}</p>"
            f"<p>Average: {average:.2f}</p>"
            f"<p>Result: {result}</p>"
            f'<a href="/">Back</a>'
        )

    return """
    <h2>Student Result Application</h2>
    <form method="post">
        Student Name:
        <input type="text" name="name" required><br><br>

        Mark 1:
        <input type="number" name="mark1" min="0" max="100"
               step="any" required><br><br>

        Mark 2:
        <input type="number" name="mark2" min="0" max="100"
               step="any" required><br><br>

        Mark 3:
        <input type="number" name="mark3" min="0" max="100"
               step="any" required><br><br>

        <button type="submit">Calculate Result</button>
    </form>
    """


if __name__ == "__main__":
    app.run(debug=True)
