from typing import Tuple

class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        temperatura_total = 0
        humedad_total = 0
        presion_total = 0
        velocidad_viento_total = 0
        direcciones_viento = []

        with open(self.nombre_archivo, 'r') as file:
            for linea in file:
                if linea.startswith("Temperatura:"):
                    temperatura_total += float(linea.split(":")[1])
                elif linea.startswith("Humedad:"):
                    humedad_total += float(linea.split(":")[1])
                elif linea.startswith("Presion:"):
                    presion_total += float(linea.split(":")[1])
                elif linea.startswith("Viento:"):
                    datos_viento = linea.split(":")[1].split(",")
                    velocidad_viento_total += float(datos_viento[0])
                    direcciones_viento.append(datos_viento[1].strip())

        num_registros = len(direcciones_viento)
        temperatura_promedio = temperatura_total / num_registros
        humedad_promedio = humedad_total / num_registros
        presion_promedio = presion_total / num_registros
        velocidad_viento_promedio = velocidad_viento_total / num_registros

        # Calculando dirección predominante del viento
        direccion_grados = {
            "N": 0, "NNE": 22.5, "NE": 45, "ENE": 67.5,
            "E": 90, "ESE": 112.5, "SE": 135, "SSE": 157.5,
            "S": 180, "SSW": 202.5, "SW": 225, "WSW": 247.5,
            "W": 270, "WNW": 292.5, "NW": 315, "NNW": 337.5
        }

        grados_viento_total = sum([direccion_grados[d] for d in direcciones_viento])
        direccion_promedio_grados = grados_viento_total / num_registros

        # Encontrar la dirección más cercana en grados
        direccion_cercana = min(direccion_grados, key=lambda x: abs(direccion_promedio_grados - direccion_grados[x]))

        return temperatura_promedio, humedad_promedio, presion_promedio, velocidad_viento_promedio, direccion_cercana

# Datos de uso:
archivo = "datos_meteorologicos.txt"
datos = DatosMeteorologicos(archivo)
estadisticas = datos.procesar_datos()
print("Temperatura promedio:", estadisticas[0])
print("Humedad promedio:", estadisticas[1])
print("Presión promedio:", estadisticas[2])
print("Velocidad promedio del viento:", estadisticas[3])
print("Dirección predominante del viento:", estadisticas[4])
