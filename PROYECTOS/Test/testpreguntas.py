import tkinter as tk
import random

class TestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Test de Conocimientos")
        self.root.geometry("800x600")
        self.root.configure(bg="lightblue")

        self.puntaje = 0
        self.pregunta_actual = 0
        self.preguntas = [] 

        self.boton_reiniciar = tk.Button(root, text="Volver a Empezar", font=("Arial", 22), command=self.reiniciar_test, bg="lightblue")
        self.boton_reiniciar.pack(pady=10)
        self.boton_reiniciar.pack_forget()

        self.label_pregunta = None
        self.botones_respuesta = []

        self.inicializar_preguntas()
        self.mostrar_siguiente_pregunta()

    def inicializar_preguntas(self):
        self.preguntas = [
            {
                'pregunta': '¿Pregunta 1? \n\n A) Respuesta \nB) Respuesta\nC) Respuesta',
                'respuestas': ['A', 'B', 'C'],
                'respuesta_correcta': 'A'
            },
            {
                'pregunta': '¿Pregunta 2? \n\n A) Respuesta \nB) Respuesta\nC) Respuesta',
                'respuestas': ['A', 'B', 'C'],
                'respuesta_correcta': 'A'
            },
             {
                'pregunta': '¿Pregunta 3? \n\n A) Respuesta \nB) Respuesta\nC) Respuesta',
                'respuestas': ['A', 'B', 'C'],
                'respuesta_correcta': 'A'
            },
             {
                'pregunta': '¿Pregunta 4? \n\n A) Respuesta \nB) Respuesta\nC) Respuesta',
                'respuestas': ['A', 'B', 'C'],
                'respuesta_correcta': 'A'
            }
            # Pueden agregarse más preguntas aquí

  
        ]
        random.shuffle(self.preguntas)  # Mezcla las preguntas en un orden aleatorio

    '''Si se quisiera cargar las preguntas desde un archivo JSON, lo primero sería definir la estructura de datos de ese fichero: 
    
    [
    {
        "pregunta": "¿Cuál es la capital de Francia?",
        "respuestas": ["A", "B", "C"],
        "respuesta_correcta": "A"
    },
    {
        "pregunta": "¿De qué color se ve el cielo?",
        "respuestas": ["A", "B", "C"],
        "respuesta_correcta": "A"
    },
    // Agrega más preguntas aquí
    ]
    
    Una vez definida la estructura de datos del .json, lo siguiente es llamarlo desde el programa:

    def cargar_preguntas_desde_json(self):
        # Abre el archivo JSON y carga las preguntas en la lista preguntas
        with open("preguntas.json", "r") as archivo_json:
            self.preguntas = json.load(archivo_json)
        random.shuffle(self.preguntas)  # Mezcla las preguntas en un orden aleatorio
    '''

    def reiniciar_test(self):
        self.puntaje = 0
        self.pregunta_actual = 0
        self.inicializar_preguntas()
        self.mostrar_siguiente_pregunta()
        self.boton_reiniciar.pack_forget()

    def mostrar_siguiente_pregunta(self):
        if self.pregunta_actual < len(self.preguntas):
            pregunta = self.preguntas[self.pregunta_actual]
            if self.label_pregunta:
                self.label_pregunta.destroy()
            # Usa una fuente en negrita para mostrar el texto en negrita
            self.label_pregunta = tk.Label(self.root, text=pregunta['pregunta'], font=("Arial", 22, "bold"), bg="lightblue")
            self.label_pregunta.pack(pady=100)
            
            for boton in self.botones_respuesta:
                boton.destroy()
            self.botones_respuesta = []
            for i in range(3):
                boton = tk.Button(self.root, text=pregunta['respuestas'][i], font=("Arial", 18 , "bold"), command=lambda i=i: self.verificar_respuesta(i), bg="white")
                boton.pack(side=tk.LEFT, padx=110)
                self.botones_respuesta.append(boton)
        else:
            self.mostrar_resultado()

    def verificar_respuesta(self, opcion):
        pregunta = self.preguntas[self.pregunta_actual]
        if pregunta['respuestas'][opcion] == pregunta['respuesta_correcta']:
            self.puntaje += 1
        self.pregunta_actual += 1
        self.mostrar_siguiente_pregunta()

    def mostrar_resultado(self):
        if self.label_pregunta:
            self.label_pregunta.destroy()
        for boton in self.botones_respuesta:
            boton.destroy()
        resultado_texto = f"Resultado: {self.puntaje} aciertos de {len(self.preguntas)}"
        self.label_pregunta = tk.Label(self.root, text=resultado_texto, font=("Arial", 22), bg="lightblue")
        self.label_pregunta.pack(pady=20)
        self.boton_reiniciar.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = TestApp(root)
    root.mainloop()
