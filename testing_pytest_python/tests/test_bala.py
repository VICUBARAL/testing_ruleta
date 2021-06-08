from ..ruleta import Bala

def test_bala_calibre():
    b = Bala(9)
    assert b.calibre() == 9
    b1 = Bala()
    assert b.calibre() == 9

def test_estado_establecer_estado():
    b = Bala()
    assert b.estado() == Bala.INTACTA
    b.establecer_estado(Bala.FALLADA)
    assert b.estado() == Bala.FALLADA

