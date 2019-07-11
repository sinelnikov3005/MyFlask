from flask import blueprints


posts = blueprints('posts', __name__, template_folder='templates')

@posts.rout('/')
def index():
    return render_template('posts/index.html')