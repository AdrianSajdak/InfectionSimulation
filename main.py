from simulation.simulation import Simulation

def main():
    simulation = Simulation()
    # Przypadek 1: brak odporności
    simulation.initialize(immunity_rate=0.0)
    # Przypadek 2: część populacji posiada odporność
    # simulation.initialize(immunity_rate=0.2)
    simulation.run()

if __name__ == '__main__':
    main()