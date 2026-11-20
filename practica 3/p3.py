# Práctica 3: Programación Dinámica - Algoritmos Recursivos - Monte Carlo
# Algoritmia y Estructuras de Datos Avanzadas - Curso 2026-2027

import math
import random

# =============================================================================
# I. Alineamiento de Proteínas
# =============================================================================

# I.A Alineamiento Global: Needleman-Wunsch

def needleman_wunsch_matrix(seq1: str, seq2: str, match: int = 2, mismatch: int = -1, gap: int = -1) -> list[list[int]]:
    columnas = len(seq1 + 1)
    filas = len(seq2) + 1
    matriz = [[0 for _ in range(columnas)] for _ in range(filas)]

    for i in range(filas):
        matriz[i][0] = i * gap

    for j in range(columnas):
        matriz[0][j] = j * gap


    for i in range(1, filas):
        for j in range(1, columnas):

            if seq2[i-1] == seq1[j-1]:
                score = match
            else:
                score = mismatch

            diagonal = matriz[i-1][j-1] + score

            arriba = matriz[i-1][j] + gap
            izquierda = matriz[i][j-1] + gap

            matriz[i][j] = max(diagonal, arriba, izquierda)
    return matriz

def needleman_wunsch_backtracking(matrix: list[list[int]], seq1: str, seq2: str, match: int = 2, mismatch: int = -1, gap: int = -1) -> tuple[str, str, int]:
    """"
    Reconstruye las secuencias alineadas globalmente y calcula el score total a partir 
    de la matriz de programación dinámica de Needleman-Wunsch mediante backtracking.

    El backtracking comienza en la esquina inferior derecha (len(seq2), len(seq1)) y 
    recorre la matriz hasta la esquina superior izquierda (0, 0). 
    En la estructura de la matriz, seq1 se desarrolla en columnas y seq2 en filas.

    :param matrix: Matriz de programación dinámica previamente calculada.
    :param seq1: Primera secuencia original (desarrollada en columnas).
    :param seq2: Segunda secuencia original (desarrollada en filas).
    :param match: Puntuación acordada para una coincidencia.
    :param mismatch: Penalización por diferencia.
    :param gap: Penalización por hueco.
    :return: Tupla con (aligned_seq1, aligned_seq2, total_score).
    """
    i = len(seq2)
    j = len(seq1)
    align1 = ""
    align2 = ""

    while i > 0 or j > 0:
        if i > 0 and j > 0:
            if seq2[i-1] == seq1[j-1]:
                score = match
            else:
                score = mismatch
        else:
            score = 0
        if i > 0 and j > 0 and matrix[i][j] == matrix[i-1][j-1] + score:
            align1 += seq1
            align2 += seq2
            i -= 1
            j -= 1
        elif i > 0 and  matrix[i][j] == matrix[i-1][j] + gap:
            align1 += "-"
            align2 += seq2[i-1]
            i -= 1
        elif j > 0 and matrix[i][j] == matrix[i][j-1] + gap:
            align1 += seq1[j-1]
            align2 += "-"
            j -= 1
    #invertir cadenas de texto
    align1 = align1[::-1]
    align2 = align2[::-1]

    total_score = matrix[-1][-1]
    #return tupla
    return (align1, align2, total_score)

    pass

# I.B Alineamiento Local: Smith-Waterman

def smith_waterman_matrix(seq1: str, seq2: str, match: int = 2, mismatch: int = -1, gap: int = -1) -> list[list[int]]:
    """
    Construye y devuelve la matriz de programación dinámica para el alineamiento 
    local de dos secuencias mediante el algoritmo Smith-Waterman.

    Aplica inicialización a ceros en los bordes (primera fila y primera columna) 
    y truncamiento a cero en cada celda para evitar valores negativos. 
    La matriz tiene dimensiones (len(seq2) + 1) x (len(seq1) + 1), donde seq1 se 
    desarrolla a lo largo de las columnas y seq2 a lo largo de las filas.

    :param seq1: Primera secuencia a alinear (desarrollada en columnas).
    :param seq2: Segunda secuencia a alinear (desarrollada en filas).
    :param match: Puntuación por coincidencia.
    :param mismatch: Penalización por diferencia.
    :param gap: Penalización por hueco.
    :return: Matriz de programación dinámica local (lista de listas de enteros).
    """
    pass

def smith_waterman_backtracking(matrix: list[list[int]], seq1: str, seq2: str, match: int = 2, mismatch: int = -1, gap: int = -1) -> tuple[str, str, int]:
    """
    Reconstruye el alineamiento local óptimo y su puntuación a partir de la matriz 
    de Smith-Waterman mediante backtracking.

    Localiza el valor máximo global en la matriz y realiza el backtracking hasta 
    alcanzar una celda con valor 0. En la matriz, seq1 se desarrolla en columnas 
    y seq2 en filas.

    :param matrix: Matriz de programación dinámica local previamente calculada.
    :param seq1: Primera secuencia original (desarrollada en columnas).
    :param seq2: Segunda secuencia original (desarrollada en filas).
    :param match: Puntuación por coincidencia.
    :param mismatch: Penalización por diferencia.
    :param gap: Penalización por hueco.
    :return: Tupla con (sub_seq1, sub_seq2, max_score).
    """
    pass

# =============================================================================
# II. Optimización de Rutas en una Cuadrícula
# =============================================================================

# II.A Recursividad Ingenua (Enfoque de Fuerza Bruta)

def min_path_recursive(grid: list[list[int]], i: int, j: int) -> int:
    """
    Calcula el coste mínimo para alcanzar la celda (i, j) desde el origen (0, 0) 
    utilizando una estrategia recursiva pura (fuerza bruta sin memoización).

    :param grid: Matriz rectangular de costes numéricos enteros.
    :param i: Índice de la fila de la celda destino.
    :param j: Índice de la columna de la celda destino.
    :return: Coste acumulado mínimo para llegar a la celda (i, j).
    """
    if i == 0 and j == 0:
        return grid[0][0]

    if i == 0:
        return grid[i][j] + min_path_recursive(grid, i, j-1)

    if j == 0:
        return grid[i][j] + min_path_recursive(grid, i-1, j)

    coste_arriba = min_path_recursive(grid, i - 1, j)
    coste_izquierda= min_path_recursive(grid, i, j-1)

    return grid[0][0] + min(coste_arriba, coste_izquierda)

# II.B Programación Dinámica (Enfoque Bottom-Up)

def min_path_dp(grid: list[list[int]]) -> tuple[int, list[list[int]]]:
    """
    Calcula el coste mínimo para ir desde la celda (0, 0) hasta (N-1, M-1) 
    mediante programación dinámica ascendente (bottom-up).

    :param grid: Matriz de costes de dimensiones N x M.
    :return: Tupla con el coste mínimo global (int) y la matriz dp de costes acumulados.
    """
    n = len(grid)
    m = len(grid[0])
    costes = [[0] * m for _ in range(n)]

    costes[0][0] = grid[0][0]

    #rellenamos la primera fila i = 0
    for j in range(1, m):
        grid[0][j] = costes[0][j-1] + grid[0][j]

    #rellenamos primera columna j = 0
    for i in range(1, n):
        costes[i][0] = costes[i-1][0] + grid[i][0]

    #Rellenamos interior de la tabla
    for i in range(1, n):
        for j in range(1, m):
            costes[i][j] = grid[i][j] + min(costes[i-1][j], costes[i][j-1])

    return (costes[n-1], [m -1], costes)

# II.C Reconstrucción de la Ruta Óptima

def get_optimal_path(grid: list[list[int]]) -> tuple[int, list[tuple[int, int]]]:
    """
    Reconstruye la secuencia exacta de coordenadas (0, 0) ... (N-1, M-1) que forman 
    el camino de coste mínimo en la cuadrícula.

    Invoca internamente a min_path_dp(grid) para generar la matriz de costes acumulados.

    :param grid: Matriz original de costes.
    :return: Tupla con el coste total mínimo y la lista de coordenadas (i, j) de la ruta.
    """
    n = len(grid)
    m = len(grid[0])

    costes_min, coste = min_path_dp(grid)

    path = []
    i, j = n - 1, m - 1

    while i > 0 or j > 0:
        path.append((i, j))
        if i == 0:
            j -= 1
        elif j == 0:
            i -= 0
        elif coste[i-1][j] < coste[i][j-1]:
            i -= 1
        else:
            j -= 1

    path.append((0, 0))
    path.reverse()
    return costes_min, path

# =============================================================================
# III. Simulación de Movimiento y Difusión mediante Caminata Aleatoria (Random Walk)
# =============================================================================

# III.A El comportamiento de una partícula individual

def simulate_single_walk(steps: int) -> tuple[float, float, float]:
    """
    Simula la trayectoria bidimensional de una sola partícula que parte desde el origen (0.0, 0.0) 
    y da un número determinado de pasos en direcciones aleatorias uniformes [0, 2*pi).

    :param steps: Número de pasos a simular.
    :return: Tupla con la posición final (x, y) y la distancia euclidiana final al origen.
    """

    if steps <= 0:
        return (0.0, 0.0, 0.0)
    x, y = 0.0, 0.0
    for i in range(steps): 
        theta = random.uniform(0, 2*math.pi)
        x += math.cos(theta)
        y += math.sin(theta)

    d = math.sqrt(x**2 + y**2)

    return (x, y, d)


# III.B El enfoque de Monte Carlo y la Ley de Difusión

def monte_carlo_diffusion_simulation(num_particles: int, num_steps: int) -> float:
    """
    Aplica el método de Monte Carlo simulando un conjunto masivo de partículas independientes 
    para calcular la Distancia Cuadrática Media (R^2).

    :param num_particles: Número total de partículas independientes a simular.
    :param num_steps: Número de pasos por caminata.
    :return: Valor de la Distancia Cuadrática Media (R^2).
    """
    total_dist = 0.0
    if num_particles <= 0:
        return 0.0
    for i in range(num_particles):
        _, _, d = simulate_single_walk(num_steps)
        total_dist += d**2

    return total_dist/num_particles

# III.C Confinamiento y barreras absorbentes

def simulate_particle_with_barrier(steps: int, max_radius: float) -> bool:
    """
    Simula la caminata paso a paso de una partícula evaluando en cada paso si supera 
    un radio límite (barrera absorbente).

    :param steps: Número máximo de pasos.
    :param max_radius: Radio límite de la barrera desde el origen.
    :return: True si la partícula cruza la barrera en algún paso, False en caso contrario.
    """
    x, y = 0.0, 0.0
    for i in range(steps):
        theta = random.uniform(0, 2*math.pi)
        x += math.cos(theta)
        y += math.sin(theta)
       
        d = math.sqrt(x**2 + y**2)
        if d > max_radius:
            return True

    return False
def calculate_escape_probability(num_particles: int, num_steps: int, max_radius: float) -> float:
    """
    Estima la probabilidad de escape de un conjunto de partículas en presencia 
    de una barrera absorbente mediante el método de Monte Carlo.

    :param num_particles: Número de partículas a simular.
    :param num_steps: Número máximo de pasos por partícula.
    :param max_radius: Radio de la barrera absorbente.
    :return: Probabilidad de escape expresada en el intervalo [0.0, 1.0].
    """
    probabilidad = 0.0
    if num_particles <= 0:
        return 0.0
    for i in range(num_particles):
        if simulate_particle_with_barrier(num_steps, max_radius) == True:
            probabilidad += 1

    return probabilidad/num_particles
