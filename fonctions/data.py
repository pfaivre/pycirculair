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


def liste_constantes():
	Bbis = 10
	Coef_route = 5
	#etc

	liste_constantes = [Bbis, Coef_route, .....]
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

def data_vitesset(ligne):
	'''a metrre bien sur a jour pour chaque ligne'''

 	# profil_ mensu comme : [profil_mensu_jo, profil_mensu_df],idem pour horraire
	prof_mensu=[0.0339122241, 0.0371614244, 0.0339833616, 0.0346645706, 0.0342286425, 0.0345905557, 0.0340547981, 0.0336714411, 0.0345905557, 0.0338119936]
	prof_horr=[0.0028423142, 0.0015490055,0.0014097903,0.0025961526, 0.0086030848,0.0128994131, 0.0268299465, 0.070944956, 0.0731453713, 0.0555334855,0.0548777468,0.0548621553, 0.0565096438,0.0601289849, 0.0655839926, 0.0678451106, 0.0843167518, 0.0997859959, 0.0829982594, 0.0517932584, 0.0287224761, 0.0178483903, 0.011654021, 0.0067196932]
	prof_mensu_PL=[0.0339122241, 0.0371614244, 0.0339833616, 0.0346645706, 0.0342286425, 0.0345905557, 0.0340547981, 0.0336714411, 0.0345905557, 0.0338119936]
	prof_horr_PL=[0.0028423142, 0.0015490055,0.0014097903,0.0025961526, 0.0086030848,0.0128994131, 0.0268299465, 0.070944956, 0.0731453713, 0.0555334855,0.0548777468,0.0548621553, 0.0565096438,0.0601289849, 0.0655839926, 0.0678451106, 0.0843167518, 0.0997859959, 0.0829982594, 0.0517932584, 0.0287224761, 0.0178483903, 0.011654021, 0.0067196932]
	prc_PL = 0.007
	prc_VL = 0.68
	prc_Vul = 0.22
	prc_Bus = 0.005
	prc_Autocar = 0.05

	TMJA = 1000
	capacite = 1080
	cat_voie = 2
	UnsurCapacite = 1 / Capacite
	B = calcl_B(cat_voie)
	Vmax = calc_vmax(cat_voie)


	data_vitesse = [prof_mensu_jo, prof_horr_jo=, prof_mensu_PL, prc_PL, prc_Vl, prc_Vul, prc_Bus, prc_Autocar, TMJA , capacite, cat_voie, UnsurCapacite, B, Vmax ]
	return(data_vitesse)

