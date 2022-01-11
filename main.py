from matplotlib import pyplot as plt
from mapa import Mapa
from time import sleep

TAXA_ATUALIZACAO = 0

mapa = Mapa()
# mapa.imprime('Inicialização')

plt.ion()

figure, ax = plt.subplots()

plt.imshow(Mapa.mapa)

i = 0

while True:

    i += 1

    figure.canvas.draw()
    figure.canvas.flush_events()

    mapa.converte_em_numeros()
    plt.imshow(mapa.mapa)

    mapa.converte_em_objetos()
    mapa.busca_proximo_passo()

    sleep(TAXA_ATUALIZACAO)

    if i == 100:
        break
