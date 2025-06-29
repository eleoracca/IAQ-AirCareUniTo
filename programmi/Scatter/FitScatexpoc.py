import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2
from scipy.optimize import curve_fit
import pandas as pd

# Imposta lo stile
sns.set_theme(style='whitegrid')

# Legge i dati dal file con separatore di tabulazione
df = pd.read_csv("scatoc.txt", sep="\t", header=None)

# Estrae le colonne come array
y1 = df[0].to_numpy()       # CO₂
y1_error = df[1].to_numpy()
x1 = df[2].to_numpy()       # Temperatura
x1_error = df[3].to_numpy()

# Maschera per filtrare i valori validi
mask = (~np.isnan(x1) & (x1 != 0) &
        ~np.isnan(y1) & (y1 != 0) &
        ~np.isnan(x1_error) & (x1_error != 0) &
        ~np.isnan(y1_error) & (y1_error != 0))

x1 = x1[mask]
y1 = y1[mask]
x1_error = x1_error[mask]
y1_error = y1_error[mask]

# ————————————————————————————————
# Fit esponenziale inverso del logaritmo
# ————————————————————————————————
def exp_fit(T, lambda_, C0):
    return C0 * 2**(T / lambda_)

initial_guess = [3.0, 280.0]
popt, pcov = curve_fit(exp_fit, x1, y1, sigma=y1_error, absolute_sigma=True, p0=initial_guess)
lambda_fit, C0_fit = popt
lambda_err, C0_err = np.sqrt(np.diag(pcov))

# Calcolo del fit sui dati
y1_fit = exp_fit(x1, *popt)

# ————————————————————————————————
# Calcolo del χ² e χ² ridotto
# ————————————————————————————————
residuals = y1 - y1_fit
chi2_val = np.sum((residuals / y1_error)**2)
dof = len(x1) - 2
chi2_red = chi2_val / dof
p_value = 1 - chi2.cdf(chi2_val, dof)

# Stampa risultati del fit
print(f"λ (lambda) = {lambda_fit:.3f} ± {lambda_err:.3f} °C")
print(f"C₀         = {C0_fit:.1f} ± {C0_err:.1f} ppm")
print(f"Chi²       = {chi2_val:.2f}")
print(f"χ² ridotto = {chi2_red:.2f}  (ν={dof})")
print(f"p-value    = {p_value:.3f}")

# ————————————————————————————————
# Plot con errorbar e curva di fit
# ————————————————————————————————
plt.figure(figsize=(8, 5))

# Dati sperimentali
plt.errorbar(
    x1, y1,
    yerr=y1_error, xerr=x1_error,
    label='Dati sperimentali',
    color='tab:blue', marker='o',
    capsize=4, alpha=0.5,
    linestyle='none'
)

# Curva di fit
x_fit = np.linspace(x1.min() - 1, x1.max() + 1, 200)
y_fit = exp_fit(x_fit, *popt)
plt.plot(x_fit, y_fit,
         label=fr'Fit: $CO₂ = {C0_fit:.1f} \cdot 2^{{T / {lambda_fit:.2f}}}$',
         color='tab:red', linewidth=2)

# Etichette
plt.xlabel('Temperatura (°C)')
plt.ylabel('Concentrazione CO₂ (ppm)')
plt.title('CO₂ in funzione della Temperatura (Fit esponenziale)')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Salvataggio e visualizzazione
plt.savefig("Grafici/Temp-CO₂_fitLOG.png", dpi=300)
plt.show()

# Diagnostica su errori
print("Valori nulli o NaN in y1_error:")
print("Zero:", np.any(y1_error == 0))
print("NaN:", np.any(np.isnan(y1_error)))