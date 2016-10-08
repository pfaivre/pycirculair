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

from fonctions_vitesse import *


def calc_vitesse(TMJA, liste_facteur_corect, Vmax, Coef_route, B, Bbis, Pct_VL, Pct_Vul, prc_PL, Pct_Bus, Pct_Autocar, UnsurCapacite, prof_mensu_PL_DF, prof_horr_PL_DF, prof_mensu_DF, prof_horr_ete_DF, prof_horr_DF, prof_mensu_PL_JO, prof_horr_PL_JO, prof_mensu_JO, prof_horr_ete_JO, prof_horr_JO, nbr_j_an):

	#on calc le tableau des coefs charge (besoin de 1/capacite), pour JO puis DF	
	tableau_coef_charge_JO = tableau_coef_charge(TMJA, prof_mensu_PL_JO, prof_horr_PL_JO, prof_mensu_JO, prof_horr_ete_JO, prof_horr_JO, Pct_VL, Pct_Vul, prc_PL, Pct_Bus, Pct_Autocar, UnsurCapacite, nbr_j_an)	
	tableau_coef_charge_DF = tableau_coef_charge(TMJA, prof_mensu_PL_DF, prof_horr_PL_DF, prof_mensu_DF, prof_horr_ete_DF, prof_horr_DF, Pct_VL, Pct_Vul, prc_PL, Pct_Bus, Pct_Autocar, UnsurCapacite, nbr_j_an)

	#on calcul la vitesse brute a l'annee
	tableau_vitesse_brute_JO = tableau_vitesse_brute(tableau_coef_charge_JO, Vmax, Coef_route, B, Bbis)
	tableau_vitesse_brute_DF = tableau_vitesse_brute(tableau_coef_charge_DF, Vmax, Coef_route, B, Bbis)
	
		#on calc toutes les autres vitesses JO (jours ouvres)
	tableau_vitesse_vl_JO = tableau_vitesse_vl(tableau_vitesse_brute_JO)
	tableau_vitesse_motoinf50_JO = tableau_vitesse_motoinf50(tableau_vitesse_brute_JO)
	tableau_vitesse_motosup50_JO = tableau_vitesse_motosup50(tableau_vitesse_brute_JO, tableau_coef_charge_JO, liste_facteur_corect)
	tableau_vitesse_PL_JO = tableau_vitesse_PL(tableau_vitesse_brute_JO, tableau_coef_charge_JO, liste_facteur_corect)
	tableau_vitesse_Bus_JO = tableau_vitesse_Bus(tableau_vitesse_brute_JO, tableau_coef_charge_JO, liste_facteur_corect)
	tableau_vitesse_Autocar_JO = tableau_vitesse_Autocar(tableau_vitesse_brute_JO, tableau_coef_charge_JO, liste_facteur_corect)
	
		#on calc toutes les autres vitesses DF (dimanches et jours feries)
	tableau_vitesse_vl_DF = tableau_vitesse_vl(tableau_vitesse_brute_DF)
	tableau_vitesse_motoinf50_DF = tableau_vitesse_motoinf50(tableau_vitesse_brute_DF)
	tableau_vitesse_motosup50_DF = tableau_vitesse_motosup50(tableau_vitesse_brute_DF, tableau_coef_charge_DF, liste_facteur_corect)
	tableau_vitesse_PL_DF = tableau_vitesse_PL(tableau_vitesse_brute_DF, tableau_coef_charge_DF, liste_facteur_corect)
	tableau_vitesse_Bus_DF = tableau_vitesse_Bus(tableau_vitesse_brute_DF, tableau_coef_charge_DF, liste_facteur_corect)
	tableau_vitesse_Autocar_DF = tableau_vitesse_Autocar(tableau_vitesse_brute_DF, tableau_coef_charge_DF, liste_facteur_corect)

	toutes_vitesses = {	'vl_JO':tableau_coef_charge_vl_JO , 'vl_DF':tableau_coef_charge_vl_DF , 'motoinf50_JO':tableau_vitesse_motoinf50_JO , 'motoinf50_DF':tableau_vitesse_motoinf50_DF , 'motosup50_JO':tableau_vitesse_motosup50_JO , 'motosup50_DF':tableau_vitesse_motosup50_DF , 'PL_JO':tableau_vitesse_PL_JO , 'PL_DF':tableau_vitesse_PL_DF , 'Bus_JO':tableau_vitesse_Bus_JO , 'Bus_DF':tableau_vitesse_Bus_DF, 'Autocar_JO':tableau_vitesse_Autocar_JO , 'Autocar_DF':tableau_vitesse_Autocar_DF }

	return(toutes_vitesses)
