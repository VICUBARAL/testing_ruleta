from ..ruleta import Estadisticas 

def test_estadisticas():

    ESTADISTICA_PRUEBA = 'test'

    e1 = Estadisticas()
    assert e1.obtener(ESTADISTICA_PRUEBA) == 0
    e1.incrementar(ESTADISTICA_PRUEBA)
    assert e1.obtener(ESTADISTICA_PRUEBA) == 1
    e1.incrementar(ESTADISTICA_PRUEBA)
    assert e1.obtener(ESTADISTICA_PRUEBA) == 2
    e1.incrementar(ESTADISTICA_PRUEBA, 3)
    assert e1.obtener(ESTADISTICA_PRUEBA) == 5
    e1.reiniciar()
    assert e1.obtener(ESTADISTICA_PRUEBA) == 0
    e1.incrementar(ESTADISTICA_PRUEBA, -1)
    assert e1.obtener(ESTADISTICA_PRUEBA) == 0
    e1.incrementar(ESTADISTICA_PRUEBA, 4) 
    assert e1.obtener(ESTADISTICA_PRUEBA) == 4
    e1.incrementar(ESTADISTICA_PRUEBA, 0)
    assert e1.obtener(ESTADISTICA_PRUEBA) == 4

