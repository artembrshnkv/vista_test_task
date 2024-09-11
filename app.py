from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap

from config_reader import secret_key
from models import get_all_wishes, create_wish, \
    update_wish_by_id, delete_wish_by_id
from forms import CreateWishForm, UpdateWishForm, DeleteWishForm

app = Flask(__name__)
app.config["SECRET_KEY"] = secret_key
bootstrap = Bootstrap(app)

menu = [
    {"title": "All wishes", "url": "wish_list"},
    {"title": "Create wish", "url": "create_wish_by_id"},
    {"title": "Update wish", "url": "update_wish_by_id"},
    {"title": "Delete wish", "url": "delete_wish_by_id"}
]


@app.route('/')
@app.route('/wish_list')
def wish_list():
    all_wishes = get_all_wishes()
    return render_template("all_wishes.html", menu=menu, all_wishes=all_wishes)


@app.route('/create_wish_by_id', methods=['GET', 'POST'])
def create_wish_by_id():
    form = CreateWishForm()
    if form.validate_on_submit():
        create_wish(
            title=form.title.data,
            price=form.price.data,
            url=form.url.data,
            note=form.note.data
        )
        return redirect('/wish_list')

    return render_template("create_wish_by_id.html", menu=menu, form=form)


@app.route('/update_wish_by_id', methods=['GET', 'POST'])
def update_wish():
    form = UpdateWishForm()
    if form.validate_on_submit():
        update_wish_by_id(
            wish_id=form.wish_id.data,
            title=form.title.data,
            price=form.price.data,
            url=form.url.data,
            note=form.note.data
        )
        return redirect('/wish_list')

    return render_template("update_wish_by_id.html", menu=menu, form=form)


@app.route('/delete_wish_by_id', methods=['GET', 'POST'])
def delete_wish():
    form = DeleteWishForm()
    if form.validate_on_submit():
        delete_wish_by_id(wish_id=form.wish_id.data)
        return redirect('/wish_list')

    return render_template("delete_wish_by_id.html", menu=menu, form=form)


if __name__ == '__main__':
    app.run(debug=True)
