from flask import Flask
from pymongo import MongoClient
from jinja2 import Environment, PackageLoader
import os

# init globals
app = Flask(__name__)
client = MongoClient(os.environ['MONGODB_URI'])
env = Environment(loader=PackageLoader(__name__, 'templates'))
db = client.flaskblog

@app.route("/")
def index():
    template = env.get_template('index.html')
    postsCC = db.posts.aggregate(
      [
        { "$sort" : { "date" : -1 } },
        { "$limit" : 5 }
      ]
    )
    latestPosts = []
    for post in postsCC:
        latestPosts.append(post)
        print post
    return template.render({"posts":latestPosts})

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'fetching Post %d from database' % post_id

if __name__ == "__main__":
    app.run(debug=True)
