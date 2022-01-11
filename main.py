from matplotlib import pyplot as plt
from mapa import Mapa
from time import sleep

TAXA_ATUALIZACAO = 0
QUANT_ATUALIZACOES = 40

mapa = Mapa()

plt.ion()

figure, ax = plt.subplots()

# print('Plotando mapa ...')
# plt.imshow(mapa.get_matriz())

i = 0

while True:

    i += 1

    # print('Plotando mapa ...')
    plt.imshow(mapa.get_matriz())

    # figure.canvas.draw()
    figure.canvas.flush_events()

    mapa.busca_proximo_passo()

    sleep(TAXA_ATUALIZACAO)

    if i == QUANT_ATUALIZACOES:
        break
