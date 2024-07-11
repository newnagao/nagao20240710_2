#Note: The openai-python library support for Azure OpenAI is in preview.

import subprocess
from flask import Flask, request, jsonify, render_template

# Flask起動
app = Flask(__name__)

#初期表示
@app.route('/', methods=['GET'])
def index():
    return render_template('onseiget.html')
    

#テキスト送信時
@app.route('/download', methods=['POST'])
def textread():

#バッチファイル名
  bat_file = "curl4.sh"
  
#入力文字
  reading_txt = ""
  reading_data = request.form['text']
  reading_fix = reading_data.split()
  
  for unit in reading_fix:
    reading_txt += unit
    
#出力ファイル名
#  output_file_path = "files/"
  output_file_name = "test.mp3"
#  output_file = output_file_path + output_file_name
#  download_switch = "<a href=\"/download/" + output_file_name + "\" download=\"" + output_file_name + "\">ここから音声ファイルがダウンロードできます。</a>"


#リクエスト送信バッチファイル取得
  command = "./" + bat_file + " " + reading_txt + " " + output_file_name
  result = subprocess.run(command, shell=True)

  if os.path.isfile(output_file):
	  return jsonify("ファイルのダウンロードができました")
  else :
      return jsonify("ファイルの作成に失敗しました")

#ダウンロードリンク押下時
#@app.route('/download/<string:file>')
#def download(file):
#    return send_from_directory('files', file, as_attachment=True)

if __name__ == "__main__":
  app.run(debug=True)