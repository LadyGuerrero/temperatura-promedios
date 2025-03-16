def calcular_temperatura_promedio(temperaturas):
    """
    Calcula la temperatura promedio de cada ciudad basado en datos de temperaturas durante varias semanas.
    """
    promedios = {}

    # Recorremos cada ciudad en el diccionario de temperaturas
    for ciudad, temp_semanales in temperaturas.items():
        # Calculamos el promedio dividiendo la suma de temperaturas entre la cantidad de valores
        promedio = sum(temp_semanales) / len(temp_semanales)
        # Almacenamos el resultado en el diccionario de promedios sin redondear
        promedios[ciudad] = promedio

    return promedios


# Ejemplo de uso:
if __name__ == "__main__":
    # Datos de ejemplo: temperaturas de 3 ciudades durante 4 semanas
    datos_temperaturas = {
        "Quito": [18.5, 19.2, 17.8, 18.9],
        "Guayaquil": [28.7, 29.5, 30.1, 28.9],
        "Cuenca": [17.2, 16.8, 17.5, 16.9]
    }

    # Calculamos las temperaturas promedio usando nuestra función
    temperaturas_promedio = calcular_temperatura_promedio(datos_temperaturas)

    # Mostramos los resultados
    print("Temperaturas promedio por ciudad:")
    for ciudad, promedio in temperaturas_promedio.items():
        print(f"{ciudad}: {promedio}°C")