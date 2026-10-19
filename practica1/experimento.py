
import practica1.p1 as p1
import matplotlib.pyplot as plt

# Caso favorable: la pareja aparece al principio.
def favorable(n):
    return [1, 9] + [0] * (n - 2)

# Caso desfavorable: no existe ninguna pareja que sume 1.
def desfavorable(n):
    return [0] * n

Nlist = [100, 500, 1000, 2000, 4000, 8000]

# Número de ejecuciones por medición y de mediciones.
Nrep = 100
Nstat = 20

favorables = p1.time_measure(
    lambda x: p1.has_sum_pair(x, 10),
    favorable,
    Nlist,
    Nrep,
    Nstat
)

desfavorables = p1.time_measure(
    lambda x: p1.has_sum_pair(x, 1),
    desfavorable,
    Nlist,
    Nrep,
    Nstat
)

# Extraemos las medias y las varianzas.
medias_f = [media for media, var in favorables]
medias_d = [media for media, var in desfavorables]

# Gráfica de los tiempos medios.
plt.plot(Nlist, medias_f, "o-", label="Favorable")
plt.plot(Nlist, medias_d, "o-", label="Desfavorable")

plt.xlabel("Tamaño de entrada n")
plt.ylabel("Tiempo medio por ejecución (s)")
plt.title("Tiempos de has_sum_pair")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("has_sum_pair.png", dpi=300)
plt.show()

# Mostramos también los resultados numéricos.
for n, f, d in zip(Nlist, favorables, desfavorables):
    print(
        f"n={n}: "
        f"favorable={f[0]:.8e} s, "
        f"varianza={f[1]:.8e}; "
        f"desfavorable={d[0]:.8e} s, "
        f"varianza={d[1]:.8e}"
    )



# ---------------------------------------------
# EXPERIMENTO RLE
# ---------------------------------------------

def pocas_rachas(n):
    # Todos los elementos son iguales.
    return ["A"] * n


def muchas_rachas(n):
    # Los elementos alternan, creando muchas rachas.
    return [
        "A" if i % 2 == 0 else "B"
        for i in range(n)
    ]


Nlist_rle = [100, 250, 500, 1000, 2000]

# Menos repeticiones porque la versión ingenua
# puede tardar bastante con muchas rachas.
Nrep_rle = 3
Nstat_rle = 8

# Cuatro experimentos.
naive_pocas = p1.time_measure(
    p1.rle_encode_naive,
    pocas_rachas,
    Nlist_rle,
    Nrep_rle,
    Nstat_rle
)

optimized_pocas = p1.time_measure(
    p1.rle_encode_optimized,
    pocas_rachas,
    Nlist_rle,
    Nrep_rle,
    Nstat_rle
)

naive_muchas = p1.time_measure(
    p1.rle_encode_naive,
    muchas_rachas,
    Nlist_rle,
    Nrep_rle,
    Nstat_rle
)

optimized_muchas = p1.time_measure(
    p1.rle_encode_optimized,
    muchas_rachas,
    Nlist_rle,
    Nrep_rle,
    Nstat_rle
)

# Convertimos los tiempos a milisegundos.
def a_ms(resultados):
    return [media * 1000 for media, var in resultados]


# Gráfica 1: pocas rachas.
plt.figure()
plt.plot(
    Nlist_rle, a_ms(naive_pocas),
    "o-", label="Naive"
)
plt.plot(
    Nlist_rle, a_ms(optimized_pocas),
    "o-", label="Optimized"
)
plt.xlabel("Tamaño de entrada n")
plt.ylabel("Tiempo medio (ms)")
plt.title("RLE con pocas rachas")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("rle_pocas.png", dpi=300)
plt.show()


# Gráfica 2: muchas rachas.
plt.figure()
plt.plot(
    Nlist_rle, a_ms(naive_muchas),
    "o-", label="Naive"
)
plt.plot(
    Nlist_rle, a_ms(optimized_muchas),
    "o-", label="Optimized"
)
plt.xlabel("Tamaño de entrada n")
plt.ylabel("Tiempo medio (ms)")
plt.title("RLE con muchas rachas")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("rle_muchas.png", dpi=300)
plt.show()


# Resultados numéricos.
print("\nCOMPARACIÓN RLE (milisegundos)")
print(
    "n | Ingenua-pocas | Optimizada-pocas | "
    "Ingenua-muchas | Optimizada-muchas"
)

for i, n in enumerate(Nlist_rle):
    print(
        f"{n} | "
        f"{a_ms(naive_pocas)[i]:.4f} | "
        f"{a_ms(optimized_pocas)[i]:.4f} | "
        f"{a_ms(naive_muchas)[i]:.4f} | "
        f"{a_ms(optimized_muchas)[i]:.4f}"
    )
