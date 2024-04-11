from flask import Flask, render_template, request, flash
from bs4 import BeautifulSoup as soup
import re
import openai

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():  # put application's code here
    if request.method == 'POST':
        openai.api_key = "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"
        print(request.form.get('textarea'))
        if request.form.get('comp_select') == "complete the  story with this answers?":
            text = str(request.form.get('textarea'))
            text = " ".join(text.split())
            print(text)
            text = text.replace("Answer", "....")
            Soup = soup(request.form.get('htmlsoup'), features="html.parser")
            find = Soup.find_all("option")
            val = ''
            for i in find:
                if i['value'] == "":
                    continue
                valu = find.index(i) + 1
                value = i.text
                val += str(valu) + '-' + value + "/n"
            text = text + "/n" + "/n" + val + "complete the  story with this answers?"
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=text,
                temperature=0.4,
                max_tokens=2006,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            print(response)
            return render_template('apq.html', response=response["choices"][0]["text"].replace("/n", ""))
        if str(request.form.get('comp_select')) != "choose the correct answer?":
            text = str(request.form.get('textarea'))
            text = " ".join(text.split())
            text = text if text.find("Answer") == -1 else text.replace("Answer", "....")
            if request.form.get('htmlsoup') == "":
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=text,
                    temperature=0.4,
                    max_tokens=2006,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )
                return render_template('apq.html', response=response["choices"][0]["text"].replace("/n", ""))
            else:
                Soup = soup(request.form.get('htmlsoup'))
                find = Soup.find_all("option")
                val = ''
                for i in find:
                    if i['value'] == "":
                        continue
                    value = i.text
                    x = re.search(r"\b()\w+", value).span()
                    value = value.replace(value[x[0] - 1] + value[x[0]] + value[x[1]], "") if value[x.span()[ 0] - 1] == "(" and value[x.span()[1]] == ")" else value
                    valu = find.index(i) + 1
                    val += str(valu) + '-' + value + "/n"
                text = text + "/n" + "/n" + val + "choose the correct answer?"
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=text,
                    temperature=0.4,
                    max_tokens=2006,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )
            return render_template('apq.html', response=response["choices"][0]["text"].replace("/n", ""))
        else:
            text = str(request.form.get('textarea'))
            text = " ".join(text.split())
            text = text.replace("Answer", "....")
            Soup = soup(request.form.get('htmlsoup'))
            find = Soup.find_all("option")
            val = ''
            for i in find:
                if i['value'] == "":
                    continue
                value = i.text
                valu = find.index(i) + 1
                x = re.search(r"\b()\w+", value).span()
                value = value.replace(value[x[0] - 1] + value[x[0]] + value[x[1]], "")
                val += str(valu) + '-' + value + "/n"
            text = text + "/n" + "/n" + val + "choose the correct answer?"
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=text,
                temperature=0.4,
                max_tokens=2006,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            print(response)
            return render_template('apq.html', response=response["choices"][0]["text"].replace("/n", ""))
    if request.method == 'GET':
        return render_template('apq.html')


if __name__ == "__main__":
    app.run()
