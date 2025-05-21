nomes = []
anos = []
generos = []
notas = []

def cadastrar_filme():
    nome = input("Digite o nome do filme: ")
    ano = input("Digite o ano de lançamento do filme: ")
    genero = input("Qual o gênero desse filme? ")
    nota = input("Diga sua nota para este filme: ")
    print("Filme cadastrado com sucesso! ")

    nomes.append(nome)
    anos.append(ano)
    generos.append(genero)
    notas.append(nota)
    menu()
    


def buscar_filmes():
    busca = input("Qual filme você pretende buscar? ")

    for i in range(len(nomes)):
        if busca == nomes[i]:
            print(f'{nomes[i]} {anos[i]} {generos[i]} {notas[i]}')

def remover_filmes():
    busca_remover = input("Qual filme você pretende remover? ")

    for i in range(len(nomes)):
        if busca_remover == nomes[i]:
            nomes.pop(i)
            anos.pop(i)
            generos.pop(i)
            notas.pop(i)

def listar_filmes():
    if len(nomes) == 0:
        print("Nenhum filme cadastrado.")
    else:
        for i in range(len(nomes)):
            print(f'{nomes[i]} {anos[i]} {generos[i]} {notas[i]}')

def estatisticas(self):
        
        total_filmes = len(self.filmes)
        media_notas = sum(filme.nota for filme in self.filmes) / total_filmes
        generos = [filme.genero for filme in self.filmes]
        genero_mais_comum = max(set(generos), key=generos.count)
        filmes_8_ou_mais = [filme.nome for filme in self.filmes if filme.nota >= 8]

        if media_notas <= 4:
            classificacao = "Ruim"
        elif 5 <= media_notas <= 7:
            classificacao = "Regular"
        else:
            classificacao = "Bom"

        print(f"Quantidade de filmes: {total_filmes}")
        print(f"Média das notas: {media_notas:.2f} ({classificacao})")
        print(f"Gênero mais cadastrado: {genero_mais_comum}")
        print(f"Filmes com nota >= 8: {', '.join(filmes_8_ou_mais) if filmes_8_ou_mais else 'Nenhum filme'}")

def menu():
    while True:
        print("1. Cadastrar filme" )
        print("2. Buscar filmes" )
        print("3. Listar filmes" )
        print("4. Remover filme" )
        print("5. Ver estatísticas" )

        opcao = input("Escolha uma opção: ")

        if opcao == '1':  # Cadastrar filme
            cadastrar_filme()
        elif opcao == '2':  # Listar filmes
            listar_filmes()
        elif opcao == '3':  # Buscar filme
            buscar_filmes()
        elif opcao == '4':  # Remover filme
            remover_filmes()
        elif opcao == '5':  # Exibir estatísticas
            estatisticas()

menu()