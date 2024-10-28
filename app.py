from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    return render_template("hello.html", name=input_name, age=input_age)


def output_the_largest_number(input_string):
    string_list = input_string.split(",")
    num1 = int(string_list[0][-2:])
    num2 = int(string_list[1][-2:])
    num3 = int(string_list[2][:-1])
    max_num = num1
    if max_num < num2:
        max_num = num2
    if max_num < num3:
        max_num = num3
    return max_num


def add_two_number(input_string):
    string_list = input_string.split("plus")
    num1 = int(string_list[0][-3:])
    num2 = int(string_list[1][:-1])
    sum1 = num1 + num2
    return sum1


def multiply_two_number(input_string):
    string_list = input_string.split("multiplied by")
    num1 = int(string_list[0][-3:])
    num2 = int(string_list[1][:-1])
    product1 = num1 * num2
    return product1


def find_square_and_cube(input_string):
    string_list = input_string.split(":")
    string_list2 = string_list[1].split(",")
    string_list2[-1] = string_list2[-1][:-1]
    for i in range(7):
        k = int(string_list2[i])
        string_list2[i] = k
        residue1 = round(k ** (1/2))
        residue2 = round(k ** (1/3))
        if (residue1 ** 2 == k) and (residue2 ** 3 == k):
            return k


def process_query(content):
    if content == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    elif content == "asteroids":
        return "Unknown"
    elif content == "What is your name?":
        return "qz824"
    elif "largest" in content:
        return str(output_the_largest_number(content))
    elif "plus" in content:
        return str(add_two_number(content))
    elif "multiplied" in content:
        return str(multiply_two_number(content))
    elif "square" in content:
        return str(find_square_and_cube(content))
    return "Unrecorded query, sorry"


@app.route("/query", methods=["GET"])
def query_route():
    query_param = request.args.get("q")

    if query_param:
        result = process_query(query_param)
        return result
    else:
        return "No query parameter required", 400
