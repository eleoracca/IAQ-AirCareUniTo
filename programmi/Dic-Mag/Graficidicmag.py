import matplotlib.pyplot as plt
import os

# ORARI
x1 = [9, 10, 11, 12, 14, 15, 16, 17]  # Dicembre
x2 = [9, 10, 11, 12, 14, 15, 16, 17]  # Maggio

# CO2
y1 = [761, 912, 933, 984, 911, 996, 896, 849]            # Dicembre
y1_err = [20, 21, 23, 27, 12, 14, 13, 16]

y2 = [741.7, 929.0, 1004.0, 1083.5, 828.9, 899.3, 795.3, 774.4]  # Maggio
y2_err = [20.0, 25.9, 24.0, 31.2, 14.5, 21.3, 20.4, 20.8]

# Temperatura
y3 = [18.7, 19.1, 19.5, 19.8, 20.1, 20.1, 20.6, 20.7]     # Dicembre
y3_err = [0.2, 0.2, 0.1, 0.1, 0.1, 0.2, 0.1, 0.1]

y4 = [22.02, 22.51, 22.80, 23.03, 23.06, 23.24, 23.16, 23.22]  # Maggio
y4_err = [0.04, 0.04, 0.04, 0.03, 0.03, 0.03, 0.03, 0.03]

# PM10
y5 = [20, 24, 25, 27, 21, 23, 25, 23]                    # Dicembre
y5_err = [1, 1, 1, 2, 1, 1, 3, 2]

y6 = [12.9, 17.8, 19.9, 21.9, 15.9, 16.7, 14.8, 16.2]     # Maggio
y6_err = [0.5, 1.1, 0.9, 2.4, 1.0, 0.7, 0.8, 1.2]

# PM2.5
y7 = [19, 22, 24, 26, 20, 22, 24, 22]                    # Dicembre
y7_err = [1, 1, 1, 2, 0, 1, 3, 2]

y8 = [11.9, 16.6, 18.7, 20.7, 14.8, 15.5, 13.7, 15.1]     # Maggio
y8_err = [0.5, 1.1, 0.9, 2.3, 0.9, 0.7, 0.8, 1.2]

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
    titolo='Aula D-Concentrazione di CO₂: Dicembre vs Maggio',
    nome_file='CO2',
    label1='CO₂ Dicembre',
    label2='CO₂ Maggio'
)

# Temperatura
plot_singolo(
    x1, y3, y3_err, x2, y4, y4_err,
    ylabel='Temperatura (°C)',
    titolo='Aula D-Temperatura: Dicembre vs Maggio',
    nome_file='Temperatura',
    label1='Temperatura Dicembre',
    label2='Temperatura Maggio'
)

# PM10
plot_singolo(
    x1, y5, y5_err, x2, y6, y6_err,
    ylabel='PM10 (µg/m³)',
    titolo='Aula D-PM10: Dicembre vs Maggio',
    nome_file='PM10',
    label1='PM10 Dicembre',
    label2='PM10 Maggio'
)

# PM2.5
plot_singolo(
    x1, y7, y7_err, x2, y8, y8_err,
    ylabel='PM2.5 (µg/m³)',
    titolo='Aula D-PM2.5: Dicembre vs Maggio',
    nome_file='PM2_5',
    label1='PM2.5 Dicembre',
    label2='PM2.5 Maggio'
)
