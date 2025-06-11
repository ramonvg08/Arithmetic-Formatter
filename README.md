Arithmetic Formatter 🧮
Este es un proyecto de Python que formatea problemas aritméticos (sumas y restas) de forma vertical y los alinea correctamente, tal como lo harían los estudiantes de primaria para facilitar su resolución.
Opcionalmente, también puede mostrar el resultado de cada operación.

📂 Descripción
El programa recibe una lista de cadenas de texto, cada una representando un problema aritmético simple (solo suma o resta).
El objetivo es organizar estos problemas en columnas bien alineadas, con un formato limpio y ordenado.

✔️ Ejemplo de Entrada:

["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
✔️ Ejemplo de Salida:

   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----

✔️ Con resultados (modo opcional):

arithmetic_arranger(["32 + 8", "1 - 3801"], True)


Resultado:

  32         1
+  8    - 3801
----    ------
  40     -3800


⚙️ Cómo usarlo

Clona el repositorio o copia el archivo arithmetic_formatter.py.

Llama a la función arithmetic_arranger() pasando una lista de problemas como primer argumento.

Si quieres que muestre las respuestas, pasa True como segundo argumento.

Ejemplo:
from arithmetic_formatter import arithmetic_arranger

print(arithmetic_arranger(["32 + 698", "3801 - 2"], True))


✅ Reglas de Validación

El programa devolverá mensajes de error si:

❌ Hay más de 5 problemas.
Error: Too many problems.

❌ Se usa un operador no permitido (solo se acepta + o -).
Error: Operator must be '+' or '-'.

❌ Los operandos contienen caracteres no numéricos.
Error: Numbers must only contain digits.

❌ Los operandos tienen más de cuatro cifras.
Error: Numbers cannot be more than four digits.

📚 Estructura del Código
Validación de problemas.

Separación de operandos y operadores.

Formateo vertical y alineación con .rjust().

Opcionalmente, cálculo y visualización de resultados.

🛠️ Posibles Mejoras
Soporte para multiplicación y división.

Personalización del espaciado entre problemas.

Interfaz gráfica para visualizar los problemas.

📃 Licencia
Este proyecto es de libre uso para fines educativos y personales.
