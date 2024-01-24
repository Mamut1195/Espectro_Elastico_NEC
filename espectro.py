class EspectroNEC:
    """
    Clase que representa un Espectro de acuerdo a la NEC 2015.

    Attributes:
        n (float): Razón entre la aceleración espectral Sa (T = 0.1 s) y el PGA para el periodo de retorno seleccionado.
        Fa (float): Coeficiente de amplificación de suelo en la zona de periodo cortó. Amplifica las ordenadas del espectro elástico de respuesta de aceleraciones para diseño en roca, considerando los efectos de sitio
        Fd (float): Coeficiente de amplificación de suelo. Amplifica las ordenadas del espectro elástico de respuesta de desplazamientos para diseño en roca, considerando los efectos de sitio
        Fs (float): Coeficiente de amplificación de suelo. Considera el comportamiento no lineal de los suelos, la degradación del periodo del sitio que depende de la intensidad y contenido de frecuencia de la excitación sísmica y los desplazamientos relativos del suelo, para los espectros de aceleraciones y desplazamientos
        Z (float): Aceleración máxima en roca esperada para el sismo de diseño, expresada como fracción de la aceleración de la gravedad g
        r (float): Factor usado en el espectro de diseño elástico, cuyos valores dependen de la ubicación geográfica del proyecto
    """

    # Constructor
    def __init__(self, n: float, Fa: float, Fd: float,
                 Fs: float, Z: float, r: float):
        """
        Constructor de la clase espectro.

        Args:
            n (float): Razón entre la aceleración espectral Sa (T = 0.1 s) y el PGA para el periodo de retorno seleccionado.
            Fa (float): Coeficiente de amplificación de suelo en la zona de periodo cortó. Amplifica las ordenadas del espectro elástico de respuesta de aceleraciones para diseño en roca, considerando los efectos de sitio
            Fd (float): Coeficiente de amplificación de suelo. Amplifica las ordenadas del espectro elástico de respuesta de desplazamientos para diseño en roca, considerando los efectos de sitio
            Fs (float): Coeficiente de amplificación de suelo. Considera el comportamiento no lineal de los suelos, la degradación del periodo del sitio que depende de la intensidad y contenido de frecuencia de la excitación sísmica y los desplazamientos relativos del suelo, para los espectros de aceleraciones y desplazamientos
            Z (float): Aceleración máxima en roca esperada para el sismo de diseño, expresada como fracción de la aceleración de la gravedad g
            r (float): Factor usado en el espectro de diseño elástico, cuyos valores dependen de la ubicación geográfica del proyecto
        """

        self.n = n
        self.Fa = Fa  
        self.Fd = Fd   
        self.Fs = Fs  
        self.Z = Z  
        self.r = r  

    def tc(self):
        """
        Funcion que retorna el periodo límite de vibración en el espectro sísmico elástico de aceleraciones que representa el sismo de diseño.

        Returns :
            float : valor de Tc
        """
        return 0.55 * self.Fa * self.Fd / self.Fa

    # def periodo_fundamental(self, Ct: float, hn: float, alfa: float, Ab: float, nw: int, hwi: float, Awi: float, Iwi: float):

    #     # Coeficiente que depende del tipo de edificacion
    #     # Altura máxima de la edificación de n pisos, medida desde la base de la estructura, en metros.
    #     # Coeficiente para el periodo fundamental, alfa = 1, si posee muros
    #     # Ab Área de la edificación en su base, en metros cuadrados.
    #     # Número de muros de la edificación diseñados para resistir las fuerzas sísmica en la dirección de estudio.
    #     # Altura del muro i medida desde la base, en metro
    #     # Área mínima de cortante de la sección de un muro estructural i,
    #     # medida en un plano horizontal, en el primer nivel de la estructura y en la dirección de estudio, en metros cuadrados.
    #     # Longitud medida horizontalmente, en metros,
    #     # de un muro estructural i en el primer nivel de la estructura y en la dirección de estudio.

    #     # Obtenido mediante el metodo 1
    #     if alfa != 1:
    #         return Ct ** (hn ** alfa)

    #     if self.alfa == 1:
    #         Cw: float
    #         Cw = (100/Ab) * nw * ((hn/hwi)**2) * Awi / (1+0.83 * ((hn/hwi)**2))

    #         Ct = 0.0062 / math.sqrt(Cw)

    #         return Ct ** (hn ** alfa)

    def espectro(self):
        """
        Funcion que retorna el espectro sismico elasttico

        Returns:
            matplotlib.figure.Figure: Objeto de figura de matplotlib.
        """
        
        import matplotlib.pyplot as plt
        import numpy as np
        
        Tc = self.tc()
        x_values_1 = np.linspace(0, Tc, 100)
        meceta = self.n * self.Z * self.Fa
        y_values_1 = np.repeat(meceta, 100)
        x_values_2 = np.linspace(Tc, 2.4, 100)
        y_values_2 = self.n * self.Z * self.Fa *  ((Tc/ x_values_2) ** self.r)

        # Crea el gráfico
        plt.plot(x_values_1, y_values_1)
        plt.plot(x_values_2, y_values_2)

        # Agrega etiquetas y título al gráfico
        plt.xlabel('S(a)g')
        plt.ylabel('T')
        plt.title('Espectro sísmico elástico de aceleraciones')

        # Agrega una leyenda para identificar cada función
        plt.legend()

        # Muestra el gráfico
        return plt.show()
