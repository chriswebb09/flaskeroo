from wtforms import Form, TextField, TextAreaField, SubmitField, validators
class SearchForm(Form):
    subject = TextField("Search:  ")
    submit = SubmitField("Search")

class NavButtons(Form):
    about = SubmitField("What is Froleeyo about?")
    search = SubmitField("Check out a new project")
    searchone = SubmitField("Search for a new project!")

class ContactForm(Form):
    name = TextField("Name:", [validators.Required("Please enter your name.")])
    email = TextField("Email:", [validators.Required("Please enter your name.")])
    message_subject = TextField("Subject:", [validators.Required("Please enter your name.")])
    message = TextAreaField("Message:", [validators.Required("Please enter your name.")])
    send_message = SubmitField("Send Message")
