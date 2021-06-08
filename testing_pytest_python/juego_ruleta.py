
def esOpcionValida(opcion, valoresValidos: list) -> bool:
    try:
        return opcion in valoresValidos
    except TypeError:
        return False
