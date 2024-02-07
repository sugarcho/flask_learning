### Python Flask - Hello World basic ###
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
@app.route("/hello")

def hello():
    return "Hi world"

@app.route("/data/appInfo/<name>", methods=["GET"])
def queryDataMessageByName(name):
    print("type(name):", type(name))
    return f"string: {name}"

@app.route("/data/appInfo/id/<int:id>", methods=["GET"])
def queryDataMessageById(id):
    print("type(id):", type(id))
    return f"int: {id}"

@app.route("/data/appInfo/version/<float:version>", methods=["GET"])
def queryDataMessageByVersion(version):
    print("type(version): ", type(version))
    return f"float: {version}"

@app.route('/text')
def text():
    return '<html><body><h1>Hello World</h1></body></html>'


### Jinja2 模板引擎, 網頁模版 - Html 回傳 ###

from flask import Flask, render_template
# app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/page/text')
def pageText():
    return render_template('page.html', text="Python Flask!")

@app.route('/page/app')
def pageAppInfo():
    appInfo = {
        'id' : 5,
        'name': 'Python - Flask',
        'version' : '1.0.1',
        'author' : 'Enoxs',
        'remark' : 'Python - Web Framework'
    }
    return render_template('page.html', appInfo=appInfo)

@app.route('/page/data')
def pageData():
    data = {  # dict
        '01': 'Text Text Text',
        '02': 'Text Text Text',
        '03': 'Text Text Text',
        '04': 'Text Text Text',
        '05': 'Text Text Text'
    }
    return render_template('page.html', data=data)

@app.route('/static')
def staticPage():
    return render_template('static.html')


### form way, 資料交換 - Form 表單提交 ###
from flask import Flask, request, render_template, redirect, url_for
# app = Flask(__name__)

@app.route('/form')
def formPage():
    return render_template('form.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        user = request.form['user']
        print("post: user :", user)
        return redirect(url_for('success', name=user, action='post'))
    else:
        user = request.args.get('user')
        print('get: user: ', user)
        return redirect(url_for('success', name=user, action='get'))

@app.route('/success/<action>/<name>')
def success(name, action):
    return f'{action} : Welcome {name} ~!!!'

### jQuery - Ajax 資料交換 ###
from flask import Flask, render_template, request, jsonify, json
# app = Flask(__name__)

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
    
### upload file 
    
# 設定上傳文件的最大為16MB
app.config['MAX_CONTENT_LENGTH'] = 16*1024*1024

# 定義上傳資料夾的位址
UPLOAD_FOLDER = os.path .join(os.getcwd(), 'uploads')

# 路由定義 - 上傳頁面
@app.route('/upload')
def uploadPage():
    return render_template('upload.html')

@app.route('/upload/submit', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file.'

    file = request.files['file']
    if file.filename == '':
        return 'No selected file.'
    
    if file:
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)
        
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        return 'File uploaded sueecssfully.'




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

