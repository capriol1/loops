# Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já
# é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços
# de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo

print(f'Preço do pão: R$ 0,18\n'
      f'Panificadora Pão de Ontem - Tabela de preço')

for i in range(1, 51):
    print(f'{i} - R$ {0.18 * i:.2f}')