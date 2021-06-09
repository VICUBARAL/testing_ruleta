from ..ruleta import Bala

def test_bala_calibre():
    b = Bala()
    assert b.calibre() == 9
    b1 = Bala(0)
    assert b1.calibre() == 9
    b2 = Bala(5)
    assert b2.calibre() == 5
    b3 = Bala(-5)
    assert b3.calibre() == 9

def test_estado_establecer_estado():
    b = Bala()
    assert b.estado() == Bala.INTACTA
    b.establecer_estado(0)
    assert b.estado() == Bala.FALLADA
    b.establecer_estado(2)
    assert b.estado() == Bala.EXPLOTADA
    b.establecer_estado(-2)
    assert b.estado() == Bala.EXPLOTADA
    b.establecer_estado(None)
    assert b.estado() == Bala.FALLADA






