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




