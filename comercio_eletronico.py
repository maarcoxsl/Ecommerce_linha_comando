# Back end de ecommerce 
while True:
    print('Progama iniciado !!')
    Iniciar = input('Digite i para encerrar o progama ou qualquer comando para prosseguir: ')
    if Iniciar == 'i':
       print('Progama encerrado')
       break
    print('Bem vindo ao ecommerce-X')
    lista_compra = ['Tv','controle','video game','camisa']
    print(f'lista de compra {lista_compra}')
    escolha = input('digite qual item você deseja verificar: ')

    if escolha in lista_compra[0]:
       print(f'Produto escolhido: {lista_compra[0]}')
       Tv_valor = 150.00
       quantidade = int(input('Quantos produtos você deseja comprar\nEscolha um numeros de 1 a 5'))
       if quantidade >= 0 and quantidade <= 5:
        total_compra = quantidade * Tv_valor

        print(f'Valor da compra: {total_compra}')
        
        def Pagar(total_compra):
            metodo_pagamento = input('Como deseja realizar o pagamento desta compra\n obs: pagamentos no cartão com acrescimo de 50 reais ').strip()
            if metodo_pagamento == 'cartão':
                conta_final = total_compra + 50
                print(f'Valor de sua compra: {conta_final}')
            elif metodo_pagamento == 'dinheiro':
                 pagamento_dinheiro = total_compra - 50
            else:
                print('Formação informada não existe')

              

        Pagar(total_compra)
        

    elif escolha in lista_compra[1]:
        print(f'Produto escolhido: {lista_compra[1]}')
    elif escolha in lista_compra[2]:
        print(f'Produto escolhido: {lista_compra[2]}')  
    elif escolha in lista_compra[3]:
        print(f'Produto escolhido: {lista_compra[3]}')         
    else:
        print('produto inexistente')
    
    
    
    
       





