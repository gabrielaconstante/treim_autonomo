class Train:
    def __init__(self):
        self.position = 0
        self.movements = 0
        self.consecutive_moves = 0
        self.last_direction = None

    def move(self, commands):
        for command in commands:
            if command not in ["ESQUERDA", "DIREITA"]:
                raise ValueError("Comando inválido")
            
            if self.movements >= 50:
                break

            if command == self.last_direction:
                self.consecutive_moves += 1
            else:
                self.consecutive_moves = 1

            if self.consecutive_moves > 20:
                break

            # Executa o movimento
            if command == "ESQUERDA":
                self.position -= 1
            elif command == "DIREITA":
                self.position += 1

            # Atualiza contadores
            self.movements += 1
            self.last_direction = command

        return self.position
