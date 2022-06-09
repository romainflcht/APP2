def insertion_sort(data_to_sort: list) -> list:
    """
    Fonction qui execute un tri par insertion sur une liste mise en paramètre.
    :param data_to_sort: Liste à trier où le nombre permettant l'ordre ce trouve à l'index -1.
    exemple : [['E', 0], ['M', 2], ['E', 3], ['S', 1]] -> [['E', 0], ['S', 1], ['M', 2], ['E', 3]]
    :return: Renvoie la liste trié.
    """

    for index in range(1, len(data_to_sort)):

        distance = data_to_sort[index][-1]
        value_to_move = data_to_sort[index]
        moving_index = index - 1

        while moving_index >= 0 and distance < data_to_sort[moving_index][-1]:
            data_to_sort[moving_index + 1] = data_to_sort[moving_index]
            moving_index -= 1

        data_to_sort[moving_index + 1] = value_to_move

    return data_to_sort


def fusion(list_1: list, list_2: list) -> list:
    """
    Fonction fusion permettant de fusionner deux listes dans l'ordre. Le nombre permettant
    l'ordre ce trouve à l'index -1.
    :param list_1: Liste trié.
    :param list_2: Liste trié.
    :return: Renvoie les deux listes fusionné dans le bon ordre.
    """
    result_list = []
    i, j = 0, 0
    while i < len(list_1) and j < len(list_2):
        if list_1[i][-1] <= list_2[j][-1]:
            result_list.append(list_1[i])
            i += 1
        else:
            result_list.append(list_2[j])
            j += 1
    while i < len(list_1):
        result_list.append(list_1[i])
        i += 1
    while j < len(list_2):
        result_list.append(list_2[j])
        j += 1
    return result_list


def fusion_sort(data_to_sort: list) -> list:
    """
    Fonction qui execute un tri par Fusion sur un liste mise en paramètre.
    :param data_to_sort: Liste à trier.
    :return: Renvoie la liste triée.
    """

    # Si la liste a entre 0 et 1 élément, alors elle est déjà triée.
    if len(data_to_sort) <= 1:
        return data_to_sort[:]
    else:
        # Sinon on execute le tri Fusion.
        middle = len(data_to_sort) // 2
        list_1 = fusion_sort(data_to_sort[:middle])
        list_2 = fusion_sort(data_to_sort[middle:])

        return fusion(list_1, list_2)


if __name__ == '__main__':
    print('Ce script n\'est pas destiné a être executé seul, importez le dans un autre programme.')

    print(fusion_sort())