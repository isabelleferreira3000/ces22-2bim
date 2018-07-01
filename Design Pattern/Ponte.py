# Implementação 1
class Desenhando_1(object):

    def desenhando_circulo(self, x, y, raio):
        print('implementacao 1: circulo em ({},{}) raio {}'.format(x, y, raio))


# Implementação 2
class Desenhando_2(object):

    def desenhando_circulo(self, x, y, raio):
        print('implementacao 2: circulo em ({},{}) raio {}'.format(x, y, raio))


# Refined Abstraction
class Circulo(object):

    def __init__(self, x, y, raio, desenhando_modo):
        self._x = x
        self._y = y
        self._raio = raio
        self._desenhando_modo = desenhando_modo

    # low-level
    def desenha(self):
        self._desenhando_modo.desenhando_circulo(self._x, self._y, self._raio)

    # high-level
    def escala(self, pct):
        self._raio *= pct


def main():
    shapes = (
        Circulo(1, 2, 3, Desenhando_1()),
        Circulo(5, 7, 11, Desenhando_2())
    )

    for shape in shapes:
        shape.escala(2.5)
        shape.desenha()


if __name__ == '__main__':
    main()
