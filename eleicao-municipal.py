candidatos_vereador = {
    1: "CandidatoV A",
    2: "CandidatoV B",
    3: "CandidatoV C",
    4: "CandidatoV D"
}

candidatos_prefeito = {
    1: "CandidatoP A",
    2: "CandidatoP B",
    3: "CandidatoP C"
}

votos_vereador = {1: 0, 2: 0, 3: 0, 4: 0}
votos_prefeito = {1: 0, 2: 0, 3: 0}

def votar():
    print("\nEscolha até dois vereadores para votar:")
    for numero, nome in candidatos_vereador.items():
        print(f"{numero}: {nome}")

    # Coleta de votos
    vereador1 = int(input("Digite o número do primeiro candidato: "))
    vereador2 = int(input("Digite o número do segundo candidato (ou 0 para pular): "))
    prefeito = int(input("Digite o número do candidato a Prefeito (ou 0 para nulo):"))

    # Verificação da validade dos votos e contagem
    if vereador1 in votos_vereador:
        votos_vereador[vereador1] += 1
    if vereador2 in votos_vereador and vereador2 != 0:
        if vereador2 != vereador1:  # Evita que o eleitor vote duas vezes no mesmo candidato
            votos_vereador[vereador2] += 1
        else:
            print("Você não pode votar duas vezes no mesmo candidato.")
    
    if prefeito in votos_prefeito:
        votos_prefeito[prefeito] += 1
        
    else:
        print("Seu voto já foi registrado!")
        
    # Função para exibir resultados
def resultados():
    print("\nResultado da votação:")
    for numero, nome in candidatos_vereador.items():
        print(f"{nome} recebeu {votos_vereador[numero]} votos")
    
    for numero, nome in candidatos_prefeito.items():
        print(f"{nome} recebeu {votos_prefeito[numero]} votos")

        
# Simulação de votação
numero_eleitores = int(input("Quantos eleitores irão votar? "))
for i in range(numero_eleitores):
    print(f"\nEleitor {i + 1}:")
    votar()

resultados()
