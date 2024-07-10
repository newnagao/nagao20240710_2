#Note: The openai-python library support for Azure OpenAI is in preview.

import os
from pathlib import Path
from flask import Flask, render_template

#カレントディレクトリ移動
path = os.getcwd()
os.chdir(path)
    
#テンプレートのパス指定
tmp_path = path + '\\templates'

# Flask起動
app = Flask(__name__, template_folder=tmp_path)

#初期表示
@app.route('/', methods=['GET'])
def index():
    print(tmp_path)
    return render_template('onseiget.html')

if __name__ == "__main__":
  app.run(debug=True)