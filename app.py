# 从flask工具包取出Flask功能（类）
# from flask import Flask, render_template
from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route("/submit_quiz", methods=["POST"])
def submit_quiz():

    score = 0

    q1 = request.form.get("q1")
    q2 = request.form.get("q2")
    q3 = request.form.get("q3")
    q4 = request.form.get("q4")
    q5 = request.form.get("q5")

    if q1 == "B":
        score += 2
    else:
        score += 1

    if q2 == "B":
        score += 2
    else:
        score += 1

    if q3 == "B":
        score += 2
    else:
        score += 1

    if q4 == "B":
        score += 2
    else:
        score += 1

    if q5 == "B":
        score += 2
    else:
        score += 1

    if score < 6:
        return f"你的豪意值：{score}<br>你依然不够豪，继续沉淀"

    else:
        return f"你的豪意值：{score}<br>你从来都不会输，欢迎进入网站"

# ⭐ Railway 正确启动方式
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)