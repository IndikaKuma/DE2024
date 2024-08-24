# importing Flask and other modules

from flask import Flask, request, render_template, jsonify

# Flask constructor
app = Flask(__name__)


# A decorator used to tell the application
# which URL is associated function
@app.route('/checkdiabetes', methods=["GET", "POST"])
def check_diabetes():
    if request.method == "GET":
        return render_template("input_form_page.html")

    elif request.method == "POST":
        ntp = int(request.form.get("ntp"))  # getting input with name = ntp in HTML form
        pgc = int(request.form.get("pgc"))  # getting input with name = pgc in HTML form
        dbp = int(request.form.get("dbp"))
        tsft = int(request.form.get("tsft"))
        si = int(request.form.get("si"))
        bmi = float(request.form.get("bmi"))
        dpf = float(request.form.get("dpf"))
        age = int(request.form.get("age"))

        # we will replace this simple (and inaccurate logic) with a prediction from a machine learning model in a
        # future in a future lab
        if pgc > 120:
            prediction_value = True
        else:
            prediction_value = False

        return render_template("response_page.html",
                               prediction_variable=prediction_value)

    else:
        return jsonify(message="Method Not Allowed"), 405  # The 405 Method Not Allowed should be used to indicate
    # that our app that does not allow the users to perform any other HTTP method (e.g., PUT and  DELETE) for
    # '/checkdiabetes' path


# The code within this conditional block will only run the python file is executed as a
# script. See https://realpython.com/if-name-main-python/
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
