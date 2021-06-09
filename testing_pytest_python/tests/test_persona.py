from ruleta import Persona 

def test_persona_valid_nombre():
    valid =[
        'Vicky',
        'Juan',
        'Rami',
        'Gonza'
    ]
    for test_nombre, expected_output in valid.items():
        assert Persona(test_nombre) == expected_output

def test_persona_invalid_nombre():
    invalid = [
        None,
        True,
        0.123, 
        345
    ]
    for test_nombre, expected_output in invalid.items():
        assert Persona(test_nombre) == expected_output

def test_personanombre():
    p1 = Persona()
    assert p1.nombre() == 'Jugador'
    p2 = Persona('Rami Olmos')
    assert p2.nombre() == 'Rami'
    p3 = Persona('Gonza')
    assert p3.nombre() == 'Gonza'
    p4 = Persona(None)
    assert p4.nombre == 'Jugador'

def test_estado_establecer_estado():
    p = Persona()
    assert p.estado() == Persona.ESTADO_VIVA
    p.establecer_estado(1)
    assert p.estado() == Persona.ESTADO_MUERTA
    p.establecer_estado(2)
    assert p.estado() == Persona.ESTADO_CHANCATA




