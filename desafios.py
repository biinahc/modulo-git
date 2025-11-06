
def mostrar_mensagem_inicial():
    
    return "Bem-vindo ao Desafio de Git! :D"

print(f"{mostrar_mensagem_inicial()}")

def listar_comandos_git_basicos():
    
    return "git init", "git add", "git commit", "git status", "git push", "git pull", "git clone", "git branch", "git checkout", "git merge", "git log", "git remote"
    
print(f"{listar_comandos_git_basicos()}")

print('---'*10)

def criar_mensagem_commit(funcao_nome):
   funcao_nome = {listar_comandos_git_basicos()}

   return f"Implementa a função e mostra a lista de comandos do git {funcao_nome}"
print(f"{criar_mensagem_commit({listar_comandos_git_basicos()})}")

print('---'*10)

def verificar_tag_valida(tag):
    """
    Verifica se uma tag está no formato 'vX.Y' (ex: v1.0, v2.1).
    Retorna True se o formato for válido, caso contrário False.
    """
    pass

print('---'*10)

def gerar_relatorio_final(funcoes_concluidas):
    """
    Recebe uma lista com os nomes das funções implementadas
    e retorna uma mensagem final do desafio.

    Exemplo:
    gerar_relatorio_final(["mostrar_mensagem_inicial", "listar_comandos_git_basicos"])
    ->
    "Desafio concluído! 2 funções implementadas com sucesso."
    """
    pass
