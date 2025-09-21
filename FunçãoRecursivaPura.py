
def vence_recursivo(n: int) -> bool:
    """
    Determina se o jogador da vez tem uma estratégia vencedora no Jogo das Pedras
    para um monte com 'n' pedras, usando recursão pura.

    Uma posição é vencedora se existe um movimento que leva a uma posição perdedora
    para o oponente.

    Args:
        n: O número de pedras no monte.

    Returns:
        True se o jogador da vez pode vencer, False caso contrário.
    """
    # Caso base: Se não há pedras, o jogador da vez não pode mover, então perde.
    if n <= 0:
        return False
    
    # Casos base: Se pode pegar todas as pedras (1, 2 ou 3), o jogador vence.
    if n <= 3:
        return True

    # Um jogador vence se puder fazer uma jogada que coloque o oponente
    # em uma posição perdedora.
    # A posição do oponente será perdedora se 'vence' para ele for False.
    # Verificamos se existe algum movimento (retirar 1, 2 ou 3 pedras)
    # tal que o oponente não consiga vencer a partir do estado resultante.
    pode_vencer = not vence_recursivo(n - 1) or \
                   not vence_recursivo(n - 2) or \
                   not vence_recursivo(n - 3)

    return pode_vencer

print("--- Função Recursiva Pura ---")
print(f"Com 4 pedras, o jogador da vez vence? {vence_recursivo(4)}")   # Esperado: False
print(f"Com 5 pedras, o jogador da vez vence? {vence_recursivo(5)}")   # Esperado: True
print(f"Com 12 pedras, o jogador da vez vence? {vence_recursivo(12)}") # Esperado: False
print(f"Com 13 pedras, o jogador da vez vence? {vence_recursivo(13)}") # Esperado: True
