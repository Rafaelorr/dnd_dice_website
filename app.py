from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "POST":
        dice = request.form.get("dice")
        dice = int(dice)
        extra = request.form.get("extra")
        aantal = request.form.get("aantal")
        aantal = int(aantal)
        resulaat = 0
        resulaat_temp : list[int] = [0,0]
        if extra == "advantage":
            for _ in range(aantal):
                resulaat_temp = [randint(1,dice),randint(1,dice)]
                if resulaat_temp[0] > resulaat_temp[1]:
                    resulaat += resulaat_temp[0]
                else:
                    resulaat += resulaat_temp[1]
        elif extra == "normal":
            for _ in range(aantal):
                resulaat += randint(1, dice)
        elif extra == "disadvantage":
            for _ in range(aantal):
                resulaat_temp = [randint(1,dice),randint(1,dice)]
                if resulaat_temp[0] < resulaat_temp[1]:
                    resulaat += resulaat_temp[0]
                else:
                    resulaat += resulaat_temp[1]
        if resulaat == 0:
            return render_template("home.html", resulaat="Fout")
        return render_template("home.html", resulaat=resulaat)     
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)