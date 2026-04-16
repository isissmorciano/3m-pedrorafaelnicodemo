import math

def crea_punto(x: float, y: float) -> dict:
    return {
        "X": x,
        "Y": y
    }

def distanza_tra_punti(p1: dict, p2: dict) -> float:
    dx = (p2['X'] - p1['X'])**2
    dy = (p2['Y'] - p1['Y'])**2
    distanza = math.sqrt(dx + dy)
    return distanza

def info_punto(punto: dict) -> str:
    return f"({punto['X']}, {punto['Y']})"