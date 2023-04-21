# OpenAI GPT-3を使った対話式ツール

Pythonを使用してOpenAI GPT-3を使った対話式ツールについて説明します。
このPythonスクリプトは、OpenAI GPT-3を使って対話を行う対話式ツールです。OpenAI APIのアクセスキーが必要です。

## 手順

1. プロジェクトの作成
2. パッケージのインストール
3. API Keyの入手と設定
4. コードの作成

### プロジェクトの作成

最初に、プロジェクトを作成する必要があります。Windowsのコマンドプロンプトを開き、プロジェクト用の新しいディレクトリを作成します。

```
mkdir chatgpt-app
cd chatgpt-app
```

次に、Pythonのvirtualenvを使用して、独立したPython環境を作成します。

```
python -m venv venv
```

そして、仮想環境をアクティブにします。

```
.\venv\Scripts\activate
```

### パッケージのインストール

次に必要なパッケージをインストールします。
```
pip install openai
```



### API Keyの入手と設定

次にAPI Keyの入手し設定します。

[こちら](https://programming-zero.net/openai-api-key/)を参考にAPI Keyを入手します。そしてAPI Keyを設定します。
```
set OPENAI_API_KEY="入手したAPI Key"
```

### コードの作成

次のコードをエディターで`main.py`として保存してください。

```
import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

text = input("Prompt: ")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": text},
    ],
)

print(response.choices[0]["message"]["content"].strip())
```

これで、対話式ツールが完成しました。

## 実行

対話式ツールを実行するには、Windowsのシェルで以下のコマンドを実行します。

```
python main.py
```

## 解説

```python
import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]
```

まず、`os`モジュールと`openai`モジュールをインポートしています。次に、環境変数からOpenAI APIキーを取得し、`openai.api_key`に設定しています。

```python
text = input("Prompt: ")
```

`input()`関数を使って、ユーザーに対して入力を求めるプロンプトを表示します。ユーザーが入力すると、その値が`text`変数に格納されます。

```python
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": text},
    ],
)
```

`openai.ChatCompletion.create()`メソッドを呼び出して、OpenAI APIにリクエストを送信します。`model`引数には使用するGPT-3のモデルを指定します。`messages`引数には、ユーザーの入力内容を含むリストを渡します。ここでは、`{"role": "user", "content": text}`という辞書をリストの中に入れています。



```python
print(response.choices[0]["message"]["content"].strip())
```

`response`オブジェクトに含まれる、AIからの応答を表示します。応答の中に余計な空白が含まれている場合があるため、`.strip()`メソッドを使用して、応答から余計な空白を除去しています。ここでは、`response.choices[0]["message"]["content"]`という表記を使って、応答の本文を取得しています。最初の要素のみが必要な場合、`response.choices[0]`を使うことで、リスト内の最初の要素にアクセスできます。
