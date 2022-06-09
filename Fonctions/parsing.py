# Copyright : romain_flcht

from Fonctions.utilities import *
from math import pi


def parse_csv_file(file_path: str) -> list:
    """
    :param file_path: Correspond au chemin du fichier.
    :return: Revoie les données du csv mis en forme :
    [Code_commune_INSEE, Nom_commune, Code_postal, Second_nom_commune, Libellé_d'acheminement,
    Lattitude, Longitude, distance (initialement vide)].
    """

    parced_data = []
    removed_elt_count = 0
    i = 0

    with open(file_path) as csv_file:
        current_line = csv_file.readline()

        while current_line:
            current_line = current_line.split(';')

            # Vérification des données : Le nom, le code INSEE, le code postal ainsi que
            # les coordonnées ne doivent pas être vide.
            if current_line[0] != '' or current_line[1] != '' or current_line[2] != '' or current_line[5] != '':
                # Données valides : Mise en forme des coordonnées GPS.
                gps_coordinates = current_line.pop(5).split('\n')[0].split(',')

                # Verification des coordonnées : Est ce qu'elles sont complètes et est ce qu'elles
                # sont convertible en float.
                if len(gps_coordinates) == 2:
                    if gps_coordinates[0] != '' and gps_coordinates[1] != '':
                        if is_float(gps_coordinates[0]) and is_float(gps_coordinates[1]):
                            # Conversion des coordonnées en radians.
                            current_line.append(float(gps_coordinates[0]) * pi / 180)
                            current_line.append(float(gps_coordinates[1]) * pi / 180)
                            current_line.append('empty_distance')

                            parced_data.append(current_line)

                    else:
                        removed_elt_count += 1

                else:
                    removed_elt_count += 1

            else:
                removed_elt_count += 1

            # Fin de la mise en forme.
            i += 1
            current_line = csv_file.readline()

    # Affichage des resultats.
    print(f'{len(parced_data)} éléments on été traitées et {removed_elt_count} '
          f'{"élément a été supprimé" if removed_elt_count < 2 else "éléments ont été supprimés"}'
          ' car certaines données étaient manquante ou incorrecte.', end='\n\n')

    return parced_data


if __name__ == '__main__':
    print('Ce script n\'est pas destiné a être executé seul, importez le dans un autre programme.')
