clientes = list()

def salvar(x):
    print("print antes do append",clientes)
    clientes.append(x)
    print(" print depois do append",clientes)
    print("função recebe: ",x)


print("print no final de tudo ",clientes)