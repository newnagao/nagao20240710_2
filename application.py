#Note: The openai-python library support for Azure OpenAI is in preview.

from flask import Flask, render_template

# Flask起動
app = Flask(__name__)

#初期表示
@app.route('/', methods=['GET'])
def index():
    return render_template('onseiget.html')

if __name__ == "__main__":
  app.run(debug=True)
