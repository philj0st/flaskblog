from flask import Flask
from pymongo import MongoClient
import os
import datetime
app = Flask(__name__)

client = MongoClient(os.environ['MONGODB_URI'])
db = client.flaskblog
@app.route("/")
def hello():
    # post = {"author": "Mike",
    #     "text": "My first blog post!",
    #     "tags": ["mongodb", "python", "pymongo"],
    #     "date": datetime.datetime.utcnow()}
    # post_id = db.posts.insert_one(post).inserted_id
    # print db.collection_names(include_system_collections=False)

    return db.posts.find_one({"author":"phip"})['text']

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'fetching Post %d from database' % post_id

if __name__ == "__main__":
    app.run(debug=True)
