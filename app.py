from config import create_app
from controllers.pessoa_controller import pessoa_bp

app = create_app()
app.register_blueprint(pessoa_bp, url_prefix='/pessoas')

from models.BancoSQLite import inicializar_banco

# Inicializa o banco de dados
inicializar_banco()

if __name__ == '__main__':
    app.run(host='localhost', port=5001)
