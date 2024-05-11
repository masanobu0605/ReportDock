from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)

openai_api_key = 'sk-proj-muxkA88fi0Pwvwa60HlaT3BlbkFJzfSsaFpX810STCnEZu4r'


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

# テンプレートから
@app.route('/from_templates_page')
def from_templates_page():
    return render_template('from_templates.html')

# 日本語に翻訳
@app.route('/translate_to_japanese_page')
def translate_to_japanese_page():
    return render_template('translate_to_japanese.html')

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
    text_1 = request.json['text']
    old_text = request.json['old']
    new_text = request.json['new']
    # 文字を置き換える処理を実装
    processed_text = text_1.replace(old_text, new_text)
    return jsonify({'result': processed_text})



# 文字数カウント処理
@app.route('/count_characters', methods=['POST'])
def count_characters():
    text = request.json['text']
    # 文字数をカウントする処理を実装
    count = len(text)
    return jsonify({'count': count})

# テンプレートから
@app.route('/from_templates', methods=['POST'])
def from_templates():
    text = request.json['text']
    # 文字数をカウントする処理を実装
    count = "まだ実装してないです～"
    return jsonify({'count': count})

# 日本語に翻訳
@app.route('/translate_to_japanese', methods=['POST'])
def translate_to_japanese():
    text = request.json['text']
    def openai_process_translate(prompt,openai_api_key): 
        prompt = prompt + (
            """
            \n
            \n
            \n
            □あなたは優秀なアシスタントです。以下のルールを守って回答してください。\n
            ・上の文章を日本語に翻訳してください。\n
            ・回答は翻訳した結果のみを返してください。\n
            ・他の要素は必要ないので、決して答えないでください。\n
            ------------------------------------------------------------------------------------------------\n 
            """
        )
        client = OpenAI(
            api_key=openai_api_key,
        )
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo-0125",
            max_tokens=4096 #MAXトークン数を最大値にしているが、あまり文章量が伸びない。
        )
        return chat_completion.choices[0].message.content
    result_text = openai_process_translate(text,openai_api_key)
    return jsonify({'result': result_text})

# 要約処理
@app.route('/summarize_text', methods=['POST'])
def summarize_text():
    text = request.json['text']
    def openai_process_translate(prompt,openai_api_key): 
        prompt = prompt + (
            """
            \n
            \n
            \n
            □あなたは優秀なアシスタントです。以下のルールを守って回答してください。\n
            ・上の文章を日本語で要約してください。\n
            ・回答は要約した結果のみを返してください。\n
            ・文章量は質問文の半分程度にしてください。\n
            ・他の要素は必要ないので、決して答えないでください。\n
            ------------------------------------------------------------------------------------------------\n 
            """
        )
        client = OpenAI(
            api_key=openai_api_key,
        )
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo-0125",
            max_tokens=4096 #MAXトークン数を最大値にしているが、あまり文章量が伸びない。
        )
        return chat_completion.choices[0].message.content
    result_text = openai_process_translate(text,openai_api_key)
    return jsonify({'result': result_text})

if __name__ == '__main__':
    app.run(debug=True)
