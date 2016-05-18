from flask import Flask, render_template, flash, request, redirect
from forms import SearchForm, NavButtons, ContactForm

app = Flask(__name__)

@app.route('/')
def home():
    form = NavButtons()
    return render_template('home.html', form=form)

@app.route('/about')
def about():
    form = NavButtons()
    return render_template('about.html', form=form)

@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if request.method == "GET":
        return render_template('search.html', form=form)
    elif request.method == "POST":
        return redirect(url_for('results', search_term = request.form['subject']))

@app.route('/contact')
def contact():
    form = ContactForm()
    if request.method == "POST":
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            return render_template('contact.html', success=True)
    elif request.method == 'GET':
        return render_template('contact.html', form=form)
    return render_template('contact.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
