from dataclasses import dataclass

@dataclass
class Main:
    thing: int

main = Main('oi')
print(main.thing)