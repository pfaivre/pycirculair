'''Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.'''

#ces fonctions ont pour but d'importer les donnees


def dict_constantes():
	Bbis = 10
	Coef_route = 5
	liste_facteur_corect = [[5.85, 5.55, 5.6, 9.3, -45.15, -40.65, -7.65, -2.3, -45.15, -40.65, -7.65, -2.3, -33.2, -33.65, -7.65, -2.3],\
	[6.9, 6.2, 5.6, 9.3, -25.05, -23.1, -7.65, -2.3, -25.05, -23.1, -7.65, -2.3, -14.15, -18.1, -7.65, -2.3],\
	[6.9, 6.6, 5.45, 9.3, -9.5, -9.4, -5.05, -2.3, -9.5, -9.4, -5.05, -2.3, -5.8, -6.5, -5.05, -2.3],\
	[6.6, 5.4, 5.3, 9.5, -2.6, -3.1, -2, -1, -2.6, -3.1, -2, -1, -2.6, -3.1, -2, -1],\
	[4.9, 3.6, 4.3, 9.5, -6.8, -6.3, -3.6, -1, -17.8, -12.4, -9.5, -1, -6.8, -6.3, -3.6, -1],\
	[6.4, 5.9, 4.9, 6.4, -26.8, -22.1, -17.9, -2.4, -42.3, -35.3, -25.6, -2.4, -20.8, -22.1, -17.9, -2.4],\
	[6.7, 5.65, 3.9, 6.4, -7.1, -5.9, -6.55, -2.4, -24.45, -21.5, -16.45, -2.4, -6.35, -5.9, -6.55, -2.4],\
	[6.7, 5.65, 3.9, 6.4, -7.1, -5.9, -6.55, -2.4, -24.45, -21.5, -16.45, -2.4, -6.35, -5.9, -6.55, -2.4],\
	[5.7, 5.5, 4.4, 6.4, -6.05, -4.8, -5.05, -2.4, -12.95, -10.75, -4.85, -2.4, -6.05, -4.8, -5.05, -2.4],\
	[6, 4.9, 3.6, 9.5, -4, -4.1, -5.7, -1, -10.1, -9, -7.8, -1, -4, -4.1, -5.7, -1],\
	[4.9, 3.6, 4.3, 9.5, -6.8, -6.3, -3.6, -1, -17.8, -12.4, -9.5, -1, -6.8, -6.3, -3.6, -1],\
	[1.7, 2.6, 2.4, 9.5, -8.9, -6.2, -4.4, -1, -8.9, -14.7, -10.8, -1, -18.1, -6.2, -4.4, -1]]
	nbr_j_an = 365

	liste_constantes = {'Bbis':Bbis, 'Coef_route':Coef_route, 'liste_facteur_corect':liste_facteur_corect, 'nbr_j_an':nbr_j_an}
	return(liste_constantes)

def calc_B(cat_voie):
	if cat_voie == 1 or cat_voie == 2 or cat_voie == 3 or cat_voie == 6 or cat_voie == 7:
		b = 10
	else:
		b = 6
	return(b)

def calc_vmax(cat_voie):
	#liste des vitesses en fonction de la categorie de voie, sous forme liste = [vitesse_pour_cat_1, vitesse_pour_cat_2, ...]
	liste_v_a_vide = [129.3, 109.2, 90.6, 69.4, 46.5, 107.8, 86.6, 86.6, 66.6, 47.7, 46.5, 30.9]
	vmax = liste_v_a_vide[cat_voie - 1]
	return(vmax)


#### par defaut en attendant des vraies valeurs

def imp_data_vitesse(ligne):
	'''a metrre bien sur a jour pour que ca recherche dans les bases de donnees'''

	prof_mensu_DF = [0.0339122241, 0.0371614244, 0.0339833616, 0.0346645706, 0.0342286425, 0.0345905557, 0.0340547981, 0.0336714411, 0.0345905557, 0.0338119936, 0.0345905557, 0.0338119936]
	prof_horr_DF = [0.0028423142, 0.0015490055,0.0014097903,0.0025961526, 0.0086030848,0.0128994131, 0.0268299465, 0.070944956, 0.0731453713, 0.0555334855,0.0548777468,0.0548621553, 0.0565096438,0.0601289849, 0.0655839926, 0.0678451106, 0.0843167518, 0.0997859959, 0.0829982594, 0.0517932584, 0.0287224761, 0.0178483903, 0.011654021, 0.0067196932]
	prof_mensu_PL_DF = [0.0339122241, 0.0371614244, 0.0339833616, 0.0346645706, 0.0342286425, 0.0345905557, 0.0340547981, 0.0336714411, 0.0345905557, 0.0338119936, 0.0345905557, 0.0338119936]
	prof_horr_PL_DF = [0.0028423142, 0.0015490055,0.0014097903,0.0025961526, 0.0086030848,0.0128994131, 0.0268299465, 0.070944956, 0.0731453713, 0.0555334855,0.0548777468,0.0548621553, 0.0565096438,0.0601289849, 0.0655839926, 0.0678451106, 0.0843167518, 0.0997859959, 0.0829982594, 0.0517932584, 0.0287224761, 0.0178483903, 0.011654021, 0.0067196932]

	prof_mensu_JO = [0.0339122241, 0.0371614244, 0.0339833616, 0.0346645706, 0.0342286425, 0.0345905557, 0.0340547981, 0.0336714411, 0.0345905557, 0.0338119936, 0.0345905557, 0.0338119936]
	prof_horr_JO = [0.0028423142, 0.0015490055,0.0014097903,0.0025961526, 0.0086030848,0.0128994131, 0.0268299465, 0.070944956, 0.0731453713, 0.0555334855,0.0548777468,0.0548621553, 0.0565096438,0.0601289849, 0.0655839926, 0.0678451106, 0.0843167518, 0.0997859959, 0.0829982594, 0.0517932584, 0.0287224761, 0.0178483903, 0.011654021, 0.0067196932]
	prof_mensu_PL_JO = [0.0339122241, 0.0371614244, 0.0339833616, 0.0346645706, 0.0342286425, 0.0345905557, 0.0340547981, 0.0336714411, 0.0345905557, 0.0338119936, 0.0345905557, 0.0338119936]
	prof_horr_PL_JO = [0.0028423142, 0.0015490055,0.0014097903,0.0025961526, 0.0086030848,0.0128994131, 0.0268299465, 0.070944956, 0.0731453713, 0.0555334855,0.0548777468,0.0548621553, 0.0565096438,0.0601289849, 0.0655839926, 0.0678451106, 0.0843167518, 0.0997859959, 0.0829982594, 0.0517932584, 0.0287224761, 0.0178483903, 0.011654021, 0.0067196932]

	prof_horr_ete_DF = [0.0028423142, 0.0015490055,0.0014097903,0.0025961526, 0.0086030848,0.0128994131, 0.0268299465, 0.070944956, 0.0731453713, 0.0555334855,0.0548777468,0.0548621553, 0.0565096438,0.0601289849, 0.0655839926, 0.0678451106, 0.0843167518, 0.0997859959, 0.0829982594, 0.0517932584, 0.0287224761, 0.0178483903, 0.011654021, 0.0067196932]
	prof_horr_ete_JO = [0.0028423142, 0.0015490055,0.0014097903,0.0025961526, 0.0086030848,0.0128994131, 0.0268299465, 0.070944956, 0.0731453713, 0.0555334855,0.0548777468,0.0548621553, 0.0565096438,0.0601289849, 0.0655839926, 0.0678451106, 0.0843167518, 0.0997859959, 0.0829982594, 0.0517932584, 0.0287224761, 0.0178483903, 0.011654021, 0.0067196932]

	prc_PL = 0.007
	prc_VL = 0.68
	prc_Vul = 0.22
	prc_Bus = 0.005
	prc_Autocar = 0.05

	TMJA = 1000
	capacite = 1080
	cat_voie = 2
	UnsurCapacite = 1 / capacite
	B = calc_B(cat_voie)
	Vmax = calc_vmax(cat_voie)

	data_vitesse = {'prof_mensu_DF':prof_mensu_DF, 'prof_horr_DF':prof_horr_DF, 'prof_mensu_PL_DF':prof_mensu_PL_DF, 'prof_horr_PL_DF':prof_horr_PL_DF, 'prof_mensu_JO':prof_mensu_JO, 'prof_horr_JO':prof_horr_JO, 'prof_mensu_PL_JO':prof_mensu_PL_JO, 'prof_horr_PL_JO':prof_horr_PL_JO, 'prof_horr_ete_DF':prof_horr_ete_DF, 'prof_horr_ete_JO':prof_horr_ete_JO, 'prc_PL':prc_PL, 'prc_VL':prc_VL, 'prc_Vul':prc_Vul, 'prc_Bus':prc_Bus, 'prc_Autocar':prc_Autocar, 'TMJA':TMJA, 'capacite':capacite, 'cat_voie':cat_voie, 'UnsurCapacite':UnsurCapacite, 'B':B, 'Vmax':Vmax }

	return(data_vitesse)




















