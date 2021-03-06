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
    template = env.get_template('post-overview.html')
    # sort by date descending and limit the result to 5
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
    # grab the post from the MongoDB
    post = db.posts.find_one({"id":post_id})
    template = env.get_template('post-detail.html')
    # show the post with the given id, the id is an integer
    return template.render(post)

if __name__ == "__main__":
    app.run(debug=True)
