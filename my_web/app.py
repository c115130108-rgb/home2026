from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # 這裡會自動去 templates 資料夾找 index.html 並讀取渲染
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
