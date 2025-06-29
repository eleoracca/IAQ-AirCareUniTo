import matplotlib.pyplot as plt
import numpy as np


# Asse x (ore 0–23)
x = list(range(24))

# ————————————————————————————————————————————————
# 1) DEFINIZIONE DATI: per ciascun giorno (Lun–Ven), per le 4 variabili (CO₂, Temperatura, PM10, PM2.5),
#    inserisci due coppie di array: “assenza” (A) e “presenza” (B),
#    ciascuna con valori e errori. Se in “presenza” non esistono dati per alcune ore,
#    usa “None” per quei posizioni (Matplotlib le salterà automaticamente).
# ————————————————————————————————————————————————



# LUNEDÌ – dati in ASSENZA di lezioni (24 elementi)
co2_abs_lun     = [433.21, 433.38, 432.33, 432.32, 431.57, 433.71, 433.76, 437.02, 442.35, 446.17, 447.38, 446.26, 443.98, 441.66, 439.81, 452.18, 453.94, 446.73, 442.98, 442.27, 441.70, 440.10, 438.05, 436.49]
co2_abs_err_lun = [2.16, 2.24, 2.28, 2.41, 2.20, 1.77, 1.80, 2.01, 2.22, 2.37, 2.43, 2.49, 2.54, 2.45, 2.41, 5.16, 5.96, 4.32, 3.06, 2.79, 2.64, 2.47, 2.47, 2.27]

temp_abs_lun     = [22.13, 22.11, 22.03, 21.82, 22.02, 22.02, 21.95, 21.98, 22.03, 22.17, 22.19, 22.30, 22.35, 22.44, 22.48, 22.50, 22.48, 22.61, 22.59, 22.61, 22.64, 22.58, 22.52, 22.47]
temp_abs_err_lun = [0.23, 0.23, 0.23, 0.24, 0.23, 0.23, 0.23, 0.23, 0.23, 0.21, 0.20, 0.19, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.17, 0.17, 0.17, 0.19, 0.20, 0.20]

pm10_abs_lun     = [12.16, 12.21, 12.24, 12.79, 12.04, 11.49, 10.82, 10.66, 10.82, 10.48, 10.29, 9.80, 9.89, 9.91, 9.77, 9.97, 10.06, 9.94, 9.71, 9.31, 9.02, 9.11, 9.19, 9.33]
pm10_abs_err_lun = [0.57, 0.58, 0.62, 0.71, 0.64, 0.59, 0.50, 0.45, 0.45, 0.40, 0.38, 0.33, 0.36, 0.34, 0.34, 0.34, 0.34, 0.34, 0.31, 0.29, 0.27, 0.28, 0.28, 0.26]

pm25_abs_lun     = [11.09, 11.13, 11.11, 11.65, 10.90, 10.39, 9.81, 9.66, 9.82, 9.48, 9.29, 8.80, 8.89, 8.91, 8.77, 8.97, 9.06, 8.94, 8.71, 8.31, 8.02, 8.11, 8.19, 8.33]
pm25_abs_err_lun = [0.55, 0.57, 0.60, 0.69, 0.62, 0.57, 0.50, 0.45, 0.45, 0.40, 0.38, 0.33, 0.36, 0.34, 0.34, 0.34, 0.34, 0.34, 0.31, 0.29, 0.27, 0.28, 0.28, 0.26]

# LUNEDÌ – dati in PRESENZA di lezioni (24 elementi, usa nan dove non ci sono dati)
co2_pres_lun     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 885.0, 1104.0, 1146.0, 1204.0, np.nan, 1082.0, 1115.0, 1102.0, 1058.0, 1075.0, np.nan, np.nan, np.nan, np.nan, np.nan]
co2_pres_err_lun = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 13.0, 16.0, 15.0, 17.0, np.nan, 15.0, 13.0, 13.0, 14.0, 29.0, np.nan, np.nan, np.nan, np.nan, np.nan]

temp_pres_lun     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 21.7, 22.3, 22.5, 22.7, np.nan, 22.5, 22.7, 22.8, 22.7, 22.2, np.nan, np.nan, np.nan, np.nan, np.nan]
temp_pres_err_lun = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.1, 0.1, 0.0, 0.0, np.nan, 0.1, 0.1, 0.0, 0.1, 0.1, np.nan, np.nan, np.nan, np.nan, np.nan]

pm10_pres_lun     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 13.0, 15.0, 15.0, 15.0, np.nan, 15.0, 14.0, 14.0, 14.0, 12.0, np.nan, np.nan, np.nan, np.nan, np.nan]
pm10_pres_err_lun = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.0, 0.0, 0.0, 0.0, np.nan, 0.0, 0.0, 0.0, 0.0, 1.0, np.nan, np.nan, np.nan, np.nan, np.nan]

pm25_pres_lun     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 12.0, 14.0, 14.0, 14.0, np.nan, 14.0, 13.0, 13.0, 13.0, 11.0, np.nan, np.nan, np.nan, np.nan, np.nan]
pm25_pres_err_lun = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.0, 0.0, 0.0, 0.0, np.nan, 0.0, 0.0, 0.0, 0.0, 1.0, np.nan, np.nan, np.nan, np.nan, np.nan]


# MARTEDÌ – dati in ASSENZA di lezioni (24 elementi)
co2_abs_mar     = [443.15, 440.64, 436.94, 434.70, 435.31, 436.20, 438.20, 443.98, 447.41, 453.66, 462.32, 472.11, 480.54, 485.41, 486.37, 499.64, 504.72, 508.95, 493.66, 469.63, 460.07, 451.83, 448.19, 444.05]
co2_abs_err_mar = [2.51, 2.21, 1.85, 1.71, 1.71, 1.70, 1.63, 1.62, 1.73, 1.99, 2.98, 4.63, 6.28, 6.65, 7.28, 10.12, 11.55, 12.47, 9.90, 5.89, 4.57, 3.75, 3.29, 2.84]

temp_abs_mar     = [22.65, 22.54, 22.56, 22.46, 22.43, 22.50, 22.38, 22.42, 22.43, 22.57, 22.65, 22.75, 22.79, 22.85, 22.89, 22.94, 22.95, 22.91, 23.00, 22.95, 22.99, 22.88, 22.66, 22.80]
temp_abs_err_mar = [0.18, 0.18, 0.18, 0.19, 0.18, 0.19, 0.19, 0.19, 0.18, 0.16, 0.16, 0.16, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.16, 0.17, 0.17]

pm10_abs_mar     = [8.98, 8.90, 9.17, 9.27, 9.50, 9.95, 10.54, 11.18, 12.01, 14.26, 12.90, 11.17, 10.59, 9.75, 11.27, 26.18, 22.87, 17.23, 13.64, 11.42, 10.21, 9.60, 9.24, 9.32]
pm10_abs_err_mar = [0.23, 0.24, 0.22, 0.25, 0.27, 0.33, 0.40, 0.41, 0.58, 0.97, 0.72, 0.42, 0.33, 0.27, 0.97, 4.82, 3.88, 2.32, 1.29, 0.71, 0.46, 0.35, 0.31, 0.29]

pm25_abs_mar     = [7.98, 7.90, 8.17, 8.27, 8.50, 8.95, 9.50, 10.14, 10.95, 13.15, 11.81, 10.13, 9.58, 8.75, 10.24, 24.96, 21.68, 16.11, 12.58, 10.36, 9.15, 8.58, 8.24, 8.32]
pm25_abs_err_mar = [0.23, 0.24, 0.22, 0.25, 0.27, 0.32, 0.40, 0.41, 0.57, 0.95, 0.70, 0.41, 0.32, 0.27, 0.96, 4.76, 3.83, 2.29, 1.28, 0.70, 0.45, 0.35, 0.31, 0.29]

# MARTEDÌ – dati in PRESENZA di lezioni (24 elementi, usa nan dove non ci sono dati)
co2_pres_mar     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 883.04, 1109.73, 1237.13, 1337.55, np.nan, 1083.24, 1137.93, 1213.88, 1126.04, 876.23, np.nan, np.nan, np.nan, np.nan, np.nan]
co2_pres_err_mar = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 11.96, 14.53, 15.62, 18.65, np.nan, 14.55, 15.41, 18.04, 17.20, 22.24, np.nan, np.nan, np.nan, np.nan, np.nan]

temp_pres_mar     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 21.75, 22.41, 22.79, 23.14, np.nan, 22.88, 23.01, 23.07, 22.90, 23.03, np.nan, np.nan, np.nan, np.nan, np.nan]
temp_pres_err_mar = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.05, 0.05, 0.05, 0.04, np.nan, 0.05, 0.05, 0.06, 0.06, 0.12, np.nan, np.nan, np.nan, np.nan, np.nan]

pm10_pres_mar     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 14.02, 16.33, 17.01, 15.58, np.nan, 14.05, 13.14, 13.92, 13.91, 12.39, np.nan, np.nan, np.nan, np.nan, np.nan]
pm10_pres_err_mar = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.24, 0.25, 0.28, 0.28, np.nan, 0.28, 0.26, 0.27, 0.33, 0.61, np.nan, np.nan, np.nan, np.nan, np.nan]

pm25_pres_mar     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 12.95, 15.20, 15.85, 14.47, np.nan, 12.98, 12.08, 12.85, 12.83, 11.34, np.nan, np.nan, np.nan, np.nan, np.nan]
pm25_pres_err_mar = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.23, 0.24, 0.27, 0.27, np.nan, 0.28, 0.26, 0.26, 0.32, 0.60, np.nan, np.nan, np.nan, np.nan, np.nan]

# MERCOLEDÌ – dati in ASSENZA di lezioni (24 elementi)
co2_abs_mer     = [481.79, 473.64, 468.50, 461.91, 455.89, 451.06, 448.80, 448.04, 451.77, 455.62, 463.82, 477.56, 482.68, 481.64, 476.20, 476.86, 485.35, 476.58, 460.49, 451.87, 447.60, 446.35, 445.11, 445.47]
co2_abs_err_mer = [8.58, 6.88, 5.68, 4.62, 3.76, 3.14, 2.63, 2.32, 2.27, 2.45, 2.99, 4.40, 5.37, 5.63, 6.85, 7.82, 8.80, 8.00, 4.65, 3.11, 2.51, 2.40, 2.55, 2.65]

temp_abs_mer     = [22.37, 22.35, 22.16, 22.15, 22.23, 22.17, 22.15, 22.17, 22.12, 22.07, 22.18, 22.20, 22.23, 22.34, 22.39, 22.35, 22.33, 22.47, 22.48, 22.47, 22.49, 22.42, 22.34, 22.20]
temp_abs_err_mer = [0.23, 0.23, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.22, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.20, 0.20, 0.20, 0.20, 0.21, 0.23, 0.23]

pm10_abs_mer     = [11.21, 12.96, 13.84, 13.99, 13.56, 13.30, 13.18, 12.33, 12.25, 12.17, 13.56, 16.12, 15.05, 14.12, 13.22, 13.61, 12.59, 11.87, 10.96, 10.68, 10.43, 10.30, 10.67, 10.82]
pm10_abs_err_mer = [0.53, 0.89, 1.12, 1.10, 1.01, 0.92, 0.87, 0.76, 0.67, 0.65, 0.92, 1.29, 1.01, 0.75, 0.61, 0.65, 0.59, 0.43, 0.36, 0.31, 0.28, 0.29, 0.32, 0.34]

pm25_abs_mer     = [10.17, 11.88, 12.76, 12.91, 12.49, 12.22, 12.10, 11.25, 11.17, 11.09, 12.43, 14.96, 13.89, 12.97, 12.08, 12.47, 11.53, 10.86, 9.95, 9.68, 9.43, 9.30, 9.67, 9.82]
pm25_abs_err_mer = [0.51, 0.87, 1.10, 1.08, 0.99, 0.90, 0.85, 0.74, 0.65, 0.63, 0.89, 1.27, 0.98, 0.72, 0.58, 0.63, 0.57, 0.43, 0.36, 0.31, 0.28, 0.29, 0.32, 0.34]

# MERCOLEDÌ – dati in PRESENZA di lezioni (24 elementi, usa nan dove non ci sono dati)
co2_pres_mer     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 999.95, 1235.97, 1262.28, 1384.48, np.nan, 1090.72, 1151.93, 1048.76, 976.27, 820.18, np.nan, np.nan, np.nan, np.nan, np.nan]
co2_pres_err_mer = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 13.48, 17.17, 16.93, 19.75, np.nan, 20.30, 20.75, 15.24, 15.10, 24.21, np.nan, np.nan, np.nan, np.nan, np.nan]

temp_pres_mer     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 21.89, 22.74, 22.89, 23.02, np.nan, 22.98, 23.25, 23.20, 23.09, 23.49, np.nan, np.nan, np.nan, np.nan, np.nan]
temp_pres_err_mer = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.05, 0.05, 0.05, 0.05, np.nan, 0.05, 0.05, 0.05, 0.05, 0.11, np.nan, np.nan, np.nan, np.nan, np.nan]

pm10_pres_mer     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 16.25, 17.16, 16.91, 17.38, np.nan, 14.21, 13.74, 13.24, 12.68, 9.99, np.nan, np.nan, np.nan, np.nan, np.nan]
pm10_pres_err_mer = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.31, 0.30, 0.28, 0.27, np.nan, 0.28, 0.24, 0.23, 0.21, 0.26, np.nan, np.nan, np.nan, np.nan, np.nan]

pm25_pres_mer     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 15.10, 15.98, 15.73, 16.24, np.nan, 13.15, 12.69, 12.19, 11.66, 8.99, np.nan, np.nan, np.nan, np.nan, np.nan]
pm25_pres_err_mer = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.30, 0.29, 0.27, 0.26, np.nan, 0.27, 0.23, 0.22, 0.20, 0.26, np.nan, np.nan, np.nan, np.nan, np.nan]

# GIOVEDÌ – dati in ASSENZA di lezioni (24 elementi)
co2_abs_gio     = [462.01, 455.80, 450.37, 450.65, 448.06, 446.71, 447.45, 448.19, 448.91, 451.32, 454.47, 459.65, 465.16, 473.64, 483.89, 486.70, 482.68, 489.77, 489.21, 480.44, 467.11, 459.13, 448.79, 443.08]
co2_abs_err_gio = [5.07,   3.84,   2.92,   2.84,   2.71,   2.91,   2.99,   2.28,   1.97,   2.08,   1.98,   2.48,   4.04,   5.59,   8.60,   10.16,  10.27,  9.98,   10.20,  9.67,   6.65,   4.70,   3.55,   2.70]

temp_abs_gio     = [22.64, 22.63, 22.58, 22.44, 22.44, 22.45, 22.41, 22.40, 22.38, 22.39, 22.43, 22.44, 22.46, 22.54, 22.57, 22.60, 22.62, 22.63, 22.66, 22.61, 22.66, 22.63, 22.77, 22.77]
temp_abs_err_gio = [0.23,  0.23,  0.23,  0.24,  0.24,  0.24,  0.25,  0.25,  0.24,  0.22,  0.21,  0.21,  0.20,  0.20,  0.20,  0.20,  0.20,  0.19,  0.19,  0.20,  0.20,  0.21,  0.22,  0.23]

pm10_abs_gio     = [11.42, 11.86, 12.18, 12.40, 11.91, 11.88, 11.98, 12.31, 11.53, 11.20, 10.92, 11.43, 11.40, 11.37, 12.03, 12.07, 12.11, 11.48, 11.20, 10.74, 10.40, 10.29, 10.29, 10.66]
pm10_abs_err_gio = [0.35,  0.42,  0.45,  0.48,  0.48,  0.44,  0.41,  0.38,  0.34,  0.32,  0.31,  0.34,  0.29,  0.29,  0.36,  0.39,  0.46,  0.35,  0.33,  0.29,  0.27,  0.27,  0.29,  0.30]

pm25_abs_gio     = [10.42, 10.80, 11.11, 11.32, 10.84, 10.81, 10.93, 11.30, 10.53, 10.20, 9.92,  10.43, 10.40, 10.37, 11.02, 11.06, 11.08, 10.48, 10.20, 9.74,  9.40,  9.29,  9.29,  9.66]
pm25_abs_err_gio = [0.35,  0.41,  0.43,  0.46,  0.46,  0.43,  0.40,  0.38,  0.34,  0.32,  0.31,  0.34,  0.29,  0.29,  0.36,  0.39,  0.45,  0.35,  0.33,  0.29,  0.27,  0.27,  0.29,  0.30]

# GIOVEDÌ – dati in PRESENZA di lezioni (24 elementi, usa nan dove non ci sono dati)
co2_pres_gio     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 951.29, 1085.04, 1026.82, 1128.63, np.nan, 964.39, 1017.35, 1023.16, 956.75, 1029.90, np.nan, np.nan, np.nan, np.nan, np.nan]
co2_pres_err_gio = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 14.36, 20.32, 16.42, 17.69, np.nan, 11.24, 10.81, 15.22, 12.89, 19.16, np.nan, np.nan, np.nan, np.nan, np.nan]

temp_pres_gio     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 22.49, 23.08, 23.02, 23.30, np.nan, 23.01, 23.16, 23.28, 23.00, 23.09, np.nan, np.nan, np.nan, np.nan, np.nan]
temp_pres_err_gio = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.05, 0.05, 0.05, 0.05, np.nan, 0.05, 0.04, 0.05, 0.04, 0.06, np.nan, np.nan, np.nan, np.nan, np.nan]

pm10_pres_gio     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 14.96, 15.29, 14.11, 15.06, np.nan, 13.47, 12.67, 14.30, 12.78, 11.07, np.nan, np.nan, np.nan, np.nan, np.nan]
pm10_pres_err_gio = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.27, 0.32, 0.22, 0.25, np.nan, 0.22, 0.21, 0.28, 0.26, 0.29, np.nan, np.nan, np.nan, np.nan, np.nan]

pm25_pres_gio     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 13.89, 14.21, 13.07, 13.98, np.nan, 12.42, 11.64, 13.22, 11.73, 10.03, np.nan, np.nan, np.nan, np.nan, np.nan]
pm25_pres_err_gio = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.27, 0.31, 0.22, 0.24, np.nan, 0.22, 0.20, 0.27, 0.25, 0.28, np.nan, np.nan, np.nan, np.nan, np.nan]

# VENERDÌ – dati in ASSENZA di lezioni (24 elementi)
co2_abs_ven     = [465.22, 457.89, 451.89, 448.76, 447.28, 447.64, 448.86, 453.40, 458.55, 464.17, 470.65, 474.85, 482.88, 505.71, 514.25, 530.92, 518.00, 514.98, 488.70, 473.39, 459.50, 448.71, 441.90, 437.69]
co2_abs_err_ven = [3.24, 2.43, 1.84, 1.51, 1.40, 1.60, 1.69, 1.52, 1.51, 1.62, 2.59, 3.95, 5.69, 8.18, 9.32, 12.28, 11.37, 11.22, 6.86, 4.42, 3.03, 2.36, 2.03, 1.81]

temp_abs_ven     = [22.16, 22.12, 22.08, 22.04, 21.99, 21.95, 21.88, 21.72, 21.77, 21.88, 22.02, 22.07, 22.14, 22.22, 22.27, 22.35, 22.39, 22.40, 22.40, 22.39, 22.40, 22.25, 22.15, 22.09]
temp_abs_err_ven = [0.14, 0.14, 0.14, 0.14, 0.14, 0.14, 0.14, 0.15, 0.14, 0.13, 0.13, 0.13, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.13, 0.13, 0.13, 0.13, 0.14, 0.14]

pm10_abs_ven     = [10.45, 10.64, 10.81, 10.90, 11.09, 11.21, 11.31, 12.55, 11.41, 11.14, 11.15, 11.07, 10.68, 10.32, 9.78, 9.54, 9.38, 9.23, 8.97, 8.74, 8.40, 8.42, 8.70, 8.95]
pm10_abs_err_ven = [0.28, 0.29, 0.31, 0.33, 0.35, 0.34, 0.32, 0.47, 0.29, 0.30, 0.30, 0.32, 0.29, 0.28, 0.25, 0.24, 0.21, 0.21, 0.20, 0.19, 0.18, 0.18, 0.19, 0.20]

pm25_abs_ven     = [9.45, 9.61, 9.78, 9.86, 10.04, 10.16, 10.27, 11.49, 10.40, 10.13, 10.15, 10.05, 9.67, 9.32, 8.78, 8.54, 8.38, 8.23, 7.97, 7.74, 7.40, 7.42, 7.70, 7.95]
pm25_abs_err_ven = [0.28, 0.28, 0.30, 0.32, 0.34, 0.33, 0.31, 0.46, 0.28, 0.29, 0.30, 0.32, 0.29, 0.28, 0.25, 0.24, 0.21, 0.21, 0.20, 0.19, 0.18, 0.18, 0.19, 0.20]

# VENERDÌ – dati in PRESENZA di lezioni (24 elementi, usa nan dove non ci sono dati)
co2_pres_ven     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 821.71, 1011.03, 973.55, 1049.21, np.nan, 887.73, 946.06, 952.15, 874.03, 838.58, np.nan, np.nan, np.nan, np.nan, np.nan]
co2_pres_err_ven = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 14.22, 19.79, 19.24, 20.86, np.nan, 9.96, 10.68, 16.13, 22.30, 30.26, np.nan, np.nan, np.nan, np.nan, np.nan]

temp_pres_ven     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 22.28, 22.83, 23.04, 23.19, np.nan, 23.05, 23.18, 23.26, 23.02, 22.87, np.nan, np.nan, np.nan, np.nan, np.nan]
temp_pres_err_ven = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.05, 0.05, 0.06, 0.06, np.nan, 0.04, 0.05, 0.07, 0.10, 0.14, np.nan, np.nan, np.nan, np.nan, np.nan]

pm10_pres_ven     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 13.59, 14.03, 14.02, 14.55, np.nan, 13.91, 13.41, 14.38, 16.05, 10.80, np.nan, np.nan, np.nan, np.nan, np.nan]
pm10_pres_err_ven = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.33, 0.31, 0.29, 0.32, np.nan, 0.31, 0.28, 0.46, 0.79, 0.71, np.nan, np.nan, np.nan, np.nan, np.nan]

pm25_pres_ven     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 12.52, 12.97, 12.95, 13.48, np.nan, 12.79, 12.31, 13.25, 14.89, 9.80, np.nan, np.nan, np.nan, np.nan, np.nan]
pm25_pres_err_ven = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.32, 0.31, 0.28, 0.32, np.nan, 0.30, 0.27, 0.44, 0.77, 0.71, np.nan, np.nan, np.nan, np.nan, np.nan]  
 

# ————————————————————————————————————————
# 2) FUNZIONE DI PLOTTAGGIO CON DOPPIO ASSE Y
# ————————————————————————————————————————

def plot_doppio_y(
    x,
    y_abs, err_abs,
    y_pres, err_pres,
    giorno, variabile,
    colore_abs='tab:blue', colore_pres='tab:red',
    file_out=None
):
    """
    Disegna un grafico con doppio asse Y:
      - serie “assenza” (assi sinistro)
      - serie “presenza” (assi destro)
    x: lista ore (0–23)
    y_abs, err_abs: valori ed errori in assenza di lezioni
    y_pres, err_pres: valori ed errori in presenza di lezioni
    giorno: stringa (‘Lunedì’, …)
    variabile: stringa (‘CO₂’, ‘Temperatura’, ‘PM10’, ‘PM2.5’)
    file_out: percorso file PNG di destinazione (None per non salvare)
    """
    fig, ax1 = plt.subplots(figsize=(8, 5))
    ax2 = ax1.twinx()

    # Plot “assenza” su ax1
    ax1.errorbar(
        x, y_abs, yerr=err_abs,
        label=f'{variabile} (assenza lezioni)',
        color=colore_abs, marker='o', linestyle='none', capsize=3
    )
    ax1.set_ylabel(f'{variabile} (assenza)', color=colore_abs)
    ax1.tick_params(axis='y', labelcolor=colore_abs)

    # Plot “presenza” su ax2
    ax2.errorbar(
        x, y_pres, yerr=err_pres,
        label=f'{variabile} (presenza lezioni)',
        color=colore_pres, marker='x', linestyle='none', capsize=3
    )
    ax2.set_ylabel(f'{variabile} (presenza)', color=colore_pres)
    ax2.tick_params(axis='y', labelcolor=colore_pres)

    # Etichette e titolo
    ax1.set_xlabel('Ora')
    plt.title(f'Aula C – {variabile} – {giorno}')
    ax1.grid(True)

    # Leggenda combinata
    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax1.legend(h1 + h2, l1 + l2, loc='upper right')

    plt.tight_layout()
    if file_out:
        plt.savefig(file_out)
    plt.show()


# ————————————————————————————————————————
# 3) CREAZIONE DEI 20 GRAFICI (4 variabili × 5 giorni)
# ————————————————————————————————————————

# Lista di giorni e variabili
giorni = ['Lunedì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì']
variabili = ['CO₂', 'Temperatura', 'PM10', 'PM2.5']

# Mappatura dei dati: dati[giorno][variabile] = (y_abs, err_abs, y_pres, err_pres)
dati = {
    'Lunedì': {
        'CO₂':        (co2_abs_lun,  co2_abs_err_lun,  co2_pres_lun,  co2_pres_err_lun),
        'Temperatura':(temp_abs_lun, temp_abs_err_lun, temp_pres_lun, temp_pres_err_lun),
        'PM10':       (pm10_abs_lun, pm10_abs_err_lun, pm10_pres_lun, pm10_pres_err_lun),
        'PM2.5':      (pm25_abs_lun, pm25_abs_err_lun, pm25_pres_lun, pm25_pres_err_lun)
    },
    'Martedì': {
        'CO₂':        (co2_abs_mar,  co2_abs_err_mar,  co2_pres_mar,  co2_pres_err_mar),
        'Temperatura':(temp_abs_mar, temp_abs_err_mar, temp_pres_mar, temp_pres_err_mar),
        'PM10':       (pm10_abs_mar, pm10_abs_err_mar, pm10_pres_mar, pm10_pres_err_mar),
        'PM2.5':      (pm25_abs_mar, pm25_abs_err_mar, pm25_pres_mar, pm25_pres_err_mar)
    },
    'Mercoledì': {
        'CO₂':        (co2_abs_mer,  co2_abs_err_mer,  co2_pres_mer,  co2_pres_err_mer),
        'Temperatura':(temp_abs_mer, temp_abs_err_mer, temp_pres_mer, temp_pres_err_mer),
        'PM10':       (pm10_abs_mer, pm10_abs_err_mer, pm10_pres_mer, pm10_pres_err_mer),
        'PM2.5':      (pm25_abs_mer, pm25_abs_err_mer, pm25_pres_mer, pm25_pres_err_mer)
    },
    'Giovedì': {
        'CO₂':        (co2_abs_gio,  co2_abs_err_gio,  co2_pres_gio,  co2_pres_err_gio),
        'Temperatura':(temp_abs_gio, temp_abs_err_gio, temp_pres_gio, temp_pres_err_gio),
        'PM10':       (pm10_abs_gio, pm10_abs_err_gio, pm10_pres_gio, pm10_pres_err_gio),
        'PM2.5':      (pm25_abs_gio, pm25_abs_err_gio, pm25_pres_gio, pm25_pres_err_gio)
    },
    'Venerdì': {
        'CO₂':        (co2_abs_ven,  co2_abs_err_ven,  co2_pres_ven,  co2_pres_err_ven),
        'Temperatura':(temp_abs_ven, temp_abs_err_ven, temp_pres_ven, temp_pres_err_ven),
        'PM10':       (pm10_abs_ven, pm10_abs_err_ven, pm10_pres_ven, pm10_pres_err_ven),
        'PM2.5':      (pm25_abs_ven, pm25_abs_err_ven, pm25_pres_ven, pm25_pres_err_ven)
    }
}

# Itera giorni e variabili per generare ciascun grafico
for giorno in giorni:
    for variabile in variabili:
        y_abs, err_abs, y_pres, err_pres = dati[giorno][variabile]
        # Genera nome file in minuscolo senza spazi, p.es. "co2_lunedi.png"
        variabile_clean = (variabile
                           .lower()
                           .replace('₂', '2')
                           .replace('₂', '2')
                           .replace('₂', '2')
                           .replace('₂', '2')
                           .replace('₂', '2')
                           .replace('₂', '2')
                           .replace('₂', '2')
                           .replace('₂', '2')
                           .replace('₂', '2')
                           .replace(' ', '')
                           .replace('°', ''))
        giorno_clean = giorno.lower().replace('è', 'e').replace('í', 'i')
        file_nome = f"Grafici/{variabile_clean}_{giorno_clean}.png"
        # Chiama la funzione di plotting
        plot_doppio_y(
            x,
            y_abs, err_abs,
            y_pres, err_pres,
            giorno, variabile,
            colore_abs='tab:blue',
            colore_pres='tab:red',
            file_out=file_nome
        )
