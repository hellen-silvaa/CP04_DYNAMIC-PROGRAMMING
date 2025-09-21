def vence_com_dicionario(n: int, memo: dict = None) -> bool:
    """Determina se existe uma estratégia vencedora a partir de um estado com 'n' pedras.

    Esta função utiliza programação dinâmica top-down (memoização) para resolver
    o Jogo das Pedras. Ela evita recalcular os resultados para um mesmo número 
    de pedras, armazenando-os em um dicionário (cache).

    Args:
        n: O número atual de pedras no monte.
        memo: Dicionário usado como cache para a memoização. Deve ser omitido 
              na chamada inicial da função.

    Returns:
        True se o jogador da vez puder forçar uma vitória, False caso contrário.
    """
    # Inicializa o cache na primeira chamada (quando memo é None).
    if memo is None:
        memo = {}

    # Retorna o resultado do cache se este subproblema já foi resolvido.
    if n in memo:
        return memo[n]

    # Caso base: um jogador que não pode mover (n <= 0) perde.
    if n <= 0:
        resultado = False
    else:
        # A posição é vencedora se *qualquer* um dos nossos movimentos possíveis
        # levar a uma posição perdedora para o oponente.
        # A expressão `any(...)` verifica exatamente isso de forma concisa.
        pode_forcar_derrota = any(
            not vence_com_dicionario(n - jogada, memo) for jogada in [1, 2, 3]
        )
        resultado = pode_forcar_derrota

    # Armazena o resultado calculado no cache antes de retorná-lo.
    memo[n] = resultado
    return resultado

# --- Testes para a função profissional ---
print("--- Testando a Função com Memoização (Dicionário - Profissional) ---")
print(f"Com 4 pedras, o jogador da vez vence? {vence_com_dicionario(4)}")      # Esperado: False
print(f"Com 5 pedras, o jogador da vez vence? {vence_com_dicionario(5)}")      # Esperado: True
print(f"Com 12 pedras, o jogador da vez vence? {vence_com_dicionario(12)}")    # Esperado: False
