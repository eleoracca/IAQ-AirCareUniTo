import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2

# imposta lo stile whitegrid
sns.set_theme(style='whitegrid')

import pandas as pd

# Legge i dati dal file con separatore di tabulazione
df = pd.read_csv("scatoc.txt", sep="\t", header=None)

# Estrae le colonne come liste
y1 = df[0].tolist()
y1_error = df[1].tolist()
x1 = df[2].tolist()
x1_error = df[3].tolist()

x1 = np.array(x1) 
y1 = np.array(y1) 
x1_error = np.array(x1_error) 
y1_error = np.array(y1_error) 
# ————————————————————————————————
# 2) Fit lineare via polyfit
# ————————————————————————————————
mask = (~np.isnan(x1) & (x1 != 0) &
        ~np.isnan(y1) & (y1 != 0) &
        ~np.isnan(x1_error) & (x1_error != 0) &
        ~np.isnan(y1_error) & (y1_error != 0))

# 2. Applica la maschera per filtrare i dati:
x1 = x1[mask]
y1 = y1[mask]
x1_error = x1_error[mask]
y1_error = y1_error[mask]

coeffs = np.polyfit(x1, y1, 1)        # [slope, intercept]
slope, intercept = coeffs

# calcolo della retta di fit sugli stessi x
y1_fit = slope * x1 + intercept

# ————————————————————————————————
# 3) Calcolo del χ² e χ² ridotto
# ————————————————————————————————
residuals = y1 - y1_fit
chi2_val  = np.sum((residuals / y1_error)**2)
dof       = len(x1) - 2             # n punti – n parametri (a e b)
chi2_red  = chi2_val / dof
p_value   = 1 - chi2.cdf(chi2_val, dof)

# Stampa risultati di bontà del fit
print(f"Chi²     = {chi2_val:.2f}")
print(f"χ² ridotto = {chi2_red:.2f}  (ν={dof})")
print(f"p-value  = {p_value:.3f}")

# ————————————————————————————————
# 4) Plot con errorbar e retta di fit
# ————————————————————————————————
plt.figure(figsize=(8, 5))

# Serie con barre d'errore (solo marker, nessuna linea)
plt.errorbar(
    x1, y1,
    label='Aule Vuote',
    color='tab:blue', marker='o',
    capsize=4, alpha=0.5,
    linestyle='none'
)

# Traccia la retta di fit
x_fit = np.linspace(x1.min()-0.1, x1.max()+0.1, 200)
y_fit = slope * x_fit + intercept
plt.plot(x_fit, y_fit,
         label=f'Fit lineare\ny = {slope:.1f}x + {intercept:.1f}',
         linewidth=2)

# Etichette e legenda
plt.xlabel('Temperatura (°C)')
plt.ylabel('Concentrazione CO₂ (ppm)')
plt.title('CO₂ vs Temperatura (aule piene) con Fit e χ²')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Salva e mostra
plt.savefig("Grafici/Temp-CO₂_chi2.png", dpi=300)
plt.show()
print("Valori nulli o nan in y1_error:")
print("Zero:", np.any(y1_error == 0))
print("NaN:", np.any(np.isnan(y1_error)))

