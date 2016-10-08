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


from data import *
from calcul_vitesse import *


#quelques constantes
constante = dict_constantes()

#la liste habituelle, une ligne par troncon

# pour les test, liste_troncon = ['ligne1'], a changer quand data sera a jour

liste_troncon = ['ligne1']

for ligne in liste_troncon:
	# data relatives a la ligne
	data_vitesse = data_vitesse(ligne)

	#calcul des vitesses, ressort un dictionnaire contenant les tableaux de vitesses pour chaque categorie, separe en JO et DF
	tableaux_vitesse = calc_vitesse(data_vitesse['TMJA'], constante['liste_facteur_corect'], data_vitesse['Vmax'], constante['Coef_route'], data_vitesse['B'], constante['Bbis'], data_vitesse['prc_VL'], data_vitesse['prc_Vul'], data_vitesse['prc_PL'], data_vitesse['prc_Bus'], data_vitesse['prc_Autocar'], data_vitesse['UnsurCapacite'],data_vitesse['prof_mensu_PL_DF'], data_vitesse['prof_horr_PL_DF'], data_vitesse['prof_mensu_DF'], data_vitesse['prof_horr_ete_DF'], data_vitesse['prof_horr_DF'], data_vitesse['prof_mensu_PL_JO'], data_vitesse['prof_horr_PL_JO'], data_vitesse['prof_mensu_JO'], data_vitesse['prof_horr_ete_JO'], data_vitesse['prof_horr_JO'], constante['nbr_j_an'], data_vitesse['cat_voie'])


########
'''
	liste_facteur_emission_vulE = fonction(tableaux_vitesse[0], ...)
	liste_facteur_emission_vulD =
	...
	
	liste_emissionsType_vulE = calc_emission(liste_tableau_vitesse[0], liste_facteur_emission_vulE)
	liste_emissionsType_vulD = calc_emission(liste_tableau_vitesse[2], liste_facteur_emission_vulD)
	...
	liste_simpli = somme_emission(liste_emissionsType_vul, liste_emissionsType_vulD, ...)
	export_emissions(liste_simpli, donnee_de_connection)
'''


print('fin')


