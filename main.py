from matplotlib import pyplot as plt
from mapa import Mapa
from time import sleep

TAXA_ATUALIZACAO = 0.1

mapa = Mapa()

plt.ion()

figure, ax = plt.subplots()

plt.imshow(Mapa.mapa)




i = 0

while True:

    i += 1

    figure.canvas.draw()

    figure.canvas.flush_events()

    plt.imshow(mapa.mapa)

    sleep(TAXA_ATUALIZACAO)

    # mapa.busca_proximo_passo()
    # print('Converte mapa ... ')
    mapa.converte_mapa_objetos()

    if i == 50:
        break

# plt.imshow(Mapa.mapa)
# plt.title("Cavaleiros do Zodíaco")
# # for i in range(4):
#
# plt.pause(1)
# sleep(2)
# plt.show()
# print('sleep')
# plt.imshow(Mapa2.mapa)
#
# # plt.pause(1)
# # print('......')


