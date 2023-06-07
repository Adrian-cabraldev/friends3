while True:
    lista = []
    lista.append(input("Digite o livro que você deseja:"))
    Sair = (input("Deseja sair?"))
    if Sair == "sim":
        print("Fim!")
        break
print(lista)
print("O número de livros é", len(lista), "o número de vezes que voxê repetiu o livro foi", lista.count("livros"))