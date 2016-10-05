
def calc_vmax(cat_voie):
	#liste des vitesses en fonction de la categorie de voie, sous forme liste = [vitesse_pour_cat_1, vitesse_pour_cat_2, ...]
	liste_v_a_vide = [129.3, 109.2, 90.6, 69.4, 46.5, 107.8, 86.6, 86.6, 66.6, 47.7, 46.5, 30.9]
	vmax = liste_v_a_vide[cat_voie - 1]
	return(vmax)


def calc_B(cat_voie):
	if cat_voie == 1 or cat_voie == 2 or cat_voie == 3 or cat_voie == 6 or cat_voie == 7:
		b = 10
	else:
		b = 6
	return(b)



'''
Nombre de vehicule
'''
#calcul du nombre de veh legers par h du mois 
######################################################################################


def Calc_nbr_vref_h(mois, TMJA, nbr_j_an, val_profil_mensu, val_profil_horraire_ete, val_profil_horraire):
	if mois == 7 or mois == 8:
		Nbr_Vref= TMJA * nbr_j_an * val_profil_mensu * val_profil_horraire_ete
	elif:
		Nbr_Vref= TMJA * nbr_j_an * val_profil_mensu * val_profil_horraire
	return(Nbr_Vref)

def Calc_nombre_PL_h(TMJA * bnr_j_an * val_profil_mensu_PL, val_profil_horraire_PL, prc_PL):
	Nbr_PL = TMJA * bnr_j_an * val_profil_mensu_PL * val_profil_horraire_PL * prc_PL
	return(Nbr_Pl)

Nombre_VL_h_jo = Nombre_Vref_h_jo * Pct_VL
Nombre_VUL_h_jo= Nombre_VL_h_jo * Pct_Vul
Nombre_VP_h_jo = Nombre_VL_h_jo - Nombre_VUL_h_jo
Nombre_BUS_h_jo = Nombre_Vref_h_jo * Pct_Bus
Nombre_AUTOCAR_h_jo = Nombre_Vref_h_jo * Pct_Autocar



				###################################################
'''
coef de charge, a calculer pour chaque heure
'''



def calc_coef_charge(Nombre_VUL_h, Nombre_VP_h, Nombre_PL_h, Nombre_BUS_h, Nombre_AUTOCAR_h, UnsurCapacite):
	Coef_charge = ((Nombre_VUL_h + Nombre_VP_h + (Nombre_PL_h + Nombre_BUS_h + Nombre_AUTOCAR_h)*2 ) * UnsurCapacite)  ##coef de charge a partir duquel on calculera la vitesse de chaque categorie
	return(Coef_charge)

def calc_taux_congestion(Coef_charge)
	Taux_congestion = Coef_charge * 100
	return(Taux_congestion)



'''
vitesse de trafic
'''


def Correction_vitesse(cat_voie, taux_congestion):

# les fact de corr dependent de la caegorie de la voi
# tableau des facteurs correctifs sous la forme de liste, tel que:
# liste_facteur_correct = [ liste_des_valeurs_pour_la_categorie_de_voie_1, liste_des_valeurs_pour_la_categorie_de_voie_2, ...]
# dans lequel :
# liste_des_valeurs_pour_la_categorie_de_voie_1 = [fact_2roues_traf_fluide , fact_2roues_traf_dense, fact_2roues_traf_sature, fact_PL_bouchon, fact_PL_traf_fluide , fact_PL_traf_dense, fact_PL_traf_sature, fact_PL_bouchon, fact_bus_traf_fluide, ..., fact_Autocar_bouchon], etc
# donnees d’après rapport final ARTEMIS – Oct 2007 (p27)

	liste_facrteur_corect = [[5.85, 5.55, 5.6, 9.3, -45.15, -40.65, -7.65, -2.3, -45.15, -40.65, -7.65, -2.3, -33.2, -33.65, -7.65, -2.3],\
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

	if Taux_congestion < 40:
		correc_vitesse_PL = liste_facteur_correct[cat_voie - 1][4]
		correc_vitesse_Bus = liste_facteur_correct[cat_voie - 1][8]
		correc_vitesse_Autocar = liste_facteur_correct[cat_voie - 1][12]
		correc_vitesse_moto =  liste_facteur_correct[cat_voie - 1][0]
	elif Taux_congestion > 40 And Taux_congestion <= 80:
		correc_vitesse_PL = liste_facteur_correct[cat_voie - 1][5]
		correc_vitesse_Bus = liste_facteur_correct[cat_voie - 1][9]
		correc_vitesse_Autocar = liste_facteur_correct[cat_voie - 1][13]
		correc_vitesse_moto =liste_facteur_correct[cat_voie - 1][1]
	elif Taux_congestion > 80 And Taux_congestion <= 100:
		correc_vitesse_PL = liste_facteur_correct[cat_voie - 1][6]
		correc_vitesse_Bus = liste_facteur_correct[cat_voie - 1][10]
		correc_vitesse_Autocar = liste_facteur_correct[cat_voie - 1][14]
		correc_vitesse_moto =liste_facteur_correct[cat_voie - 1][2]
	elif Taux_congestion > 100:
		correc_vitesse_PL = liste_facteur_correct[cat_voie - 1][7]
		correc_vitesse_Bus = liste_facteur_correct[cat_voie - 1][11]
		correc_vitesse_Autocar = liste_facteur_correct[cat_voie - 1][15]
		correc_vitesse_moto = liste_facteur_correct[cat_voie - 1][3]
	correcteurs = [correc_vitesse_moto, correc_vitesse_PL, correc_vitesse_Bus, correc_vitesse_Autocar]
	return(correcteurs)
		
############################################################################





def vitesse_brute(coef_charge, Vmax, Coef_route, Coef_charge, B, Bbis):
	#vitesse_brute
	if coef_charge < 1:
		vitesse_brute = 1/ ((1/Vmax)*(1+coef_route*Coef_charge.exposant(B))
	else vitesse_brute = 1/ ((1/Vmax)*(1+coef_route*Coef_charge.exposant(Bbis))
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

def calc_vit_motosup50(Vitesse_vl, correcteurs[0] as correc_vitesse_moto):
	if vitesse_vl + correc_vitesse_moto >= 140 :
		Vitesse_moto_sup50 = 140
	elif vitesse_vl + correc_vitesse_moto <= 10 :
		Vitesse_moto_sup50 = 10
	else:
		Vitesse_moto_inf50 = vitesse_vl + correc_vitesse_moto
	return(Vitesse_moto_sup50)

def calc_vit_PL(Vitesse_vl, correcteurs[1] as correc_vitesse_PL):
	if vitesse_vl + correc_vitesse_PL >= 110 :
		Vitesse_PL = 140
	elif vitesse_vl + correc_vitesse_PL <= 10 :
		Vitesse_PL = 10
	else:
		Vitesse_PL = vitesse_vl + correc_vitesse_PL
	return(Vitesse_PL)

def calc_vit_Bus(Vitesse_vl, correcteurs[1] as correc_vitesse_Bus):
	if vitesse_vl + correc_vitesse_Bus >= 50 :
		Vitesse_Bus = 140
	elif vitesse_vl + correc_vitesse_Bus <= 10 :
		Vitesse_Bus = 10
	else:
		Vitesse_Bus = vitesse_vl + correc_vitesse_Bus
	return(Vitesse_Bus)


def calc_vit_Autocar(Vitesse_vl, correcteurs[1] as correc_vitesse_Car):
	if vitesse_vl + correc_vitesse_Car >= 120 :
		Vitesse_Car = 140
	elif vitesse_vl + correc_vitesse_Car <= 10 :
		Vitesse_Car = 10
	else:
		Vitesse_Car = vitesse_vl + correc_vitesse_Car
	return(Vitesse_Car)




####################################################################################
### 	creation d'un tableau de vitesse pour chaque categorie de vehicule		###
###						montrant chaque heure du mois							###
###################################################################################

def tableau_coef_charge(
	for mois in range(1,12):
		for heure in range(1;23):
			ca


def tableau_vitesse_brute(
	for mois in range(1,12):
		for heure in range(1;23):
			ca





























