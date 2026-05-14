# 从flask工具包取出Flask功能（类）
# from flask import Flask, render_template
from flask import Flask, render_template, request, redirect, url_for
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

    if q2 == "A":
        score += 1
    else:
        score += 2

    if q3 == "A":
        score += 1
    else:
        score += 2

    if q4 == "A":
        score += 1
    else:
        score += 2

    if q5 == "A":
        score += 1
    else:
        score += 2

    if score >= 6:
        return redirect(url_for("success", score=score))
    else:
        return redirect(url_for("fail", score=score))

@app.route("/success")
def success():
    score = request.args.get("score")

    return f"""
    <div style="
        display:flex;
        justify-content:center;
        align-items:center;
        height:100vh;
        background:#f5f5f5;
        font-family:Arial;
    ">
        <div style="
            background:white;
            padding:40px;
            border-radius:12px;
            text-align:center;
            box-shadow:0 4px 12px rgba(0,0,0,0.1);
        ">
            <h2>✔ 通过测试,你从来都不会输，恭喜你，成为一位合格的三角洲嘉豪,允许进入网站！</h2>
            <p>你的分数：{score}</p>

            <a href="/" style="display:block;margin-top:10px;">进入网站</a>
        </div>
    </div>
    """


@app.route("/fail")
def fail():
    score = request.args.get("score")

    return f"""
    <div style="
        display:flex;
        justify-content:center;
        align-items:center;
        height:100vh;
        background:#f5f5f5;
        font-family:Arial;
    ">
        <div style="
            background:white;
            padding:40px;
            border-radius:12px;
            text-align:center;
            box-shadow:0 4px 12px rgba(0,0,0,0.1);
        ">
            <h2>❌ 未通过,你依然不够豪，继续沉淀!!!</h2>
            <p>你的分数：{score}</p>

            <a href="/quiz">再来一次</a>
        </div>
    </div>
    """

# ⭐ Railway 正确启动方式
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)