print('Progama iniciado !!')
while True:
    print('Bem vindo ao ecommerce-X')
    cadastro = input('Insira o seu nome para iniciar o progama ').strip()
    print(f'Olá {cadastro} seja bem vindo ao e commerce-X')
    lista_compra = ['Tv','controle','video game','camisa']
    print(lista_compra)
    escolha = input(f'{cadastro}, digite qual item você deseja comprar: ')
    
    pesquisa = [escolha for escolha in lista_compra if escolha in lista_compra]
    print(f'produto escolhido {pesquisa}')

    if cadatro == 'parar':
        print('Progama encerrado')
        break
   
    
    
       





