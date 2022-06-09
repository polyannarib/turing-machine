import time


class TuringMachine:
    def __init__(self):
        self.states = None
        self.final = None
        self.initial = None
        self.alphabet = None
        self.symbols = None
        self.transitions = {}
        self.tm_file = None

    def open_tm(self, filepath: str):
        self.tm_file = open(filepath, "r")
        if self.tm_file is not None:
            return 0
        return 1

    def set_states(self):
        states = self.tm_file.readline()
        self.states = states.split()

    def set_initial(self):
        self.initial = self.states[0]

    def set_final(self):
        final = self.tm_file.readline()
        self.final = final.split()

    def set_alphabet(self):
        alphabet = self.tm_file.readline()
        self.alphabet = alphabet.split()

    def set_symbols(self):
        symbols = self.tm_file.readline()
        self.symbols = symbols.split()

    def set_transitions(self):
        for line in self.tm_file:
            if line == "\n":
                break
            transition = line.split("=", maxsplit=1)
            self.transitions[tuple(transition[0].split())] = tuple(transition[1].split())

    def process_input(self, input_str: str):
        tape = list(self.symbols[-1] + input_str + self.symbols[-1])
        current_state = self.initial
        direction = "r"
        index = 1
        while True:
            current_tuple = (current_state, tape[index])
            if current_tuple in self.transitions:
                result = self.transitions[current_tuple]
                current_state = result[0]
                tape[index] = result[1]
                direction = result[2]
                if current_state in self.final:
                    path = str(current_tuple) + " -> " + str(result) + " = " + "".join(tape)
                    time.sleep(1)
                    print(path + ", index " + str(index))
                    return "Estado final alcançado, cadeia aceita"
                path = str(current_tuple) + " -> " + str(result) + " = " + "".join(tape)
                time.sleep(1)
                print(path + ", index " + str(index))
                if direction == "r":
                    index = index + 1
                elif direction == "l":
                    index = index - 1
            else:
                return "Cadeia rejeitada"

    def run(self, input_str: str, filepath: str):
        self.open_tm(filepath)
        self.set_states()
        self.set_initial()
        self.set_final()
        self.set_alphabet()
        self.set_symbols()
        self.set_transitions()
        try:
            return self.process_input(input_str)

        except IndexError:
            return "Processamento finalizado"


if __name__ == "__main__":
    tm = TuringMachine()
    w = input("Digite a cadeia: ")
    print(tm.run(w, "tm_teste3.txt"))
