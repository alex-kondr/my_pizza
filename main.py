from flask import Flask, render_template


app = Flask(__name__)


@app.get("/")
def index():
    


    return render_template("index.html")


@app.get('/results/')
def results():
    context = {
        "max_score": 100,
        "test_name": "Python Challenge",
        "students": [
        {"name": "Vlad", "score": 100},
        {"name": "Sviatoslav", "score": 99},
        {"name": "Юстин", "score": 100},
        {"name": "Viktor", "score": 79},
        {"name": "Ярослав", "score": 93},
        ],
        "title": "Результати тестування"
    }

    return render_template("results.html", **context)


if __name__ == "__main__":
    app.run(debug=True)