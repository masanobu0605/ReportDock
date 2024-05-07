from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# CORS(app)


# トップページ
@app.route('/')
def home():
    return render_template('home.html')

# スペース削除ページ
@app.route('/remove_spaces_page')
def remove_spaces_page():
    return render_template('remove_spaces.html')

# 文字置き換えページ
@app.route('/replace_text_page')
def replace_text_page():
    return render_template('replace_text.html')

# 文字数カウントページ
@app.route('/count_characters_page')
def count_characters_page():
    return render_template('count_characters.html')

# 要約ページ
@app.route('/summarize_text_page')
def summarize_text_page():
    return render_template('summarize_text.html')





# スペース削除処理
@app.route('/remove_spaces', methods=['POST'])
def remove_spaces():
    text = request.json['text']
    # スペースを削除する処理を実装
    processed_text = text.replace(" ", "")
    text = processed_text.replace("　", "")
    return jsonify({'result': text})

# 文字置き換え処理
@app.route('/replace_text', methods=['POST'])
def replace_text():
    text = request.json['text']
    old_text = request.json['old']
    new_text = request.json['new']
    # 文字を置き換える処理を実装
    processed_text = text.replace(old_text, new_text)
    print(type(processed_text))
    return jsonify({'result': processed_text})



# 文字数カウント処理
@app.route('/count_characters', methods=['POST'])
def count_characters():
    text = request.json['text']
    # 文字数をカウントする処理を実装
    count = len(text)
    return jsonify({'count': count})

# 要約処理
@app.route('/summarize_text', methods=['POST'])
def summarize_text():
    text = request.json['text']
    # 要約する処理を実装
    # ここでは要約機能が未実装なので、仮の結果を返す
    summary = "要約機能はまだ実装されていません"
    return jsonify({'result': summary})

if __name__ == '__main__':
    app.run(debug=True)
