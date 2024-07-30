
class TrafficLight:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.green_light = canvas.create_oval(x+5, y+5, x+45, y+45, fill="black")
        self.yellow_light = canvas.create_oval(x+5, y+55, x+45, y+95, fill="black")
        self.red_light = canvas.create_oval(x+5, y+105, x+45, y+145, fill="black")

    def set_state(self, state):
        if state == "green":
            self.canvas.itemconfig(self.green_light, fill="green")
            self.canvas.itemconfig(self.yellow_light, fill="black")
            self.canvas.itemconfig(self.red_light, fill="black")
        elif state == "yellow":
            self.canvas.itemconfig(self.green_light, fill="black")
            self.canvas.itemconfig(self.yellow_light, fill="yellow")
            self.canvas.itemconfig(self.red_light, fill="black")
        elif state == "red":
            self.canvas.itemconfig(self.green_light, fill="black")
            self.canvas.itemconfig(self.yellow_light, fill="black")
            self.canvas.itemconfig(self.red_light, fill="red")
        elif state == "off":
            self.canvas.itemconfig(self.green_light, fill="black")
            self.canvas.itemconfig(self.yellow_light, fill="black")
            self.canvas.itemconfig(self.red_light, fill="black")
