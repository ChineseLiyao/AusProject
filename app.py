from flask import Flask, render_template, json

app = Flask(__name__)

def get_cfg():
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.context_processor
def inject_config():
    return dict(cfg=get_cfg())

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download')
def download():
    return render_template('download.html')

@app.route('/team')
def team():
    return render_template('team.html')

if __name__ == '__main__':
    app.run(debug=True)