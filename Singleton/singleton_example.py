class Singleton:
    """Classe Singleton que garante uma única instância."""
    _instance = None  # Armazena a única instância da classe

    def __new__(cls, *args, **kwargs):
        """Controla a criação da instância."""
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, value):
        """Inicializa a instância com um valor."""
        self.value = value


# Testando o padrão Singleton
if __name__ == "__main__":
    s1 = Singleton("Primeira Instância")
    print(f"s1.value: {s1.value}")  # Saída: Primeira Instância

    s2 = Singleton("Segunda Instância")
    print(f"s2.value: {s2.value}")  # Saída: Primeira Instância (não é recriado)

    # Verificando se ambas as variáveis apontam para o mesmo objeto
    print(f"s1 é s2? {s1 is s2}")  # Saída: True

