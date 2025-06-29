import matplotlib.pyplot as plt
# Dati di esempio
x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

# Sabato (a) e Domenica (b) – variabili numerate:
# 1 = co2, 2 = temp, 3 = pm10, 4 = pm25

# 1a = media_co2 sabato
y1a = [
    445.79, 442.48, 439.91, 438.74, 437.61, 437.20, 440.42, 446.48,
    451.92, 453.80, 452.11, 446.21, 439.67, 433.96, 428.97, 425.44,
    422.74, 423.45, 426.81, 431.02, 434.70, 436.07, 436.74, 436.55
]
# 1a_error = err_co2 sabato
y1a_error = [
    1.01, 0.91, 0.87, 0.86, 0.82, 0.79, 0.79, 0.83,
    0.89, 0.96, 0.96, 0.90, 0.83, 0.78, 0.72, 0.67,
    0.66, 0.69, 0.74, 0.80, 0.83, 0.82, 0.80, 0.75
]

# 1b = media_co2 domenica
y1b = [
    437.02, 437.44, 436.71, 436.88, 437.14, 438.40, 441.16, 445.92,
    450.13, 452.06, 451.02, 445.73, 438.55, 433.01, 427.18, 423.24,
    422.46, 424.26, 428.06, 432.25, 434.85, 436.66, 437.76, 437.53
]
# 1b_error = err_co2 domenica
y1b_error = [
    0.70, 0.65, 0.63, 0.65, 0.63, 0.62, 0.64, 0.70,
    0.76, 0.81, 0.84, 0.82, 0.74, 0.67, 0.62, 0.58,
    0.57, 0.62, 0.72, 0.77, 0.76, 0.75, 0.74, 0.67
]

# 2a = media_temp sabato
y2a = [
    22.87, 22.81, 22.77, 22.72, 22.67, 22.62, 22.58, 22.56,
    22.55, 22.57, 22.57, 22.58, 22.61, 22.64, 22.66, 22.68,
    22.71, 22.71, 22.71, 22.68, 22.68, 22.64, 22.60, 22.57
]
# 2a_error = err_temp sabato
y2a_error = [
    0.04, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05,
    0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05,
    0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05
]

# 2b = media_temp domenica
y2b = [
    22.55, 22.51, 22.46, 22.42, 22.43, 22.40, 22.36, 22.34,
    22.33, 22.33, 22.33, 22.37, 22.38, 22.40, 22.44, 22.47,
    22.48, 22.48, 22.48, 22.47, 22.48, 22.45, 22.41, 22.39
]
# 2b_error = err_temp domenica
y2b_error = [
    0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05,
    0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05,
    0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05
]

# 3a = media_pm10 sabato
y3a = [
    10.88, 10.89, 11.15, 11.43, 11.39, 11.35, 11.23, 11.18,
    11.40, 11.30, 11.21, 11.02, 10.55, 10.15, 9.83, 9.46,
    9.27, 9.49, 9.64, 9.76, 9.88, 10.22, 10.67, 10.86
]
# 3a_error = err_pm10 sabato
y3a_error = [
    0.16, 0.17, 0.17, 0.18, 0.18, 0.18, 0.17, 0.17,
    0.17, 0.17, 0.17, 0.18, 0.17, 0.16, 0.16, 0.15,
    0.15, 0.16, 0.15, 0.15, 0.16, 0.16, 0.16, 0.17
]

# 3b = media_pm10 domenica
y3b = [
    11.33, 11.82, 11.90, 11.65, 11.34, 11.25, 11.10, 10.87,
    10.80, 10.80, 10.81, 10.54, 10.05, 9.50, 9.01, 8.58,
    8.50, 8.73, 9.01, 9.26, 9.71, 9.85, 10.17, 10.36
]
# 3b_error = err_pm10 domenica
y3b_error = [
    0.18, 0.20, 0.21, 0.20, 0.19, 0.19, 0.18, 0.17,
    0.16, 0.16, 0.17, 0.17, 0.16, 0.14, 0.13, 0.12,
    0.12, 0.12, 0.12, 0.12, 0.14, 0.14, 0.15, 0.15
]

# 4a = media_pm25 sabato
y4a = [
    9.85, 9.86, 10.12, 10.39, 10.34, 10.30, 10.19, 10.15,
    10.36, 10.27, 10.17, 9.98, 9.50, 9.10, 8.80, 8.43,
    8.24, 8.46, 8.61, 8.72, 8.85, 9.19, 9.64, 9.84
]
# 4a_error = err_pm25 sabato
y4a_error = [
    0.16, 0.16, 0.17, 0.18, 0.18, 0.18, 0.17, 0.17,
    0.17, 0.17, 0.17, 0.18, 0.17, 0.16, 0.16, 0.15,
    0.15, 0.15, 0.15, 0.15, 0.15, 0.16, 0.16, 0.16
]

# 4b = media_pm25 domenica
y4b = [
    10.29, 10.78, 10.86, 10.61, 10.31, 10.21, 10.06, 9.83,
    9.76, 9.76, 9.77, 9.49, 9.02, 8.49, 8.00, 7.58,
    7.49, 7.72, 8.01, 8.26, 8.70, 8.83, 9.15, 9.34
]
# 4b_error = err_pm25 domenica
y4b_error = [
    0.17, 0.20, 0.20, 0.20, 0.19, 0.18, 0.18, 0.17,
    0.16, 0.16, 0.16, 0.17, 0.16, 0.14, 0.13, 0.12,
    0.12, 0.12, 0.12, 0.12, 0.13, 0.14, 0.14, 0.15
]


fig, axs = plt.subplots(2, 2, figsize=(12, 10), sharex=True)

# CO₂
axs[0, 0].errorbar(x, y1a, yerr=y1a_error,
                   label='CO₂ Sabato', color='red', marker='o', capsize=4)
axs[0, 0].errorbar(x, y1b, yerr=y1b_error,
                   label='CO₂ Domenica', color='blue', marker='x', linestyle='--', capsize=4)
axs[0, 0].set_title('CO₂ media')
axs[0, 0].set_ylabel('CO₂ [ppm]')
axs[0, 0].legend()
axs[0, 0].grid(True)

# Temperatura
axs[0, 1].errorbar(x, y2a, yerr=y2a_error,
                   label='Temp Sabato', color='orange', marker='o', capsize=4)
axs[0, 1].errorbar(x, y2b, yerr=y2b_error,
                   label='Temp Domenica', color='green', marker='x', linestyle='--', capsize=4)
axs[0, 1].set_title('Temperatura media')
axs[0, 1].set_ylabel('Temp [°C]')
axs[0, 1].legend()
axs[0, 1].grid(True)

# PM10
axs[1, 0].errorbar(x, y3a, yerr=y3a_error,
                   label='PM10 Sabato', color='magenta', marker='o', capsize=4)
axs[1, 0].errorbar(x, y3b, yerr=y3b_error,
                   label='PM10 Domenica', color='cyan', marker='x', linestyle='--', capsize=4)
axs[1, 0].set_title('PM10 medio')
axs[1, 0].set_xlabel('Ora')
axs[1, 0].set_ylabel('PM10 [μg/m³]')
axs[1, 0].legend()
axs[1, 0].grid(True)

# PM2.5
axs[1, 1].errorbar(x, y4a, yerr=y4a_error,
                   label='PM2.5 Sabato', color='purple', marker='o', capsize=4)
axs[1, 1].errorbar(x, y4b, yerr=y4b_error,
                   label='PM2.5 Domenica', color='brown', marker='x', linestyle='--', capsize=4)
axs[1, 1].set_title('PM2.5 medio')
axs[1, 1].set_xlabel('Ora')
axs[1, 1].set_ylabel('PM2.5 [μg/m³]')
axs[1, 1].legend()
axs[1, 1].grid(True)

plt.tight_layout()
plt.savefig("Grafici/quattro_graficiG.png")
plt.show()

# -------------------------------------------------------------------
# 2) GRAFICI SEPARATI (uno per ciascuna variabile)
# -------------------------------------------------------------------

# --- Grafico 1: CO₂ ---
plt.figure(figsize=(8, 5))
plt.errorbar(x, y1a, yerr=y1a_error,
             label='CO₂ Sabato', color='red', marker='o', capsize=4)
plt.errorbar(x, y1b, yerr=y1b_error,
             label='CO₂ Domenica', color='blue', marker='x', linestyle='--', capsize=4)
plt.title('CO₂ media Sabato vs Domenica')
plt.xlabel('Ora')
plt.ylabel('CO₂ [ppm]')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("Grafici/co2_separatoG.png")
plt.show()

# --- Grafico 2: Temperatura ---
plt.figure(figsize=(8, 5))
plt.errorbar(x, y2a, yerr=y2a_error,
             label='Temp Sabato', color='orange', marker='o', capsize=4)
plt.errorbar(x, y2b, yerr=y2b_error,
             label='Temp Domenica', color='green', marker='x', linestyle='--', capsize=4)
plt.title('Temperatura media Sabato vs Domenica')
plt.xlabel('Ora')
plt.ylabel('Temperatura [°C]')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("Grafici/temperatura_separatoG.png")
plt.show()

# --- Grafico 3: PM10 ---
plt.figure(figsize=(8, 5))
plt.errorbar(x, y3a, yerr=y3a_error,
             label='PM10 Sabato', color='magenta', marker='o', capsize=4)
plt.errorbar(x, y3b, yerr=y3b_error,
             label='PM10 Domenica', color='cyan', marker='x', linestyle='--', capsize=4)
plt.title('PM10 medio Sabato vs Domenica')
plt.xlabel('Ora')
plt.ylabel('PM10 [μg/m³]')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("Grafici/pm10_separatoG.png")
plt.show()

# --- Grafico 4: PM2.5 ---
plt.figure(figsize=(8, 5))
plt.errorbar(x, y4a, yerr=y4a_error,
             label='PM2.5 Sabato', color='purple', marker='o', capsize=4)
plt.errorbar(x, y4b, yerr=y4b_error,
             label='PM2.5 Domenica', color='brown', marker='x', linestyle='--', capsize=4)
plt.title('PM2.5 medio Sabato vs Domenica')
plt.xlabel('Ora')
plt.ylabel('PM2.5 [μg/m³]')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("Grafici/pm25_separatoG.png")
plt.show()