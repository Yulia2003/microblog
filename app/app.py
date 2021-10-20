from flask import Flask, render_template , greet , db
app = Flask(__name__)
@app.route("/greet")
def greet():
	return render_template('index.html', name=username)
	if __name__ == "__main__":
		app.run()
