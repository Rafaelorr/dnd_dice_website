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
            dice :int = int(request.form.get("dice"))
            amount :int = int(request.form.get("aantal"))
            mode :str = request.form.get("extra")
            modifier :int = int(request.form.get("modifier"))

            total :int = sum(roll_dice(dice, mode) for _ in range(amount)) + modifier

            result_text :str = f"{amount}d{dice} met {mode} = {total}"

            return render_template("home.html", resultaat=result_text)

        except Exception as ex:
            resultaat = f"Er is een fout gebeurd. Error: {ex}"

            return render_template("home.html", resultaat=resultaat)

    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
