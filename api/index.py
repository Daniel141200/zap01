import sys
import os

# Adicionar o diretório pai ao path para importar os módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.main import app

# Esta é a função que a Vercel vai chamar
def handler(request):
    return app(request.environ, lambda status, headers: None)

