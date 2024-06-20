def obter_notas(disciplina):
    nota = float(input(f"Digite a nota de {disciplina}: "))
    while nota < 0 or nota > 10:
        print("A nota deve estar entre 0 e 10.")
        nota = float(input(f"Digite novamente a nota de {disciplina}: "))
    return nota

def verificar_recuperacao(media_final):
    if media_final < 5:
        print("Você está de recuperação.")
    else:
        print("Parabéns, você foi aprovado!")

def main():
    notas_finais = []
    disciplinas = ["Prova Prática", "Vistos no Caderno", "Apresentação", "Mapa Mental"]

    for disciplina in disciplinas:
        nota = obter_notas(disciplina)
        notas_finais.append(nota)

    media_final = sum(notas_finais) / len(notas_finais)
    print(f"\nSua média final é: {media_final:.2f}")
    verificar_recuperacao(media_final)

if __name__ == "__main__":
    main()
