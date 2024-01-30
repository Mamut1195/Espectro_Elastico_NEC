import tkinter as tk
from tkinter import ttk, messagebox
import espectro as nec

class EspectroElasticoUI():

    def __init__(self, root):
        self.root = root
        self.root.title("NEC 15 Espectro de respuesta elástico")

        # Variables para almacenar los parámetros de entrada
        self.n_var = tk.DoubleVar()
        self.Fa_var = tk.DoubleVar()
        self.Fd_var = tk.DoubleVar()
        self.Fs_var = tk.DoubleVar()
        self.Z_var = tk.DoubleVar()
        self.r_var = tk.DoubleVar()
        self.ruta_de_archivo = tk.StringVar()
        self.nombre_archivo = tk.StringVar()

    # Crear widgets
        self.create_widgets()

    def create_widgets(self):
        # Etiquetas y campos de entrada
        ttk.Label(self.root, text="n : ").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        n_var_entry = ttk.Entry(self.root, textvariable=self.n_var)
        n_var_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Fa : ").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        Fa_var_entry = ttk.Entry(self.root, textvariable=self.Fa_var)
        Fa_var_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Fd : ").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        Fd_var_entry = ttk.Entry(self.root, textvariable=self.Fd_var)
        Fd_var_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Fs : ").grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        Fs_var_entry = ttk.Entry(self.root, textvariable=self.Fs_var)
        Fs_var_entry.grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Z : ").grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
        Z_var_entry = ttk.Entry(self.root, textvariable=self.Z_var)
        Z_var_entry.grid(row=4, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="r : ").grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
        r_var_entry = ttk.Entry(self.root, textvariable=self.r_var)
        r_var_entry.grid(row=5, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Especifique la ruta del archivo : ").grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)
        ruta_de_archivo_var_entry = ttk.Entry(self.root, textvariable=self.ruta_de_archivo)
        ruta_de_archivo_var_entry.grid(row=6, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Especifique el nombre del archivo : ").grid(row=7, column=0, padx=10, pady=5, sticky=tk.W)
        nombre_archivo_var_entry = ttk.Entry(self.root, textvariable=self.nombre_archivo)
        nombre_archivo_var_entry.grid(row=7, column=1, padx=10, pady=5)


        # Botón para calcular el espectro
        calculate_button = ttk.Button(self.root, text="Calcular Espectro", command=self.calculate_spectrum)
        calculate_button.grid(row=8, column=0, columnspan=2, pady=10)

    def calculate_spectrum(self):
        
        # Aquí puedes agregar la lógica para calcular el espectro elástico de respuesta según la NEC 15
        # Utiliza los valores almacenados en las variables self.site_class_var, self.magnitude_var y self.distance_var
        # El resultado puede mostrarse en una nueva ventana, en una etiqueta, o en cualquier otro widget que prefieras.

        n_value = self.n_var.get()
        Fa_value = self.Fa_var.get()
        Fd_value = self.Fd_var.get()
        Fs_value = self.Fs_var.get()
        Z_value = self.Z_var.get()
        r_value = self.r_var.get()
        
        Espectro_1 = nec.EspectroNEC(n=n_value, Fa=Fa_value, Fd=Fd_value, Fs=Fs_value, Z=Z_value, r=r_value)

        Espectro_1.tc()

        Espectro_1.espectro()

        Espectro_1.graficar_espectro()

        Espectro_1.creacion_de_tuplas()

        Espectro_1.extraccion_de_puntos(nombre_archivo = self.ruta_de_archivo.get() , ruta_de_archivo = self.nombre_archivo.get())

        # Ejemplo de mensaje de salida
        result_message = "El espectro elástico de respuesta se ha calculado."
        tk.messagebox.showinfo("Resultado", result_message)

if __name__ == "__main__":
    root = tk.Tk()
    app = EspectroElasticoUI(root)
    root.mainloop()


