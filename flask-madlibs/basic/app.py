from flask import Flask, render_template, request

from stories import story

app = Flask(__name__)




@app.route("/")
def ask_questions():
    """Generate form to and prompt for words."""

    prompts = story.prompts

    return render_template("questions.html", prompts=prompts)


@app.route("/story")
def show_story():
    """Show story result."""

    text = story.generate(request.args)

    return render_template("story.html", text=text)