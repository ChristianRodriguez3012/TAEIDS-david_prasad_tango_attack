import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Parámetros de configuración
num_tests = 10000  # Número de pruebas (sesiones)
num_bits_options = [4, 8]  # Número de bits para K1, K2, e ID

# Simulación de valores de K1, K2, e ID
def simular_valores(num_bits):
    return np.random.randint(0, 2, num_bits)

# Función para simular el ataque
def tango_attack(num_tests, num_bits):
    K1_approx = np.zeros(num_bits)
    K2_approx = np.zeros(num_bits)
    ID_approx = np.zeros(num_bits)

    for _ in range(num_tests):
        K1_response = np.random.randint(0, 2, num_bits)
        K2_response = np.random.randint(0, 2, num_bits)
        ID_response = np.random.randint(0, 2, num_bits)

        K1_approx += K1_response
        K2_approx += K2_response
        ID_approx += ID_response

    K1_approx /= num_tests
    K2_approx /= num_tests
    ID_approx /= num_tests

    return K1_approx, K2_approx, ID_approx

# Visualización de los resultados
def plot_results(num_bits, ejecucion_numero, carpeta_resultados):
    K1_real = simular_valores(num_bits)
    K2_real = simular_valores(num_bits)
    ID_real = simular_valores(num_bits)
    
    K1_approx, K2_approx, ID_approx = tango_attack(num_tests, num_bits)

    # Guardar los resultados en un DataFrame
    df = pd.DataFrame({
        'Bits': np.arange(num_bits),
        'K1 Real': K1_real,
        'K1 Aproximado': K1_approx,
        'K2 Real': K2_real,
        'K2 Aproximado': K2_approx,
        'ID Real': ID_real,
        'ID Aproximado': ID_approx
    })

    # Guardar el DataFrame como CSV
    df.to_csv(os.path.join(carpeta_resultados, f'Resultados_{num_bits}_bits.csv'), index=False)

    # Generación del gráfico
    plt.figure(figsize=(12, 6))  # Tamaño del gráfico
    x = np.arange(num_bits)
    width = 0.15

    plt.bar(x - width, K1_real, width, label='K1 Real')
    plt.bar(x, K1_approx, width, label='K1 Aproximado', alpha=0.7)

    plt.bar(x + width, K2_real, width, label='K2 Real', alpha=0.5)
    plt.bar(x + 2 * width, K2_approx, width, label='K2 Aproximado', alpha=0.5)

    plt.bar(x + 3 * width, ID_real, width, label='ID Real', alpha=0.2)
    plt.bar(x + 4 * width, ID_approx, width, label='ID Aproximado', alpha=0.2)

    plt.xlabel('Bits')
    plt.ylabel('Valor')
    plt.title(f'Aproximaciones de K1, K2 e ID en el Tango Attack ({num_bits} bits)')
    plt.xticks(x + 2 * width, range(num_bits))
    plt.legend()
    
    # Guardar gráfico como imagen
    plt.savefig(os.path.join(carpeta_resultados, f'Grafico_{num_bits}_bits.png'), bbox_inches='tight')
    plt.close()

    return df

# Función para crear la tabla comparativa
def crear_tabla_comparativa(df_4bits, df_8bits, carpeta_resultados, ejecucion_numero):
    df_comparativa = pd.DataFrame({
        'Bits': ['4 bits', '8 bits'],
        'K1 Real': [df_4bits['K1 Real'].values.tolist(), df_8bits['K1 Real'].values.tolist()],
        'K1 Aproximado': [df_4bits['K1 Aproximado'].values.tolist(), df_8bits['K1 Aproximado'].values.tolist()],
        'K2 Real': [df_4bits['K2 Real'].values.tolist(), df_8bits['K2 Real'].values.tolist()],
        'K2 Aproximado': [df_4bits['K2 Aproximado'].values.tolist(), df_8bits['K2 Aproximado'].values.tolist()],
        'ID Real': [df_4bits['ID Real'].values.tolist(), df_8bits['ID Real'].values.tolist()],
        'ID Aproximado': [df_4bits['ID Aproximado'].values.tolist(), df_8bits['ID Aproximado'].values.tolist()],
    })

    # Guardar la tabla como CSV
    df_comparativa.to_csv(os.path.join(carpeta_resultados, f'Tabla_Comparativa_Ejecucion_{ejecucion_numero}.csv'), index=False)

    # Generar imagen de la tabla
    fig, ax = plt.subplots(figsize=(12, 4))  # Tamaño de la imagen
    ax.axis('tight')
    ax.axis('off')
    table = ax.table(cellText=df_comparativa.values, colLabels=df_comparativa.columns, cellLoc='center', loc='center')

    # Establecer el tamaño de las celdas
    table.scale(1, 1.5)  # Ajustar la altura de las celdas para que el texto se vea mejor

    # Guardar la figura con mayor resolución
    plt.savefig(os.path.join(carpeta_resultados, f'Tabla_Comparativa_Ejecucion_{ejecucion_numero}.png'), bbox_inches='tight', dpi=300)
    plt.close()

# Función para crear la carpeta de resultados
def obtener_numero_ejecucion():
    base_path = '/workspaces/TAEIDS-david_prasad_tango_attack/RESULTADOS'
    ejecucion_numero = 1
    while os.path.exists(os.path.join(base_path, str(ejecucion_numero))):
        ejecucion_numero += 1
    nueva_carpeta = os.path.join(base_path, str(ejecucion_numero))
    os.makedirs(nueva_carpeta)
    return nueva_carpeta, ejecucion_numero

# Obtener carpeta de resultados para la ejecución actual
carpeta_resultados, ejecucion_numero = obtener_numero_ejecucion()

# Generar gráficos y recoger resultados
resultados_4bits = plot_results(4, ejecucion_numero, carpeta_resultados)
resultados_8bits = plot_results(8, ejecucion_numero, carpeta_resultados)

# Crear la tabla comparativa
crear_tabla_comparativa(resultados_4bits, resultados_8bits, carpeta_resultados, ejecucion_numero)
