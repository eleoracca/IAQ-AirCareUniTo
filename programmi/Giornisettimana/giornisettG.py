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

# LUNEDÌ – dati in ASSENZA di occupazione
co2_abs_lun     = [443.33, 442.03, 441.70, 440.51, 441.13, 441.60, 445.14, 456.75, 468.57, 501.28, 522.71, 535.19, 535.29, 526.60, 514.62, 549.57, 563.54, 565.66, 571.29, 522.72, 490.28, 477.43, 470.17, 462.83]
co2_abs_err_lun = [1.68,   1.71,   1.64,   1.64,   1.60,   1.52,   1.59,   1.89,   2.11,   6.62,   8.51,   9.59,   8.35,   7.27,   6.22,   9.01,   10.10,  10.08,  10.25,  6.86,   4.97,   4.28,   3.66,   3.20]

temp_abs_lun     = [22.51, 22.48, 22.45, 22.40, 22.39, 22.37, 22.31, 22.26, 22.25, 22.27, 22.31, 22.40, 22.47, 22.55, 22.59, 22.69, 22.69, 22.58, 22.54, 22.52, 22.54, 22.53, 22.54, 22.51]
temp_abs_err_lun = [0.13,  0.14,  0.14,  0.14,  0.14,  0.14,  0.14,  0.14,  0.13,  0.13,  0.13,  0.13,  0.13,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12]

pm10_abs_lun     = [12.89, 12.94, 13.13, 13.55, 12.96, 12.39, 12.12, 12.29, 12.38, 12.58, 12.73, 12.80, 12.49, 11.99, 11.53, 11.12, 10.93, 11.02, 10.90, 10.62, 10.55, 10.64, 10.88, 11.08]
pm10_abs_err_lun = [0.48,  0.50,  0.52,  0.57,  0.54,  0.51,  0.46,  0.44,  0.43,  0.43,  0.41,  0.43,  0.43,  0.40,  0.37,  0.35,  0.36,  0.38,  0.34,  0.32,  0.29,  0.29,  0.28,  0.29]

pm25_abs_lun     = [11.78, 11.82, 12.02, 12.43, 11.85, 11.31, 11.03, 11.23, 11.29, 11.51, 11.67, 11.70, 11.42, 10.94, 10.48, 10.09, 9.90,  9.98,  9.89,  9.61,  9.55,  9.64,  9.88, 10.08]
pm25_abs_err_lun = [0.47,  0.48,  0.50,  0.56,  0.52,  0.49,  0.45,  0.43,  0.42,  0.42,  0.40,  0.42,  0.42,  0.39,  0.36,  0.34,  0.36,  0.37,  0.33,  0.32,  0.29,  0.29,  0.28,  0.29]

# LUNEDÌ – dati in PRESENZA di occupazione (usa np.nan per ore senza dati)
co2_pres_lun     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 763.77, 838.07, 788.23, 753.19, np.nan, 1150.52, 1286.74, 1226.10, 1066.43, 587.08, np.nan, np.nan, np.nan, np.nan, np.nan]
co2_pres_err_lun = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 7.78,   8.59,   11.01,   11.88,   np.nan, 13.58,   16.02,   15.75,   14.11,   20.08,   np.nan, np.nan, np.nan, np.nan, np.nan]

temp_pres_lun     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 21.90, 22.34, 22.99, 23.09, np.nan, 22.61, 23.01, 23.18, 23.21, 21.64, np.nan, np.nan, np.nan, np.nan, np.nan]
temp_pres_err_lun = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.07,  0.07,  0.08,   0.08,   np.nan, 0.06,   0.06,   0.06,   0.06,   0.08,   np.nan, np.nan, np.nan, np.nan, np.nan]

pm10_pres_lun     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 12.94, 13.21, 12.06, 11.24, np.nan, 11.22, 11.49, 10.90, 11.18, 7.79, np.nan, np.nan, np.nan, np.nan, np.nan]
pm10_pres_err_lun = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.29,  0.32,   0.45,   0.45,   np.nan, 0.22,   0.24,   0.22,   0.22,   0.64,   np.nan, np.nan, np.nan, np.nan, np.nan]

pm25_pres_lun     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 11.84, 12.12, 11.02, 10.21, np.nan, 10.19, 10.46, 9.88,  10.15,  6.79,  np.nan, np.nan, np.nan, np.nan, np.nan]
pm25_pres_err_lun = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.28,  0.31,   0.44,   0.44,   np.nan, 0.22,   0.23,   0.21,   0.22,   0.64,   np.nan, np.nan, np.nan, np.nan, np.nan]


# MARTEDÌ – dati in ASSENZA di occupazione
co2_abs_mar     = [448.3, 445.7, 441.2, 440.5, 441.8, 444.1, 447.9, 460.9, 472.4, 483.1, 511.7, 540.8, 562.9, 537.0, 563.0, 611.0, 607.8, 604.1, 550.7, 508.6, 480.5, 462.2, 452.4, 447.8]
co2_abs_err_mar = [1.4,   1.2,   1.1,   1.1,   1.2,   1.3,   1.4,   1.7,   1.8,   2.1,   4.2,   6.4,   8.2,   6.5,   9.5,   13.1,  13.2,  13.3,  9.5,   6.4,   3.7,   2.3,   1.6,   1.4]

temp_abs_mar     = [22.3,  22.3,  22.3,  22.3,  22.2,  22.2,  22.1,  22.0,  21.9,  21.9,  22.1,  22.2,  22.3,  22.4,  22.5,  22.6,  22.7,  22.7,  22.7,  22.6,  22.5,  22.5,  22.4,  22.4]
temp_abs_err_mar = [0.1,   0.1,   0.1,   0.1,   0.1,   0.1,   0.1,   0.1,   0.1,   0.1,   0.1,   0.1,   0.1,   0.1,   0.1,   0.1,   0.1,   0.1,   0.1,   0.1,   0.1,   0.1,   0.1,   0.1]

pm10_abs_mar     = [10.2,  10.3,  10.4,  10.8,  11.6,  12.1,  12.1,  12.7,  13.3,  14.7,  13.4,  12.9,  12.6,  12.5,  16.0,  23.2,  15.6,  12.5,  11.8,  11.6,  11.7,  11.7,  11.8,  11.9]
pm10_abs_err_mar = [0.3,   0.3,   0.3,   0.4,   0.4,   0.4,   0.4,   0.4,   0.4,   0.7,   0.4,   0.4,   0.4,   0.4,   1.7,   3.3,   1.3,   0.5,   0.4,   0.3,   0.3,   0.4,   0.4,   0.4]

pm25_abs_mar     = [9.2,   9.3,   9.4,   9.8,   10.6,  11.0,  11.0,  11.7,  12.2,  13.6,  12.3,  11.8,  11.5,  11.4,  14.8,  22.0,  14.4,  11.4,  10.8,  10.6,  10.6,  10.7,  10.7,  10.8]
pm25_abs_err_mar = [0.3,   0.3,   0.3,   0.3,   0.4,   0.4,   0.4,   0.4,   0.4,   0.7,   0.4,   0.3,   0.4,   0.3,   1.7,   3.3,   1.3,   0.5,   0.3,   0.3,   0.3,   0.4,   0.4,   0.4]

# MARTEDÌ – dati in PRESENZA di occupazione (usa np.nan per ore senza dati)
co2_pres_mar     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 727.28, 811.89, 836.05, 820.60, 778.85, 1122.81, 1221.99, 1185.10, 1095.03, 1006.94, np.nan, np.nan, np.nan, np.nan, np.nan]
co2_pres_err_mar = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 11.67,  11.73,   13.02,   13.13,   25.04,   15.10,   16.44,   15.45,   13.56,   47.50,   np.nan, np.nan, np.nan, np.nan, np.nan]

temp_pres_mar     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 22.23, 22.65, 22.75, 22.73, 24.26, 23.13, 23.65, 23.92, 23.89, 23.04, np.nan, np.nan, np.nan, np.nan, np.nan]
temp_pres_err_mar = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.08,  0.08,  0.08,   0.08,   0.75,   0.06,   0.06,   0.06,   0.06,   0.30,   np.nan, np.nan, np.nan, np.nan, np.nan]

pm10_pres_mar     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 13.78, 14.44, 13.93, 13.17, 10.54, 12.30, 21.62, 23.92, 26.53, 12.25, np.nan, np.nan, np.nan, np.nan, np.nan]
pm10_pres_err_mar = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.35,  0.36,   0.37,   0.41,   0.76,   0.29,   0.56,   1.00,   1.15,   1.60,   np.nan, np.nan, np.nan, np.nan, np.nan]

pm25_pres_mar     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 12.68, 13.32, 12.82, 12.06, 9.54,  11.24, 20.35, 22.62, 25.17, 11.08, np.nan, np.nan, np.nan, np.nan, np.nan]
pm25_pres_err_mar = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.34,  0.35,   0.36,   0.40,   0.76,   0.28,   0.54,   0.99,   1.13,   1.54,   np.nan, np.nan, np.nan, np.nan, np.nan]


# MERCOLEDÌ – dati in ASSENZA di occupazione
co2_abs_mer     = [449.41, 443.93, 440.35, 438.01, 436.30, 435.50, 439.23, 451.31, 463.18, 502.34, 547.49, 604.33, 617.41, 547.98, 543.38, 583.96, 597.25, 586.13, 551.45, 502.93, 479.27, 466.40, 458.90, 456.19]
co2_abs_err_mer = [2.28,   1.89,   1.69,   1.62,   1.57,   1.50,   1.55,   1.62,   2.03,   5.20,   6.15,   9.60,   11.21,  6.70,   7.18,   10.78,  11.10,  10.15,  7.58,   4.00,   2.49,   2.38,   2.30,   2.19]

temp_abs_mer     = [23.22, 23.16, 23.11, 23.05, 22.99, 23.02, 22.95, 22.94, 22.94, 22.97, 23.04, 23.13, 23.22, 23.16, 23.23, 23.33, 23.37, 23.36, 23.30, 23.20, 23.27, 23.23, 23.21, 23.19]
temp_abs_err_mer = [0.11,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.13,  0.13]

pm10_abs_mer     = [12.61, 13.81, 14.25, 14.19, 13.97, 13.37, 13.76, 14.09, 14.30, 14.62, 16.45, 16.03, 15.27, 14.01, 13.13, 12.21, 11.74, 11.43, 11.94, 12.29, 11.60, 11.52, 11.68, 11.89]
pm10_abs_err_mer = [0.53,  0.77,  0.90,  0.77,  0.72,  0.63,  0.63,  0.53,  0.52,  0.56,  0.86,  0.71,  0.58,  0.48,  0.44,  0.39,  0.37,  0.34,  0.37,  0.39,  0.33,  0.33,  0.34,  0.35]

pm25_abs_mer     = [11.54, 12.75, 13.20, 13.15, 12.93, 12.33, 12.71, 13.04, 13.25, 13.55, 15.32, 14.91, 14.15, 12.92, 12.08, 11.17, 10.70, 10.39, 10.88, 11.21, 10.56, 10.48, 10.64, 10.84]
pm25_abs_err_mer = [0.52,  0.76,  0.88,  0.76,  0.71,  0.62,  0.62,  0.52,  0.51,  0.55,  0.84,  0.69,  0.56,  0.47,  0.43,  0.38,  0.36,  0.33,  0.36,  0.38,  0.32,  0.32,  0.34,  0.34]

# MERCOLEDÌ – dati in PRESENZA di occupazione (usa np.nan per ore senza dati)
co2_pres_mer     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 789.65, 901.49, 908.60, 897.08, 715.66, 1014.62, 1086.92, 1077.75, 986.62, 764.55, np.nan, np.nan, np.nan, np.nan, np.nan]
co2_pres_err_mer = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 8.64,   9.10,   13.01,   13.47,   35.80,   14.14,   15.00,   16.23,   17.76,   40.97,   np.nan, np.nan, np.nan, np.nan, np.nan]

temp_pres_mer     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 21.89, 22.41, 22.67, 22.86, 21.79, 23.01, 23.33, 23.43, 23.41, 23.09, np.nan, np.nan, np.nan, np.nan, np.nan]
temp_pres_err_mer = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.08,  0.07,   0.09,   0.08,   0.13,   0.05,   0.05,   0.05,   0.09,   0.30,   np.nan, np.nan, np.nan, np.nan, np.nan]

pm10_pres_mer     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 15.84, 16.32, 14.74, 14.91, 15.51, 13.02, 12.43, 11.96, 11.58, 16.29, np.nan, np.nan, np.nan, np.nan, np.nan]
pm10_pres_err_mer = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.30,  0.30,   0.32,   0.32,   0.91,   0.28,   0.26,   0.26,   0.24,   1.00,   np.nan, np.nan, np.nan, np.nan, np.nan]

pm25_pres_mer     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 14.71, 15.18, 13.66, 13.84, 14.46, 11.98, 11.39, 10.93, 10.56, 15.19, np.nan, np.nan, np.nan, np.nan, np.nan]
pm25_pres_err_mer = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.29,  0.30,   0.31,   0.31,   0.90,   0.28,   0.26,   0.26,   0.24,   1.00,   np.nan, np.nan, np.nan, np.nan, np.nan]


# GIOVEDÌ – dati in ASSENZA di occupazione
co2_abs_gio     = [453.1,  449.1,  446.8,  444.2,  442.6,  442.9,  447.5,  460.4,  473.6,  490.9,  514.3,  568.0,  622.9,  593.1,  614.7,  718.7,  750.9,  724.8,  661.5,  586.8,  532.6,  500.9,  481.1,  466.3]
co2_abs_err_gio = [1.7,    1.6,    1.5,    1.4,    1.4,    1.4,    1.5,    1.8,    2.1,    3.1,    4.0,    7.5,    11.6,   10.7,   12.7,   16.7,   18.1,   16.2,   13.6,   9.8,    6.8,    5.1,    3.9,    2.9]

temp_abs_gio     = [23.0,   22.9,   22.9,   22.8,   22.7,   22.7,   22.7,   22.6,   22.5,   22.6,   22.7,   22.8,   22.9,   23.0,   23.1,   23.3,   23.4,   23.4,   23.3,   23.3,   23.2,   23.2,   23.2,   23.2]
temp_abs_err_gio = [0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1]

pm10_abs_gio     = [10.9,   11.3,   11.7,   11.3,   11.1,   11.1,   11.4,   12.5,   13.3,   12.9,   12.3,   12.1,   11.8,   11.4,   11.3,   10.2,   10.0,   10.0,   10.6,   10.5,   10.2,   13.8,   10.3,   10.5]
pm10_abs_err_gio = [0.4,    0.4,    0.4,    0.4,    0.4,    0.4,    0.4,    0.4,    0.4,    0.4,    0.4,    0.5,    0.4,    0.4,    0.4,    0.3,    0.3,    0.3,    0.4,    0.4,    0.4,    0.4,    0.5,    0.6]

pm25_abs_gio     = [9.9,    10.2,   10.6,   10.3,   10.0,   10.0,   10.3,   11.4,   12.2,   11.8,   11.2,   11.0,   10.8,   10.4,   10.2,    9.2,    9.0,    9.0,    9.5,    9.5,    9.2,    9.5,    9.3,    9.5]
pm25_abs_err_gio = [0.4,    0.4,    0.4,    0.4,    0.4,    0.4,    0.4,    0.7,    0.6,    0.6,    0.7,    0.7,    0.5,    0.5,    0.5,    0.3,    0.3,    0.3,    0.4,    0.4,    0.4,    0.4,    0.4,    0.5]

# GIOVEDÌ – dati in PRESENZA di occupazione (usa np.nan per ore senza dati)
co2_pres_gio     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 760.17, 776.05, 860.37, 1087.93, 1134.22, 1222.92, 1120.45, 1169.69, 1204.84, 1077.11, 625.89, np.nan, np.nan, np.nan, np.nan, np.nan]
co2_pres_err_gio = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.83,   15.52,  12.51,   14.27,    15.95,    21.82,    15.34,    15.82,    17.18,    15.70,    23.10,   np.nan, np.nan, np.nan, np.nan, np.nan]

temp_pres_gio     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 21.30, 22.23, 22.45, 22.86, 23.27, 23.83, 23.50, 23.77, 23.87, 23.95, 24.53, np.nan, np.nan, np.nan, np.nan, np.nan]
temp_pres_err_gio = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.00,  0.11,  0.07,  0.05,   0.06,   0.01,    0.05,    0.05,    0.06,    0.06,    0.23,   np.nan, np.nan, np.nan, np.nan, np.nan]

pm10_pres_gio     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,  9.67,  15.21, 15.77, 21.21, 20.25, 14.25, 21.64, 25.92, 23.98, 24.35, 17.95, np.nan, np.nan, np.nan, np.nan, np.nan]
pm10_pres_err_gio = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,  0.56,   0.52,   0.36,   0.29,    0.39,   0.68,   0.82,   0.88,   1.05,   0.83,   2.87,   np.nan, np.nan, np.nan, np.nan, np.nan]

pm25_pres_gio     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,  8.67,  14.09, 14.69, 19.95, 19.02, 13.25, 20.39, 24.58, 22.68, 23.04, 16.63, np.nan, np.nan, np.nan, np.nan, np.nan]
pm25_pres_err_gio = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,  0.56,   0.51,   0.35,   0.39,    0.38,   0.68,   0.81,   0.87,   1.03,   0.81,   2.76,   np.nan, np.nan, np.nan, np.nan, np.nan]


# VENERDÌ – dati in ASSENZA di occupazione
co2_abs_ven     = [459.5,  455.5,  450.3,  447.0,  444.3,  445.1,  447.5,  459.7,  470.3,  503.0,  548.7,  554.6,  546.2,  510.0,  502.6,  532.6,  547.6,  541.1,  541.4,  505.1,  484.1,  473.4,  463.5,  457.1]
co2_abs_err_ven = [2.1,    1.9,    1.7,    1.5,    1.3,    1.3,    1.3,    1.4,    1.6,    4.0,    7.5,    8.9,    9.6,    6.8,    5.8,    8.4,    9.1,    8.0,    9.6,    6.6,    5.2,    4.5,    4.1,    3.6]

temp_abs_ven     = [22.7,   22.7,   22.6,   22.6,   22.5,   22.5,   22.5,   22.4,   22.4,   22.4,   22.4,   22.5,   22.5,   22.5,   22.6,   22.7,   22.8,   22.8,   22.8,   22.8,   22.8,   22.7,   22.7,   22.7]
temp_abs_err_ven = [0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.2,    0.2,    0.2,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1]

pm10_abs_ven     = [12.5,   12.7,   12.8,   13.1,   13.2,   13.0,   18.2,   17.3,   14.1,   15.4,   17.0,   18.3,   18.0,   11.5,   11.2,   10.4,   10.1,   9.7,    15.1,   12.9,   12.3,   12.2,   13.2,   13.6]
pm10_abs_err_ven = [0.3,    0.4,    0.4,    0.4,    0.4,    0.4,    0.7,    0.4,    0.4,    0.5,    0.7,    0.8,    0.8,    0.3,    0.3,    0.2,    0.2,    0.2,    1.5,    0.4,    0.4,    0.4,    0.5,    0.5]

pm25_abs_ven     = [11.5,   11.7,   11.7,   12.0,   12.1,   12.0,   17.0,   16.1,   13.0,   14.3,   15.9,   17.2,   16.8,   10.4,   10.2,   9.4,    9.1,    8.7,    14.0,   11.9,   11.2,   11.2,   12.2,   12.6]
pm25_abs_err_ven = [0.3,    0.4,    0.4,    0.4,    0.4,    0.4,    0.7,    0.4,    0.4,    0.5,    0.7,    0.8,    0.8,    0.3,    0.3,    0.2,    0.2,    0.2,    1.5,    0.4,    0.4,    0.4,    0.4,    0.5]

# VENERDÌ – dati in PRESENZA di occupazione (usa np.nan per ore senza dati)
co2_pres_ven     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 743.33, 859.40, 1032.82, 1035.83, np.nan, 1133.40, 1034.88, 1143.45, 1106.94, 911.76, 786.50, np.nan, np.nan, np.nan, np.nan, np.nan]
co2_pres_err_ven = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 8.39,   10.09,   14.48,    15.91,   np.nan,   24.29,    15.60,    16.02,    16.47,    12.88,    33.20,   np.nan, np.nan, np.nan, np.nan, np.nan]

temp_pres_ven     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 22.26, 22.60, 23.04, 23.33, np.nan, 23.81, 23.54, 23.95, 24.10, 24.10, 24.12, np.nan, np.nan, np.nan, np.nan, np.nan]
temp_pres_err_ven = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.05,   0.04,    0.05,    0.05,   np.nan,   0.09,     0.06,     0.06,     0.06,     0.06,     0.32,   np.nan, np.nan, np.nan, np.nan, np.nan]

pm10_pres_ven     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 13.89, 14.28, 15.18, 13.87, np.nan, 11.00, 12.29, 11.64, 11.95, 12.02, 9.46,  np.nan, np.nan, np.nan, np.nan, np.nan]
pm10_pres_err_ven = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.34,   0.35,    0.38,    0.36,   np.nan,   0.64,     0.35,     0.30,     0.34,     0.38,     0.78,   np.nan, np.nan, np.nan, np.nan, np.nan]

pm25_pres_ven     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 12.78, 13.16, 14.05, 12.77, np.nan, 10.00, 11.22, 10.58, 10.90, 10.95, 8.46,  np.nan, np.nan, np.nan, np.nan, np.nan]
pm25_pres_err_ven = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.34,   0.34,    0.37,    0.35,   np.nan,   0.54,     0.34,     0.30,     0.33,     0.38,     0.78,   np.nan, np.nan, np.nan, np.nan, np.nan]


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
    plt.title(f'Aula G – {variabile} – {giorno}')
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
