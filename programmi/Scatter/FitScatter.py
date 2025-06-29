import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.odr import ODR, RealData, Model
from scipy.stats import chi2

# 1) Imposta lo stile
sns.set_theme(style='whitegrid')

# 2) I tuoi dati
x1       = np.array([22.1,22.1,22.0,21.8,22.0,22.0,21.9,22.0,22.0,22.2,22.2,22.3,22.4,22.4,22.5,22.5,22.5,22.6,22.6,22.6,22.6,22.6,22.5,22.5])
x1_error = np.array([0.2]*len(x1))
y1       = np.array([433,433,432,432,432,434,434,437,442,446,447,446,444,442,440,452,454,447,443,442,442,440,438,436])
y1_error = np.array([2,2,2,2,2,2,2,2,2,2,2,2,3,2,2,5,6,4,3,3,3,2,2,2])

# 3) Definisci il modello esponenziale per ODR
def expo_model(B, x):
    A, k = B
    return A * np.exp(k * x)

# 4) Prepara i dati per ODR (considera sia sx che sy)
data = RealData(x1, y1, sx=x1_error, sy=y1_error)
model = Model(expo_model)
odr   = ODR(data, model, beta0=[440, 0.0])  # stima iniziale per [A, k]

# 5) Esegui l’ODR
out   = odr.run()
A_fit, k_fit = out.beta
A_err, k_err = out.sd_beta

# 6) Calcolo di chi² e p-value (rispetto a sy)
y1_fit    = expo_model([A_fit, k_fit], x1)
residuals = y1 - y1_fit
chi2_val  = np.sum((residuals / y1_error)**2)
dof       = len(x1) - len(out.beta)
chi2_red  = chi2_val / dof
p_value   = 1 - chi2.cdf(chi2_val, dof)

# 7) Stampa i risultati
print("Parametri di fit esponenziale:")
print(f"  A = {A_fit:.2f} ± {A_err:.2f}")
print(f"  k = {k_fit:.4f} ± {k_err:.4f}\n")
print("Goodness of fit:")
print(f"  χ²        = {chi2_val:.2f}")
print(f"  χ² ridotto = {chi2_red:.2f}  (ν = {dof})")
print(f"  p-value   = {p_value:.3f}")

# 8) Disegna il grafico
fig, ax = plt.subplots(figsize=(8,5))

# Barre d'errore con marker only
ax.errorbar(
    x1, y1,
    xerr=x1_error, yerr=y1_error,
    fmt='o', capsize=4, alpha=0.6,
    label='Dati sperimentali',
    color='tab:blue',
    linestyle='none'
)

# Curva di fit esponenziale
x_fit = np.linspace(x1.min()-0.1, x1.max()+0.1, 200)
y_fit = expo_model([A_fit, k_fit], x_fit)
ax.plot(
    x_fit, y_fit,
    '-', lw=2,
    label=(f'Fit exp:\n'
           rf'$y={A_fit:.1f}e^{{{k_fit:.3f}x}}$' + '\n'
           rf'$χ^2_{{\rm red}}={chi2_red:.2f}$, $p={p_value:.2f}$')
)

# Formattazione
ax.set_xlabel('Temperatura (°C)', fontsize=12)
ax.set_ylabel('Concentrazione CO₂ (ppm)', fontsize=12)
ax.set_title('Fit esponenziale con errori su X e Y e χ²', fontsize=14)
ax.legend(frameon=True, loc='best')
plt.tight_layout()
plt.show()
