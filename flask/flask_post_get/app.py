from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        naziv = request.form['naziv']
        #text = text + '123'
        return render_template('result.html', naziv=naziv)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

