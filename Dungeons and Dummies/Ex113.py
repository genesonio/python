def isInt(msg):
    while True:
        try:
            n = int(input(msg))
        # except KeyboardInterrupt:
            # print('O usuário preferiu não informar um valor')
        except:
            print('O valor digitado não é um inteiro.')
        else:
            return n
        
def isFloat(msg):
    while True:
        num = input(msg).strip().replace(',', '.')
        try:
            float(num)
        except KeyboardInterrupt:
            print('O usuário preferiu não informar um valor')
        except:
            print('O valor digitado não é um inteiro')
        else:
            return f'{num.replace(".", ",")} é um número float'