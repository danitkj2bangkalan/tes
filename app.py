from flask import Flask, render_template, flash, request, redirect, url_for
from webforms import LoginForm
# membuat instance flask
app = Flask(__name__)
# untuk individual page
app.config['SECRET_KEY'] = "sahur amin"


@app.route("/materi")
def materi():
	return render_template("materi.html")

@app.route("/video")
def video():
	return render_template("video.html")

@app.route("/tugas")
def tugas():
	return render_template("tugas.html")

@app.route("/quiz")
def quiz():
	return render_template("quiz.html")

@app.route("/absen")
def absen():
	return render_template("absen.html")

@app.route("/referensi")
def referensi():
	return render_template("referensi.html")

@app.route("/pengaturan")
def pengaturan():
	return render_template("pengaturan.html")

@app.route("/daftar")
def daftar():
	return render_template("daftar.html")

@app.route("/lupasandi")
def lupasandi():
	return render_template("lupasandi.html")

@app.route("/guru")
def guru():
	return render_template("guru.html")

@app.route('/login',methods=['GET','POST'])
def login():
	form = LoginForm()
	username = None
	password = None
	if form.validate_on_submit():
		username = form.username.data
		password = form.password.data
		print(username,password)
		if username == 'amin' and password == 'amin':
			flash("Sudah bisa masuk min")
			return redirect(url_for('guru'))

	return (form)

@app.route("/")
def home():
	form = login()
	return render_template("home.html", form=form)

#membuat custom error pages
# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500
