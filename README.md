# Simulación del Método de Encriptación de David-Prasad Usando el "Tango Attack"

| **Autor**                                 | **Correo**                       | **Institución**                    |
|-------------------------------------------|----------------------------------|-------------------------------------|
| Christian Omar Rodriguez Huamanñahui      | crodriguezh@ulasalle.edu.pe      | Universidad La Salle Arequipa      |
| Pedro Humberto Rondon Ponce               | prondonp@ulasalle.edu.pe         | Universidad La Salle Arequipa      |


## Introducción

La seguridad en la encriptación de datos es un tema crítico en el campo de la informática y las telecomunicaciones. En el contexto de la ciberseguridad, la protección de la información sensible es esencial para salvaguardar la privacidad y la integridad de los datos. El método de encriptación propuesto por David-Prasad representa un enfoque innovador en la generación y recuperación de claves a partir de interacciones aleatorias. Sin embargo, como toda técnica de encriptación, también es susceptible a ataques que buscan comprometer la seguridad del sistema.

El **Tango Attack** se presenta como un método de ataque diseñado para recuperar claves en sistemas de encriptación. Este ataque implica la generación de respuestas aleatorias que simulan las interacciones con el sistema, permitiendo al atacante aproximar las claves utilizadas en el proceso. Este proyecto se centra en la simulación de este ataque, buscando no solo entender su funcionamiento, sino también evaluar su efectividad al comparar los valores reales y aproximados de las claves en diferentes configuraciones de bits.

## Resumen del Método

El enfoque de David-Prasad en la encriptación se basa en el uso de claves binarias, que pueden ser de diferentes longitudes, específicamente 4 y 8 bits en esta simulación. El ataque Tango se lleva a cabo a través de un proceso de múltiples pruebas en las que se generan aleatoriamente respuestas para las claves `K1`, `K2`, y `ID`. Al promediar estas respuestas, se obtiene una aproximación de los valores reales, lo que permite evaluar la robustez del método de encriptación.

## Funcionamiento del Código

### Estructura del Código

El código está estructurado en varias funciones, cada una con propósitos específicos:

1. **Simulación de Valores**: Genera valores binarios aleatorios para las claves.
2. **Simulación del Ataque**: Implementa el método de ataque Tango, donde se generan respuestas aleatorias y se promedian para obtener valores aproximados de las claves.
3. **Visualización de Resultados**: Genera gráficos que muestran la comparación entre los valores reales y aproximados de las claves `K1`, `K2`, y `ID`.
4. **Creación de Tablas Comparativas**: Genera tablas que comparan los resultados de las simulaciones para 4 y 8 bits.
5. **Gestión de Resultados**: Organiza los resultados en carpetas específicas para cada ejecución, asegurando que los archivos no se sobreescriban.

### Ejecución del Código

El flujo de trabajo se maneja mediante una función principal que coordina las simulaciones y genera resultados para 4 y 8 bits. Los resultados se guardan en archivos CSV y se organizan en carpetas numeradas según la ejecución actual. Los gráficos generados facilitan la visualización de la efectividad del ataque al comparar los valores reales con los aproximados.

## Resultados

Los resultados se estructuran en archivos CSV y gráficos, donde la comparación entre los valores reales y aproximados revela la eficacia del método de ataque en diferentes longitudes de clave. Los datos obtenidos pueden ser analizados para evaluar la robustez de las claves y la efectividad del sistema de encriptación.

## Conclusiones

La simulación del método de encriptación de David-Prasad bajo el ataque Tango proporciona una comprensión valiosa de la dinámica del ataque y sus implicaciones en la seguridad. A medida que se varían las longitudes de los bits, se observa una diferencia en los resultados, lo que destaca la necesidad de fortalecer las claves utilizadas en sistemas de encriptación.

## Requisitos

Para ejecutar el código, asegúrate de tener las siguientes bibliotecas de Python instaladas:

- `numpy`
- `matplotlib`
- `pandas`

## Ejecución

Para ejecutar el código, asegúrate de tener instaladas las bibliotecas necesarias y luego ejecuta el script `Main.py`. Los resultados se generarán en una carpeta bajo `RESULTADOS`, con subcarpetas específicas para cada ejecución.
