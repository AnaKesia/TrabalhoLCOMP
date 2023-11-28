#Todo esse código é um teste da primeira restrição
from pysat.solvers import Glucose3

# Número de cursos e slots
k = 4  #Cursos
m = 2  #Slots

# Criar solver
solver = Glucose3()

# Restrição 1: Cada minicurso deve ser ofertado em pelo menos um slot. Teste
for c in range(1, k + 1):
    clause = [c * m + s for s in range(1, m + 1)]
    solver.add_clause(clause)


result = solver.solve()

if result == True:
    print("Solução encontrada:")
    modelo = solver.get_model()

    # Interpretar o modelo
    agenda = {i: [] for i in range(1, m + 1)}
    for literal in modelo:
        if literal > 0:
            cursos, slot = divmod(literal - 1, m)  # Ajustar index
            agenda[slot + 1].append(cursos)

    # Imprimir o horário
    for slot, cursos in agenda.items():
        print(f"Slot {slot}: {cursos}")
else:
    print("Nenhuma solução encontrada.")