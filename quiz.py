from flask import Flask, render_template, request
import pymysql
import random

app = Flask(__name__)

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'ciaossu12',
    'database': 'quiz',
    'cursorclass': pymysql.cursors.DictCursor
}

PERGUNTAS_COMPLETAS = [
    {
        'pergunta': 'Qual foi o local do desastre nuclear de 1986?',
        'opcoes': ['Chernobyl', 'Fukushima', 'Three Mile Island', 'Hiroshima'],
        'resposta_correta': 'Chernobyl'
    },
    {
        'pergunta': 'Em qual país fica Chernobyl?',
        'opcoes': ['Rússia', 'Ucrânia', 'Bielorrússia', 'Polônia'],
        'resposta_correta': 'Ucrânia'
    },
    {
        'pergunta': 'Qual o principal efeito da radiação sobre os seres humanos?',
        'opcoes': ['Doenças por radiação', 'Queimaduras leves', 'Fadiga muscular', 'Problemas respiratórios'],
        'resposta_correta': 'Doenças por radiação'
    },
    {
        'pergunta': 'Em que ano ocorreu o desastre de Fukushima?',
        'opcoes': ['2011', '1986', '2005', '1999'],
        'resposta_correta': '2011'
    },
    {
        'pergunta': 'Qual tipo de radiação é mais perigosa na contaminação nuclear?',
        'opcoes': ['Radiação alfa', 'Radiação beta', 'Radiação gama', 'Radiação ultravioleta'],
        'resposta_correta': 'Radiação gama'
    },
    {
        'pergunta': 'Qual é o elemento radioativo mais conhecido usado em armas nucleares?',
        'opcoes': ['Urânio', 'Césio', 'Polônio', 'Tório'],
        'resposta_correta': 'Urânio'
    },
    {
        'pergunta': 'Qual o nome da central nuclear que explodiu em Chernobyl?',
        'opcoes': ['Reator 4', 'Reator 2', 'Reator 1', 'Reator 3'],
        'resposta_correta': 'Reator 4'
    },
    {
        'pergunta': 'Qual o órgão mais afetado pela radiação no corpo humano?',
        'opcoes': ['Pele', 'Pulmão', 'Medula óssea', 'Coração'],
        'resposta_correta': 'Medula óssea'
    },
    {
        'pergunta': 'Qual é a unidade usada para medir a radioatividade?',
        'opcoes': ['Becquerel', 'Tesla', 'Newton', 'Joule'],
        'resposta_correta': 'Becquerel'
    },
    {
        'pergunta': 'Qual país tem o maior número de usinas nucleares?',
        'opcoes': ['Estados Unidos', 'França', 'China', 'Japão'],
        'resposta_correta': 'Estados Unidos'
    },
    {
        'pergunta': 'Qual o nome do protocolo internacional que regula energia nuclear?',
        'opcoes': ['Tratado de Não Proliferação Nuclear', 'Protocolo de Kyoto', 'Acordo de Paris', 'Carta da ONU'],
        'resposta_correta': 'Tratado de Não Proliferação Nuclear'
    },
    {
        'pergunta': 'Qual é o principal método para descontaminar áreas radioativas?',
        'opcoes': ['Remoção do solo contaminado', 'Lavagem com água', 'Isolamento com plástico', 'Exposição ao sol'],
        'resposta_correta': 'Remoção do solo contaminado'
    },
    {
        'pergunta': 'Qual é o símbolo internacional da radioatividade?',
        'opcoes': ['Trevo', 'Caveira', 'Três hélices', 'Rosa'],
        'resposta_correta': 'Três hélices'
    },
    {
        'pergunta': 'Qual das seguintes partículas é a mais penetrante?',
        'opcoes': ['Alfa', 'Beta', 'Gama', 'Neutrônica'],
        'resposta_correta': 'Gama'
    },
    {
        'pergunta': 'Qual é o tempo de meia-vida do Urânio-235?',
        'opcoes': ['700 milhões de anos', '24 horas', '5 anos', '100 anos'],
        'resposta_correta': '700 milhões de anos'
    },
    {
        'pergunta': 'O que é um reator nuclear?',
        'opcoes': ['Um tipo de usina elétrica', 'Um acelerador de partículas', 'Um gerador eólico', 'Um tipo de painel solar'],
        'resposta_correta': 'Um tipo de usina elétrica'
    },
    {
        'pergunta': 'Qual evento causou evacuação em massa em 1986?',
        'opcoes': ['Chernobyl', 'Fukushima', 'Hiroshima', 'Three Mile Island'],
        'resposta_correta': 'Chernobyl'
    },
    {
        'pergunta': 'O que é radiação ionizante?',
        'opcoes': ['Radiação que pode remover elétrons de átomos', 'Radiação visível', 'Radiação ultravioleta', 'Radiação sonora'],
        'resposta_correta': 'Radiação que pode remover elétrons de átomos'
    },
    {
        'pergunta': 'Qual país tem maior histórico de testes nucleares?',
        'opcoes': ['Estados Unidos', 'Rússia', 'França', 'China'],
        'resposta_correta': 'Estados Unidos'
    },
    {
        'pergunta': 'Qual é o principal efeito da radiação na água?',
        'opcoes': ['Produção de radicais livres', 'Mudança de cor', 'Evaporação', 'Congelamento'],
        'resposta_correta': 'Produção de radicais livres'
    }
]

@app.route('/', methods=['GET'])
def quiz():
    perguntas_aleatorias = random.sample(PERGUNTAS_COMPLETAS, 5)
    for pergunta in perguntas_aleatorias:
        random.shuffle(pergunta['opcoes'])
    return render_template('index.html', perguntas=perguntas_aleatorias)

@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form.get('nome')
    ra = request.form.get('ra')

    respostas_recebidas = []
    corretas = 0

    for i in range(5):
        pergunta_texto = request.form.get(f'pergunta_texto_{i}')
        resposta_usuario = request.form.get(f'pergunta_{i}')
        respostas_recebidas.append((pergunta_texto, resposta_usuario))

        pergunta_original = next(
            (p for p in PERGUNTAS_COMPLETAS if p['pergunta'] == pergunta_texto), None)

        if pergunta_original and resposta_usuario == pergunta_original['resposta_correta']:
            corretas += 1

    percentual_acerto = (corretas / 5) * 100

    conn = pymysql.connect(**DB_CONFIG)
    try:
        with conn.cursor() as cursor:
            sql = 'INSERT INTO resultados (nome, ra, percentual_acerto) VALUES (%s, %s, %s)'
            cursor.execute(sql, (nome, ra if ra else None, percentual_acerto))
        conn.commit()
    finally:
        conn.close()

    premio = corretas >= 3

    return render_template('resultado.html', nome=nome, percentual=percentual_acerto, premio=premio)


if __name__ == '__main__':
    app.run(debug=True)
