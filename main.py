from Fonctions.parsing import parse_csv_file
from Fonctions.utilities import calculate_dist
from Fonctions.sort_algorithm import insertion_sort, fusion_sort
from time import time

if __name__ == '__main__':

    parsed_data = parse_csv_file('laposte_hexasmal.csv')

    user_input = input('Entrez votre lieu : ').upper()

    # Récupération des coordonnées de la ville entrée.
    is_found = False
    city_index = -1

    for index, elt in enumerate(parsed_data):
        if elt[1] == user_input:
            is_found = True
            city_index = index

            print(f' • [✓] Votre lieu a été trouvé :\n\t ➜ {elt[2]}, {elt[1].capitalize()}', end='\n\n')

    if not is_found:
        print(' • [✗] Votre lieu n\'as pas été trouvée, veuillez réessayer...')

    else:
        # Si la ville a été trouvé, alors on calcul la distance avec toutes les autres villes.
        for elt in parsed_data:
            elt[-1] = calculate_dist((elt[-3], elt[-2]), (parsed_data[city_index][-3], parsed_data[city_index][-2]))

        print("Tri par Fusion en cours, veuillez patienter...")
        timer = time()
        algo_result = fusion_sort(parsed_data)
        print(f'➜ {len(algo_result)} éléments ont été trié en {time() - timer} secondes avec '
              f'un tri par Fusion.', end='\n\n')

        print(f' • Résultat : '
              f'\n\t ➜ Minimum : {algo_result[1][1].capitalize()}.'
              f'\n\t ➜ Premier quartile : {algo_result[len(algo_result) // 4][1].capitalize()}.'
              f'\n\t ➜ Médiane : {algo_result[len(algo_result) // 2][1].capitalize()}.'
              f'\n\t ➜ Troisième quartile : {algo_result[(len(algo_result) // 4) * 3][1].capitalize()}.'
              f'\n\t ➜ Maximum : {algo_result[len(algo_result) - 1][1].capitalize()}.', end='\n\n')

        print("Tri par Insertion en cours, veuillez patienter...")
        timer = time()
        algo_result = insertion_sort(parsed_data)
        print(f'➜ {len(algo_result)} éléments ont été trié en {time() - timer} secondes avec '
              f'un tri par Insertion.', end='\n\n')

        print(f' • Résultat : '
              f'\n\t ➜ Minimum : {algo_result[1][1].capitalize()}.'
              f'\n\t ➜ Premier quartile : {algo_result[len(algo_result) // 4][1].capitalize()}.'
              f'\n\t ➜ Médiane : {algo_result[len(algo_result) // 2][1].capitalize()}.'
              f'\n\t ➜ Troisième quartile : {algo_result[(len(algo_result) // 4) * 3][1].capitalize()}.'
              f'\n\t ➜ Maximum : {algo_result[len(algo_result) - 1][1].capitalize()}.', end='\n\n')
