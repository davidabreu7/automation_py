import numpy as np

dados = np.array(
    [
        ['Roberto', 'casado', 'masculino'],
        ['Sheila', 'solteiro', 'feminino'],
        ['Bruno', 'solteiro', 'masculino'],
        ['Rita', 'casado', 'feminino']
    ]
)
# SOLUÇÃO USADO FOR/IF
for line in dados:
    if line[2] == "casado":
        print(line[:2])

# SOLUÇÃO USANDO LIST COMPREHENSION
[print(list(line[:1])) for line in dados if line[1] == "casado"]

# SOLUÇÃO PERFORMÁTICA USANDO NUMPY
dados = dados.T
print(dados[:, dados[1] == "casado"])