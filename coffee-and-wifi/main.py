from flask import Flask, render_template,redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField
from wtforms.validators import DataRequired,URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    lo = StringField('location', validators=[DataRequired(),URL()])
    open = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
    close = StringField("Closing Time e.g. 5:30PM", validators=[DataRequired()])
    Coffee=SelectField("COFFEE",choices=["☕☕☕☕☕","☕☕☕☕","☕☕☕","☕☕","☕","X"])
    wifi = SelectField("COFFEE", choices=["💪💪💪💪💪", "💪💪💪💪", "💪💪💪", "💪💪", "💪", "X"])
    power = SelectField("COFFEE", choices=["🔌🔌🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌", "🔌🔌", "🔌", "X"])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods=['POST','GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", mode="a", encoding="utf8") as file:
            file.write(f"\n{form.cafe.data},{form.lo.data},{form.open.data},{form.close.data},{form.Coffee.data},{form.wifi.data},{form.power.data}")
        return redirect("/cafes")

    return render_template('add.html', form=form)


@app.route('/cafes',methods=['POST','GET'])
def cafes():
    with open('cafe-data.csv', newline='',encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)

    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
