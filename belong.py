from flask import Flask,render_template#引入
app = Flask(__name__)#实例  
@app.route('/')#装饰器,route为网址
def index():#普通函数，一个页面一个函数
    return render_template('index.html')
if __name__ =='__main__':
    app.run(debug=True, threaded= True)#运行函数