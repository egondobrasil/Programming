def input_email(msg):
    posicao = msg.find(msg,"@")
    if posicao == 0:
        print("email inválido")