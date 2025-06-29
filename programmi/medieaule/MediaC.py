import matplotlib.pyplot as plt
# Dati di esempio
xa = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
xb = [9,10,11,12,14,15,16,17,18]
# Aule Piene - con studenti
y1b = [908.11, 1113.62, 1138.56, 1234.19, 1018.82, 1072.09, 1078.70, 1008.58, 990.86]
y1b_error = [6.01, 7.78, 7.58, 8.62, 6.50, 6.51, 7.09, 7.12, 12.60]

y2b = [22.00, 22.64, 22.82, 23.05, 22.89, 23.04, 23.11, 22.94, 22.92]
y2b_error = [0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.03, 0.04]

y3b = [14.34, 15.56, 15.51, 15.52, 14.06, 13.50, 13.85, 13.55, 11.31]
y3b_error = [0.12, 0.13, 0.12, 0.12, 0.13, 0.11, 0.13, 0.14, 0.21]

y4b = [13.26, 14.45, 14.41, 14.42, 12.97, 12.43, 12.77, 12.49, 10.26]
y4b_error = [0.12, 0.12, 0.12, 0.12, 0.12, 0.11, 0.12, 0.14, 0.20]

# Aule Vuote - senza studenti
y1a = [459.41, 455.13, 450.43, 446.91, 446.78, 447.06, 450.99, 463.29, 470.03, 491.23,
            520.74, 545.31, 558.62, 541.99, 539.69, 553.92, 551.52, 540.42, 523.09, 496.82,
            482.62, 473.36, 467.38, 463.01]
y1a_error = [1.50, 1.37, 1.29, 1.22, 1.27, 1.26, 1.24, 1.25, 1.35, 2.13,
                  3.99, 5.68, 6.46, 5.44, 5.40, 6.50, 6.49, 5.70, 4.84, 3.51,
                  2.73, 2.29, 2.02, 1.76]

y2a = [20.83, 20.74, 20.68, 20.42, 20.45, 20.48, 20.41, 20.54, 20.69, 20.77,
            20.92, 21.05, 21.09, 21.15, 21.27, 21.38, 21.42, 21.45, 21.41, 21.24,
            21.07, 20.97, 20.87, 20.71]
y2a_error = [0.10] * 8 + [0.09] * 12 + [0.10] * 4

y3a = [16.79, 17.31, 17.38, 17.52, 16.99, 16.85, 17.89, 17.61, 14.71, 15.20,
            15.96, 16.54, 16.32, 14.65, 14.93, 14.96, 14.82, 14.91, 14.07, 13.59,
            13.08, 13.28, 14.12, 14.83]
y3a_error = [0.35, 0.40, 0.45, 0.44, 0.39, 0.38, 0.40, 1.06, 0.23, 0.25,
                  0.31, 0.33, 0.31, 0.25, 0.29, 0.29, 0.28, 0.37, 0.42, 0.22,
                  0.21, 0.22, 0.24, 0.26]

y4a = [15.61, 16.12, 16.22, 16.37, 15.82, 15.66, 16.68, 16.46, 13.63, 14.11,
            14.84, 15.41, 15.18, 13.57, 13.84, 13.87, 13.74, 13.83, 13.02, 12.54,
            12.04, 12.23, 13.02, 13.70]
y4a_error = [0.34, 0.39, 0.44, 0.43, 0.38, 0.37, 0.39, 1.05, 0.23, 0.25,
                  0.30, 0.32, 0.30, 0.24, 0.29, 0.28, 0.27, 0.37, 0.41, 0.21,
                  0.20, 0.21, 0.23, 0.25]




fig, axs = plt.subplots(2, 2, figsize=(12, 10), sharex=True)

# CO₂
axs[0, 0].errorbar(xa, y1a, yerr=y1a_error,
                   label='Senza lezioni', color='blue', marker='o', linestyle='none', capsize=4)
axs[0, 0].errorbar(xb, y1b, yerr=y1b_error,
                   label='Durante le lezioni', color='red', marker='x', linestyle='none', capsize=4)
axs[0, 0].set_title('CO₂ media')
axs[0, 0].set_ylabel('CO₂ [ppm]')
axs[0, 0].legend()
axs[0, 0].grid(True)

# Temperatura
axs[0, 1].errorbar(xa, y2a, yerr=y2a_error,
                   label='senza lezioni', color='orange', marker='o', linestyle='none', capsize=4)
axs[0, 1].errorbar(xb, y2b, yerr=y2b_error,
                   label='Durante le lezioni', color='green', marker='x', linestyle='none', capsize=4)
axs[0, 1].set_title('Temperatura media')
axs[0, 1].set_ylabel('Temp [°C]')
axs[0, 1].legend()
axs[0, 1].grid(True)

# PM10
axs[1, 0].errorbar(xa, y3a, yerr=y3a_error,
                   label='senza lezioni', color='magenta', marker='o', linestyle='none', capsize=4)
axs[1, 0].errorbar(xb, y3b, yerr=y3b_error,
                   label='Durante le lezioni', color='cyan', marker='x',  linestyle='none', capsize=4)
axs[1, 0].set_title('PM10 medio')
axs[1, 0].set_xlabel('Ora')
axs[1, 0].set_ylabel('PM10 [μg/m³]')
axs[1, 0].legend()
axs[1, 0].grid(True)

# PM2.5
axs[1, 1].errorbar(xa, y4a, yerr=y4a_error,
                   label='senza lezioni', color='purple', marker='o', linestyle='none', capsize=4)
axs[1, 1].errorbar(xb, y4b, yerr=y4b_error,
                   label='Durante le lezioni', color='brown', marker='x',  linestyle='none', capsize=4)
axs[1, 1].set_title('PM2.5 medio')
axs[1, 1].set_xlabel('Ora')
axs[1, 1].set_ylabel('PM2.5 [μg/m³]')
axs[1, 1].legend()
axs[1, 1].grid(True)

plt.tight_layout()
plt.savefig("Grafici/quattro_graficiC.png")
plt.show()

# -------------------------------------------------------------------
# 2) GRAFICI SEPARATI (uno per ciascuna variabile)
# -------------------------------------------------------------------

# --- Grafico 1: CO₂ ---
plt.figure(figsize=(8, 5))
plt.errorbar(xa, y1a, yerr=y1a_error,
             label='senza lezioni', color='blue', marker='o',  linestyle='none', capsize=4)
plt.errorbar(xb, y1b, yerr=y1b_error,
             label='Durante le lezioni', color='red', marker='x', linestyle='none', capsize=4)
plt.title('CO₂ media aula C')
plt.xlabel('Ora')
plt.ylabel('CO₂ [ppm]')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("Grafici/co2_separatoC.png")
plt.show()

# --- Grafico 2: Temperatura ---
plt.figure(figsize=(8, 5))
plt.errorbar(xa, y2a, yerr=y2a_error,
             label='senza lezioni', color='orange', marker='o', linestyle='none', capsize=4)
plt.errorbar(xb, y2b, yerr=y2b_error,
             label='Durante le lezioni', color='green', marker='x',  linestyle='none', capsize=4)
plt.title('Temperatura media aula C')
plt.xlabel('Ora')
plt.ylabel('Temperatura [°C]')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("Grafici/temperatura_separatoC.png")
plt.show()

# --- Grafico 3: PM10 ---
plt.figure(figsize=(8, 5))
plt.errorbar(xa, y3a, yerr=y3a_error,
             label='senza lezioni', color='magenta', marker='o', linestyle='none', capsize=4)
plt.errorbar(xb, y3b, yerr=y3b_error,
             label='Durante le lezioni', color='cyan', marker='x',  linestyle='none', capsize=4)
plt.title('PM10 medio aula C')
plt.xlabel('Ora')
plt.ylabel('PM10 [μg/m³]')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("Grafici/pm10_separatoC.png")
plt.show()

# --- Grafico 4: PM2.5 ---
plt.figure(figsize=(8, 5))
plt.errorbar(xa, y4a, yerr=y4a_error,
             label='senza lezioni', color='purple', marker='o', linestyle='none', capsize=4)
plt.errorbar(xb, y4b, yerr=y4b_error,
             label='Durante le lezioni', color='brown', marker='x',  linestyle='none', capsize=4)
plt.title('PM2.5 medio aula C')
plt.xlabel('Ora')
plt.ylabel('PM2.5 [μg/m³]')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("Grafici/pm25_separatoC.png")
plt.show()