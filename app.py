# importing Flask and other modules
from flask import Flask, request, render_template 
from Ber import Predict
print("Have been trained the data,Please Go to the website below")
# Flask constructor
app = Flask(__name__) 

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
        first_name = request.form.get("contents")
        prediction = Predict(first_name)
        result = f"Esitmate ID: {prediction[0][0]}, Probability: {prediction[1][0]}"
        return result
    return render_template("register.html")

if __name__=='__main__':
    app.run()