from flask import Flask, jsonify, request
from web_crawler import crawl

app = Flask(__name__)

@app.route('/')
def main_message():
    return jsonify('Welcome! Please send your requests to the /crawl with domain and depth parameters.')

@app.route('/crawl/', methods=['GET'])
def get_tasks():
    try:
        domain = request.args.get('domain')
        depth = request.args.get('depth')
        return jsonify(crawl(domain, depth))
    except:
        return jsonify('Something went wrong, please try again')

if __name__ == '__main__':
    app.run(threaded=True, port=5000)