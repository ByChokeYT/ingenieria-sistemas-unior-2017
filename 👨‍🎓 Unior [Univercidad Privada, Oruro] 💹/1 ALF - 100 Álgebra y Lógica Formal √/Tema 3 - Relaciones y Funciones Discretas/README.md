# Tema 3: Relaciones y Funciones Discretas
## 🏫 Materia: Álgebra y Lógica Formal (ALF-100)

---

### 📚 Apuntes y Conceptos Clave
##### 3.1 Relaciones Binarias

Una **relación binaria** R de A en B es cualquier subconjunto del producto cartesiano $A \times B$.

##### 3.2 Propiedades de las Relaciones (en un conjunto A)

| Propiedad | Definición | Ejemplo |
|---|---|---|
| **Reflexiva** | ∀a∈A: (a,a)∈R | "es igual a" |
| **Simétrica** | Si (a,b)∈R entonces (b,a)∈R | "es hermano de" |
| **Antisimétrica** | Si (a,b)∈R y (b,a)∈R entonces a=b | "es menor o igual que" |
| **Transitiva** | Si (a,b)∈R y (b,c)∈R entonces (a,c)∈R | "es ancestro de" |

**Relación de equivalencia:** cumple reflexiva + simétrica + transitiva (ej: "tiene la misma edad que").
**Relación de orden:** cumple reflexiva + antisimétrica + transitiva (ej: "≤").

##### 3.3 Funciones

Una **función** f: A → B asigna a cada elemento de A exactamente un elemento de B.

| Tipo | Definición | ¿Cómo verificarlo? |
|---|---|---|
| **Inyectiva (1 a 1)** | Elementos distintos del dominio tienen imágenes distintas | Ningún elemento de B recibe dos flechas |
| **Sobreyectiva (sobre)** | Todo elemento de B tiene al menos una preimagen | Todos los elementos de B son alcanzados |
| **Biyectiva** | Es inyectiva y sobreyectiva a la vez | Correspondencia uno a uno perfecta, admite función inversa |

##### 3.4 Composición de Funciones

$$(f \circ g)(x) = f(g(x))$$

Primero se aplica $g$, luego $f$ al resultado.

---

##### 📑 Banco de Preguntas (Auto-Evaluación)
1. **¿Qué condiciones debe cumplir una relación para ser de equivalencia?**
   * *Respuesta:* Debe ser reflexiva, simétrica y transitiva.
2. **Explique la diferencia entre una función inyectiva y una sobreyectiva.**
   * *Respuesta:* Inyectiva (1 a 1): elementos distintos del dominio tienen imágenes distintas. Sobreyectiva (sobre): el rango de la función es igual a su codominio (toda imagen tiene preimagen).
3. **Si una función es inyectiva y sobreyectiva al mismo tiempo, se clasifica como:**
   * A) Reflexiva
   * B) Identidad
   * C) Biyectiva
   * D) Compuesta
   * *Respuesta correcta:* C) Biyectiva.
4. **Dada la relación $R = \{(1,1), (2,2)\}$ en el conjunto $A = \{1, 2, 3\}$, ¿es reflexiva? ¿Por qué?**
   * *Respuesta:* No es reflexiva en $A$, porque falta el elemento $(3,3)$, y la definición exige que $(a,a) \in R$ para todo $a \in A$.

---

### ✍️ Mis Resúmenes y Notas de Clase
*Haz doble clic en este archivo para registrar tus notas, fórmulas o resúmenes de las clases del docente.*

---

### 📂 Archivos y Tareas de esta Unidad
*Arrastra tus prácticas, códigos o diapositivas a esta carpeta para organizarlas aquí.*

---
*Documento autogenerado para el control de estudios del Ing. José Luis Choquevilca - UNIOR*