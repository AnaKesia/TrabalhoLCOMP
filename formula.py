# Trabalho: definição de horários de cursos em um evento
# Objetivo: fazer um programa que diga se é possível agendar os cursos na quantidade de slots disponíveis e, se possível,
# dizer em que horário devem ser alocados.

# Número de cursos: k
# Número de slots de tempo: m; 
# conjunto P: pares de cursos com inscrições em comum.
# Participantes podem se inscrever em mais de um curso, mas não no mesmo 

#Restrições:
#1. Cada minicurso deve ser ofertado em pelo menos um slot.
#2. Cada minicurso deve ser ofertado em no máximo um slot.
#3. Minicursos com inscrições em comum não podem ser ofertados no mesmo slot.

#1. Para a primeira fórmula, usa-se E grande variando de 1 até k para representar os cursos, e
# OU grande variando de de 1 até m para representar os slots.
#2. E grande variando de 1 até k, E grande variando de 1 até s, E grande sendo s diferente de s', temos negação de ¬(Xc,s ∧ Xc,s')
#3.E grande(c1,c2) pertencente ao conjunto P que varia de 1 até m, negação de ¬(Xc,s ∧ Xc2,s)