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



#calcul du nombre de veh legers par h du mois 
######################################################################################


def Calc_nbr_vref_h(mois, TMJA, nbr_j_an, val_profil_mensu, val_profil_horraire_ete, val_profil_horraire):
	if mois == 7 or mois == 8:
		Nbr_Vref= TMJA * nbr_j_an * val_profil_mensu * val_profil_horraire_ete
	else:
		Nbr_Vref= TMJA * nbr_j_an * val_profil_mensu * val_profil_horraire
	return(Nbr_Vref)

def Calc_nombre_PL_h(TMJA , nbr_j_an , val_profil_mensu_PL, val_profil_horraire_PL, prc_PL):
	Nbr_PL = TMJA * nbr_j_an * val_profil_mensu_PL * val_profil_horraire_PL * prc_PL
	return(Nbr_PL)

#####################################################################################

def calc_coef_charge(Nombre_VUL_h, Nombre_VP_h, Nombre_PL_h, Nombre_BUS_h, Nombre_AUTOCAR_h, UnsurCapacite):
	##coef de charge a partir duquel on calculera la vitesse de chaque categorie
	Coef_charge = ((Nombre_VUL_h + Nombre_VP_h + (Nombre_PL_h + Nombre_BUS_h + Nombre_AUTOCAR_h)*2 ) * UnsurCapacite)
	return(Coef_charge)

def calc_taux_congestion(Coef_charge):
	#est-ce bien utile?
	Taux_congestion = Coef_charge * 100
	return(Taux_congestion)
		
############################################################################

def vitesse_brute(Coef_charge, Vmax, Coef_route, B, Bbis):
	#vitesse_brute
	if Coef_charge < 1:
		vitesse_brute = 1/ ((1/Vmax)*(1+Coef_route*(Coef_charge**B)))
	else:
		vitesse_brute = 1/ ((1/Vmax)*(1+Coef_route*(Coef_charge**Bbis)))
	return(vitesse_brute)

def calc_vitesse_vl(vitesse_brute):
	if vitesse_brute >= 130 :
		Vitesse_vl = 130
	elif vitesse_brute <= 10 :
		Vitesse_vl = 10
	else:
		Vitesse_vl = vitesse_brute
	return(Vitesse_vl)

def calc_vit_motoinf50(vitesse_brute):
	if vitesse_brute >= 50 :
		Vitesse_moto_inf50 = 50
	elif vitesse_brute <= 10 :
		Vitesse_moto_inf50 = 10
	else:
		Vitesse_moto_inf50 = vitesse_brute
	return(Vitesse_moto_inf50)

def calc_vit_motosup50(vitesse_vl, Taux_congestion, liste_facteur_correct, cat_voie):

	if Taux_congestion < 40:
		correc_vitesse_moto =  liste_facteur_correct[cat_voie - 1][0]
	elif Taux_congestion > 40 and Taux_congestion <= 80:
		correc_vitesse_moto =liste_facteur_correct[cat_voie - 1][1]
	elif Taux_congestion > 80 and Taux_congestion <= 100:
		correc_vitesse_moto =liste_facteur_correct[cat_voie - 1][2]
	elif Taux_congestion > 100:
		correc_vitesse_moto = liste_facteur_correct[cat_voie - 1][3]

	if vitesse_vl + correc_vitesse_moto >= 140 :
		Vitesse_moto_sup50 = 140
	elif vitesse_vl + correc_vitesse_moto <= 10 :
		Vitesse_moto_sup50 = 10
	else:
		Vitesse_moto_sup50 = vitesse_vl + correc_vitesse_moto
	return(Vitesse_moto_sup50)

def calc_vit_PL(vitesse_vl, Taux_congestion, liste_facteur_correct, cat_voie):

	if Taux_congestion < 40:
		correc_vitesse_PL = liste_facteur_correct[cat_voie - 1][4]
	elif Taux_congestion > 40 and Taux_congestion <= 80:
		correc_vitesse_PL = liste_facteur_correct[cat_voie - 1][5]
	elif Taux_congestion > 80 and Taux_congestion <= 100:
		correc_vitesse_PL = liste_facteur_correct[cat_voie - 1][6]
	elif Taux_congestion > 100:
		correc_vitesse_PL = liste_facteur_correct[cat_voie - 1][7]

	if vitesse_vl + correc_vitesse_PL >= 110 :
		Vitesse_PL = 110
	elif vitesse_vl + correc_vitesse_PL <= 10 :
		Vitesse_PL = 10
	else:
		Vitesse_PL = vitesse_vl + correc_vitesse_PL
	return(Vitesse_PL)

def calc_vit_Bus(vitesse_vl, Taux_congestion, liste_facteur_correct, cat_voie):

	if Taux_congestion < 40:
		correc_vitesse_Bus = liste_facteur_correct[cat_voie - 1][8]
	elif Taux_congestion > 40 and Taux_congestion <= 80:
		correc_vitesse_Bus = liste_facteur_correct[cat_voie - 1][9]
	elif Taux_congestion > 80 and Taux_congestion <= 100:
		correc_vitesse_Bus = liste_facteur_correct[cat_voie - 1][10]
	elif Taux_congestion > 100:
		correc_vitesse_Bus = liste_facteur_correct[cat_voie - 1][11]

	if vitesse_vl + correc_vitesse_Bus >= 50 :
		Vitesse_Bus = 50
	elif vitesse_vl + correc_vitesse_Bus <= 10 :
		Vitesse_Bus = 10
	else:
		Vitesse_Bus = vitesse_vl + correc_vitesse_Bus
	return(Vitesse_Bus)


def calc_vit_Autocar(vitesse_vl, Taux_congestion, liste_facteur_correct, cat_voie):

	if Taux_congestion < 40:
		correc_vitesse_Autocar = liste_facteur_correct[cat_voie - 1][12]
	elif Taux_congestion > 40 and Taux_congestion <= 80:
		correc_vitesse_Autocar = liste_facteur_correct[cat_voie - 1][13]
	elif Taux_congestion > 80 and Taux_congestion <= 100:
		correc_vitesse_Autocar = liste_facteur_correct[cat_voie - 1][14]
	elif Taux_congestion > 100:
		correc_vitesse_Autocar = liste_facteur_correct[cat_voie - 1][15]

	if vitesse_vl + correc_vitesse_Autocar >= 120 :
		Vitesse_Car = 120
	elif vitesse_vl + correc_vitesse_Autocar <= 10 :
		Vitesse_Car = 10
	else:
		Vitesse_Car = vitesse_vl + correc_vitesse_Autocar
	return(Vitesse_Car)

####################################################################################
### 	creation d'un tableau de vitesse pour chaque categorie de vehicule
###		montrant chaque heure du mois	
###################################################################################

def tableau_coef_charge(TMJA, prof_mensu_PL, prof_horr_PL, prof_mensu, prof_horr_ete, prof_horr, Pct_VL, Pct_Vul, prc_PL, Pct_Bus, Pct_Autocar, UnsurCapacite, nbr_j_an):
	liste_CoefC_annee = []
	for mois in range(12):
		liste_coefC_h = []
		for heure in range(24):
			val_profil_mensu_PL = prof_mensu_PL[mois]
			val_profil_horraire_PL = prof_horr_PL[heure]
			val_profil_mensu = prof_mensu[mois]
			val_profil_horraire_ete = prof_horr_ete[heure]
			val_profil_horraire = prof_horr[heure]

			nbr_pl = Calc_nombre_PL_h(TMJA , nbr_j_an , val_profil_mensu_PL, val_profil_horraire_PL, prc_PL)
			nbr_vref = Calc_nbr_vref_h(mois, TMJA, nbr_j_an, val_profil_mensu, val_profil_horraire_ete, val_profil_horraire)
			Nombre_VL_h = nbr_vref * Pct_VL
			Nombre_VUL_h= Nombre_VL_h * Pct_Vul
			Nombre_VP_h = Nombre_VL_h - Nombre_VUL_h
			Nombre_BUS_h = nbr_vref * Pct_Bus
			Nombre_AUTOCAR_h = nbr_vref * Pct_Autocar
			
			coef_charge = calc_coef_charge(Nombre_VUL_h, Nombre_VP_h, nbr_pl, Nombre_BUS_h, Nombre_AUTOCAR_h, UnsurCapacite)
			
			liste_coefC_h.append(coef_charge)
		liste_CoefC_annee.append(liste_coefC_h)
	return(liste_CoefC_annee)


def tableau_vitesse_brute(liste_coefC_annee, Vmax, Coef_route, B, Bbis):
	liste_vitesse_brute_annee = []
	for mois in range(12):
		liste_vitesse_brute_h = []
		for heure in range(24):
			coef_charge = liste_coefC_annee[mois][heure]
			Vitesse_brute = vitesse_brute(coef_charge, Vmax, Coef_route, B, Bbis)
			liste_vitesse_brute_h.append(Vitesse_brute)
		liste_vitesse_brute_annee.append(liste_vitesse_brute_h)
	return(liste_vitesse_brute_annee)

def tableau_vitesse_vl(liste_vitesse_brute_annee):
	liste_vitesse_vl_annee = []
	for mois in range(12):
		liste_vitesse_vl_h = []
		for heure in range(24):
			vitesse_vl = calc_vitesse_vl(liste_vitesse_brute_annee[mois][heure])
			liste_vitesse_vl_h.append(vitesse_vl)
		liste_vitesse_vl_annee.append(liste_vitesse_vl_h)
	return(liste_vitesse_vl_annee)

def tableau_vitesse_motoinf50(liste_vitesse_brute_annee):
	liste_vitesse_motoinf50_annee = []
	for mois in range(12):
		liste_vitesse_motoinf50_h = []
		for heure in range(24):
			vitesse_motoinf50 = calc_vit_motoinf50(liste_vitesse_brute_annee[mois][heure])
			liste_vitesse_motoinf50_h.append(vitesse_motoinf50)
		liste_vitesse_motoinf50_annee.append(liste_vitesse_motoinf50_h)
	return(liste_vitesse_motoinf50_annee)

def tableau_vitesse_motosup50(liste_vitesse_brute_annee, tableau_coef_charge, liste_facteur_corect, cat_voie):
	liste_vitesse_motosup50_annee = []
	for mois in range(12):
		liste_vitesse_motosup50_h = []
		for heure in range(24):
			vitesse_motosup50 = calc_vit_motosup50(liste_vitesse_brute_annee[mois][heure], tableau_coef_charge[mois][heure] * 100, liste_facteur_corect, cat_voie)
			liste_vitesse_motosup50_h.append(vitesse_motosup50)
		liste_vitesse_motosup50_annee.append(liste_vitesse_motosup50_h)
	return(liste_vitesse_motosup50_annee)

def tableau_vitesse_PL(liste_vitesse_brute_annee, tableau_coef_charge, liste_facteur_corect, cat_voie):
	liste_vitesse_PL_annee = []
	for mois in range(12):
		liste_vitesse_PL_h = []
		for heure in range(24):
			vitesse_PL = calc_vit_PL(liste_vitesse_brute_annee[mois][heure], tableau_coef_charge[mois][heure] * 100, liste_facteur_corect, cat_voie)
			liste_vitesse_PL_h.append(vitesse_PL)
		liste_vitesse_PL_annee.append(liste_vitesse_PL_h)
	return(liste_vitesse_PL_annee)

def tableau_vitesse_Bus(liste_vitesse_brute_annee, tableau_coef_charge, liste_facteur_corect, cat_voie):
	liste_vitesse_Bus_annee = []
	for mois in range(12):
		liste_vitesse_Bus_h = []
		for heure in range(24):
			vitesse_Bus = calc_vit_Bus(liste_vitesse_brute_annee[mois][heure], tableau_coef_charge[mois][heure] * 100, liste_facteur_corect, cat_voie)
			liste_vitesse_Bus_h.append(vitesse_Bus)
		liste_vitesse_Bus_annee.append(liste_vitesse_Bus_h)
	return(liste_vitesse_Bus_annee)

def tableau_vitesse_Autocar(liste_vitesse_brute_annee, tableau_coef_charge, liste_facteur_corect, cat_voie):
	liste_vitesse_Car_annee = []
	for mois in range(12):
		liste_vitesse_Car_h = []
		for heure in range(24):
			vitesse_Car = calc_vit_Autocar(liste_vitesse_brute_annee[mois][heure], tableau_coef_charge[mois][heure] * 100, liste_facteur_corect, cat_voie)
			liste_vitesse_Car_h.append(vitesse_Car)
		liste_vitesse_Car_annee.append(liste_vitesse_Car_h)
	return(liste_vitesse_Car_annee)


