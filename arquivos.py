import json
from pathlib import Path

PASTA_PROJETO = Path(__file__).resolve().parent
PASTA_DADOS = PASTA_PROJETO / "dados"
ARQUIVO_PRODUTOS = PASTA_DADOS / "produtos.json"

def salvar_produtos(lista, caminho=ARQUIVO_PRODUTOS):
    caminho = Path(caminho)

    caminho.parent.mkdir(parents=True, exist_ok=True)
    
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False, indent=4)

def carregar_produtos(caminho=ARQUIVO_PRODUTOS):
    caminho = Path(caminho)
    
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
            
    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("O arquivo de produtos está vazio ou inválido.")
        return []
    