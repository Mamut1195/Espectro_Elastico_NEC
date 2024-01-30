def añadir_diagonal(self, ruta):
    # Verifica si la ruta ya termina con una diagonal
    if ruta.endswith('\\') or ruta.endswith('/'):
        return ruta  # La ruta ya tiene una diagonal al final
    else:
        # Añade una diagonal al final de la ruta
        return ruta + '\\'
    
prueba = añadir_diagonal('\Users\joftv\OneDrive\Documentos')

print(prueba)