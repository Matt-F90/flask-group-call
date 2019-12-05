import os
from flask import Flask, request, render_template


app = Flask(__name__)
@app.route('/')
def home_page():
    return "This is the home page"


@app.route('/europe')
def europe():
    return render_template('index.html')


the_title = "this is the about page"
info_about = "this is where you read about things"
some_stuff = "this be extra stuff and gubbins"


@app.route('/about')
def about():
    return render_template('about.html',
                           about_title=the_title,
                           about_info=info_about,
                           about_stuff=some_stuff)


@app.route('/north-america')
def northamerica():
    return "This is the north american home page"


@app.route('/Asia')
def asia():
    return "This is the asian home page"


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'), port=int(
        os.environ.get('PORT', '5000')), debug=True)
