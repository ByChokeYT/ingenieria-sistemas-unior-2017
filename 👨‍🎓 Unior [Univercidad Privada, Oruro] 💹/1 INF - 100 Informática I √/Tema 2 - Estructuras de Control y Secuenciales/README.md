# Tema 2: Estructuras de Control y Secuenciales
## 🏫 Materia: Informática I (INF-100)

---

### 📚 Apuntes y Conceptos Clave
##### 2.1 Estructura Secuencial

Es la forma más básica: las instrucciones se ejecutan **una tras otra**, en el orden exacto en que aparecen escritas, sin saltos ni repeticiones, de arriba hacia abajo.

```python
# Ejemplo en Python
nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tienes? "))
print(f"Hola {nombre}, el próximo año tendrás {edad + 1} años")
```

##### 2.2 Estructuras de Decisión (Selectivas)

**a) Simple (`if`)**

```python
if nota >= 51:
    print("Aprobado")
```

**b) Doble (`if-else`)**

```python
if nota >= 51:
    print("Aprobado")
else:
    print("Reprobado")
```

**c) Múltiple (`if-elif-else` / `switch-case`)**

```python
if nota >= 90:
    letra = "A"
elif nota >= 80:
    letra = "B"
elif nota >= 70:
    letra = "C"
else:
    letra = "F"
```

```c
// switch en C/Java
switch (dia) {
    case 1: printf("Lunes"); break;
    case 2: printf("Martes"); break;
    default: printf("Día inválido");
}
```

**d) Anidada** — un `if` dentro de otro `if`, para evaluar condiciones dependientes:

```python
if edad >= 18:
    if tiene_licencia:
        print("Puede conducir")
    else:
        print("Necesita sacar licencia")
else:
    print("Es menor de edad")
```

##### 2.3 Estructuras de Repetición (Iterativas / Bucles)

| Estructura | ¿Cuándo evalúa la condición? | ¿Se ejecuta al menos 1 vez? | Cuándo usarla |
|---|---|---|---|
| **for** | Al inicio, con contador definido | Solo si la condición inicial es verdadera | Se conoce el número exacto de repeticiones |
| **while** | ANTES de cada iteración | No, si la condición es falsa desde el inicio | Repetición controlada por una condición que puede cambiar |
| **do-while** | DESPUÉS de cada iteración | **Sí, siempre al menos una vez** | Cuando se necesita ejecutar el bloque mínimo una vez (ej: menús) |

**Bucle `for`:**
```python
for i in range(1, 11):  # del 1 al 10
    print(i)
```

**Bucle `while`:**
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

**Bucle `do-while` (ejemplo en C, Python no lo tiene nativamente):**
```c
int opcion;
do {
    printf("Menu:\n1. Nuevo\n2. Salir\n");
    scanf("%d", &opcion);
} while (opcion != 2);
```

##### 2.4 Control de Flujo dentro de Bucles

- **`break`**: termina el bucle inmediatamente, sin evaluar más iteraciones.
- **`continue`**: salta directamente a la siguiente iteración, sin ejecutar el resto del código de la iteración actual.

```python
for i in range(1, 10):
    if i == 5:
        break          # se detiene completamente al llegar a 5
    if i % 2 == 0:
        continue        # se saltan los pares, sin imprimirlos
    print(i)             # imprime: 1, 3
```

---

##### 📑 Banco de Preguntas (Auto-Evaluación)
1. **¿Qué diferencia existe entre un bucle `while` y un bucle `do-while`?**
   * *Respuesta:* El bucle `while` evalúa la condición al inicio (si es falsa, el bucle puede no ejecutarse ninguna vez). El bucle `do-while` evalúa la condición al final, garantizando que el cuerpo se ejecute al menos una vez.
2. **¿Cuándo es preferible utilizar una estructura `switch-case` en lugar de múltiples condicionales `if-else`?**
   * *Respuesta:* Cuando se evalúa una única variable contra múltiples valores constantes enteros o de caracteres, mejorando la legibilidad y eficiencia del código.
3. **En un bucle `for (int i = 0; i < 5; i++)`, ¿cuántas veces se ejecuta el bloque de código?**
   * A) 4 veces
   * B) 5 veces
   * C) 6 veces
   * D) Infinitas veces
   * *Respuesta correcta:* B) 5 veces (para i = 0, 1, 2, 3, 4).
4. **¿Cuál es la función de las sentencias `break` y `continue` dentro de un bucle?**
   * *Respuesta:* `break` termina y sale inmediatamente del bucle actual; `continue` salta el resto de la iteración actual y avanza a la siguiente evaluación de la condición del bucle.

---

### ✍️ Mis Resúmenes y Notas de Clase
*Haz doble clic en este archivo para registrar tus notas, fórmulas o resúmenes de las clases del docente.*

---

### 📂 Archivos y Tareas de esta Unidad
*Arrastra tus prácticas, códigos o diapositivas a esta carpeta para organizarlas aquí.*

---
*Documento autogenerado para el control de estudios del Ing. José Luis Choquevilca - UNIOR*