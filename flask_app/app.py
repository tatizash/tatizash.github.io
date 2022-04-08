from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def flask():
    title = "Flask App"
    text = "I'm here to learn"

    return render_template ('main.html', title=title, text=text)

@app.route("/fizzbuzz/<int:fizzbuzz_to>")
def fizzbuzz(fizzbuzz_to):
    l = []
    i = 1
    for i in range(1, fizzbuzz_to + 1):
        if i % 3 == 0 and i % 5 == 0:
            l.append('FizzBuzz') 
        elif i % 3 == 0:
                l.append('Fizz')
        elif i % 5 == 0:
                l.append('Buzz')
        else:
            l.append(i)

    return render_template ('fizzbuzz.html', last_number=fizzbuzz_to, numbers=l)

@app.route("/words")
def anagrams():
    return render_template ('anagrams.html')