from flask import Flask,request,render_template


app = Flask(__name__)


@app.route('/page/<username>')
def show_names(username):
    return "Hey there %s" % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return "Post id:%s " % post_id

@app.route('/sausage/',methods=['GET','POST'])
def sausage():
    if request.method=='POST':
        return "You are using %s" % request.method +"dude"
    else:
        return "You are using GET dude"
if __name__ == '__main__':
    app.run(debug=True)

