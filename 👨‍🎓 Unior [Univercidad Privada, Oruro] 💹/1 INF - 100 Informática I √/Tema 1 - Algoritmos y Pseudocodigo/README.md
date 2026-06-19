# Tema 1: Algoritmos y Pseudocódigo
## 🏫 Materia: Informática I (INF-100)

---

### 📚 Apuntes y Conceptos Clave
##### 1.1 ¿Qué es un Algoritmo?

Un **algoritmo** es una secuencia finita y ordenada de pasos lógicos que, dado un conjunto de datos de entrada, produce un resultado de salida, resolviendo un problema específico.

**Las 5 características que TODO algoritmo debe cumplir:**

| Característica | Significa que... |
|---|---|
| **Finito** | Debe terminar en algún momento, en un número determinado de pasos |
| **Definido (preciso)** | Cada paso debe estar claramente especificado, sin ambigüedad de interpretación |
| **Tiene entrada** | Recibe cero o más datos del exterior |
| **Tiene salida** | Produce al menos un resultado relacionado con la entrada |
| **Efectivo** | Cada paso debe poder ejecutarse exactamente, en tiempo finito, sin necesitar "intuición" |

> Un algoritmo NO es lo mismo que un programa: el algoritmo es la idea/lógica (independiente del lenguaje), el programa es su implementación concreta en un lenguaje como Python, C++ o Java.

##### 1.2 Fases para Resolver un Problema Computacional

```
1. Análisis del problema    → ¿Qué datos tengo? ¿Qué necesito obtener?
2. Diseño del algoritmo     → Pseudocódigo / Diagrama de flujo
3. Codificación             → Traducir el algoritmo a un lenguaje de programación
4. Prueba y depuración      → Ejecutar con distintos casos, corregir errores (debugging)
5. Documentación            → Comentar el código, explicar la lógica
6. Mantenimiento            → Actualizar el programa ante nuevos requisitos
```

##### 1.3 Pseudocódigo

El **pseudocódigo** es un lenguaje intermedio entre el español/inglés natural y un lenguaje de programación real. No tiene una sintaxis estricta, pero sí convenciones ampliamente usadas:

```
ALGORITMO SumaDeDosNumeros
    Inicio
        Definir a, b, suma Como Entero
        Escribir "Ingrese el primer número:"
        Leer a
        Escribir "Ingrese el segundo número:"
        Leer b
        suma <- a + b
        Escribir "La suma es: ", suma
    Fin
FinAlgoritmo
```

**Palabras clave típicas en pseudocódigo (español):** `Inicio`, `Fin`, `Leer`, `Escribir`, `Si...Entonces...Sino...FinSi`, `Mientras...FinMientras`, `Para...FinPara`, `Definir`, `<-` (asignación).

##### 1.4 Diagramas de Flujo (Flowcharts)

Representación gráfica de un algoritmo usando símbolos estandarizados (norma ANSI):

| Símbolo | Forma | Significado |
|---|---|---|
| **Óvalo / Elipse** | ⬭ | Inicio o Fin del algoritmo |
| **Paralelogramo** | ▱ | Entrada de datos (Leer) o Salida (Escribir/Mostrar) |
| **Rectángulo** | ▭ | Proceso: cálculo, asignación de valores |
| **Rombo** | ◇ | Decisión: evalúa una condición y bifurca el flujo (V/F) |
| **Círculo pequeño** | ○ | Conector (une partes separadas del diagrama) |
| **Flecha** | → | Línea de flujo: indica la dirección de ejecución |

**Ejemplo — diagrama de flujo para determinar si un número es par o impar:**
```
   [Inicio]
       ↓
[Leer número N]
       ↓
  ◇ ¿N % 2 == 0? ◇
   /          \
  SÍ           NO
   ↓            ↓
[Escribir   [Escribir
 "Es par"]   "Es impar"]
   ↓            ↓
       [Fin]
```

##### 1.5 Variables, Constantes y Tipos de Datos Primitivos

| Tipo de Dato | Descripción | Tamaño típico | Ejemplo |
|---|---|---|---|
| **Entero (int)** | Números sin parte decimal | 4 bytes | `edad = 20` |
| **Flotante (float)** | Números decimales, precisión simple | 4 bytes | `precio = 19.99` |
| **Doble (double)** | Números decimales, precisión doble (más exactos) | 8 bytes | `pi = 3.14159265` |
| **Carácter (char)** | Un solo símbolo | 1-2 bytes | `letra = 'A'` |
| **Cadena (string)** | Secuencia de caracteres | Variable | `nombre = "Juan"` |
| **Booleano (bool)** | Solo dos valores posibles | 1 bit (lógico) | `activo = true` |

- **Variable:** espacio de memoria con un identificador (nombre) cuyo **valor puede cambiar** durante la ejecución del programa.
- **Constante:** espacio de memoria cuyo valor se fija una vez y **no puede modificarse** después (ej: `CONST PI = 3.1416`).

**Reglas comunes para nombrar variables:**
- Deben empezar con una letra o guion bajo (`_`), nunca con un número.
- No pueden contener espacios ni símbolos especiales (`@`, `#`, `%`).
- Son sensibles a mayúsculas/minúsculas (`edad` ≠ `Edad`).
- Deben ser descriptivas: `saldoCuenta` es mejor que `x`.

##### 1.6 Operadores

| Categoría | Operadores | Ejemplo | Resultado |
|---|---|---|---|
| **Aritméticos** | `+ - * / %` | `17 % 5` | `2` (resto de la división) |
| **Relacionales** | `== != > < >= <=` | `5 > 3` | `true` |
| **Lógicos** | `AND (&&)` `OR (\|\|)` `NOT (!)` | `(5>3) && (2<4)` | `true` |
| **Asignación** | `= += -= *= /=` | `x += 5` (equivale a `x = x+5`) | — |

**Jerarquía de operadores (precedencia, de mayor a menor):**
1. Paréntesis `()`
2. Multiplicación/División/Módulo `* / %`
3. Suma/Resta `+ -`
4. Relacionales `> < >= <= == !=`
5. Lógicos `&& ||`

> *Ejemplo:* `2 + 3 * 4` se evalúa como `2 + (3*4) = 14`, no como `(2+3)*4 = 20`.

---

##### 📑 Banco de Preguntas (Auto-Evaluación)
1. **¿Qué es un algoritmo y cuáles son sus características indispensables?**
   * *Respuesta:* Un algoritmo es una secuencia finita, ordenada y lógica de pasos para resolver un problema. Características: Finito, Preciso (definido), Entrada, Salida y Eficiente.
2. **Mencione tres tipos de datos primitivos comunes en programación.**
   * *Respuesta:* Entero (int), Real/Flotante (float/double), Booleano (bool) y Carácter (char).
3. **¿Cuál de las siguientes es la representación gráfica de un algoritmo?**
   * A) Pseudocódigo
   * B) Diagrama de Flujo
   * C) Código fuente
   * D) Compilador
   * *Respuesta correcta:* B) Diagrama de Flujo.
4. **Escriba un pseudocódigo simple para sumar dos números ingresados por el usuario.**
   * *Respuesta:*
     ```text
     Inicio
       Escribir "Ingrese número 1:"
       Leer num1
       Escribir "Ingrese número 2:"
       Leer num2
       suma <- num1 + num2
       Escribir "La suma es: ", suma
     Fin
     ```

---

### ✍️ Mis Resúmenes y Notas de Clase
*Haz doble clic en este archivo para registrar tus notas, fórmulas o resúmenes de las clases del docente.*

---

### 📂 Archivos y Tareas de esta Unidad
*Arrastra tus prácticas, códigos o diapositivas a esta carpeta para organizarlas aquí.*

---
*Documento autogenerado para el control de estudios del Ing. José Luis Choquevilca - UNIOR*