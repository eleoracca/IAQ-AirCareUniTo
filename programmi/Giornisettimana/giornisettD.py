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
co2_abs_lun     = [445.4, 444.7, 443.4, 439.4, 439.8, 438.9, 441.0, 450.3, 461.1, 477.5, 483.9, 488.8, 490.9, 482.6, 481.2, 499.3, 507.4, 518.6, 519.9, 505.6, 492.3, 488.0, 480.0, 475.0]
co2_abs_err_lun = [2.6,   2.8,   2.8,   2.9,   2.9,   2.9,   3.0,   2.9,   3.1,   3.8,   5.2,   7.1,   9.7,   9.4,   9.3,   14.6,  16.6,  18.3,  17.7,  13.8,  10.8,  9.1,   7.4,   6.3]

temp_abs_lun     = [21.0, 21.0, 20.9, 20.5, 20.8, 20.7, 20.7, 20.8, 20.9, 21.1, 21.2, 21.3, 21.2, 21.3, 21.3, 21.4, 21.5, 21.5, 21.5, 21.4, 21.2, 21.1, 20.9, 20.7]
temp_abs_err_lun = [0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2]

pm10_abs_lun     = [17.4, 17.6, 17.2, 17.6, 15.6, 14.8, 14.5, 13.2, 13.1, 14.2, 12.7, 12.6, 13.3, 12.4, 12.7, 12.7, 13.1, 13.6, 12.8, 12.6, 11.9, 12.6, 13.0, 13.7]
pm10_abs_err_lun = [1.1,  1.1,  1.2,  1.2,  1.0,  1.0,  0.8,  0.6,  0.5,  0.6,  0.5,  0.5,  0.5,  0.5,  0.5,  0.6,  0.6,  0.7,  0.6,  0.6,  0.5,  0.5,  0.6,  0.6]

pm25_abs_lun     = [16.2, 16.3, 16.0, 16.4, 14.5, 13.7, 13.4, 12.1, 12.1, 13.2, 11.6, 11.6, 12.2, 11.4, 11.7, 11.7, 12.0, 12.5, 11.7, 11.5, 10.9, 11.5, 12.0, 12.6]
pm25_abs_err_lun = [1.1,  1.1,  1.1,  1.2,  1.0,  0.9,  0.8,  0.6,  0.5,  0.6,  0.5,  0.5,  0.5,  0.5,  0.5,  0.6,  0.6,  0.7,  0.6,  0.6,  0.5,  0.5,  0.5,  0.5]

# LUNEDÌ – dati in PRESENZA di occupazione (usa np.nan per ore senza dati)
co2_pres_lun     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 662.17, 803.35, 1008.80, 1188.18, np.nan, 1035.75, 1138.63, 979.96, 801.52, 1452.50, np.nan, np.nan, np.nan, np.nan, np.nan]
co2_pres_err_lun = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 6.18,   8.18,   13.16,   20.28,   np.nan, 14.10,   19.17,   17.99,   10.46,   32.73,   np.nan, np.nan, np.nan, np.nan, np.nan]

temp_pres_lun     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 20.81, 21.37, 21.62, 21.90, np.nan, 21.95, 22.14, 21.95, 21.93, 22.03, np.nan, np.nan, np.nan, np.nan, np.nan]
temp_pres_err_lun = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.09,  0.08,  0.07,   0.07,   np.nan, 0.07,   0.07,   0.08,   0.08,   0.03,   np.nan, np.nan, np.nan, np.nan, np.nan]

pm10_pres_lun     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 17.70, 20.46, 21.51, 25.92, np.nan, 22.01, 25.97, 21.09, 17.44, 58.58, np.nan, np.nan, np.nan, np.nan, np.nan]
pm10_pres_err_lun = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.37,  0.51,   1.06,   0.78,   np.nan, 0.92,   1.07,   1.80,   0.75,   3.26,   np.nan, np.nan, np.nan, np.nan, np.nan]

pm25_pres_lun     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 16.54, 19.20, 20.25, 24.56, np.nan, 20.78, 24.61, 19.89, 16.31, 56.58, np.nan, np.nan, np.nan, np.nan, np.nan]
pm25_pres_err_lun = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.37,  0.50,   1.05,   0.77,   np.nan, 0.91,   1.05,   1.77,   0.74,   3.26,   np.nan, np.nan, np.nan, np.nan, np.nan]


# MARTEDÌ – dati in ASSENZA di occupazione
co2_abs_mar     = [467.6, 463.0, 458.4, 447.4, 456.5, 458.1, 462.2, 480.8, 483.7, 492.3, 501.6, 506.5, 521.7, 527.6, 538.5, 539.6, 540.3, 529.8, 523.0, 499.1, 486.7, 476.5, 468.2, 465.0]
co2_abs_err_mar = [7.0,   6.5,   6.0,   4.9,   5.4,   5.0,   4.5,   4.0,   3.9,   4.5,   6.2,   8.5,   13.6,  14.8,  16.3,  16.9,  16.5,  13.6,  11.6,  7.5,   5.6,   4.7,   3.9,   3.2]

temp_abs_mar     = [20.3,  20.2,  20.2,  19.9,  20.0,  19.9,  19.9,  20.1,  20.4,  20.3,  20.5,  20.5,  20.6,  20.7,  20.9,  21.1,  21.2,  21.2,  21.3,  21.1,  20.9,  20.8,  20.6,  20.4]
temp_abs_err_mar = [0.2,   0.2,   0.2,   0.2,   0.2,   0.2,   0.2,   0.2,   0.2,   0.2,   0.2,   0.2,   0.2,   0.2,   0.2,   0.2,   0.2,   0.2,   0.2,   0.2,   0.2,   0.2,   0.2,   0.2]

pm10_abs_mar     = [13.8,  13.5,  12.8,  13.4,  13.9,  14.4,  14.9,  24.0,  14.2,  13.9,  14.2,  14.3,  14.5,  13.5,  13.2,  12.8,  12.5,  12.5,  11.8,  12.8,  13.5,  13.2,  14.1,  15.1]
pm10_abs_err_mar = [0.6,   0.6,   0.5,   0.6,   0.7,   0.7,   0.8,   7.3,   0.6,   0.5,   0.6,   0.6,   0.6,   0.6,   0.6,   0.5,   0.5,   0.5,   0.4,   0.5,   0.6,   0.6,   0.7,   0.7]

pm25_abs_mar     = [12.7,  12.4,  11.8,  12.3,  12.8,  13.2,  13.7,  22.7,  13.2,  12.9,  13.2,  13.2,  13.4,  12.4,  12.1,  11.7,  11.5,  11.4,  10.8,  11.8,  12.5,  12.1,  13.0,  14.0]
pm25_abs_err_mar = [0.6,   0.6,   0.5,   0.6,   0.7,   0.7,   0.7,   7.2,   0.6,   0.5,   0.6,   0.6,   0.6,   0.6,   0.6,   0.5,   0.5,   0.5,   0.4,   0.5,   0.6,   0.6,   0.6,   0.7]

# MARTEDÌ – dati in PRESENZA di occupazione (usa np.nan per ore senza dati)
co2_pres_mar     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 716.89, 849.54, 908.34, 951.50, np.nan, 889.13, 982.64, 921.00, 827.14, 559.83, np.nan, np.nan, np.nan, np.nan, np.nan]
co2_pres_err_mar = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 6.75,   7.88,   10.53,   13.72,   np.nan, 8.01,   11.99,  10.20,   9.01,   4.12,   np.nan, np.nan, np.nan, np.nan, np.nan]

temp_pres_mar     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 21.14, 21.35, 21.58, 21.92, np.nan, 22.02, 22.15, 22.34, 22.41, 17.66, np.nan, np.nan, np.nan, np.nan, np.nan]
temp_pres_err_mar = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.07,  0.07,   0.07,   0.07,   np.nan, 0.06,   0.07,   0.06,   0.06,   0.01,   np.nan, np.nan, np.nan, np.nan, np.nan]

pm10_pres_mar     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 17.40, 20.03, 21.46, 21.28, np.nan, 20.23, 21.62, 23.92, 26.53, 12.58, np.nan, np.nan, np.nan, np.nan, np.nan]
pm10_pres_err_mar = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.29,  0.31,   0.41,   0.46,   np.nan, 0.54,   0.56,   1.00,   1.15,   1.03,   np.nan, np.nan, np.nan, np.nan, np.nan]

pm25_pres_mar     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 16.23, 18.74, 20.17, 19.98, np.nan, 18.99, 20.35, 22.62, 25.17, 11.58, np.nan, np.nan, np.nan, np.nan, np.nan]
pm25_pres_err_mar = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.28,  0.30,   0.36,   0.44,   np.nan, 0.53,   0.54,   0.99,   1.13,   1.03,   np.nan, np.nan, np.nan, np.nan, np.nan]


# MERCOLEDÌ – dati in ASSENZA di occupazione
co2_abs_mer     = [459.3, 454.7, 449.9, 447.7, 445.7, 445.7, 450.0, 462.1, 472.2, 502.4, 560.3, 599.3, 624.6, 607.4, 598.2, 639.6, 630.8, 605.7, 544.6, 508.4, 489.4, 474.6, 474.4, 469.6]
co2_abs_err_mer = [2.8,   2.1,   1.9,   1.9,   2.0,   2.0,   1.8,   2.1,   2.7,   4.7,   9.8,   13.2,  14.4,  12.9,  12.6,  16.9,  17.2,  13.8,  9.6,   7.0,   5.4,   4.1,   4.0,   3.5]

temp_abs_mer     = [21.4, 21.3, 21.2, 21.0, 20.9, 21.0, 20.9, 21.0, 21.1, 21.2, 21.4, 21.5, 21.6, 21.7, 21.8, 21.9, 22.0, 22.0, 21.8, 21.7, 21.6, 21.4, 21.4, 21.3]
temp_abs_err_mer = [0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2]

pm10_abs_mer     = [17.5, 18.8, 20.1, 20.2, 19.3, 18.9, 20.5, 17.4, 16.0, 16.2, 18.1, 19.4, 18.5, 16.2, 16.1, 16.9, 18.4, 18.6, 15.7, 15.3, 14.2, 14.5, 15.2, 15.4]
pm10_abs_err_mer = [0.8,  1.1,  1.4,  1.3,  1.1,  1.0,  1.1,  0.7,  0.6,  0.6,  0.7,  0.8,  0.7,  0.6,  0.7,  0.6,  0.8,  0.7,  0.4,  0.4,  0.4,  0.5,  0.5,  0.6]

pm25_abs_mer     = [16.2, 17.5, 18.9, 19.0, 18.1, 17.6, 19.2, 16.2, 14.9, 15.1, 16.9, 18.2, 17.3, 15.0, 14.9, 15.7, 17.3, 17.5, 14.6, 14.2, 13.2, 13.5, 14.1, 14.3]
pm25_abs_err_mer = [0.8,  1.1,  1.4,  1.3,  1.1,  1.0,  1.1,  0.7,  0.6,  0.6,  0.7,  0.7,  0.6,  0.5,  0.7,  0.6,  0.7,  0.7,  0.4,  0.4,  0.4,  0.5,  0.5,  0.5]

# MERCOLEDÌ – dati in PRESENZA di occupazione (usa np.nan per ore senza dati)
co2_pres_mer     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 795.40, 961.36, 925.19, 936.50, np.nan, 844.86, 943.68, 948.12, 925.25, 1246.78, np.nan, np.nan, np.nan, np.nan, np.nan]
co2_pres_err_mer = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 12.43,  15.59,  13.59,   15.75,   np.nan, 12.27,   16.89,   18.54,   17.76,   26.18,   np.nan, np.nan, np.nan, np.nan, np.nan]

temp_pres_mer     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 21.24, 21.74, 21.88, 21.99, np.nan, 22.28, 22.28, 22.31, 22.59, 20.12, np.nan, np.nan, np.nan, np.nan, np.nan]
temp_pres_err_mer = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.08,  0.07,   0.06,   0.06,   np.nan, 0.07,   0.07,   0.08,   0.09,   0.12,   np.nan, np.nan, np.nan, np.nan, np.nan]

pm10_pres_mer     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 19.81, 26.09, 23.15, 23.79, np.nan, 18.29, 20.83, 19.75, 17.49, 13.56, np.nan, np.nan, np.nan, np.nan, np.nan]
pm10_pres_err_mer = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.42,  0.67,   0.43,   0.88,   np.nan, 0.40,   0.54,   0.61,   1.04,   1.28,   np.nan, np.nan, np.nan, np.nan, np.nan]

pm25_pres_mer     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 18.50, 24.60, 21.78, 22.45, np.nan, 17.11, 19.59, 18.56, 16.39, 12.56, np.nan, np.nan, np.nan, np.nan, np.nan]
pm25_pres_err_mer = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.41,  0.66,   0.42,   0.86,   np.nan, 0.39,   0.52,   0.60,   1.03,   1.28,   np.nan, np.nan, np.nan, np.nan, np.nan]


# GIOVEDÌ – dati in ASSENZA di occupazione
co2_abs_gio     = [465.7, 460.3, 455.5, 453.6, 449.8, 449.6, 455.0, 467.5, 476.2, 479.0, 476.1, 484.1, 491.3, 488.3, 485.8, 484.0, 488.8, 487.1, 478.4, 464.2, 462.0, 457.4, 452.6, 450.6]
co2_abs_err_gio = [2.6,   2.5,   2.4,   2.5,   2.4,   2.3,   2.6,   2.7,   2.9,   3.2,   3.7,   5.1,   5.4,   4.8,   4.2,   4.6,   5.3,   5.0,   4.2,   2.7,   2.4,   2.4,   2.3,   2.1]

temp_abs_gio     = [20.7, 20.6, 20.5, 20.0, 20.1, 20.3, 20.2, 20.3, 20.4, 20.3, 20.6, 20.9, 21.0, 21.1, 21.3, 21.4, 21.4, 21.4, 21.4, 21.2, 21.0, 20.9, 20.8, 20.7]
temp_abs_err_gio = [0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.1]

pm10_abs_gio     = [17.6,  18.8,  19.1,  18.6,  17.9,  17.7,  19.5,  17.7,  15.6,  15.6,  16.2,  16.0,  15.5,  14.8,  15.2,  14.9,  14.2,  15.0,  13.3,  13.8,  13.3,  13.8,  14.8,  16.3]
pm10_abs_err_gio = [0.7,    0.8,    0.8,    0.7,    0.7,    0.7,    0.7,    0.5,    0.5,    0.6,    0.7,    0.6,    0.6,    0.5,    0.6,    0.6,    0.5,    1.3,    0.5,    0.5,    0.4,    0.4,    0.5,    0.6]

pm25_abs_gio     = [16.4,   17.6,   17.9,   17.4,   16.8,   16.5,   18.2,   16.6,   14.5,   14.4,   15.0,   14.8,   14.3,   13.8,   14.1,    13.8,    13.1,    13.9,    12.3,    12.7,    12.3,    12.8,    13.7,    15.2]
pm25_abs_err_gio = [0.7,    0.8,    0.8,    0.7,    0.7,    0.7,    0.7,    0.5,    0.5,    0.6,    0.7,    0.5,    0.5,    0.5,    0.5,     0.6,     0.5,     1.3,     0.5,     0.5,     0.4,     0.4,     0.5,     0.6]

# GIOVEDÌ – dati in PRESENZA di occupazione (usa np.nan per ore senza dati)
co2_pres_gio     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 760.17, 821.42, 921.08, 961.75, 997.80, np.nan, 864.64, 926.35, 1031.98, 1027.41, 625.89, np.nan, np.nan, np.nan, np.nan, np.nan]
co2_pres_err_gio = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.83,   11.86,  13.64,   12.06,   12.45,   np.nan, 9.27,   10.43,  11.49,  11.38,  23.10,  np.nan, np.nan, np.nan, np.nan, np.nan]

temp_pres_gio     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 21.30, 21.43, 21.73, 21.91, 22.16, np.nan, 22.41, 22.47, 22.72, 23.02, 23.52, np.nan, np.nan, np.nan, np.nan, np.nan]
temp_pres_err_gio = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.00,  0.07,  0.07,  0.06,   0.06,   np.nan, 0.07,   0.07,   0.06,   0.06,   0.16,   np.nan, np.nan, np.nan, np.nan, np.nan]

pm10_pres_gio     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 9.67,  19.43, 24.15, 21.21, 20.25, np.nan, 21.64, 25.92, 23.98, 24.35, 17.95, np.nan, np.nan, np.nan, np.nan, np.nan]
pm10_pres_err_gio = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.56,   0.41,   1.24,   0.41,    0.39,   np.nan, 0.82,   0.88,   1.05,   0.83,   2.87,   np.nan, np.nan, np.nan, np.nan, np.nan]

pm25_pres_gio     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 8.67,  18.20, 22.79, 19.95, 19.02, np.nan, 20.39, 24.58, 22.68, 23.04, 16.63, np.nan, np.nan, np.nan, np.nan, np.nan]
pm25_pres_err_gio = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.56,   0.40,   1.22,   0.39,    0.38,   np.nan, 0.81,   0.87,   1.03,   0.81,   2.76,   np.nan, np.nan, np.nan, np.nan, np.nan]


# VENERDÌ – dati in ASSENZA di occupazione
co2_abs_ven     = [459.8, 454.5, 447.5, 445.9, 445.0, 446.0, 449.5, 460.5, 461.6, 499.1, 553.5, 603.8, 614.8, 569.8, 566.1, 572.3, 560.9, 541.4, 541.4, 505.1, 484.1, 473.4, 463.5, 457.1]
co2_abs_err_ven = [2.4,   2.2,   2.2,   2.2,   2.3,   2.5,   2.6,   2.5,   2.6,   5.5,   10.4,  15.7,  17.1,  12.5,  12.1,  12.6,  11.4,  9.9,   9.6,   6.6,   5.2,   4.5,   4.1,   3.6]

temp_abs_ven     = [20.6,  20.5,  20.5,  20.4,  20.3,  20.3,  20.2,  20.4,  20.6,  20.7,  20.8,  20.8,  20.9,  20.8,  20.9,  21.0,  21.0,  21.0,  21.0,  20.8,  20.7,  20.6,  20.5,  20.3]
temp_abs_err_ven = [0.2,    0.2,    0.2,    0.2,    0.2,    0.2,    0.2,    0.2,    0.2,    0.2,    0.2,    0.2,    0.2,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1]

pm10_abs_ven     = [16.7,   16.7,   16.1,   16.5,   16.8,   17.0,   18.2,   17.3,   14.1,   15.4,   17.0,   18.3,   18.0,   15.2,   16.1,   15.9,   14.4,   13.7,   15.1,   12.9,   12.3,   12.2,   13.2,   13.6]
pm10_abs_err_ven = [0.6,    0.6,    0.6,    0.6,    0.6,    0.7,    0.7,    0.5,    0.4,    0.5,    0.7,    0.8,    0.8,    0.3,    0.3,    0.2,    0.4,    0.4,    1.5,    0.4,    0.4,    0.4,    0.5,    0.5]

pm25_abs_ven     = [15.6,   15.5,   15.0,   15.3,   15.6,   15.8,   17.0,   16.1,   13.0,   14.3,   15.9,   17.2,   16.8,   14.1,   15.0,   14.8,   13.4,   12.6,   14.0,   11.9,   11.2,   11.2,   12.2,   12.6]
pm25_abs_err_ven = [0.5,    0.6,    0.6,    0.6,    0.6,    0.6,    0.7,    0.5,    0.4,    0.5,    0.7,    0.8,    0.8,    0.3,    0.6,    0.6,    0.4,    0.4,    1.5,    0.4,    0.4,    0.4,    0.4,    0.5]

# VENERDÌ – dati in PRESENZA di occupazione (usa np.nan per ore senza dati)
co2_pres_ven     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 773.97, 908.84, 1032.82, 1035.83, np.nan, 1133.40, 1034.88, 1143.45, 1106.94, 911.76, 786.50, np.nan, np.nan, np.nan, np.nan, np.nan]
co2_pres_err_ven = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 11.68,  14.74,   14.48,    15.91,   np.nan,   24.29,    15.60,    16.02,    16.47,    12.88,    33.20,   np.nan, np.nan, np.nan, np.nan, np.nan]

temp_pres_ven     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 21.65, 21.89, 23.04, 23.33, np.nan, 23.81, 23.54, 23.95, 24.10, 24.10, 24.12, np.nan, np.nan, np.nan, np.nan, np.nan]
temp_pres_err_ven = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.07,   0.08,    0.05,    0.05,   np.nan,   0.09,     0.06,     0.06,     0.06,     0.06,     0.32,   np.nan, np.nan, np.nan, np.nan, np.nan]

pm10_pres_ven     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 15.74, 17.53, 20.69, 13.87, np.nan, 11.00, 12.29, 11.64, 11.95, 12.02, 9.46,  np.nan, np.nan, np.nan, np.nan, np.nan]
pm10_pres_err_ven = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.33,   0.38,    0.47,    0.36,   np.nan,   0.64,     0.35,     0.30,     0.34,     0.38,     0.78,   np.nan, np.nan, np.nan, np.nan, np.nan]

pm25_pres_ven     = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 14.62, 16.32, 14.05, 12.77, np.nan, 10.00, 11.22, 10.58, 10.90, 10.95, 8.46,  np.nan, np.nan, np.nan, np.nan, np.nan]
pm25_pres_err_ven = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.32,   0.35,    0.45,    0.35,   np.nan,   0.64,     0.28,     0.23,     0.33,     0.38,     0.78,   np.nan, np.nan, np.nan, np.nan, np.nan]


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
    plt.title(f'Aula D – {variabile} – {giorno}')
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
