import matplotlib.pyplot as plt
import os

# Dati originali
x1 = [9, 10, 11, 12, 14, 15, 16, 17]
x2 = [9,10,11,12,14,15,16,17]
# CO2
# CO2
y1 = [1197.2, 1622.5, 1701.4, 1847.3, 1369.2, 1318.9, 1306.9, 1194.0]         # Dicembre
y1_err = [25.3, 31.1, 30.8, 32.3, 27.7, 23.0, 26.4, 32.4]

y2 = [695.2, 873.6, 944.6, 1024.7, 827.5, 930.8, 1183.5, 1208.6]              # Maggio
y2_err = [17.6, 25.7, 24.4, 23.9, 24.8, 29.4, 43.3, 60.0]

# Temperatura
y3 = [21.0, 22.0, 22.3, 22.7, 22.3, 22.4, 22.6, 22.6]                         # Dicembre
y3_err = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

y4 = [21.7, 22.1, 22.2, 22.4, 22.4, 22.6, 23.0, 23.0]                         # Maggio
y4_err = [0.1, 0.1, 0.0, 0.0, 0.0, 0.0, 0.1, 0.1]

# PM10
y5 = [15.3, 16.9, 17.4, 17.0, 13.5, 13.0, 14.6, 14.6]                         # Dicembre
y5_err = [0.3, 0.4, 0.4, 0.3, 0.2, 0.2, 0.4, 0.5]

y6 = [12.8, 16.7, 18.9, 17.2, 11.4, 13.0, 11.3, 11.3]                         # Maggio
y6_err = [0.6, 0.8, 0.9, 0.7, 0.3, 0.4, 0.5, 0.5]

# PM2.5
y7 = [14.3, 15.8, 16.3, 16.0, 12.5, 12.0, 13.6, 13.5]                         # Dicembre
y7_err = [0.3, 0.4, 0.3, 0.3, 0.2, 0.2, 0.4, 0.4]

y8 = [11.7, 15.5, 17.6, 16.0, 10.4, 12.0, 10.3, 10.2]                         # Maggio
y8_err = [0.6, 0.8, 0.9, 0.7, 0.3, 0.4, 0.5, 0.5]
# Crea cartella per salvataggio
os.makedirs("Grafici", exist_ok=True)

# Crea quattro subplot verticali
fig, axs = plt.subplots(4, 1, figsize=(8, 16), sharex=True)

# 1) CO2
axs[0].errorbar(x1, y1, yerr=y1_err, label='CO₂ Dicembre', marker='o', linestyle='none', capsize=5)
axs[0].errorbar(x2, y2, yerr=y2_err, label='CO₂ Maggio', marker='x', linestyle='none', capsize=5)
axs[0].set_ylabel('CO₂ (ppm)')
axs[0].set_title('Concentrazione di CO₂: Dicembre vs Maggio')
axs[0].legend()
axs[0].grid(True)

# 2) Temperatura
axs[1].errorbar(x1, y3, yerr=y3_err, label='Temp Dicembre', marker='o', linestyle='none', capsize=5)
axs[1].errorbar(x2, y4, yerr=y4_err, label='Temp Maggio', marker='x', linestyle='none', capsize=5)
axs[1].set_ylabel('Temperatura (°C)')
axs[1].set_title('Temperatura: Dicembre vs Maggio')
axs[1].legend()
axs[1].grid(True)

# 3) PM10
axs[2].errorbar(x1, y5, yerr=y5_err, label='PM10 Dicembre', marker='o', linestyle='none', capsize=5)
axs[2].errorbar(x2, y6, yerr=y6_err, label='PM10 Maggio', marker='x', linestyle='none', capsize=5)
axs[2].set_ylabel('PM10 (µg/m³)')
axs[2].set_title('PM10: Dicembre vs Maggio')
axs[2].legend()
axs[2].grid(True)

# 4) PM2.5
axs[3].errorbar(x1, y7, yerr=y7_err, label='PM2.5 Dicembre', marker='o', linestyle='none', capsize=5)
axs[3].errorbar(x2, y8, yerr=y8_err, label='PM2.5 Maggio', marker='x', linestyle='none', capsize=5)
axs[3].set_xlabel('Ora')
axs[3].set_ylabel('PM2.5 (µg/m³)')
axs[3].set_title('PM2.5: Dicembre vs Maggio')
axs[3].legend()
axs[3].grid(True)

# Imposta ticks asse x solo sull'ultimo subplot
axs[3].set_xticks(x1)

plt.tight_layout()
# Salva figura
plt.savefig("Grafici/quattroSerie.png")
plt.show()


def plot_singolo(x1, y1, y1_err, x2, y2, y2_err, ylabel, titolo, nome_file, label1, label2):
    plt.figure(figsize=(8, 4))
    plt.errorbar(x1, y1, yerr=y1_err, label=label1, marker='o', linestyle='none', capsize=5)
    plt.errorbar(x2, y2, yerr=y2_err, label=label2, marker='x', linestyle='none', capsize=5)
    plt.xlabel('Ora')
    plt.ylabel(ylabel)
    plt.title(titolo)
    plt.xticks(x1)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"Grafici/{nome_file}.png")
    plt.close()

# CO2
plot_singolo(
    x1, y1, y1_err, x2, y2, y2_err,
    ylabel='CO₂ (ppm)',
    titolo='Aula C-Concentrazione di CO₂: Dicembre vs Maggio',
    nome_file='CO2',
    label1='CO₂ Dicembre',
    label2='CO₂ Maggio'
)

# Temperatura
plot_singolo(
    x1, y3, y3_err, x2, y4, y4_err,
    ylabel='Temperatura (°C)',
    titolo='Aula C-Temperatura: Dicembre vs Maggio',
    nome_file='Temperatura',
    label1='Temperatura Dicembre',
    label2='Temperatura Maggio'
)

# PM10
plot_singolo(
    x1, y5, y5_err, x2, y6, y6_err,
    ylabel='PM10 (µg/m³)',
    titolo='Aula C-PM10: Dicembre vs Maggio',
    nome_file='PM10',
    label1='PM10 Dicembre',
    label2='PM10 Maggio'
)

# PM2.5
plot_singolo(
    x1, y7, y7_err, x2, y8, y8_err,
    ylabel='PM2.5 (µg/m³)',
    titolo='Aula C-PM2.5: Dicembre vs Maggio',
    nome_file='PM2_5',
    label1='PM2.5 Dicembre',
    label2='PM2.5 Maggio'
)
