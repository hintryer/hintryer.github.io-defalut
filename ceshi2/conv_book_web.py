import json
import os
import requests
from flask import Flask, render_template, request, send_from_directory, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

def replace_selectors(json_data):
    # 替换选择器的函数
    def replace_selector(selector):
        if "." in selector and "@" in selector:
            parts = selector.split('.')
            tag = parts[0]
            selector_part = parts[1]
            if "@" in selector_part:
                num, at_text = selector_part.split('@', 1)
                if ":" in num:
                    num, tag_after_colon = num.split(':', 1)
                    num = f"{num}@{tag_after_colon}"
                if num.replace("-", "").replace(".", "").isdigit():
                    num = "1" if num == "0" else num  # 处理小数点后面是0的情况
                    if num.startswith("-"):
                        num = num[1:]
                        return f"{tag}:nth-last-child({num})@{at_text}"
                    else:
                        return f"{tag}:nth-child({num})@{at_text}"
        return selector

    # 处理列表类型的 JSON 数据
    if isinstance(json_data, list):
        for item in json_data:
            replace_selectors(item)
        return

    # 替换含有!0的选择器为:not(:first-child)
    for key, value in json_data.items():
        if isinstance(value, str):
            if "@" in value:
                value = value.replace("!0", ":not(:first-child)")
                value = replace_selector(value)
            json_data[key] = value
        elif isinstance(value, dict):
            replace_selectors(value)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    replace_selectors(item)

    # 在所有的bookSourceGroup中追加',real'
    if "bookSourceGroup" in json_data and isinstance(json_data["bookSourceGroup"], str):
        json_data["bookSourceGroup"] += ",real"

    # 增加替换规则，当"ruleExplore": []时，替换为"ruleExplore": "##"
    if "ruleExplore" in json_data and not json_data["ruleExplore"]:
        json_data["ruleExplore"] = "##"

    # 遍历字典类型的 JSON 数据，查找并替换选择器
    for key, value in json_data.items():
        if isinstance(value, str):
            if "@" in value:
                value = value.replace(".0@", ":nth-child(1)@")
                value = value.replace(".1@", ":nth-child(1)@")
                value = value.replace(".2@", ":nth-child(2)@")
                value = value.replace(".3@", ":nth-child(3)@")
                value = value.replace(".4@", ":nth-child(4)@")
                value = value.replace(".5@", ":nth-child(5)@")
                value = value.replace(".6@", ":nth-child(6)@")
                value = value.replace(".7@", ":nth-child(7)@")
                value = value.replace(".8@", ":nth-child(8)@")
                value = value.replace(".9@", ":nth-child(9)@")
                value = value.replace(".-1@", ":nth-last-child(1)@")
                value = value.replace(".-2@", ":nth-last-child(2)@")
                value = value.replace(".-3@", ":nth-last-child(3)@")
                value = value.replace(".-4@", ":nth-last-child(4)@")
                value = value.replace(".-5@", ":nth-last-child(5)@")
                value = value.replace(".-6@", ":nth-last-child(6)@")
                value = value.replace(".-7@", ":nth-last-child(7)@")
                value = value.replace(".-8@", ":nth-last-child(8)@")
                value = value.replace(".-9@", ":nth-last-child(9)@")
                value = value.replace(",{'webView': true}", "")

                value = replace_selector(value)
            json_data[key] = value
        elif isinstance(value, dict):
            replace_selectors(value)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    replace_selectors(item)

def download_json(json_url):
    try:
        response = requests.get(json_url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return None

def save_json(json_data, file_name):
    json_dir = os.path.join(os.path.dirname(__file__), 'json')
    if not os.path.exists(json_dir):
        os.makedirs(json_dir)

    json_path = os.path.join(json_dir, file_name)
    with open(json_path, 'w', encoding='utf-8') as file:
        json.dump(json_data, file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            json_url = request.form['json_url']
            json_data = download_json(json_url)
            if json_data is None:
                return render_template('error.html', error='下载 JSON 数据失败')
            replace_selectors(json_data)

            file_name = os.path.basename(json_url)
            save_json(json_data, file_name)

            download_link = url_for('download', file_name=file_name)

            return render_template('result.html', json_data=json_data, download_link=download_link)
        return render_template('form.html')

    @app.route('/json/<path:file_name>', methods=['GET'])
    def download(file_name):
        json_dir = os.path.join(os.path.dirname(__file__), 'json')
        file_path = os.path.join(json_dir, file_name)
        return send_from_directory(json_dir, file_name, as_attachment=True)

    app.run(host='0.0.0.0', port=5000, debug=True)
