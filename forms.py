from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class CreateWishForm(FlaskForm):
    title = StringField("Title: ", validators=[DataRequired()])
    price = IntegerField(
        "Price: ",
        validators=[DataRequired(),
                    NumberRange(min=0)]
    )
    url = StringField("Url: ", validators=[DataRequired()])
    note = StringField("Note: ")
    submit = SubmitField("Create wish")


class UpdateWishForm(FlaskForm):
    wish_id = IntegerField(
        'Wish id:',
        validators=[DataRequired(),
                    NumberRange(min=0)]
    )
    title = StringField("Title: ")
    price = IntegerField("Price: ")
    url = StringField("Url: ")
    note = StringField("Note: ")
    submit = SubmitField("Update wish")


class DeleteWishForm(FlaskForm):
    wish_id = IntegerField(
        'Wish id:',
        validators=[DataRequired(),
                    NumberRange(min=0)]
    )
    submit = SubmitField("Delete wish")
