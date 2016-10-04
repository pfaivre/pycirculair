#calcul du nombre de veh legers par h du mois 


variable a integrer:
mois
jour
TMJA*bnr_j_an_jo
val_profil_mensu_jo[mois] et DF
val_profil_horraire_jo(heure) et DF
Pct_VL, Vul, Bus, PL Autocar
Capacite
Dif_vitesse_Pl_Fluide
Dif_vitesse_Pl_Dense
Dif_vitesse_Pl_proche_satu
Dif_vitesse_Pl_bouchon


'''
Nombre de vehicule
'''
#calcul du nombre de veh legers par h du mois 
				################################################
#jours ouvrés d'abord

Nombre_Vref_h_jo= TMJA*bnr_j_an_jo * val_profil_mensu_jo[mois] * val_profil_horraire_jo(heure)

Nombre_VL_h_jo = Nombre_Vref_h_jo * Pct_VL
Nombre_VUL_h_jo= Nombre_VL_h_jo * Pct_Vul
Nombre_VP_h_jo = Nombre_VL_h_jo - Nombre_VUL_h_jo
Nombre_BUS_h_jo = Nombre_Vref_h_jo * Pct_Bus
Nombre_AUTOCAR_h_jo = Nombre_Vref_h_jo * Pct_Autocar

Nombre_PL_h_jo = TMJA * bnr_j_an * val_profil_mensu_jo_PL[mois] * val_profil_horraire_jo_PL(heure) * prc_PL  ##profil special pour PL

				###################################################
#dimanches et jours feriés ensuite

Nombre_Vref_h_df= TMJA*bnr_j_an_df * val_profil_mensu_df[mois] * val_profil_horraire_df(heure)

Nombre_VL_h_df = Nombre_Vref_h_df * Pct_VL
Nombre_VUL_h_df= Nombre_VL_h_df * Pct_Vul
Nombre_VP_h_df = Nombre_VL_h_df - Nombre_VUL_h_jo
Nombre_BUS_h_df = Nombre_Vref_h_df * Pct_Bus
Nombre_AUTOCAR_h_df = Nombre_Vref_h_df * Pct_Autocar

Nombre_PL_h_jo = TMJA * bnr_j_an * val_profil_mensu_jo_PL[mois] * val_profil_horraire_jo_PL(heure) * prc_PL  ##profil special pour PL


#Ne pas oublier d'integrer le fait qu'il y ai un profil special pour juillet et aout dans le horraire

				###################################################
'''
coef de charge, a calculer pour chaque heure
'''

UnsurCapacite = 1 / capacite

Coef_charge = ((Nombre_VUL_h_jo + Nombre_VP_h_jo + (Nombre_PL_h_jo + Nombre_BUS_h_jo + Nombre_AUTOCAR_h_jo)*2 ) * UnsurCapacite)  ##coef de charge a partir duquel on calculera la vitesse de chaque categorie

Taux_congestion = Coef_charge * 100  ##pour fact correction vitesse ci apres

'''
vitesse de trafic
'''

les fact de corr dependent de la caegorie de la voie

correc_vitesse_PL = si taux_congestion <= 40, alors Dif_vitesse_Pl_Fluide
					si 40 < taux_congestion <= 80, alors Dif_vitesse_Pl_Dense
					si 80 < taux_congestion <= 100, alors Dif_vitesse_Pl_proche_satu
					si 100 < taux_congestion , alors Dif_vitesse_Pl_bouchon
Correc_vitesse_Bus = si taux_congestion <= 40, alors Dif_vitesse_Bus_Fluide
					si 40 < taux_congestion <= 80, alors Dif_vitesse_Bus_Dense
					si 80 < taux_congestion <= 100, alors Dif_vitesse_Bus_proche_satu
					si 100 < taux_congestion , alors Dif_vitesse_Bus_bouchons
Correc_vitesse_Autocar = si taux_congestion <= 40, alors Dif_vitesse_Autocar_Fluide
					si 40 < taux_congestion <= 80, alors Dif_vitesse_Autocar_Dense
					si 80 < taux_congestion <= 100, alors Dif_vitesse_Autocar_proche_satu
					si 100 < taux_congestion , alors Dif_vitesse_Autocar_bouchons
Correc_vitesse_moto = si taux_congestion <= 40, alors Dif_vitesse_moto_Fluide
					si 40 < taux_congestion <= 80, alors Dif_vitesse_moto_Dense
					si 80 < taux_congestion <= 100, alors Dif_vitesse_moto_proche_satu
					si 100 < taux_congestion , alors Dif_vitesse_moto_bouchons

Coeficient de route?
B
Bbis
Vmax

Vitesse_brute = si Coef_charge < 1, alors = à 1/ ((1/Vmax)*(1+coef_route*Coef_charge.exposant(B))
				sinon = à 1/ ((1/Vmax)*(1+coef_route*Coef_charge.exposant(Bbis))
Vitesse_moto_inf50 = 
Vitesse_moto_sup50 = 
Vitesse_Pl 
Vitesse_Bus =
Vitesse_Autocar
Vitesse_Vl = 
