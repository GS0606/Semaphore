# Traffic Light Controller
### Descrição
Este projeto simula o controle de dois semáforos em um cruzamento usando a biblioteca Tkinter para a criação de uma interface gráfica em Python. O ciclo dos semáforos alterna entre verde, amarelo e vermelho de forma automatizada.

### Funcionalidades
Visualização de Semáforos: Exibição gráfica de dois semáforos.
Controle de Estado: Alterna entre os estados verde, amarelo e vermelho.
Cronograma de Ciclo:
Verde / Vermelho: Semáforo 1 verde e Semáforo 2 vermelho por 5 segundos.
Amarelo / Vermelho: Semáforo 1 amarelo e Semáforo 2 vermelho por 3 segundos.
Vermelho / Verde: Semáforo 1 vermelho e Semáforo 2 verde por 5 segundos.
Vermelho / Amarelo: Semáforo 1 vermelho e Semáforo 2 amarelo por 3 segundos.
Controle Manual: Botões para iniciar e parar o ciclo dos semáforos.
### Ferramentas Utilizadas
Python: Linguagem de programação.
Tkinter: Biblioteca para a interface gráfica.
OOP (Programação Orientada a Objetos): Estruturação do código.
### Estrutura do Código
**Arquitetura do Projeto**

```plaintext
TrafficLight_Controller/
│
├── model/
│   └── model_traffic.py         # Definição da classe TrafficLight
│
├── service/
│   └── service_traffic.py       # Definição da classe TrafficService
│
├── main.py                      # Script principal que executa a aplicação
│
└── README.md                    # Documento de descrição do projeto
```

**Arquivos**
***model/model_traffic.py:*** Contém a classe TrafficLight que representa um semáforo e gerencia seus estados.



class TrafficLight:
    def __init__(self, canvas, x, y):
        # Inicializa o semáforo
        self.canvas = canvas
        self.green_light = canvas.create_oval(x+5, y+5, x+45, y+45, fill="black")
        self.yellow_light = canvas.create_oval(x+5, y+55, x+45, y+95, fill="black")
        self.red_light = canvas.create_oval(x+5, y+105, x+45, y+145, fill="black")
    def set_state(self, state):
        # Define o estado das luzes do semáforo
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

***service/service_traffic.py:*** Contém a classe TrafficService que gerencia o ciclo dos semáforos.

from model.model_traffic import TrafficLight

class TrafficService:
    def __init__(self, traffic_light1: TrafficLight, traffic_light2: TrafficLight):
        # Inicializa o serviço de tráfego
        self.traffic_light1 = traffic_light1
        self.traffic_light2 = traffic_light2
        self.run = False
        self.after_id = None

    def start(self):
        # Inicia o ciclo dos semáforos
        self.run = True
        self.current_step = 0
        self.schedule_next()

    def stop(self):
        # Para o ciclo dos semáforos
        self.run = False
        if self.after_id is not None:
            self.traffic_light1.canvas.after_cancel(self.after_id)
        self.traffic_light1.set_state("off")
        self.traffic_light2.set_state("off")

    def schedule_next(self):
        # Agenda o próximo ciclo
        if not self.run:
            return

        steps = [
            ("green", "red", 5000),   # S1 Verde, S2 Vermelho por 5 segundos
            ("yellow", "red", 3000),  # S1 Amarelo, S2 Vermelho por 3 segundos
            ("red", "green", 5000),   # S1 Vermelho, S2 Verde por 5 segundos
            ("red", "yellow", 3000)   # S1 Vermelho, S2 Amarelo por 3 segundos
        ]
        
        state1, state2, delay = steps[self.current_step]
        self.traffic_light1.set_state(state1)
        self.traffic_light2.set_state(state2)
        self.current_step = (self.current_step + 1) % len(steps)

        self.after_id = self.traffic_light1.canvas.after(delay, self.schedule_next)

***main.py:*** Contém o código principal que inicializa e executa a aplicação.

import tkinter as tk
from model.model_traffic import TrafficLight
from service.service_traffic import TrafficService

class TrafficApp:
    def __init__(self, root):
        # Inicializa a aplicação
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
        # Inicia o serviço de tráfego
        self.service.start()

    def stop(self):
        # Para o serviço de tráfego
        self.service.stop()

def main():
    root = tk.Tk()
    app = TrafficApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()



### Como Utilizar o Programa


**Instalação:** Certifique-se de ter o Python instalado. O Tkinter é incluído por padrão na maioria das distribuições Python.

**Executando o Programa:**

Clone ou baixe o repositório.
Navegue até o diretório onde os arquivos estão localizados.
Execute o script principal com o comando:

<<<python main.py>>>

**Interface:**

Iniciar: Clique no botão "Iniciar" para começar o ciclo dos semáforos.
Parar: Clique no botão "Parar" para interromper o ciclo e apagar os semáforos.
