
import practica1.p1 as p1

# 1. Duplicados
assert p1.find_duplicates([2, 1, 1, 2, 1]) == [1, 2]
assert p1.find_duplicates([]) == []
assert p1.find_duplicates([1, 2, 3]) == []

# 2. Parejas que suman target
assert p1.has_sum_pair([1, 4, 7], 8) is True
assert p1.has_sum_pair([5], 10) is False
assert p1.has_sum_pair([5, 5], 10) is True
assert p1.has_sum_pair([], 10) is False

# 3. RLE
entrada = ['A', 'A', 'A', 'B', 'B', 'C', 'A']
esperado = [('A', 3), ('B', 2), ('C', 1), ('A', 1)]

assert p1.rle_encode_naive(entrada) == esperado
assert p1.rle_encode_optimized(entrada) == esperado
assert p1.rle_encode_naive([]) == []
assert p1.rle_encode_optimized([]) == []

# 4. Conjuntos disjuntos
cd = p1.init_cd(5)
assert len(cd) == 5
assert all(x == -1 for x in cd)

p1.union(0, 1, cd)
p1.union(1, 2, cd)
assert p1.find(0, cd) == p1.find(2, cd)
assert p1.find(0, cd) != p1.find(3, cd)

# 5. Componentes conexas
assert p1.ccs(3, [(0, 1)]) == {
    0: [0, 1],
    2: [2]
}

print("Todas las pruebas han pasado")
