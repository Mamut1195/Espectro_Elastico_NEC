import espectro as nec

prueba_1 = nec.EspectroNEC(n=2.48, Fa=1.3, Fd=1.5, Fs=1.1, Z=0.25, r=1)

Tc = prueba_1.tc()

prueba_1.espectro()

prueba_1.graficar_espectro()

prueba_1.creacion_de_tuplas()

prueba_1.extraccion_de_puntos(ruta_de_archivo=r'C:\Users\joftv\OneDrive\Documentos')

