# fourth example
# File Uploads
from flask import Flask, request
import os

app = Flask(__name__)

# upload folder
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if a file was uploaded
        if 'file' not in request.files:
            return 'No file part in the request'
        
        file = request.files['file']
        
        # check if user selected a file
        if file.filename == '':
            return 'No file selected'
        
        if file:
            # save the file to the upload folder
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            return f'File {file.filename} uploaded successfully!'
    
    # display upload form for GET request
    return '''
    <!doctype html>
    <html>
    <head>
        <title>Upload File</title>
    </head>
    <body>
        <h1>Upload a File</h1>
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload">
        </form>
    </body>
    </html>
    '''

@app.route('/')
def index():
    return 'Go to <a href="/upload">/upload</a> to upload a file'

if __name__ == '__main__':
    app.run(debug=True)







# # third example
# # This is a simple Flask application that demonstrates how to 
# # render a template with a dynamic variable. 
# # hello.html stored on the templates folder.
# # HTTP Methods and Template Rendering
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/rendered')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)






# second example
# basic syntex and routing
from flask import Flask, request

app = Flask(__name__)

def doThelogin():
    return 'This was a POST request!'

def showTheLoginForm():
    return 'This was a GET request!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return doThelogin()
    else:
        return showTheLoginForm()

@app.route('/')
def hello():
    return 'Hello from Flask in venv!'

@app.route('/admin')
def admin():
    return 'This is the admin page!'

if __name__ == '__main__':
    app.run(debug=True)




# first example
# deployment basics
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Flask in venv!'

# create different pages and dynamic URL
@app.route('/admin')
def admin():
    return 'This is the admin page!'

if __name__ == '__main__':
    app.run(debug=True)