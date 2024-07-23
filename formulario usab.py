


import statistics
from collections import Counter

# Datos proporcionados
datos = [
    # Tus datos previos...
    {
        "id_localidad": 1,
        "id_alojamientos": "",
        "fiestas_patronales": 0,
        "conciertos": 0,
        "playas": 0,
        "gastronomia": 0,
        "enologia": 0,
        "acces_mob_redu": 0,
        "wifi": 0,
        "piscina": 0,
        "vistas": 0,
        "proxm_trans_public": 0,
        "f_crea": 0,
        "f_mod": 0,
        "f_elim": 0
    },
    {
        "id_localidad": 2,
        "id_alojamientos": 2,
        "fiestas_patronales": 0,
        "conciertos": 0,
        "playas": 0,
        "gastronomia": 0,
        "enologia": 0,
        "acces_mob_redu": 0,
        "wifi": 0,
        "piscina": 0,
        "vistas": 0,
        "proxm_trans_public": 0,
        "f_crea": 0,
        "f_mod": 0,
        "f_elim": 0
    },
    {
        "id_localidad": 1,
        "id_alojamientos": 3,
        "fiestas_patronales": 0,
        "conciertos": 0,
        "playas": 0,
        "gastronomia": 0,
        "enologia": 0,
        "acces_mob_redu": 0,
        "wifi": 0,
        "piscina": 0,
        "vistas": 0,
        "proxm_trans_public": 0,
        "f_crea": 0,
        "f_mod": 0,
        "f_elim": 0
    },
    # Continúa con el resto de tus datos...
]

# Diccionario para almacenar los datos de cada alojamiento
datos_por_alojamiento = {}

# Agrupar datos por id_alojamientos
for alojamiento in datos:
    id_alojamientos = alojamiento["id_alojamientos"]
    if id_alojamientos not in datos_por_alojamiento:
        datos_por_alojamiento[id_alojamientos] = {
            "fiestas_patronales": [],
            "conciertos": [],
            "playas": [],
            "gastronomia": [],
            "enologia": [],
            "acces_mob_redu": [],
            "wifi": [],
            "piscina": [],
            "vistas": [],
            "proxm_trans_public": []
        }
    
    for key in datos_por_alojamiento[id_alojamientos].keys():
        datos_por_alojamiento[id_alojamientos][key].append(alojamiento[key])

# Diccionario para almacenar resultados finales por alojamiento
resultados_por_alojamiento = {}

# Función para calcular media, mediana y moda y su suma como 'valor'
def calcular_estadisticas(valores):
    media = sum(valores) / len(valores)
    mediana = statistics.median(valores)
    moda = Counter(valores).most_common(1)[0][0]
    return media, mediana, moda, media + mediana + moda

# Calcular media, mediana y moda para cada atributo por alojamiento
for id_alojamientos, datos in datos_por_alojamiento.items():
    resultados_por_alojamiento[id_alojamientos] = {}
    for key, valores in datos.items():
        media, mediana, moda, valor_suma = calcular_estadisticas(valores)
        resultados_por_alojamiento[id_alojamientos][key] = {
            "media": media,
            "mediana": mediana,
            "moda": moda,
            "valor": valor_suma
        }

# Mostrar resultados
for id_alojamientos, resultados in resultados_por_alojamiento.items():
    print(f"Alojamiento ID: {id_alojamientos}")
    for key, stats in resultados.items():
        print(f"  Usab: {key}")
        print(f"    Media: {stats['media']:.2f}")
        print(f"    Mediana: {stats['mediana']}")
        print(f"    Moda: {stats['moda']}")
        print(f"    Valor: {stats['valor']}")