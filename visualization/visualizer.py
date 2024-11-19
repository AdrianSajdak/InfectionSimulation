# visualization/visualizer.py

import matplotlib.pyplot as plt

class Visualizer:
    def __init__(self, xlim=(0, 100), ylim=(0, 100)):
        plt.ion()
        self.figure, self.ax = plt.subplots()
        self.ax.set_xlim(xlim)
        self.ax.set_ylim(ylim)
        self.scatter = self.ax.scatter([], [])

    def render(self, persons):
        x = [person.position.x for person in persons]
        y = [person.position.y for person in persons]
        colors = [self.get_color(person) for person in persons]
        self.scatter.set_offsets(list(zip(x, y)))
        self.scatter.set_color(colors)
        self.figure.canvas.draw_idle()
        plt.pause(0.001)

    def get_color(self, person):
        state = person.get_state().__class__.__name__
        if state == 'HealthyState':
            return 'green'
        elif state == 'NoSymptomsState':
            return 'orange'
        elif state == 'SymptomsState':
            return 'red'
        elif state == 'ImmuneState':
            return 'blue'
        else:
            return 'gray'
