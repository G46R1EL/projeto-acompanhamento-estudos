import json
from datetime import date

CAMINHO_ARQUIVO = 'bd.json'
data_atual = date.today()

class ProgressoEstudos:

    def __init__(self):
        self.horas_estudadas = 0.0
        self.conteudo = ""
        self.linguagem = ""
        self.data_ultimo_estudo = ""
    
    def inserir_informacoes(self):
        self.conteudo = input('Insira a descrição do conteúdo estudado: ')
        while True:
            try:
                self.horas_estudadas = float(input('Insira a quantidade de horas estudadas: '))
                if self.horas_estudadas < 0:
                    print('Por favor insira um número que não seja negativo.')
                else:
                    break
            except ValueError:
                print('Entrada inválida. Por favor insira um valor numérico')
                
        self.linguagem = input('Insira a linguagem de programação utilizada: ')
        self.data_ultimo_estudo = input('Insira a data do último estudo(DD/MM/AAAA): ')


while True:
    print(f'Olá, hoje é dia {data_atual}, vamos registrar seus estudos!')
    opcao = input('Digite [I]nserir ou [S]air: ')
    if opcao == 'I' or opcao == 'i':
        estudo1 = ProgressoEstudos()
        estudo1.inserir_informacoes()

        dados_estudo = vars(estudo1)
        bd = [dados_estudo]

        with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
            json.dump(bd, arquivo, indent=4, ensure_ascii=False)
    elif opcao == 'S' or opcao == 's':
        print('Você saiu, obrigado!')
        break
    else:
        print('Por favor digite um valor válido.')