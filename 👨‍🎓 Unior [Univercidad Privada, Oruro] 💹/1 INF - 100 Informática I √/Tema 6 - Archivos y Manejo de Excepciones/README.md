# Tema 6: Archivos y Manejo de Excepciones
## 🏫 Materia: Informática I (INF-100)

---

### 📚 Apuntes y Conceptos Clave
##### 6.1 Manejo de Archivos

| Tipo | Descripción | Extensiones comunes |
|---|---|---|
| **Texto plano** | Contenido legible directamente, codificado en caracteres | `.txt`, `.csv`, `.json` |
| **Binario** | Contenido en formato de bytes, no legible directamente | `.dat`, imágenes, ejecutables |

**Modos de apertura de archivo:**

| Modo | Significado |
|---|---|
| `r` | Lectura (read) — falla si el archivo no existe |
| `w` | Escritura (write) — crea el archivo o **sobrescribe** su contenido |
| `a` | Append — agrega contenido al final sin borrar lo existente |
| `r+` | Lectura y escritura simultánea |

**Ejemplo en Python:**

```python
# Escribir en un archivo
with open("datos.txt", "w") as archivo:
    archivo.write("Primera línea\n")
    archivo.write("Segunda línea\n")

# Leer un archivo
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

# Agregar al final (append)
with open("datos.txt", "a") as archivo:
    archivo.write("Tercera línea agregada\n")
```

> `with` se usa porque cierra el archivo automáticamente al terminar el bloque, evitando dejar el archivo abierto innecesariamente.

##### 6.2 Manejo de Excepciones

Una **excepción** es un evento anómalo que ocurre durante la ejecución e interrumpe el flujo normal del programa (ej: dividir por cero, archivo no encontrado, conversión de tipo inválida).

**Estructura `try-except-finally`:**

```python
try:
    numero = int(input("Ingrese un número: "))
    resultado = 100 / numero
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("Error: no se puede dividir por cero")
except ValueError:
    print("Error: debe ingresar un número válido")
finally:
    print("Este bloque siempre se ejecuta, haya error o no")
```

**Tipos comunes de excepciones:**

| Excepción | Causa |
|---|---|
| `ZeroDivisionError` | División por cero |
| `IndexError` | Acceso a un índice fuera de rango en un arreglo/lista |
| `FileNotFoundError` | El archivo que se intenta abrir no existe |
| `ValueError` | Conversión de tipos inválida (ej: `int("abc")`) |
| `TypeError` | Operación entre tipos incompatibles (ej: `"5" + 5`) |

> El bloque `finally` es clave para liberar recursos (como cerrar un archivo o una conexión), ya que se ejecuta **siempre**, sin importar si hubo error o no.

---

##### 📑 Banco de Preguntas (Auto-Evaluación)
1. **¿Qué es una excepción en programación y para qué sirve el bloque `try-catch`?**
   * *Respuesta:* Una excepción es un error que ocurre en tiempo de ejecución. El bloque `try-catch` sirve para capturar y manejar el error de forma controlada sin que el programa aborte o se cierre abruptamente.
2. **Diferencie entre la lectura de archivos de texto plano y archivos binarios.**
   * *Respuesta:* Los archivos de texto contienen caracteres legibles por humanos (codificados en UTF-8, ASCII); los archivos binarios contienen datos crudos en formato de bytes (no legibles directamente, optimizados para almacenamiento de estructuras de datos complejos).
3. **¿Qué bloque se ejecuta SIEMPRE en una estructura de control de excepciones, haya ocurrido un error o no?**
   * A) `try`
   * B) `catch`
   * C) `finally`
   * D) `throw`
   * *Respuesta correcta:* C) `finally`.
4. **Mencione dos excepciones comunes en programación y qué las causa.**
   * *Respuesta:* `ZeroDivisionError` (dividir un número entre cero) e `IndexError` (intentar acceder a un índice inexistente en un arreglo/lista).

---

### ✍️ Mis Resúmenes y Notas de Clase
*Haz doble clic en este archivo para registrar tus notas, fórmulas o resúmenes de las clases del docente.*

---

### 📂 Archivos y Tareas de esta Unidad
*Arrastra tus prácticas, códigos o diapositivas a esta carpeta para organizarlas aquí.*

---
*Documento autogenerado para el control de estudios del Ing. José Luis Choquevilca - UNIOR*