from flask import Flask, render_template # type: ignore

app=Flask(__name__)

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/home')
def do():
    return render_template('do.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

if __name__=='__main__':
    app.run(debug=True)
