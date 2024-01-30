import tkinter as tk
from tkinter import ttk

class SpectralResponseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NEC 15 Spectral Response Calculator")

        # Variables para almacenar los parámetros de entrad
        self.site_class_var = tk.StringVar()
        self.magnitude_var = tk.DoubleVar()
        self.distance_var = tk.DoubleVar()

        # Crear widgets
        self.create_widgets()

    def create_widgets(self):
        # Etiquetas y campos de entrada
        ttk.Label(self.root, text="Clase del Sitio:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        site_class_entry = ttk.Entry(self.root, textvariable=self.site_class_var)
        site_class_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Magnitud Sísmica (Mw):").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        magnitude_entry = ttk.Entry(self.root, textvariable=self.magnitude_var)
        magnitude_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Distancia al Epicentro (km):").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        distance_entry = ttk.Entry(self.root, textvariable=self.distance_var)
        distance_entry.grid(row=2, column=1, padx=10, pady=5)

        # Botón para calcular el espectro
        calculate_button = ttk.Button(self.root, text="Calcular Espectro", command=self.calculate_spectrum)
        calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

    def calculate_spectrum(self):
        # Aquí puedes agregar la lógica para calcular el espectro elástico de respuesta según la NEC 15
        # Utiliza los valores almacenados en las variables self.site_class_var, self.magnitude_var y self.distance_var
        # El resultado puede mostrarse en una nueva ventana, en una etiqueta, o en cualquier otro widget que prefieras.

        # Ejemplo de mensaje de salida
        result_message = "El espectro elástico de respuesta se ha calculado. ¡Implementa la lógica real aquí!"
        tk.messagebox.showinfo("Resultado", result_message)

if __name__ == "__main__":
    root = tk.Tk()
    app = SpectralResponseApp(root)
    root.mainloop()
