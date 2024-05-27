from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)


@app.route('/')
def test_home():
    return render_template('homepage test copy 3.html')


@app.route("/aiportfolio")
def home_test():
    return render_template('ai copy 2.html')

@app.route('/uxrportfolio')
def nuxr_portfolio():
    return render_template('new_ai.html')


@app.route('/ai/uxr')
def cross_over():
    return render_template('aiuxr.html')


@app.route('/new_blog')
def new_blog_content():
    return render_template('new_blog.html')

@app.route('/project')
def project():
    return render_template('project_page1.html')


@app.route('/project2')
def project2():
    return render_template('project_page2.html')


@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy_policy.html')


# This is a practice section
@app.route('/home_old')
def home():
    return render_template('homepage.html')


@app.route('/blog')
def blog_content():
    return render_template('blog.html')


@app.route('/navigation')
def navigation():
    return render_template('navigation.html')


@app.route('/uxrportfolion')
def uxr_portfolio():
    return render_template('uxr2.html')



@app.route('/aiportfolion')
def ai_portfolio():
    return render_template('ai copy.html')








if __name__ == '__main__':
    app.run(debug=True, port=3000)