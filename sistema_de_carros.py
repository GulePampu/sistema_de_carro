carros = {'civic': [{'Marca': 'honda', 'Modelo': 'civic', 'Ano': '1993', 'Cor': 'branco', 'Quilometragem': '200000 km', 'Preço': 'R$ 23,480.00'}]}
carro_cadastro = {'Marca': None, 'Modelo': None, 'Ano': None, 'Cor': None, 'Quilometragem': None, 'Preço': None}


def menu_principal():
    menu = input('MENU\n[1] Cadastrar carro\n[2] Buscar carro\n[3] Sair\nDigite aqui: ')
    if menu.isnumeric():
        if menu == '1':
            return menu_cadastro(carro_cadastro)
        elif menu == '2':
            return menu_buscar()
        elif menu == '3':
            return
        else:
            print('Opção Inválida')
            return menu_principal()
    else:
        print('Opção Inválida')
        return menu_principal()


def set_defalut():
    return {'Marca': None, 'Modelo': None, 'Ano': None, 'Cor': None, 'Quilometragem': None, 'Preço': None}


def menu_cadastro(carro_cadastro):
    menu = input('[1] marca \n[2] modelo \n[3] ano \n[4] cor \n[5] quilometragem \n[6] preço \n[7] concluir cadastro\n[8] voltar\nDigite aqui: ')
    if menu.isnumeric() and len(menu) == 1:
        if menu == '1':
            cadastrar_marca(input('Informe a marca do veiculo: ').strip().lower())
        elif menu == '2':
            cadastrar_modelo(input('Informe o modelo do veiculo: ').strip().lower())
        elif menu == '3':
            cadastrar_ano_de_fabricacao(input('Informe o ano de fabricação(AAAA): ').strip().lower())
        elif menu == '4':
            cadastrar_cor(input('Informe a cor do veiculo: ').strip().replace(' ', '-').lower())
        elif menu == '5':
            cadastrar_quilometragem(input('Informe a quilometragem do veiculo (apenas números, sem separações): ').strip().lower())
        elif menu == '6':
            cadastrar_preco(input('Informe o preço do veiculo(apenas números, sem separações, os dois últimos valores são os centavos): ').strip().lower())
        elif menu == '7':
            concluir_cadastro(carro_cadastro, carro_cadastro['Modelo'])
            carro_cadastro = set_defalut()
            print(carros)
            menu_cadastro(carro_cadastro)
        elif menu == '8':
            carro_cadastro = set_defalut()
            menu_principal()
    else:
        print('Opção Inválida')
        menu_cadastro(carro_cadastro)


def cadastrar_marca(marca):
    if marca.isalnum():
        carro_cadastro['Marca'] = marca
        print('Marca cadastrada')
        return menu_cadastro(carro_cadastro)
    else:
        print('Valor Inválido')
        return menu_cadastro(carro_cadastro)


def cadastrar_modelo(modelo):
    if modelo.isalnum():
        carro_cadastro['Modelo'] = modelo
        print('Modelo cadastrado')
        return menu_cadastro(carro_cadastro)
    else:
        print('Valor Inválido')
        return menu_cadastro(carro_cadastro)


def cadastrar_ano_de_fabricacao(ano):
    if ano.isnumeric() and len(ano) >= 4:
        carro_cadastro['Ano'] = ano
        print('Ano de fabricação cadastrado')
        return menu_cadastro(carro_cadastro)
    else:
        print('Valor Inválido')
        return menu_cadastro(carro_cadastro)


def cadastrar_cor(cor):
    if cor.isalpha():
        carro_cadastro['Cor'] = cor
        print('Cor cadastrada')
        return menu_cadastro(carro_cadastro)
    else:
        print('Valor Inválido')
        return menu_cadastro(carro_cadastro)


def cadastrar_quilometragem(km):
    if km.isnumeric():
        km = f'{km} km'
        carro_cadastro['Quilometragem'] = km
        print('Quilometragem cadastrada')
        return menu_cadastro(carro_cadastro)
    else:
        print('Valor Inválido')
        return menu_cadastro(carro_cadastro)


def cadastrar_preco(preco):
    if preco == '0':
        return 'gratuito'
    elif preco.isnumeric():
        preco = "R$ {:,.2f}".format(int(preco) / 100)
        carro_cadastro['Preço'] = preco
        print('Preço cadastrado')
        return menu_cadastro(carro_cadastro)
    else:
        print('Valor Inválido')
        return menu_cadastro(carro_cadastro)


def concluir_cadastro(carro_cadastro, modelo):
    if modelo == None:
        print('Informe um modelo! ')
        menu_cadastro(carro_cadastro)
    else:
        for i in carros:
            if i.lower() != modelo.lower():
                carros.update({modelo: carro_cadastro})
                break
            elif i.lower() == modelo.lower():
                carros[modelo].append(carro_cadastro)
                break


def menu_buscar():
    menu = input('BUSCAR CARRO POR:\n[1] modelo\n[2] marca\n[3] ano\n[4] todos os carros\n[5] voltar\nDigite aqui: ')
    if menu.isnumeric():
        if menu == '1':
            buscar_carro_modelo(input('Informe o modelo: ').strip().lower())
        elif menu == '2':
            buscar_carro_marca(input('Informe a marca: ').strip().lower())
        elif menu == '3':
            buscar_carro_ano(input('Informe o ano(AAAA): ').strip().lower())
        elif menu == '4':
            buscar_carro_todos()
        elif menu == '5':
            menu_principal()
        else:
            print('Opção inválida')
            return menu_buscar()
    else:
        print('Opção inválida')
        return menu_buscar()


def buscar_carro_modelo(modelo_busca):
    carros_encontrados = []
    for modelos, cadastro in carros.items():
        for carro in cadastro:
            if carro['Modelo'].lower() == modelo_busca.lower():
                carros_encontrados.append(carro)
    if len(carros_encontrados) == 0:
        print('Modelo não encontrado!')
        return menu_principal()
    for i in carros_encontrados:
        print(i)
    return menu_principal()


def buscar_carro_marca(marca_busca):
    carros_encontrados = []
    for modelos, cadastro in carros.items():
        for carro in cadastro:
            if carro['Marca'].lower() == marca_busca.lower():
                carros_encontrados.append(carro)
    if len(carros_encontrados) == 0:
        print('Marca não encontrada!')
    for i in carros_encontrados:
        print(i)
    return menu_principal()


def buscar_carro_ano(ano_busca):
    carros_encontrados = []
    for modelos, cadastro in carros.items():
        for carro in cadastro:
            if carro['Ano'] == ano_busca:
                carros_encontrados.append(carro)
    if len(carros_encontrados) == 0:
        print('Ano não encontrado!')
    for i in carros_encontrados:
        print(i)
    return menu_principal()


def buscar_carro_todos():
    carros_encontrados = []
    for modelos, cadastro in carros.items():
        for carro in cadastro:
            carros_encontrados.append(carro)
    for i in carros_encontrados:
        print(i)
    return menu_principal()


menu_principal()
