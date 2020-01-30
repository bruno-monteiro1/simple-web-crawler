from flask import Flask, jsonify, request
from web_crawler import crawl

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_tasks():
    try:
        domain = request.args.get('domain')
        depth = request.args.get('depth')
        return jsonify(crawl(domain, depth))
    except:
        return jsonify("Something went wrong, please try again")

if __name__ == '__main__':
    app.run(debug=True)