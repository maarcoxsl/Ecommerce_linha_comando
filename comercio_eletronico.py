# Ecommerce

print('Seja bem vindo ao Ecommerce X')

Iniciar = input('Coloque I para iniciar ou qualquer comando para fechar esse progama ').upper()
if Iniciar == 'I':
   print('Progama iniciado !!')
   while True:
    #if Iniciar == 'i'.upper():
    Clientes = []
    print('Bem vindo')
    Cadastro = input('Oque deseja ?\n1 - Criar conta\n2 - entrar\n3 - Digite qualquer comando se você desejar encerrar esse progama : ').strip()
    if  Cadastro == 'criar conta' or Cadastro == 'Criar conta':
        print('Sua conta sera criada !!')

        Nome = input('Digite o seu nome')
        Novo_usuario = Clientes.append(Nome)

        print(f'Olá {Nome} sua conta foi criada com sucesso ')
        
    elif Cadastro == 'entrar' or Cadastro == 'Entrar':
        print('Bem vindo de volta')  
    
    elif Cadastro == 'Lima':
        print(f'Usuarios presentes {Clientes}')

        
        #Cadastro = input('Digite o seu nome para criar conta em nosso sistema')
        '''
        for Cadastro in Clientes:
            if Cadastro in Clientes:
                print('Você já possui conta em nosso sistema')
            elif Cadastro not in Clientes:
                 print('Você tem conta no nosso sistema')
                 adicao_cliente = Clientes.append(Cadastro)
        '''         
    #else:
        #print('Progama encerrado')
        #break
        '''
        verifica = input('Tem conta no sistema\nSim\nNão')
        if verifica == 'sim' or verifica == 'sim'.index():
           for verifica in Clientes:
               if verifica not in Clientes:
                  print('Você nao é nosso')
        elif verifica == 'nao' or verifica == 'não'.index() or verifica == 'não':
             print('Você vai ter que criar uma conta em nosso sistema')  
        '''        
    else:
     print('Progama encerrado !!')
     break

    
       





