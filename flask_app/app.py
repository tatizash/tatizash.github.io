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

@app.route("/words/<string:word>")
def anagram (word):
    f = open('words.txt')

    word_list = f.read().splitlines()

    is_anagram = word.upper() in word_list

    anagrams = []
    for key in word_list:
        if sorted(word.upper()) == sorted(key):
            anagrams.append(key) 

    return render_template ('anagrams.html', word=word, is_anagram=is_anagram, anagrams=anagrams)

@app.route("/dictionary/<string:prefix>")
def search_for(prefix):

    alphabet = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}
    
    strings = []
    for key, val in alphabet.items():
        strings.append(prefix + val)

    f = open('words.txt')

    word_list = f.read().splitlines()

    is_real = prefix.upper() in word_list

    count=0
    for word in word_list:
        if word.startswith(prefix.upper()):
            count+=1


    return render_template ('dictionary.html', prefix=prefix, strings=strings, is_real=is_real, count=count)