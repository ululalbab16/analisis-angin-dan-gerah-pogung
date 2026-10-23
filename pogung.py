import numpy as np
import matplotlib.pyplot as plt


angin = [2, 2, 1, 0, 2, 2, 3, 4, 2, 3, 1, 1, 3, 3, 3, 1, 1, 2, 3, 3]
gerah = [2, 2, 4, 5, 3, 2, 2, 1, 1, 2, 3, 4, 1, 2, 1, 1, 1, 2, 1, 1]

corr_ag = np.corrcoef(angin, gerah)[0, 1]
m, b = np.polyfit(angin, gerah, 1)

mean_a, std_a = np.mean(angin), np.std(angin, ddof=1)
mean_g, std_g = np.mean(gerah), np.std(gerah, ddof=1)


xs = np.linspace(0, 4, 100)
plt.figure()
plt.scatter(angin, gerah, s=90, label='Data Riil')
plt.plot(xs, m*xs + b, '--', color='red', label=f'Tren: y={m:.2f}x+{b:.2f} | r={corr_ag:.2f}')

plt.grid(True, alpha=0.3)
plt.xlabel('Angin (0-4)')
plt.ylabel('Gerah (1-5)')
plt.title('Angin vs Gerah Pogung | Analisis Lengkap')
plt.figtext(0.02, 0.02, f'Mean Angin {mean_a:.2f}±{std_a:.2f} | Mean Gerah {mean_g:.2f}±{std_g:.2f}', fontsize=8)
plt.legend()
plt.savefig("pogung_final.png", dpi=300)
plt.show()

print(f"Mean Angin: {mean_a:.2f} ± {std_a:.2f}")
print(f"Mean Gerah: {mean_g:.2f} ± {std_g:.2f}")
