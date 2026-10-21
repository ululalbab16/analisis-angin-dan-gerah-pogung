import numpy as np
import matplotlib.pyplot as plt


angin = [2, 2, 1, 0, 2, 2,3 ,4 ,2,3,1,1,3,3,3,1,1,2,3,3]
gerah = [2,2,4,5,3,2,2,1,1,2,3,4,1,2,1,1,1,2,1,1]



corr = np.corrcoef(angin, gerah)[0, 1]
m, b = np.polyfit(angin, gerah, 1)  


plt.scatter(angin, gerah, color='blue', label='Data Riil')  
plt.plot(angin, [m*x + b for x in angin], '--', color='red', label='Garis Tren') 


plt.grid(True, alpha=0.3)
plt.xlabel('Angin')
plt.ylabel('Gerah')
plt.title(f"data angin dan gerah pogung dengan Korelasi r={corr:.2f}")
plt.legend()


plt.savefig("pogung_final.png", dpi=300)
plt.show()
