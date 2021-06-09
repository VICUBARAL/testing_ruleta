from ..ruleta import Revolver, Bala

def test_revolver_tamano_tambor():
    r = Revolver()
    assert r.tamano_tambor() == 6
    r1 = Revolver('')
    assert r1.tamano_tambor() == 6
    r2 = Revolver(-6)
    assert r2.tamano_tambor() == 1
    r3 = Revolver(0)
    assert r3.tamano_tambor() == 1

def test_revolver_colocar_bala_vaciar_tambor_hay_bala():
    r = Revolver()
    assert r.en_vaina(r) == True
    assert r.colocar_bala(0) == False and r._hay_bala(0) == False
    assert r.colocar_bala(6) == True  and r._hay_bala(6) == True
    assert r.colocar_bala(8) == False and r._hay_bala(8) == False
    assert r.colocar_bala(-1) == False and r._hay_bala(-1) == False
    assert r.colocar_bala(1) == True and r._hay_bala(1) == True
    r.vaciar_tambor

def test_revolver_jalar_gatillo():
    r = Revolver()
    b = Bala()
    assert r.jalar_gatillo() == None and r._vaina_actual == 1
    



