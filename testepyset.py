from pysat.solvers import Glucose3

# Número de cursos e slots
k = 4
m = 3

# Conjunto P com os pares de cursos com inscrições em comum (exemplo)
pairs_with_common_enrollments = [(1, 2), (2, 3), (2, 4)]

# Criar solver
solver = Glucose3()

# Restrição 1: Cada minicurso deve ser ofertado em pelo menos um slot.
# Restrição 2: Cada minicurso deve ser ofertado em no máximo um slot.
# Restrição 3: Minicursos com inscrições em comum não podem ser ofertados no mesmo slot.