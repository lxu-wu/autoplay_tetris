def comparer_matrices(matrice1, matrice2):
    if len(matrice1) != len(matrice2) or len(matrice1[0]) != len(matrice2[0]):
        return False

    for i in range(len(matrice1)):
        for j in range(len(matrice1[0])):
            if matrice1[i][j] != matrice2[i][j]:
                return False

    return True