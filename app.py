from flask import Flask, render_template,request
import json
app = Flask(__name__)

# Access the JSON File
# with open("greeting_images.json") as file:
#     images = json.load(file)



@app.route("/")
def index():
    return "Hello From Flask!"
   
@app.route('/card_generator', methods=['POST',"GET"])
def card_generator():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        card_selection = request.form['card_selection']
        font_selection = request.form['font_selection']

        # image_selection = request.form['image_selection']

        if card_selection == "bday":
            return render_template("bday_greeting_card.html",age=age,name=name,font=font_selection)
        elif card_selection == "xmas":
            return render_template("xmas_greeting_card.html",age=age,name=name,font=font_selection)

    else:
        return render_template("card_generator.html", images = images)
        # return render_template("card_generator.html")

if __name__ == '__main__':
    app.run(debug=True)