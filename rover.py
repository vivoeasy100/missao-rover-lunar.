# missao-rover-lunar
# Garantia da Qualidade de Software
# Gestão e Qualidade de Software

def inicializar_sistemas():
    print("===================================")
    print("   MISSÃO ROVER LUNAR")
    print("===================================")
    print("Inicializando sistemas do Rover...")

    sistemas = [
        "Sistema de energia",
        "Sistema de comunicação",
        "Sistema de navegação",
        "Sensores",
        "Controle de movimento"
    ]

    for sistema in sistemas:
        print(f"[OK] {sistema} inicializado.")

    print("-----------------------------------")
    print("Todos os sistemas foram inicializados.")
    print("Rover pronto para a missão!")
    print("===================================")


if __name__ == "__main__":
    inicializar_sistemas()
