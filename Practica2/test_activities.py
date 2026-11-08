import time
import matplotlib.pyplot as plt
from p2 import generate_activities, activity_selection

n_values = [100, 500, 1000, 5000]
times = []
selected_counts = []
selection_percentages = []

for n in n_values:
    activities = generate_activities(n, seed=42)
    num_rep = 10
    
    start_time = time.perf_counter()
    for _ in range(num_rep):
        selected = activity_selection(activities)
    end_time = time.perf_counter()
    
    avg_time = (end_time - start_time) / num_rep
    times.append(avg_time)
    
    count = len(selected)
    selected_counts.append(count)
    selection_percentages.append((count / n) * 100)

print("Times (s):", times)
print("Selected counts:", selected_counts)
print("Percentages (%):", selection_percentages)

plt.figure()
plt.plot(n_values, times, marker='o', color='b')
plt.title("Tamaño de entrada vs Tiempo de ejecución (Actividades)")
plt.xlabel("Número de actividades (n)")
plt.ylabel("Tiempo medio (segundos)")
plt.grid(True)
plt.savefig("activities_tiempo.png")
plt.close()

plt.figure()
plt.plot(n_values, selected_counts, marker='s', color='g')
plt.title("Tamaño de entrada vs Número de actividades seleccionadas")
plt.xlabel("Número de actividades (n)")
plt.ylabel("Actividades seleccionadas")
plt.grid(True)
plt.savefig("activities_seleccionadas.png")
plt.close()

plt.figure()
plt.plot(n_values, selection_percentages, marker='^', color='r')
plt.title("Tamaño de entrada vs Porcentaje de actividades seleccionadas")
plt.xlabel("Número de actividades (n)")
plt.ylabel("Porcentaje seleccionado (%)")
plt.ylim(0, 105)
plt.grid(True)
plt.savefig("activities_porcentaje.png")
plt.close()