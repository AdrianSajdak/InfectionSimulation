from states.istate import IState

class HealthyState(IState):
    def handle(self):
        # Osobnik jest zdrowy; nie musi wykonywać żadnych działań
        pass