#Jinja2 模板引擎 網頁模版 - Html 回傳

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/text')
def text():
    return '<html><body><h1>Hello World!!</h1></body></html>'

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


## form way
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



if __name__ == '__main__':
    app.run()