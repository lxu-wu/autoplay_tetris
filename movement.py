import time
import copy
from visual import Game
import pyautogui as gui
from utils import *

J = [[2,0,0],\
     [2,2,2]]

L = [[0,0,2],\
     [2,2,2]]

O = [[2,2],\
     [2,2]]

S = [[0,2,2],\
     [2,2,0]]

Z = [[2,2,0],\
     [0,2,2]]

T = [[0,2,0],\
     [2,2,2]]

I = [[2,2,2,2]]

def rotations(matrice_before, matrice_after, piece):
	total_index=[]
	row_piece=[]
	piece_after=[]
	actions=[]

	#Change the 1 into 0
	matrice_bis_before = change_ones_to_zeros(matrice_before)
	matrice_bis_after = change_ones_to_zeros(matrice_after)
	#Find difference between the two matrices
	for i in range(len(matrice_bis_before)):
		for j in range(len(matrice_bis_before[i])):
			if matrice_bis_before[i][j]!=matrice_bis_after[i][j]:
				row_piece.append(matrice_bis_after[i][j])
				total_index.append((i,j))
		if row_piece!=[]:
			piece_after.append(row_piece)
			row_piece=[]

	#Find which rotations has been applied
	if piece==I:
		if len(piece_after)==4:
			actions.append('up')

	elif piece == O: 
		pass
	
	
	elif piece == L: 
		if len(piece_after)==2:
			if piece_after[0]==[2,2,2]:
				actions.append('up')
				actions.append('up')
		else:
			if len(piece_after[0])==2:
				actions.append('up')

			elif len(piece_after[2])==2:
				actions.append('up')
				actions.append('up')
				actions.append('up')	

	elif piece == J: 
		if len(piece_after)==2:
			if piece_after[0]==[2,2,2]:
				actions.append('up')
				actions.append('up')
		else:
			if len(piece_after[0])==2:
				actions.append('up')
				actions.append('up')
				actions.append('up')
			elif len(piece_after[2])==2:
				actions.append('up')	

	elif piece == T: 
		
		if piece_after[0]==[2,2,2]:
			actions.append('up')
			actions.append('up')

		elif len(piece_after)==3:
			
			if total_index[0][1]!=total_index[1][1]:
				actions.append('up')
			elif total_index[0][1]==total_index[1][1]:
				actions.append('up')
				actions.append('up')
				actions.append('up')

	elif piece == Z or piece == S:	
		if len(piece_after)==3:
			actions.append('up')
	return actions
			
def deplacement_pieces(matrice_before, matrice_after, piece):
	total_index=[]
	actions=[]
	
	#Replace every 1 in both bis_matrices to 0
	matrice_bis_before = change_ones_to_zeros(matrice_before)
	matrice_bis_after = change_ones_to_zeros(matrice_after)

	#Find difference between the two matrices
	for i in range(len(matrice_bis_before)):
		for j in range(len(matrice_bis_before[i])):
			if matrice_bis_before[i][j] != matrice_bis_after[i][j]:
				total_index.append((i,j))

	actions = rotations(matrice_before, matrice_after, piece)
	for i in range(7): #déplacement après rotation
		actions.append('left') 
	# special_insertion = False
	# for i,j in total_index:
	# 	if (matrice_before[i][j] != 0):
	# 		special_insertion = True
	# print(special_insertion)

	column_index=[]
	row_index=[]  
	for indexes in total_index:
		column_index.append(indexes[1])
		row_index.append(indexes[0])
	# row_index_min=min(row_index) #le x minimum de la position finale
	# if special_insertion: 
	# 	for i in range(len(matrice_before[0])):
	# 		for j in range(len(matrice_before)-1):
	# 			if row_index_min==j + 1:
	# 				position=(j,i)
	# 				return (actions, position, "left" if min(column_index) > j else "right")
	# 			elif matrice_before[j+1][i]==2:
	# 				break
	for i in range(min(column_index)):
		actions.append("right")
	for j in range(max(row_index)):
		actions.append("down")
	return(actions, (0, 0), None)

# def find_camera_insertion(matrice_before, column_indexes, row_indexes):


# def is_special_insertion(matrice_before, total_index):
# 	for i,j in total_index:
# 		if (matrice_before[i][j] != 0):
# 			return (True)
# 	return(False)
