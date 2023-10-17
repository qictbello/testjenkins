from flask import Flask, render_template, send_from_directory, url_for

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/backup")
def backup():
    return render_template("backup.html")

@app.route("/works")
def works():
    return render_template("works.html")

# Route to serve static images from the "public" folder
@app.route("/public/<path:filename>")
def public(filename):
    return send_from_directory("public", filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4040)
