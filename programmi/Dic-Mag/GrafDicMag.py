import matplotlib.pyplot as plt
import os

# Dati originali
x1 = [8,9,10,11,12,14,15,16,17,18]

y1 = [614,1326,1869,2033,2015,1517,1470,1491,1341,1136]
y1_error = [25,29,27,19,23,35,29,32,43,65]
y2 = [594.7,695.2,873.6,944.6,1024.7,827.5,930.8,1183.5,1208.6,828.9]
y2_error = [63.0,17.6,25.7,24.4,23.9,24.8,29.4,43.3,60.0,16.7]

# Nuovi dati per il secondo grafico (esempio)
y3 = [20.3,21.1,22.4,22.8,23.1,22.5,22.7,23.2,23.1,22.6]
y3_error = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
y4 = [21.93,21.66,22.08,22.21,22.44,22.40,22.60,23.02,23.00,22.72]
y4_error = [0.09,0.05,0.05,0.04,0.04,0.04,0.05,0.06,0.07,0.04]
# Prepara cartella per salvataggio
os.makedirs("Grafici", exist_ok=True)

# Crea due subplot verticali (2 righe, 1 colonna)
fig, axs = plt.subplots(2, 1, figsize=(8, 10), sharex=True)

# Primo grafico (Dicembre vs Maggio)
axs[0].errorbar(x1, y1, yerr=y1_error, label='Dicembre', color='blue', marker='o', linestyle='none', capsize=5)
axs[0].errorbar(x1, y2, yerr=y2_error, label='Maggio', color='red', marker='x', linestyle='none', capsize=5)
axs[0].set_ylabel('Valori di CO₂ (ppm)')
axs[0].set_title('Concentrazione di CO₂: Dicembre vs Maggio')
axs[0].legend()
axs[0].grid(True)

# Secondo grafico (nuovi dati)
axs[1].errorbar(x1, y3, yerr=y3_error, label='Dicembre', color='blue', marker='o', linestyle='none', capsize=5)
axs[1].errorbar(x1, y4, yerr=y4_error, label='Maggio', color='red', marker='x', linestyle='none', capsize=5)
axs[1].set_xlabel('Ora')
axs[1].set_ylabel('Valori di temperature (°C)')
axs[1].set_title('Valori di tamperatura: Dicembre vs Maggio')
axs[1].legend()
axs[1].grid(True)

# Etichette asse x solo sotto il secondo grafico
axs[1].set_xticks(x1)

plt.tight_layout()

# Salvataggio
plt.savefig("Grafici/graficoDueSerie.png")
plt.show()
