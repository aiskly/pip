from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title="Моя РПГ")

@app.route('/create_character', methods=['GET', 'POST'])
def create_character():
    if request.method == 'POST':
        name = request.form['name']
        race = request.form['race']
        return f"Персонаж {name}, раса {race}, создан!"
    return render_template('create_character.html')

if __name__ == '__main__':
    app.run(debug=True)
