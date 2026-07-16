import json

def salvar_produtos(lista, caminho="produtos.json"):
        with open(caminho, "w", encoding="utf-8") as arquivo:
            json.dump(lista, arquivo, ensure_ascii=False, indent=4)

def carregar_produtos(caminho="produtos.json"):
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            lista_produtos = json.load(arquivo)
    except FileNotFoundError:
        return []    
    return lista_produtos    
