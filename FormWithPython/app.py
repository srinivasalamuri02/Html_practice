from flask import Flask, render_template, request, jsonify



app = Flask(__name__)

@app.route("/")
def home() :
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit() :
    name = request.form.get("name")
    age = request.form.get("age")

    return jsonify({
        "message": "Form submitted successfully",
        "name": name,
        "age": age
    })

if __name__ == "__main__":
    app.run(debug=True)