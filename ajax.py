# jQuery - Ajax 資料交換
from flask import Flask, render_template, request, jsonify, json

app = Flask(__name__)

@app.route('/data')
def webapi():
    return render_template('data.html')

@app.route('/data/message', methods=['GET'])
def getDataMessage():
    if request.method == 'GET':
        with open('static/data/message.json','r') as f:
            data = json.load(f)
            print('text: ', data)
        f.close
        return jsonify(data)

@app.route('/data/message', methods=['POST'])
def setDataMessage():
    if request.method == 'POST':
        data = {
            'appInfo': {
                'id': request.form['app_id'],
                'name': request.form['app_name'],
                'version': request.form['app_version'],
                'author': request.form['app_author'],
                'remark': request.form['app_remark']
            }
        }
        print(type(data))
        with open('static/data/input.json', 'w') as f:
            json.dump(data, f)
        f.close
        return jsonify(result='OK')
    
if __name__ == '__main__':
    app.run()