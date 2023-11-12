def nombres_de_un(matrice):
	somme_de_1=0
	for rangees in (matrice):
		for case in (rangees):
			if case==1: #je check si la case est un 1 (vide mais avec une case remplie juste au dessus)
				somme_de_1+=1 

	return somme_de_1

matrice=[[2,2,2,0,2,0,0],
		[2,1,1,2,1,0,2],
		[1,0,0,2,2,2,1],
		[2,2,2,1,1,1,0],
		[1,2,1,0,0,0,0]]
matrice_2 =[[2,2,2,2,2,0,2],
			[1,1,2,1,1,0,1],
			[2,2,1,2,1,0,2],
			[1,1,1,2,2,0,1],
			[2,2,2,1,2,0,1],
			[1,2,1,1,1,0,1]]


def valeurs_des_trous(matrice):
	# fonction pour check si un 1 touche un 0
	def touche_0(i, j):
		if i > 0 and matrice[i - 1][j] == 0 or i < len(matrice) - 1 and matrice[i + 1][j] == 0 or j > 0 and matrice[i][j - 1] == 0 or j < len(matrice[i]) - 1 and matrice[i][j + 1] == 0:
			return True
		
	flag=True
	while flag: #j'itere le temps qu'il y ai plus de 0 qui touchent de 1
		flag = False  
		for i in range(len(matrice)):
			for j in range(len(matrice[i])):
				if matrice[i][j] == 1 and touche_0(i, j):
					matrice[i][j] = 0
					flag = True

	trous = []
	index_cases = []

	for i in range(len(matrice)):
		for j in range(len(matrice[i])):
			if matrice[i][j] == 1 and (i, j) not in index_cases:
				nombre_case_trou = 0
				queue = [(i, j)]
				index_cases.append((i, j))

				while queue:
					current_i, current_j = queue[0]
					nombre_case_trou += 1
					queue=[]

					# je check la case en haut
					if current_i > 0 and matrice[current_i - 1][current_j] == 1 and (current_i - 1, current_j) not in index_cases:
						queue.append((current_i - 1, current_j))
						index_cases.append((current_i - 1, current_j))

					# check la case en dessous
					if current_i < len(matrice) - 1 and matrice[current_i + 1][current_j] == 1 and (current_i + 1, current_j) not in index_cases:
						queue.append((current_i + 1, current_j))
						index_cases.append((current_i + 1, current_j))

					# check la case à gauche
					if current_j > 0 and matrice[current_i][current_j - 1] == 1 and (current_i, current_j - 1) not in index_cases:
						queue.append((current_i, current_j - 1))
						index_cases.append((current_i, current_j - 1))

					# check la case à droite
					if current_j < len(matrice[i]) - 1 and matrice[current_i][current_j + 1] == 1 and (current_i, current_j + 1) not in index_cases:
						queue.append((current_i, current_j + 1))
						index_cases.append((current_i, current_j + 1))
					

				trous.append(nombre_case_trou)

	return trous



def rotate_piece(piece):
	
	piece_pivotee = [[piece[j][i] for j in range(len(piece))] for i in range(len(piece[0])-1, -1, -1)]
	return piece_pivotee

matrice_2 =[[2,2,2,2,0,0,0],
			[1,1,2,1,0,0,0],
			[2,2,1,2,0,0,0],
			[1,1,1,2,2,0,1],
			[2,2,2,1,2,0,1],
			[1,2,1,1,1,0,1]]

matrice_3 =[[2,2,2,2,0,2,0],
			[1,1,2,1,2,2,0],
			[2,2,1,2,2,0,0],
			[1,1,1,2,2,0,1],
			[2,2,2,1,2,0,1],
			[1,2,1,1,1,0,1]]
piece=[[0,2,0],
	   [2,2,2]]


J = [[2,0,0],\
	 [2,2,2]] #fini
 
L = [[0,0,2],\
	 [2,2,2]] #fini
 
O = [[2,2],\
	 [2,2]] #fini
 
S = [[0,2,2],\
	 [2,2,0]]
 
Z = [[2,2,0],\
	 [0,2,2]]
 
T = [[0,2,0],\
	 [2,2,2]] #fini
 
I = [[2,2,2,2]] #fini

piece_jsp=[[],[]]
def placement_piece(matrice_before, matrice_after, piece):
	total_index=[]
	row_piece=[]
	piece_after=[]
	actions=[]
	matrice_bis_before = []
	matrice_bis_after = []

	#Copy both matrices
	for rows in matrice_before:
		matrice_bis_before.append(rows)
	for rows in matrice_after:
		matrice_bis_after.append(rows)
	#Replace every 1 in both bis_matrices to 0
	for rows in matrice_bis_before:
		for i in range (len(rows)):
			if rows[i]==1:
				rows[i]=0
	for rows in matrice_bis_after:
		for i in range (len(rows)):
			if rows[i]==1:
				rows[i]=0

	#Find difference between the two matrices
	for i in range(len(matrice_before)):
		for j in range(len(matrice_bis_before[i])):
			if matrice_bis_before[i][j]!=matrice_bis_after[i][j]:
				row_piece.append(matrice_bis_after[i][j])
				total_index.append((i,j))
		if row_piece!=[]:
			piece_after.append(row_piece)
			row_piece=[]
	print(piece_after)
	print(total_index)

	#Find which rotations has been applied
	if piece==I:
		if len(piece_after)==4:
			actions.append('up')

	if piece == O: #fini
		pass

	if piece == L: #fini
		if len(piece_after)==2:
			if piece_after[0]==[2,2,2]:
				actions.append('up')
				actions.append('up')
		else:
			if (total_index[0][0],total_index[0][1]) == (total_index[1][0],total_index[1][1]+1):
				actions.append('up')

			else:
				actions.append('up')
				actions.append('up')
				actions.append('up')	

	if piece == J: #fini
		if len(piece_after)==2:
			if piece_after[0]==[2,2,2]:
				actions.append('up')
				actions.append('up')
		else:
			if (total_index[0][0],total_index[0][1]) == (total_index[1][0],total_index[1][1]+1):
				actions.append('up')
				actions.append('up')
				actions.append('up')
			else:
				actions.append('up')

	if piece == T: #fini
		if piece_after[0]==[2,2,2]:
			actions.append('up')
			actions.append('up')

		elif len(piece)==3:
			if total_index[0][1]!=total_index[1][1]:
				actions.append('up')
			elif total_index[0][1]==total_index[1][1]:
				actions.append('up')
				actions.append('up')
				actions.append('up')

	if piece == Z:
		if len(piece_after)==3:
			actions.append("up")
		
	if piece == S:
		if len(piece_after)==3:
			actions.append("up")

