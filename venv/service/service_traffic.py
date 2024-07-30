
from model.model_traffic import TrafficLight

class TrafficService:
    def __init__(self, traffic_light1: TrafficLight, traffic_light2: TrafficLight):
        self.traffic_light1 = traffic_light1
        self.traffic_light2 = traffic_light2
        self.run = False
        self.after_id = None

    def start(self):
        self.run = True
        self.current_step = 0
        self.schedule_next()

    def stop(self):
        self.run = False
        if self.after_id is not None:
            self.traffic_light1.canvas.after_cancel(self.after_id)
        self.traffic_light1.set_state("off")
        self.traffic_light2.set_state("off")

    def schedule_next(self):
        if not self.run:
            return

        steps = [
            ("green", "red", 5000),   # S1 Verde, S2 Vermelho por 4 segundos
            ("yellow", "red", 3000),  # S1 Amarelo, S2 Vermelho por 1 segundo
            ("red", "green", 5000),   # S1 Vermelho, S2 Verde por 4 segundos
            ("red", "yellow", 3000)   # S1 Vermelho, S2 Amarelo por 1 segundo
        ]
        
        state1, state2, delay = steps[self.current_step]
        self.traffic_light1.set_state(state1)
        self.traffic_light2.set_state(state2)
        self.current_step = (self.current_step + 1) % len(steps)

        self.after_id = self.traffic_light1.canvas.after(delay, self.schedule_next)
