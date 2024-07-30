
import tkinter as tk
from model.model_traffic import TrafficLight
from service.service_traffic import TrafficService

class TrafficApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Semáforo Cruzamento")
        
        self.canvas = tk.Canvas(root, width=400, height=300)
        self.canvas.pack()
        
        self.traffic_light1 = TrafficLight(self.canvas, 50, 50)
        self.traffic_light2 = TrafficLight(self.canvas, 250, 50)
        
        self.service = TrafficService(self.traffic_light1, self.traffic_light2)
        
        self.start_button = tk.Button(root, text="Iniciar", command=self.start)
        self.start_button.pack(side=tk.LEFT)
        
        self.stop_button = tk.Button(root, text="Parar", command=self.stop)
        self.stop_button.pack(side=tk.RIGHT)
        
    def start(self):
        self.service.start()

    def stop(self):
        self.service.stop()

def main():
    root = tk.Tk()
    app = TrafficApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
