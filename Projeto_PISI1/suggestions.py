# suggestions.py

def gerar_sugestao_dieta(tmb, peso, objetivo):
    """
    Gera uma sugestão de dieta mais detalhada com metas calóricas e de macronutrientes.
    """
    if tmb <= 0 or peso <= 0:
        return "Dados insuficientes para calcular a dieta."

    # Fator de atividade leve (exercício 1-3 dias/semana) - um ponto de partida
    fator_atividade = 1.375
    calorias_manutencao = tmb * fator_atividade

    if objetivo == 'perder gordura':
        calorias_alvo = calorias_manutencao - 400  # Déficit moderado
        # Macros: Proteína alta, Gordura moderada, Carboidratos baixos
        proteina_g = peso * 2.0  # 2.0g por kg de peso corporal
        gordura_g = (calorias_alvo * 0.30) / 9
        carboidratos_g = (calorias_alvo - (proteina_g * 4) - (gordura_g * 9)) / 4
    elif objetivo == 'ganhar massa':
        calorias_alvo = calorias_manutencao + 300  # Superávit moderado
        # Macros: Proteína alta, Carboidratos altos, Gordura moderada
        proteina_g = peso * 1.8
        gordura_g = (calorias_alvo * 0.25) / 9
        carboidratos_g = (calorias_alvo - (proteina_g * 4) - (gordura_g * 9)) / 4
    else:  # Manter peso
        calorias_alvo = calorias_manutencao
        proteina_g = peso * 1.6
        gordura_g = (calorias_alvo * 0.30) / 9
        carboidratos_g = (calorias_alvo - (proteina_g * 4) - (gordura_g * 9)) / 4

    # Montando a string de sugestão
    sugestao = (
        f"Com base no seu objetivo de '{objetivo}', uma meta inicial seria de aproximadamente **{calorias_alvo:.0f} kcal** por dia.\n"
        f"Isto se traduz em:\n"
        f"  - **Proteínas:** {proteina_g:.0f} g\n"
        f"  - **Carboidratos:** {carboidratos_g:.0f} g\n"
        f"  - **Gorduras:** {gordura_g:.0f} g\n\n"
        f"**Estrutura de Refeições Sugerida:**\n"
        f"  - **Café da Manhã:** Fonte de proteína (ex: ovos) + carboidrato complexo (ex: aveia).\n"
        f"  - **Almoço/Jantar:** Proteína magra (ex: frango, peixe) + carboidrato complexo (ex: batata doce, arroz integral) + vegetais e salada à vontade.\n"
        f"  - **Lanches:** Frutas, iogurte natural, castanhas ou whey protein.\n\n"
        f"💧 **Lembre-se de beber bastante água!** (pelo menos 2 litros por dia).\n"
    )
    return sugestao

def gerar_sugestao_treino(nivel, objetivo):
    """
    Gera uma rotina de treino mais detalhada com exemplos de exercícios.
    """
    cardio_sugestao = ""
    if objetivo == 'perder gordura':
        cardio_sugestao = "Cardio Sugerido: 3-4 vezes por semana, 30-40 minutos (ex: corrida leve, bicicleta)."
    elif objetivo == 'ganhar massa':
        cardio_sugestao = "Cardio Sugerido: 2 vezes por semana, 20 minutos (para saúde cardiovascular, sem atrapalhar a recuperação)."
    else:
        cardio_sugestao = "Cardio Sugerido: 3 vezes por semana, 30 minutos para manutenção da saúde."

    if nivel == 'iniciante':
        return (
            "**Plano de Treino para Iniciantes (Foco em Adaptação)**\n"
            "Frequência: 3 vezes por semana, em dias alternados (ex: Seg, Qua, Sex).\n"
            "Tipo: Treino Full Body (corpo inteiro) para construir uma base sólida.\n\n"
            "**Exemplo de Treino A:**\n"
            "  - Agachamento com peso corporal ou Goblet Squat: 3 séries de 12 repetições\n"
            "  - Supino com halteres ou em máquina: 3 séries de 12 repetições\n"
            "  - Remada na polia baixa: 3 séries de 12 repetições\n"
            "  - Desenvolvimento de ombros com halteres: 3 séries de 12 repetições\n"
            "  - Prancha abdominal: 3 séries, segurando o máximo de tempo que conseguir.\n\n"
            f"{cardio_sugestao}"
        )
    elif nivel == 'intermediario':
        return (
            "**Plano de Treino para Intermediários (Foco em Força e Hipertrofia)**\n"
            "Frequência: 4 vezes por semana.\n"
            "Tipo: Divisão Superior/Inferior (Upper/Lower).\n\n"
            "**Exemplo de Estrutura:**\n"
            "  - Segunda-feira: Superior (ex: Supino, Remada Curvada, Desenvolvimento Militar, Rosca Direta)\n"
            "  - Terça-feira: Inferior (ex: Agachamento Livre, Leg Press, Stiff, Panturrilha)\n"
            "  - Quarta-feira: Descanso ou cardio leve.\n"
            "  - Quinta-feira: Superior (foco em exercícios diferentes, ex: Supino Inclinado, Puxada Alta)\n"
            "  - Sexta-feira: Inferior (foco em exercícios diferentes, ex: Afundo, Cadeira Flexora)\n\n"
            f"{cardio_sugestao}"
        )
    elif nivel == 'avancado':
        return (
            "**Plano de Treino para Avançados (Foco em Volume e Intensidade)**\n"
            "Frequência: 5 vezes por semana.\n"
            "Tipo: Divisão Push/Pull/Legs (Empurrar/Puxar/Pernas).\n\n"
            "**Exemplo de Estrutura:**\n"
            "  - Segunda-feira: Push (Peito, Ombros, Tríceps - ex: Supino Inclinado, Paralelas, Elevação Lateral)\n"
            "  - Terça-feira: Pull (Costas, Bíceps - ex: Barra Fixa, Remada Cavalinho, Rosca Scott)\n"
            "  - Quarta-feira: Legs (Pernas - ex: Agachamento Pesado, Stiff Romeno, Afundo Búlgaro)\n"
            "  - Quinta-feira: Push (foco em variações e maior volume)\n"
            "  - Sexta-feira: Pull (foco em variações e maior volume)\n\n"
            f"{cardio_sugestao} (pode incluir HIIT em dias separados)."
        )
    else:
        return "Nível de treino inválido."