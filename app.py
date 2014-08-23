#!/usr/bin/env python3


from flask import Flask
from redis import Redis

app = Flask("hello")
redis = Redis(host="redis_1", port=6379)

@app.route("/")
def hi():
   redis.incr("hits")
   return "hola!"

if __name__ == '__main__':
    print("use uWSGI")

