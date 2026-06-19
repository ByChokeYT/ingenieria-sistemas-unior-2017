# Tema 4: Álgebra de Boole y Circuitos Lógicos
## 🏫 Materia: Álgebra y Lógica Formal (ALF-100)

---

### 📚 Apuntes y Conceptos Clave
##### 4.1 Variables y Operaciones Booleanas

El **álgebra de Boole** trabaja con variables binarias (0 o 1) y es la base matemática del diseño de circuitos digitales y procesadores.

| Operación | Notación algebraica | Equivalente lógico |
|---|---|---|
| AND | A · B (o AB) | Conjunción ∧ |
| OR | A + B | Disyunción ∨ |
| NOT | A' (o Ā) | Negación ¬ |

##### 4.2 Postulados y Teoremas de Boole (Tabla Completa)

| Ley | AND | OR |
|---|---|---|
| Identidad | A·1 = A | A+0 = A |
| Nulo | A·0 = 0 | A+1 = 1 |
| Idempotencia | A·A = A | A+A = A |
| Complemento | A·A' = 0 | A+A' = 1 |
| Conmutativa | A·B = B·A | A+B = B+A |
| Asociativa | (AB)C = A(BC) | (A+B)+C = A+(B+C) |
| Distributiva | A(B+C) = AB+AC | A+BC = (A+B)(A+C) |
| **De Morgan** | (AB)' = A'+B' | (A+B)' = A'B' |

##### 4.3 Compuertas Lógicas (Hardware)

| Compuerta | Tabla de verdad (A,B → Salida) | Expresión |
|---|---|---|
| **AND** | 00→0, 01→0, 10→0, 11→1 | A·B |
| **OR** | 00→0, 01→1, 10→1, 11→1 | A+B |
| **NOT** | 0→1, 1→0 | A' |
| **NAND** | 00→1, 01→1, 10→1, 11→0 | (A·B)' |
| **NOR** | 00→1, 01→0, 10→0, 11→0 | (A+B)' |
| **XOR** | 00→0, 01→1, 10→1, 11→0 | A⊕B |
| **XNOR** | 00→1, 01→0, 10→0, 11→1 | (A⊕B)' |

> NAND y NOR son **compuertas universales**: con solo NAND (o solo NOR) repetidas se puede construir CUALQUIER circuito lógico, incluyendo AND, OR y NOT.
> Ejemplo: $A' = (A \cdot A)'$ → un NAND con ambas entradas iguales a A funciona como NOT.

##### 4.4 Simplificación de Expresiones Booleanas

**Método algebraico — ejemplo resuelto paso a paso:**

Simplificar: $F = AB + AB' + A'B$

```
F = AB + AB' + A'B
F = A(B+B') + A'B          [factor común A]
F = A(1) + A'B               [B+B' = 1, complemento]
F = A + A'B                  [identidad]
F = A + B                    [ley de absorción: A + A'B = A + B]
```

**Otro ejemplo:** Simplificar $F = (A+B)(A+B')$

```
F = AA + AB' + BA + BB'
F = A + AB' + AB + 0        [AA=A, BB'=0]
F = A + A(B'+B)
F = A + A(1)
F = A + A = A
```

##### 4.5 Mapas de Karnaugh

Método visual con tablas de $2^n$ casillas que agrupa términos adyacentes (en grupos de 1, 2, 4, 8...) para simplificar funciones booleanas sin necesidad de álgebra paso a paso.

**Ejemplo: simplificar F(A,B) con tabla de verdad: F=1 cuando AB=01, 10, 11**

| | B=0 | B=1 |
|---|---|---|
| **A=0** | 0 | 1 |
| **A=1** | 1 | 1 |

**Pasos:**
1. Ubicar los 1s en el mapa: posiciones (A=0,B=1), (A=1,B=0), (A=1,B=1).
2. Agrupar adyacentes: el grupo de la fila A=1 completa (ambas columnas) da el término **A**; el grupo de la columna B=1 completa da el término **B**.
3. Expresión simplificada: $F = A + B$

---

##### 📑 Banco de Preguntas (Auto-Evaluación)
1. **¿Qué son las compuertas universales y cuáles son en el diseño de circuitos?**
   * *Respuesta:* Son compuertas con las cuales se puede construir cualquier circuito o función lógica. Son NAND y NOR.
2. **Simplifique algebraicamente la expresión booleana $Y = A \cdot B + A \cdot B\prime$.**
   * *Respuesta:* $Y = A \cdot (B + B\prime) = A \cdot 1 = A$.
3. **¿Cuál es el valor binario de la salida de una compuerta XOR si sus entradas son $A = 1$ y $B = 1$?**
   * A) 1
   * B) 0
   * C) Z (alta impedancia)
   * D) Indefinido
   * *Respuesta correcta:* B) 0 (XOR da 1 solo si las entradas son diferentes).
4. **¿Cuál es la función de un Mapa de Karnaugh?**
   * *Respuesta:* Es una herramienta gráfica para simplificar funciones booleanas, reduciendo la cantidad de términos de forma visual mediante adyacencias lógicas.

---

### ✍️ Mis Resúmenes y Notas de Clase
*Haz doble clic en este archivo para registrar tus notas, fórmulas o resúmenes de las clases del docente.*

---

### 📂 Archivos y Tareas de esta Unidad
*Arrastra tus prácticas, códigos o diapositivas a esta carpeta para organizarlas aquí.*

---
*Documento autogenerado para el control de estudios del Ing. José Luis Choquevilca - UNIOR*