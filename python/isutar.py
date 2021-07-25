from flask import Flask, request, jsonify, abort
import MySQLdb.cursors
import os
import html
import urllib

app = Flask(__name__)

_config = {
    'db_host':       os.environ.get('ISUDA_DB_HOST', 'localhost'),
    'db_port':       int(os.environ.get('ISUDA_DB_PORT', '3306')),
    'db_user':       os.environ.get('ISUDA_DB_USER', 'root'),
    'db_password':   os.environ.get('ISUDA_DB_PASSWORD', ''),
    'isupam_origin': os.environ.get('ISUPAM_ORIGIN', 'http://localhost:5050'),
}

def config(key):
    if key in _config:
        return _config[key]
    else:
        raise "config value of %s undefined" % key

def dbh():
    if hasattr(request, 'db'):
        return request.db
    else:
        request.db = MySQLdb.connect(**{
            'host': config('db_host'),
            'port': config('db_port'),
            'user': config('db_user'),
            'passwd': config('db_password'),
            'db': 'isuda',
            'charset': 'utf8mb4',
            'cursorclass': MySQLdb.cursors.DictCursor,
            'autocommit': True,
        })
        cur = request.db.cursor()
        cur.execute("SET SESSION sql_mode='TRADITIONAL,NO_AUTO_VALUE_ON_ZERO,ONLY_FULL_GROUP_BY'")
        cur.execute('SET NAMES utf8mb4')
        return request.db

@app.teardown_request
def close_db(exception=None):
    if hasattr(request, 'db'):
        request.db.close()

@app.route("/stars", methods=['POST'])
def post_stars():
    keyword = request.args.get('keyword', "")
    if keyword == None or keyword == "":
        keyword = request.form['keyword']

    origin = os.environ.get('ISUDA_ORIGIN', 'http://localhost:5000')
    url = "%s/keyword/%s" % (origin, urllib.parse.quote(keyword))
    try:
        urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        if e.status == 404:
            abort(404)
        else:
            raise

    cur = dbh().cursor()
    user = request.args.get('user', "")
    if user == None or user == "":
        user = request.form['user']

    cur.execute('INSERT INTO star (keyword, user_name, created_at) VALUES (%s, %s, NOW())', (keyword, user))

    return jsonify(result = 'ok')

if __name__ == "__main__":
    app.run()
