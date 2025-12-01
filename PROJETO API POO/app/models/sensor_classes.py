

class DispositivoMonitoramento():

    def analisar_dado(self, valor):
        pass


class Sensor(DispositivoMonitoramento):

    def __init__(self, tipo, local):
        self.tipo = tipo
        self.local = local

    def analisar_dado(self, valor):
        return "Sem análise específica."


class SensorTemperatura(Sensor):

    def analisar_dado(self, valor):
        if valor < 10:
            return "temperatura muito baixa"
        elif valor < 18:
            return "temperatura baixa"
        elif valor <= 24:
            return "Temperatura neutra"
        elif valor <= 30:
            return "Temperatura alta"
        return "Temperatura muito alta"

class SensorUmidade(Sensor):

    def analisar_dado(self, valor):
        if valor < 20:
            return "Umidade muito baixa"
        elif valor < 30:
            return "Umidade baixa"
        elif valor <= 50:
            return "Umidade ideal"
        elif valor <= 70:
            return "Umidade alta"
        return "Umidade muito alta."


class SensorQualidadeAr(Sensor):

    def analisar_dado(self, valor):
        if valor <= 50:
            return "Qualidade do ar EXCELENTE"
        elif valor <= 100:
            return "Qualidade do ar BOA"
        elif valor <= 150:
            return "Qualidade do ar MODERADA"
        return "Qualidade do ar RUIM"
