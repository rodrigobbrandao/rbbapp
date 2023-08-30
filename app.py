from flask import Flask, render_template, redirect, url_for, request
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow

app = Flask(__name__)

# Configurar as credenciais do Google
CLIENT_ID = '519999793068-baonchpsq8sodum56mkmo6lng0uarl50.apps.googleusercontent.com'
CLIENT_SECRET = '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'
REDIRECT_URI = 'https://rodrigobbrandao.github.io/rbbapp/'

# Configurar o fluxo de autenticação
flow = Flow.from_client_secrets_file(
    'client_secret.json',
    scopes=['openid', 'https://www.googleapis.com/auth/userinfo.email'],
    redirect_uri=REDIRECT_URI
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    authorization_url, state = flow.authorization_url()
    return redirect(authorization_url)

@app.route('/callback')
def callback():
    flow.fetch_token(authorization_response=request.url)
    id_info = id_token.verify_oauth2_token(flow.credentials.id_token, None)
    
    if id_info['email'].endswith('@orama.com.br'):
        return f'Bem-vindo, {id_info["name"]}!'
    else:
        return 'Acesso não permitido para esse domínio.'

if __name__ == '__main__':
    app.run(debug=True)
