class Ventana:
    __titulo = ''
    __x_superior_izq = 0
    __y_superior_izq = 0
    __x_inferior_der = 0
    __y_inferior_der = 0

    def __init__(self, x = 'titulo', y = 0, z = 0, w = 100, f = 100):
        self.__titulo = x
        self.__x_superior_izq = max(0, y)
        self.__y_superior_izq = max(0, z)
        self.__x_inferior_der = min(500, w)
        self.__y_inferior_der = min(500, f)
        if self.__x_superior_izq >= self.__x_inferior_der:
            self.__x_superior_izq = self.__x_inferior_der-1
        if self.__y_superior_izq >= self.__y_inferior_der:
            self.__y_superior_izq = self.__y_inferior_der-1

    def mostrar(self):
        return print("nombre:{}\n punto superior izquierdo:[{},{}]\n punto inferior derecho:[{},{}]".format(self.__titulo,self.__x_superior_izq,self.__y_superior_izq,self.__x_inferior_der,self.__y_inferior_der))

    def mover(self,dx,dy):
        self.__x_superior_izq = max(0,self.__x_superior_izq+dx)
        self.__y_superior_izq = max(0,self.__y_superior_izq+dy)
        self.__x_inferior_der = min(500,self.__x_inferior_der+dx)
        self.__y_inferior_der = min(500,self.__y_inferior_der+dy)
    def moverDerecha(self,dx):
        self.mover(dx,0)
    def moverIzquierda(self,dx):
        self.mover(-dx,0)
    def subir(self,dy):
        self.mover(0,dy)
    def bajar(self,dy):
        self.mover(0,-dy)
    def getTitulo(self):
        return self.__titulo

    def alto(self):
        return self.__y_inferior_der - self.__y_superior_izq

    def ancho(self):
        return self.__x_inferior_der - self.__x_superior_izq

