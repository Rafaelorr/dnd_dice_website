from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)

def roll_dice(dice: int, mode: str) -> int:
    if mode == "advantage":
        return max(randint(1, dice), randint(1, dice))
    elif mode == "disadvantage":
        return min(randint(1, dice), randint(1, dice))
    else:  # normal
        return randint(1, dice)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            dice = int(request.form.get("dice"))
            amount = int(request.form.get("aantal"))
            mode = request.form.get("extra")
            modifier = int(request.form.get("modifier"))

            total = sum(roll_dice(dice, mode) for _ in range(amount)) + modifier

            result_text = f"{amount}d{dice} met {mode} = {total}"
            return render_template("home.html", resulaat=result_text)
        except (TypeError, ValueError):
            return render_template("home.html", resulaat="Er zijn fouten gebeurt")

    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
