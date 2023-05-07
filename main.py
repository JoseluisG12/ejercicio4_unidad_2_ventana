from ClaseVentana import Ventana
def test():
    opc = int(input("desea probar el test 1 = datos correctos 2 = datos incorrectos 0 = salir\n"))
    while opc != 0:
        if opc == 1:
            print('=======Ventana de prueva========')
            ventanaprueba = Ventana("prueba")
            ventanaprueba.mostrar()
            print('=========Ventana con datos correctos==========')
            ventanaprueba = Ventana('correcta',10,20)
            ventanaprueba.mostrar()
            print('*** Mueve a la derecha ***')

            ventanaprueba.moverDerecha(10)

            ventanaprueba.mostrar()

            print('*** Mueve a la izquierda ***')

            ventanaprueba.moverIzquierda(10)

            ventanaprueba.mostrar()

            print('*** Bajar ***')

            ventanaprueba.bajar(10)

            ventanaprueba.mostrar()

            print('==== Ventana Borrar ====')

            ventanaprueba = Ventana('Borrar', 10, 20, 100, 200)

            ventanaprueba.mostrar()

            print('*** Subir ***')

            ventanaprueba.subir(5)

            ventanaprueba.mostrar()

            print('*** Subir ***')

            ventanaprueba.subir(5)

            ventanaprueba.mostrar()

            print('*** Bajar ***')

            ventanaprueba.bajar(5)

            ventanaprueba.mostrar()


        if opc == 2:
            print('=======Ventana de prueva========')
            ventanaprueba = Ventana("prueba")
            ventanaprueba.mostrar()
            print('=========Ventana con datos inocrrectos==========')
            ventanaprueba = Ventana('correcta',0, -100,-22,22)
            ventanaprueba.mostrar()
            print('*** Mueve a la derecha ***')

            ventanaprueba.moverDerecha(10)

            ventanaprueba.mostrar()

            print('*** Mueve a la izquierda ***')

            ventanaprueba.moverIzquierda(10)

            ventanaprueba.mostrar()

            print('*** Bajar ***')

            ventanaprueba.bajar(10)

            ventanaprueba.mostrar()

            print('==== Ventana Borrar ====')

            ventanaprueba = Ventana('Borrar', 10, 20, 100, 200)

            ventanaprueba.mostrar()

            print('*** Subir ***')

            ventanaprueba.subir(5)

            ventanaprueba.mostrar()

            print('*** Subir ***')

            ventanaprueba.subir(5)

            ventanaprueba.mostrar()

            print('*** Bajar ***')

            ventanaprueba.bajar(5)

            ventanaprueba.mostrar()

        opc = int(input("desea probar el test 1 = datos correctos 2 = datos incorrectos 0 = salir\n"))


if __name__ ==  '__main__':
    opc = input("desea probar los metodos con la funcion test y = si n = no\n")
    if opc == 'y':
        test()
    print("_______main________")

    print('==== Ventana Inicio ====')

    ventanaInicio= Ventana('Inicio')

    ventanaInicio.mostrar()

    print('Ventana: {} Alto: {} Ancho: {}'.format(ventanaInicio.getTitulo(),ventanaInicio.alto(),ventanaInicio.ancho()))

    print('==== Ventana Cargar ====')

    ventanaCargar= Ventana('Cargar',10,20)

    ventanaCargar.mostrar()

    print('*** Mueve a la derecha ***')

    ventanaCargar.moverDerecha(10)

    ventanaCargar.mostrar()

    print('*** Mueve a la izquierda ***')

    ventanaCargar.moverIzquierda(10)

    ventanaCargar.mostrar()

    print('*** Bajar ***')

    ventanaCargar.bajar(10)

    ventanaCargar.mostrar()

    print('==== Ventana Borrar ====')

    ventanaBorrar = Ventana('Borrar', 10,20,100,200)

    ventanaBorrar.mostrar()

    print('*** Subir ***')

    ventanaBorrar.subir(5)

    ventanaBorrar.mostrar()

    print('*** Subir ***')

    ventanaBorrar.subir(5)

    ventanaBorrar.mostrar()

    print('*** Bajar ***')

    ventanaBorrar.bajar(5)

    ventanaBorrar.mostrar()