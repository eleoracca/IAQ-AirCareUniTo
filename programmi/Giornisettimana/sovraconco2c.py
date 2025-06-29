import matplotlib.pyplot as plt
import numpy as np

x=[0,1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23]

co2_pres_lun     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 885.0, 1104.0, 1146.0, 1204.0,  1082.0, 1115.0, 1102.0, 1058.0, 1075.0, np.nan, np.nan, np.nan, np.nan, np.nan]
co2_pres_err_lun = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 13.0, 16.0, 15.0, 17.0,  15.0, 13.0, 13.0, 14.0, 29.0, np.nan, np.nan, np.nan, np.nan, np.nan]

co2_pres_mar     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 883.04, 1109.73, 1237.13, 1337.55, 1083.24, 1137.93, 1213.88, 1126.04, 876.23, np.nan, np.nan, np.nan, np.nan, np.nan]
co2_pres_err_mar = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 11.96, 14.53, 15.62, 18.65,  14.55, 15.41, 18.04, 17.20, 22.24, np.nan, np.nan, np.nan, np.nan, np.nan]

co2_pres_mer     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 999.95, 1235.97, 1262.28, 1384.48,  1090.72, 1151.93, 1048.76, 976.27, 820.18, np.nan, np.nan, np.nan, np.nan, np.nan]
co2_pres_err_mer = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 13.48, 17.17, 16.93, 19.75,  20.30, 20.75, 15.24, 15.10, 24.21, np.nan, np.nan, np.nan, np.nan, np.nan]

co2_pres_gio     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 951.29, 1085.04, 1026.82, 1128.63,  964.39, 1017.35, 1023.16, 956.75, 1029.90, np.nan, np.nan, np.nan, np.nan, np.nan]
co2_pres_err_gio = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 14.36, 20.32, 16.42, 17.69,  11.24, 10.81, 15.22, 12.89, 19.16, np.nan, np.nan, np.nan, np.nan, np.nan]

co2_pres_ven     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 821.71, 1011.03, 973.55, 1049.21,  887.73, 946.06, 952.15, 874.03, 838.58, np.nan, np.nan, np.nan, np.nan, np.nan]
co2_pres_err_ven = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 14.22, 19.79, 19.24, 20.86,  9.96, 10.68, 16.13, 22.30, 30.26, np.nan, np.nan, np.nan, np.nan, np.nan]




plt.figure(figsize=(8, 5))
plt.errorbar(x, co2_pres_lun, yerr=co2_pres_err_lun,
             label='CO₂ lunedì', color='red', marker='o', capsize=4)
plt.errorbar(x, co2_pres_mar, yerr=co2_pres_err_mar,
             label='CO₂ martedì', color='blue', marker='x', linestyle='--', capsize=4)
plt.errorbar(x, co2_pres_mer, yerr=co2_pres_err_mer,
             label='CO₂ mercoledì', color='green', marker='x', linestyle='--', capsize=4)
plt.errorbar(x, co2_pres_gio, yerr=co2_pres_err_gio,
             label='CO₂ giovedì', color='orange', marker='x', linestyle='--', capsize=4)
plt.errorbar(x,co2_pres_ven , yerr=co2_pres_err_ven,
             label='CO₂ venerdì', color='magenta', marker='x', linestyle='--', capsize=4)
plt.title('Aula C - CO₂ media con occupazione durante la settimana')
plt.xlabel('Ora')
plt.ylabel('CO₂ [ppm]')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("Grafici/sovrappconco2C.png")
plt.show()