
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

def verificar_tag_valida_sem_regex(tag):    
    if not tag.startswith('v'):
        return False        
    conteudo_versao = tag[1:]    
    partes = conteudo_versao.split('.')

    if len(partes) != 2:
        return False
        
    major, minor = partes
    
    if not major or not minor: 
        return False
    return major.isdigit() and minor.isdigit()


print(f"verificar_tag_valida_sem_regex('v1.0'): {verificar_tag_valida_sem_regex('v1.0')}") 
print(f"verificar_tag_valida_sem_regex('v2.10'): {verificar_tag_valida_sem_regex('v2.10')}") 
print(f"verificar_tag_valida_sem_regex('v1.0.1'): {verificar_tag_valida_sem_regex('v1.0.1')}") 
print(f"verificar_tag_valida_sem_regex('1.0'): {verificar_tag_valida_sem_regex('1.0')}") 
print(f"verificar_tag_valida_sem_regex('v1.a'): {verificar_tag_valida_sem_regex('v1.a')}") 
print(f"verificar_tag_valida_sem_regex('v.'): {verificar_tag_valida_sem_regex('v.')}") 

print('---'*10)

def gerar_relatorio_final(funcoes_concluidas):
   
    num_funcoes = len(funcoes_concluidas)

    return f"Desafio concluídoo! Foi um sucesso :D {num_funcoes} funções implementadas."

print(f"gerar_relatorio_final: {gerar_relatorio_final(['f1', 'f2', 'f3, f4', 'f5'])}")


print('---'*10)

print("Desafio Finalizado! Parabéns por completar o desafio de Git!")
