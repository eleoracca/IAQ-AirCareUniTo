import matplotlib.pyplot as plt
# Dati di esempio
x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

# Aule Piene - con studenti
y1b = [751.07, 884.53, 941.15, 1006.81, 903.29, 986.03, 970.58, 889.75, 885.92]
y1b_error = [4.48, 5.38, 5.67, 7.53, 5.23, 6.94, 6.74, 5.98, 49.01]

y2b = [21.24, 21.59, 21.80, 22.03, 22.21, 22.34, 22.39, 22.51, 21.79]
y2b_error = [0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.31]

y3b = [18.02, 21.57, 21.59, 23.79, 20.31, 23.14, 22.35, 22.27, 30.28]
y3b_error = [0.17, 0.31, 0.28, 0.34, 0.32, 0.38, 0.52, 0.48, 3.54]

y4b = [16.83, 20.25, 20.29, 22.45, 19.08, 21.85, 21.09, 21.03, 28.91]
y4b_error = [0.16, 0.31, 0.28, 0.33, 0.31, 0.37, 0.51, 0.47, 3.49]

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
axs[0, 1].errorbar(x, y1a, yerr=y1a_error,
                   label='Senza lezioni', color='orange', marker='o', capsize=4)
axs[0, 1].errorbar(x, y1b, yerr=y1b_error,
                   label='Durante le lezioni', color='green', marker='x', linestyle='--', capsize=4)
axs[0, 0].set_title('CO₂ media')
axs[0, 0].set_ylabel('CO₂ [ppm]')
axs[0, 0].legend()
axs[0, 0].grid(True)

# Temperatura
axs[0, 1].errorbar(x, y2a, yerr=y2a_error,
                   label='senza lezioni', color='orange', marker='o', capsize=4)
axs[0, 1].errorbar(x, y2b, yerr=y2b_error,
                   label='Durante le lezioni', color='green', marker='x', linestyle='--', capsize=4)
axs[0, 1].set_title('Temperatura media')
axs[0, 1].set_ylabel('Temp [°C]')
axs[0, 1].legend()
axs[0, 1].grid(True)

# PM10
axs[1, 0].errorbar(x, y3a, yerr=y3a_error,
                   label='senza lezioni', color='magenta', marker='o', capsize=4)
axs[1, 0].errorbar(x, y3b, yerr=y3b_error,
                   label='Durante le lezioni', color='cyan', marker='x', linestyle='--', capsize=4)
axs[1, 0].set_title('PM10 medio')
axs[1, 0].set_xlabel('Ora')
axs[1, 0].set_ylabel('PM10 [μg/m³]')
axs[1, 0].legend()
axs[1, 0].grid(True)

# PM2.5
axs[1, 1].errorbar(x, y4a, yerr=y4a_error,
                   label='senza lezioni', color='purple', marker='o', capsize=4)
axs[1, 1].errorbar(x, y4b, yerr=y4b_error,
                   label='Durante le lezioni', color='brown', marker='x', linestyle='--', capsize=4)
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
plt.errorbar(x, y1a, yerr=y1a_error,
             label='senza lezioni', color='red', marker='o', capsize=4)
plt.errorbar(x, y1b, yerr=y1b_error,
             label='Durante le lezioni', color='blue', marker='x', linestyle='--', capsize=4)
plt.title('CO₂ media aula D')
plt.xlabel('Ora')
plt.ylabel('CO₂ [ppm]')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("Grafici/co2_separatoC.png")
plt.show()

# --- Grafico 2: Temperatura ---
plt.figure(figsize=(8, 5))
plt.errorbar(x, y2a, yerr=y2a_error,
             label='senza lezioni', color='orange', marker='o', capsize=4)
plt.errorbar(x, y2b, yerr=y2b_error,
             label='Durante le lezioni', color='green', marker='x', linestyle='--', capsize=4)
plt.title('Temperatura media aula D')
plt.xlabel('Ora')
plt.ylabel('Temperatura [°C]')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("Grafici/temperatura_separatoC.png")
plt.show()

# --- Grafico 3: PM10 ---
plt.figure(figsize=(8, 5))
plt.errorbar(x, y3a, yerr=y3a_error,
             label='senza lezioni', color='magenta', marker='o', capsize=4)
plt.errorbar(x, y3b, yerr=y3b_error,
             label='Durante le lezioni', color='cyan', marker='x', linestyle='--', capsize=4)
plt.title('PM10 medio aula D')
plt.xlabel('Ora')
plt.ylabel('PM10 [μg/m³]')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("Grafici/pm10_separatoC.png")
plt.show()

# --- Grafico 4: PM2.5 ---
plt.figure(figsize=(8, 5))
plt.errorbar(x, y4a, yerr=y4a_error,
             label='senza lezioni', color='purple', marker='o', capsize=4)
plt.errorbar(x, y4b, yerr=y4b_error,
             label='Durante le lezioni', color='brown', marker='x', linestyle='--', capsize=4)
plt.title('PM2.5 medio aula D')
plt.xlabel('Ora')
plt.ylabel('PM2.5 [μg/m³]')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("Grafici/pm25_separatoC.png")
plt.show()