import matplotlib.pyplot as plt
x=list(range(24))

co2_abs_lun     = [445.4, 444.7, 443.4, 439.4, 439.8, 438.9, 441.0, 450.3, 461.1, 477.5, 483.9, 488.8, 490.9, 482.6, 481.2, 499.3, 507.4, 518.6, 519.9, 505.6, 492.3, 488.0, 480.0, 475.0]
co2_abs_err_lun = [2.6,   2.8,   2.8,   2.9,   2.9,   2.9,   3.0,   2.9,   3.1,   3.8,   5.2,   7.1,   9.7,   9.4,   9.3,   14.6,  16.6,  18.3,  17.7,  13.8,  10.8,  9.1,   7.4,   6.3]

co2_abs_mar     = [467.6, 463.0, 458.4, 447.4, 456.5, 458.1, 462.2, 480.8, 483.7, 492.3, 501.6, 506.5, 521.7, 527.6, 538.5, 539.6, 540.3, 529.8, 523.0, 499.1, 486.7, 476.5, 468.2, 465.0]
co2_abs_err_mar = [7.0,   6.5,   6.0,   4.9,   5.4,   5.0,   4.5,   4.0,   3.9,   4.5,   6.2,   8.5,   13.6,  14.8,  16.3,  16.9,  16.5,  13.6,  11.6,  7.5,   5.6,   4.7,   3.9,   3.2]

co2_abs_mer     = [459.3, 454.7, 449.9, 447.7, 445.7, 445.7, 450.0, 462.1, 472.2, 502.4, 560.3, 599.3, 624.6, 607.4, 598.2, 639.6, 630.8, 605.7, 544.6, 508.4, 489.4, 474.6, 474.4, 469.6]
co2_abs_err_mer = [2.8,   2.1,   1.9,   1.9,   2.0,   2.0,   1.8,   2.1,   2.7,   4.7,   9.8,   13.2,  14.4,  12.9,  12.6,  16.9,  17.2,  13.8,  9.6,   7.0,   5.4,   4.1,   4.0,   3.5]

co2_abs_gio     = [465.7, 460.3, 455.5, 453.6, 449.8, 449.6, 455.0, 467.5, 476.2, 479.0, 476.1, 484.1, 491.3, 488.3, 485.8, 484.0, 488.8, 487.1, 478.4, 464.2, 462.0, 457.4, 452.6, 450.6]
co2_abs_err_gio = [2.6,   2.5,   2.4,   2.5,   2.4,   2.3,   2.6,   2.7,   2.9,   3.2,   3.7,   5.1,   5.4,   4.8,   4.2,   4.6,   5.3,   5.0,   4.2,   2.7,   2.4,   2.4,   2.3,   2.1]

co2_abs_ven     = [459.8, 454.5, 447.5, 445.9, 445.0, 446.0, 449.5, 460.5, 461.6, 499.1, 553.5, 603.8, 614.8, 569.8, 566.1, 572.3, 560.9, 541.4, 541.4, 505.1, 484.1, 473.4, 463.5, 457.1]
co2_abs_err_ven = [2.4,   2.2,   2.2,   2.2,   2.3,   2.5,   2.6,   2.5,   2.6,   5.5,   10.4,  15.7,  17.1,  12.5,  12.1,  12.6,  11.4,  9.9,   9.6,   6.6,   5.2,   4.5,   4.1,   3.6]




plt.figure(figsize=(8, 5))
plt.errorbar(x, co2_abs_lun, yerr=co2_abs_err_lun,
             label='CO₂ lunedì', color='red', marker='o', capsize=4)
plt.errorbar(x, co2_abs_mar, yerr=co2_abs_err_mar,
             label='CO₂ martedì', color='blue', marker='x', linestyle='--', capsize=4)
plt.errorbar(x, co2_abs_mer, yerr=co2_abs_err_mer,
             label='CO₂ mercoledì', color='green', marker='x', linestyle='--', capsize=4)
plt.errorbar(x, co2_abs_gio, yerr=co2_abs_err_gio,
             label='CO₂ giovedì', color='orange', marker='x', linestyle='--', capsize=4)
plt.errorbar(x,co2_abs_ven , yerr=co2_abs_err_ven,
             label='CO₂ venerdì', color='magenta', marker='x', linestyle='--', capsize=4)
plt.title('CO₂ media senza occupazione durante la settimana')
plt.xlabel('Ora')
plt.ylabel('CO₂ [ppm]')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("Grafici/sovrappsenzaco2D.png")
plt.show()