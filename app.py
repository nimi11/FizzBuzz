from flask import Flask, render_template
app = Flask(__name__)
@app.route("/fizzbuzz")
def fizzbuzz():
    numbers = []
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            numbers.append('FizzBuzz')
        elif num % 3 == 0:
            numbers.append('Fizz')
        elif num % 5 == 0:
            numbers.append('Buzz')
        else:
            numbers.append(num)
    
    return render_template("fizzbuzz_template.html", numbers=numbers)

if __name__ == "__main__":
    app.run(debug=True)