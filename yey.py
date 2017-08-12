from flask import Flask
from redis import Redis


app = Flask(__name__)

redis = Redis(host='redis', port=6379)

@app.route('/')

def yey():
    yey_count = redis.incr('yey_hits')
    hello_count = redis.get('hits').decode('utf-8')
    return 'YEEEY, you have been here {} times before!. Hello word has been seen {} times! Thats great!'.format(yey_count, hello_count)
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
