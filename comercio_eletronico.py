
# Back end de ecommerce
print('Seja bem vindo a X')
Entrada = input(' Digite:\n \n1) E para entrar e ver o catalogo de produtos\n \n2) I para Iniciar\n \n3) EN para encerrar o progama : ').upper()




#def IniciarECadastro(Entrada):

if Entrada == 'e'.upper():
    print('Bem vindo ao catalogo')
    #cadastro = input('Olá,Você possui conta em nosso sistema : ')

elif Entrada == 'i'.upper():
    lista_usuarios = []
    print('Bem vindo a area de login !!')
    Area_login = input('Digite nome para entrar')
    if Criar_conta == 'criar conta':
       Nome = input('Digite o seu nome para criar conta no nosso sistema')
       Adicao_sistema = lista_usuarios.append(Nome)
    
    elif Area_login == 'entrar':
     for Area_login in lista_usuarios:
        if Area_login not in lista_usuarios:
            print('Sua Informação de login não consta em nosso sistema, Crie uma conta')
           


elif Entrada == 'en'.upper():
    print('Progama encerrado !!')
        
       





