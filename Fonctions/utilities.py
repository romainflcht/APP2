from math import sqrt, asin, sin, cos, pi

EARTH_RADIUS = 6371


def is_float(number: str) -> bool:
    """
    :param number: Une chaine de caractère qui contient un flottant.
    :return: Renvoie True si la chaine de caractère peut être converti, sinon False.
    """
    try:
        float(number)
        return True

    except ValueError:
        return False


def calculate_dist(first_coord: tuple, second_coord: tuple) -> float:
    """
    Calcul la distance entre deux coordonnées GPS.
    :param first_coord: tuple de coordonnées en radians.
    :param second_coord: tuple de coordonnées en radians.
    :return: Renvoie un float correspondant à la distance en km.
    """

    return round(2 * EARTH_RADIUS * asin(sqrt(sin((second_coord[0] - first_coord[0]) / 2) ** 2
                                              + cos(first_coord[0]) * cos(second_coord[0]) *
                                              sin(((second_coord[1]) - first_coord[1]) / 2) ** 2)))


if __name__ == '__main__':
    print('Ce script n\'est pas destiné a être executé seul, importez le dans un autre programme.')
