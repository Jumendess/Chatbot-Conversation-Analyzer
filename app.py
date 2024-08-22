from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd
import openai
import os
from dotenv import load_dotenv

# Configuração da chave da API OpenAI
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'mysecret')  # Chave secreta para flash messages

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB, ajuste conforme necessário

def generate_recommendations_and_phrases(data):
    prompt_recommendations = f"""
    Aqui estão alguns logs de um chatbot:

    {data}

    Analise esses dados e forneça recomendações para melhorias na curadoria do chatbot. Inclua sugestões de novas frases para as intenções que parecem ter baixa cobertura ou confiança.
    """

    prompt_phrases = f"""
    Aqui estão alguns logs de um chatbot:

    {data}

    Para cada intenção mencionada, forneça novas frases que podem ser usadas para melhorar a cobertura e a precisão do chatbot.
    """

    response_recommendations = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente que ajuda a melhorar chatbots."},
            {"role": "user", "content": prompt_recommendations}
        ],
        max_tokens=500,
        temperature=0.7
    )

    response_phrases = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente que ajuda a melhorar chatbots."},
            {"role": "user", "content": prompt_phrases}
        ],
        max_tokens=500,
        temperature=0.7
    )

    recommendations = response_recommendations.choices[0].message['content'].strip()
    phrases_by_intent = response_phrases.choices[0].message['content'].strip()

    return recommendations, phrases_by_intent

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['csv_file']
        if file:
            if file.content_length > MAX_FILE_SIZE:
                flash('O arquivo é muito grande. Por favor, faça o upload de um arquivo menor.', 'warning')
                return redirect(url_for('index'))

            try:
                df = pd.read_csv(file)
                data_string = df.to_string(index=False)
                recommendations, phrases_by_intent = generate_recommendations_and_phrases(data_string)
                return redirect(url_for('recommendations', rec=recommendations, cur=phrases_by_intent))
            except Exception as e:
                flash(f'Ocorreu um erro ao processar o arquivo: {str(e)}', 'danger')
                return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/recommendations')
def recommendations():
    rec = request.args.get('rec')
    cur = request.args.get('cur')
    return render_template('recommendations.html', recommendations=rec, curadoria=cur)

if __name__ == '__main__':
    app.run(debug=True)
