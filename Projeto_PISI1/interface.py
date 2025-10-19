# interface.py
import health_calculator
import suggestions 

def exibir_menu_deslogado():
    """Exibe o menu para usuários não logados."""
    print("\n=========================")
    print(" BEM-VINDO AO Equilibr.IA")
    print("=========================")
    print("1. Cadastrar Novo Usuário")
    print("2. Acessar Conta (Login)")
    print("0. Sair do Programa")
    return input("Qual função deseja acessar? ")

def exibir_menu_logado(username):
    """Exibe o menu para usuários logados."""
    print(f"\n--- MENU DO USUÁRIO: {username} ---")
    print("1. Ver meu Painel de Saúde")
    print("2. Editar Perfil")
    print("3. Excluir Perfil")
    print("0. Logout (Voltar ao menu principal)")
    return input("Escolha uma opção: ")

def exibir_dashboard(user_data):
    """Calcula e exibe todos os resultados e as novas sugestões detalhadas."""
    # Coleta os dados do usuário
    peso = user_data['peso']
    altura = user_data['altura']
    sexo = user_data['sexo']
    idade = user_data['idade']
    objetivo = user_data['objetivo']
    nivel_treino = user_data['nivel_treino']
    
    # Usa as funções do módulo de cálculo
    imc = health_calculator.calcular_imc(peso, altura)
    tmb = health_calculator.calcular_tmb(sexo, peso, altura, idade)
    
    # Usa as funções do módulo de sugestões
    dieta_sugestao = suggestions.gerar_sugestao_dieta(tmb, objetivo, peso)
    treino_sugestao = suggestions.gerar_sugestao_treino(nivel_treino, objetivo)
    
    # Exibe os resultados
    print("\n" + "="*20 + " SEU PAINEL DE SAÚDE " + "="*20)
    print(f"IMC: {imc:.2f} (Índice de Massa Corporal)")
    print(f"TMB: {tmb:.0f} kcal (Taxa Metabólica Basal diária)")
    print("-" * 64)
    
    print("\n--- SUGESTÃO DE DIETA ---")
    print(dieta_sugestao)
    
    print("\n--- SUGESTÃO DE TREINO ---")
    print(treino_sugestao)
    print("=" * 64)