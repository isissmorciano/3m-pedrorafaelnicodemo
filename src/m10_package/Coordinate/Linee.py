import Punti
def crea_linea(p1: dict, p2: dict) -> dict:
    return {
        "P1": p1,
        "P2": p2
    }

def lunghezza_linea(linea: dict) -> float:
    return Punti.distanza_tra_punti(linea['p1'], linea['p2'])

def punto_medio(linea: dict) -> dict:
    x_medio = (linea['p1']['X'] + linea['p2']['X'])/2
    y_medio = (linea['p1']['Y'] + linea['p2']['Y'])/2
    return Punti.crea_punto(x_medio, y_medio)

def info_linea(linea: dict) -> str:
    return f"Linea da ({Punti.info_punto(linea['p1'])}) a ({Punti.info_punto(linea['p2'])})"