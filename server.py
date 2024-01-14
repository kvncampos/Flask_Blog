import datetime
from flask import Flask, render_template, url_for
import random
from api_tools.age_gender_api import *
from api_tools.blog_api import *

app = Flask(__name__,
            template_folder='templates',
            static_folder='static')


@app.route("/")
def hello_world():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    blog_link = url_for('blog')
    guess_link = url_for('guess')
    return render_template('index.html',
                           random_number=random_number,
                           copyright_year=current_year,
                           blog_url=blog_link,
                           guess_game=guess_link)


@app.route('/guess/')
@app.route('/guess/<name>', methods=['GET'])
def guess(name=None):
    home_page = url_for('hello_world')
    blog_link = url_for('blog')
    if name is not None:
        age = agify_api(name)
        gender = gender_api(name)
        return render_template('user_guess.html', name=name, age=age, gender=gender,
                               home_page=home_page, blog_url=blog_link)
    return render_template('user_guess.html', home_page=home_page, blog_url=blog_link)


@app.route('/blog')
@app.route('/blog/<int:num>')
def blog(num=None):
    blog_data = get_blogs('https://api.npoint.io/c790b4d5cab58020d391').json()
    home_page = url_for('hello_world')
    blog_link = url_for('blog')
    if num is not None:
        for each in blog_data:
            if each['id'] == num:
                blog_data = each
        return render_template('individual_blog.html', blog=blog_data, home_page=home_page,
                               blog_link=blog_link)
    return render_template('blogs.html', blogs=blog_data, home_page=home_page, blog_link=blog_link)


def each_blog():
    pass


if __name__ == '__main__':
    app.run(debug=True, port=5001)
    print(url_for('blogs'))
