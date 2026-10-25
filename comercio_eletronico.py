# Back end de ecommerce 
def SistemaEcommerce():
    print("==== Ecommerce ====")
    print()
    print("Escolha a seguir os itens que você deseja comprar")

    print("1) Tv\n2) Video game\n3) Geladeira\n4) Sofa")
    escolher = int(input("Escolha uma opção para compra o seu produto"))
    
Compras(escolha_usuario)
SistemaEcommerce()

#SistemaEcommerce()


   

def Compras(escolher):

    if escolha == 1:
       escolher_qtd = input("Digite qualquer coisa para iniciar ou sair para encerrar o progama")
       Tv_valor = 1440.00
       while escolher != "sair":
             quantidade = 0
             comprar = int(input("Digite 1 para somar os produtos"))
             if comprar == 1:
                quantidade += 1
                print(f'total de produtos: {quantidade}')
                print(f'valor final: {quantidade * Tv_valor}')
                if escolher_qtd == "sair":
                    print("Conta fechada")
                    break
        
    elif escolha == 2:
         print(f'Digite qualquer coisa para iniciar ou sair para encerrar fechar a conta')
         videogame_valor = 2250.00

         while escolher != "sair":
             quantidade = 0
             comprar = int(input("Digite 1 para somar os produtos"))
             if comprar == 1:
                quantidade += 1
                print(f'total de produtos: {quantidade}')
                print(f'valor final: {quantidade * videogame_valor}')
                if escolher_qtd == "sair":
                    print("Conta fechada")
                    break

    elif escolha == 3:
         print(f'Você ira comprar geladeira') 
         print(f'Digite qualquer coisa para iniciar ou sair para encerrar fechar a conta') 

         geladeira_valor = 1150.00

         while escolher != "sair":
             quantidade = 0
             comprar = int(input("Digite 1 para somar os produtos"))
             if comprar == 1:
                quantidade += 1
                print(f'total de produtos: {quantidade}')
                print(f'valor final: {quantidade * geladeira_valor}')
                if escolher_qtd == "sair":
                    print("Conta fechada")
                    break

    elif escolha == 4:
         print(f'Você irá compra sofa') 
         print(f'Digite qualquer coisa para inciar ou sari para encerrar o progama') 
         sofa_valor = 800.00

         while escolher != "sair":
             quantidade = 0
             comprar = int(input("Digite 1 para somar os produtos"))
             if comprar == 1:
                quantidade += 1
                print(f'total de produtos: {quantidade}')
                print(f'valor final: {quantidade * sofa_valor}')
                if escolher_qtd == "sair":
                    print("Conta fechada")
                    break

    SistemaEcommerce()
    Compras(escolha_usuario)
    
  
def Pagar(total_compra):
            metodo_pagamento = input('Como deseja realizar o pagamento desta compra\n obs: pagamentos no cartão com acrescimo de 50 reais ').strip()
            if metodo_pagamento == 'cartão':
                conta_final = total_compra + 50
                print(f'Valor de sua compra: {conta_final}')
            elif metodo_pagamento == 'dinheiro':
                 pagamento_dinheiro = total_compra - 50

                 print(f'Total da sua compra: {pagamento_dinheiro}')
            else:
                print('Formação informada não existe')
            return pagamento_dinheiro    

def Metodo_entrega():
    escolha_frete = input('Como deseja receber esse produto\n1 - Pegar na loja\n2 - Receber por entrega')
    if escolha_frete == 1:
        print('Voce pode vir buscar seu produto em 7 horas')
    elif escolha_frete == 2:
        regiao = input('Digite a região em que você mora\n1- Sudeste\n2 - norte')
        if escolha_frete == "Sudeste":
            print('Poduto enviado')
        elif escolha_frete == "norte":
            print('Produto indisponivel')
        else:
            print('Informacao informada nao é valida. TENTE NOVAMENTE')     
def lista_desejo():
    lista_desejo = []
    adicionar_item = input('')            
            
Compras()





  
    
    
    
    
       





