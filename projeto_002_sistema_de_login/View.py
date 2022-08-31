from Controller import ControllerCadastro, ControllerLogin

while True:
    print('============ MENU ============')
    decisao = int(input(
        'Digite 1 para se cadastrar:\nDigite 2 para efetuar login:\nDigite 3 para sair:\n'))
    if decisao == 1:
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        result = ControllerCadastro.cadastrar(nome, email, senha)
        if result == 2:
            print("Tamanho do nome digitado inválido!")
        elif result == 3:
            print("Tamanho do e-mail digitado inválido!")
        elif result == 4:
            print("Tamanho de senha inválido!")
        elif result == 5:
            print("Este e-mail já tem cadastro efetuado!")
        elif result == 6:
            print("Erro interno do sistema!")
        else:
            print("Cadastro realizado com sucesso!")

    elif decisao == 2:
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        result = ControllerLogin(email, senha)
        if not result:
            print("E-mail e/ou senha inválido(s)!")
        else:
            print(result)
    else:
        break
