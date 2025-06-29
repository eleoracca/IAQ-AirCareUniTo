import matplotlib.pyplot as plt
# Dati di esempio
x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

# Sabato (a) e Domenica (b) – variabili numerate:
# 1 = co2, 2 = temp, 3 = pm10, 4 = pm25

# 1a = media_co2 sabato
y1a = [
    454.31, 450.49, 447.81, 446.76, 445.04, 444.28, 447.02, 450.99,
    455.10, 457.53, 456.48, 455.83, 455.27, 450.26, 438.70, 433.13,
    430.12, 430.91, 433.15, 436.39, 439.04, 440.62, 439.81, 439.50
]
# 1a_error = err_co2 sabato
y1a_error = [
    1.57, 1.35, 1.21, 1.17, 1.06, 0.99, 0.99, 1.01,
    1.05, 1.12, 1.15, 1.79, 3.03, 3.15, 1.40, 1.02,
    0.88, 0.83, 0.84, 0.88, 0.89, 0.92, 0.88, 0.85
]

# 1b = media_co2 domenica
y1b = [
    439.30, 439.90, 439.12, 440.22, 441.23, 442.44, 444.72, 449.22,
    453.34, 455.85, 455.63, 452.32, 445.48, 437.96, 432.11, 428.90,
    427.82, 429.48, 432.43, 436.10, 437.83, 438.75, 439.00, 438.40
]
# 1b_error = err_co2 domenica
y1b_error = [
    0.81, 0.76, 0.73, 0.84, 0.88, 0.93, 0.93, 0.99,
    1.09, 1.24, 1.38, 1.52, 1.34, 0.95, 0.74, 0.64,
    0.61, 0.68, 0.77, 0.80, 0.78, 0.77, 0.76, 0.73
]

# 2a = media_temp sabato
y2a = [
    21.83, 21.75, 21.70, 21.52, 21.56, 21.52, 21.48, 21.61,
    21.76, 21.82, 21.87, 21.91, 21.97, 22.02, 22.09, 22.14,
    22.17, 22.21, 22.22, 22.08, 21.93, 21.84, 21.74, 21.65
]
# 2a_error = err_temp sabato
y2a_error = [
    0.07, 0.07, 0.07, 0.07, 0.08, 0.08, 0.08, 0.07,
    0.07, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06,
    0.06, 0.06, 0.06, 0.06, 0.06, 0.07, 0.07, 0.07
]

# 2b = media_temp domenica
y2b = [
    21.57, 21.50, 21.50, 21.26, 21.36, 21.36, 21.31, 21.41,
    21.58, 21.64, 21.72, 21.77, 21.83, 21.90, 21.95, 22.01,
    22.05, 22.08, 22.09, 21.93, 21.81, 21.70, 21.63, 21.53
]
# 2b_error = err_temp domenica
y2b_error = [
    0.07, 0.07, 0.07, 0.08, 0.08, 0.08, 0.08, 0.07,
    0.07, 0.07, 0.07, 0.07, 0.07, 0.06, 0.06, 0.06,
    0.06, 0.06, 0.06, 0.07, 0.07, 0.07, 0.07, 0.07
]

# 3a = media_pm10 sabato
y3a = [
    13.33, 13.42, 13.57, 13.95, 14.04, 13.68, 13.58, 12.38,
    11.88, 11.88, 11.85, 11.59, 11.31, 11.07, 10.60, 10.19,
    9.88, 9.98, 10.20, 10.96, 11.46, 11.81, 12.45, 13.03
]
# 3a_error = err_pm10 sabato
y3a_error = [
    0.22, 0.23, 0.23, 0.24, 0.24, 0.23, 0.22, 0.18,
    0.16, 0.16, 0.17, 0.17, 0.16, 0.17, 0.15, 0.14,
    0.14, 0.14, 0.15, 0.17, 0.18, 0.19, 0.19, 0.21
]

# 3b = media_pm10 domenica
y3b = [
    13.50, 14.05, 14.41, 14.31, 14.01, 13.74, 13.52, 12.29,
    11.74, 11.55, 11.54, 11.39, 10.96, 10.37, 9.86, 9.53,
    9.38, 9.48, 9.70, 10.72, 11.33, 11.55, 12.15, 12.49
]
# 3b_error = err_pm10 domenica
y3b_error = [
    0.22, 0.25, 0.27, 0.27, 0.26, 0.25, 0.24, 0.19,
    0.16, 0.16, 0.16, 0.17, 0.16, 0.14, 0.12, 0.12,
    0.12, 0.12, 0.12, 0.16, 0.17, 0.18, 0.19, 0.20
]

# 4a = media_pm25 sabato
y4a = [
    12.24, 12.34, 12.48, 12.83, 12.91, 12.57, 12.47, 11.32,
    10.84, 10.84, 10.80, 10.55, 10.27, 10.03, 9.56, 9.17,
    8.85, 8.95, 9.16, 9.92, 10.42, 10.77, 11.39, 11.95
]
# 4a_error = err_pm25 sabato
y4a_error = [
    0.21, 0.22, 0.22, 0.23, 0.23, 0.22, 0.21, 0.18,
    0.16, 0.16, 0.16, 0.16, 0.16, 0.17, 0.15, 0.14,
    0.14, 0.14, 0.14, 0.17, 0.18, 0.18, 0.19, 0.20
]

# 4b = media_pm25 domenica
y4b = [
    12.41, 12.95, 13.29, 13.18, 12.91, 12.63, 12.42, 11.22,
    10.69, 10.51, 10.50, 10.34, 9.92, 9.35, 8.84, 8.51,
    8.36, 8.47, 8.69, 9.68, 10.28, 10.49, 11.08, 11.42
]
# 4b_error = err_pm25 domenica
y4b_error = [
    0.22, 0.25, 0.26, 0.27, 0.25, 0.24, 0.23, 0.18,
    0.16, 0.15, 0.16, 0.16, 0.15, 0.14, 0.12, 0.12,
    0.12, 0.12, 0.12, 0.15, 0.17, 0.17, 0.19, 0.20
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
plt.savefig("Grafici/quattro_graficiD.png")
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
plt.savefig("Grafici/co2_separatoD.png")
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
plt.savefig("Grafici/temperatura_separatoD.png")
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
plt.savefig("Grafici/pm10_separatoD.png")
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
plt.savefig("Grafici/pm25_separatoD.png")
plt.show()