def validar_cpf(cpf: str) -> bool:
    """
    Remove caracteres não numéricos
    """
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Elimina CPFs com todos os dígitos iguais (ex: 11111111111)
    if cpf == cpf[0] * 11:
        return False

    # Cálculo dos dígitos verificadores
    for i in range(9, 11):
        soma = sum(int(cpf[num]) * ((i + 1) - num) for num in range(i))
        digito = (soma * 10) % 11
        if digito == 10:
            digito = 0
        if digito != int(cpf[i]):
            return False

    return True


# Programa principal
cpf_usuario = input("Digite seu CPF (apenas números ou com pontos e traço): ")

if validar_cpf(cpf_usuario):
    print("✅ CPF válido!")
else:
    print("❌ CPF inválido!")
