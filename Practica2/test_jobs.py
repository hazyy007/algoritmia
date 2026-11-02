import time
import matplotlib.pyplot as plt
from p2 import generate_jobs, job_scheduling

n_values = [100, 500, 1000, 5000]

times = []
profits = []
selection_percentages = []

for n in n_values:
    jobs = generate_jobs(n, seed=42)
    num_rep = 10
    
    start_time = time.perf_counter()
    for _ in range(num_rep):
        schedule, total_profit = job_scheduling(jobs)
    end_time = time.perf_counter()
    
    avg_time = (end_time - start_time) / num_rep
    times.append(avg_time)
    profits.append(total_profit)
    
    selection_count = sum(1 for task in schedule if task is not None)
    percentage = (selection_count / n) * 100
    selection_percentages.append(percentage)

# Corregido: times en vez de time
print("Times: ", times)
print("Profits: ", profits)
print("Percentages: ", selection_percentages)

# Gráficas:
plt.figure()
plt.plot(n_values, times, marker='o', color='b')
plt.title("Número de tareas vs Tiempo de ejecución")
plt.xlabel("Número de tareas (n)")
plt.ylabel("Tiempo medio (segundos)")
plt.grid(True)
plt.savefig("jobs_tiempo.png")
plt.show()

plt.figure()
plt.plot(n_values, profits, marker='s', color='g')
plt.title("Número de tareas vs Beneficio total")
plt.xlabel("Número de tareas (n)")
plt.ylabel("Beneficio Total")
plt.grid(True)
plt.savefig("jobs_beneficio.png")
plt.show()

plt.figure()
plt.plot(n_values, selection_percentages, marker='^', color='r')
plt.title("Número de tareas vs Porcentaje seleccionado")
plt.xlabel("Número de tareas (n)")
plt.ylabel("Porcentaje de tareas seleccionadas (%)")
plt.ylim(0, 105)
plt.grid(True)
plt.savefig("jobs_porcentaje.png")
plt.show()