#!/usr/bin/env python3


from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host="redis_1", port=6379)

@app.route("/")
def hi():
   hit = redis.incr("hits")
   return "hola! you're #{}".format(hit)

if __name__ == '__main__':
    print("use uWSGI")

