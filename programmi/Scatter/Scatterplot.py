import seaborn as sns
import matplotlib.pyplot as plt

# imposta lo stile whitegrid
sns.set_theme(style='whitegrid')


# Co2 in funzione della temperatura nel lunedì tipico in aula c, per lezioni e giorni vuoti
x1 = [22.1,22.1,22.0,21.8,22.0,22.0,21.9,22.0,22.0,22.2,22.2,22.3,22.4,22.4,22.5,22.5,22.5,22.6,22.6,22.6,22.6,22.6,22.5,22.5]
x1_error = [0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2]
#x2 = [21.83,21.69,22.32,22.45,22.72,22.55,22.67,22.84,22.72,22.2,19.51]
#x2_error = [0.06,0.06,0.05,0.05,0.05,0.05,0.05,0.05,0.06,0.1,0.01]
y1 = [433,433,432,432,432,434,434,437,442,446,447,446,444,442,440,452,454,447,443,442,442,440,438,436]    # Prima serie
#y2 = [557,885,1104,1146,1204,1082,1115,1102,1058,1075,670]     # Seconda serie
y1_error = [2,2,2,2,2,2,2,2,2,2,2,2,3,2,2,5,6,4,3,3,3,2,2,2]
#y2_error = [33,13,16,15,17,15,13,13,14,29,9]



# Creazione del grafico
plt.figure(figsize=(8, 5))               # Dimensioni del grafico
# Serie 1 con barre d'errore
plt.errorbar(x1, y1,xerr=x1_error  , yerr=y1_error, label='Aule Vuote', color='blue', marker='o',linestyle='none', capsize=4, alpha=0.4)

# Serie 2 con barre d'errore
#plt.errorbar(x2, y2,xerr=x2_error , yerr=y2_error, label='A lezione', color='red', marker='x', linestyle='none', elinewidth=1, capsize=4, alpha=0.4)


# Etichette e titolo
plt.xlabel('Temperatura (°C)')
plt.ylabel('Concentrazione CO₂ (ppm)')
#plt.title('Grafico CO₂ con occupazione in funzione della temperatura')
plt.title('Grafico CO₂ senza occupazione in funzione della temperatura')
plt.legend()                            # Legenda
plt.grid(True)

# Mostra il grafico
plt.savefig("Grafici/Temp-CO₂.png")
plt.show()