from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    title = "The Polar Express"
    
    text = """It's 5 minutes to midnight on the Christmas Eve, and you hear a loud whistle blowing outside.
    You walk out of the front door and see an old-fashioned train. 
    The conductor says the train's going to the North Pole and suggests you take it."""

    choices = [
        ('take_train',"Take the train to go to the North Pole and meet Santa!"),
        ('wake_up',"Wake up!")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/train")
def take_train():
    title = "You take the train to the North Pole..."
    
    text = """... to meet new friends and share adventures onboard the Polar Express. 
    Eventually, you reach the North Pole, get to meet Santa and receive a bell from Santa's sleigh as the first gift of Christmas."""

    choices = [
        ('believe',"Seeing is believing!"),
        ('wake_up',"Realize you were dreaming the whole time.")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/wake_up")
def wake_up():
    title = "You wake up from your dream!"
    
    text = """You go back to your life and become a cold-hearted Scrooge :("""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/believing")
def believe():
    title = "You truly believe in Santa!"
    
    text = """Now you know, it doesn't matter where the train is going - what matters is deciding to get on. And while, over the years, the Christmas bell fell silent for most of your friends, it still rings for you."""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)
