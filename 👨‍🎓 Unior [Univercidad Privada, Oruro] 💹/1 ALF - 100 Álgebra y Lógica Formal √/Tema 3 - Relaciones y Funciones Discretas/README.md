# Tema 3: Relaciones y Funciones Discretas
## 🏫 Materia: Álgebra y Lógica Formal (ALF-100)

---

### 📚 Apuntes y Conceptos Clave
##### 3.1 Relaciones Binarias

Una **relación binaria** R de A en B es cualquier subconjunto del producto cartesiano $A \times B$: $R \subseteq A \times B$.

> *Ejemplo:* Sea A = {1,2,3} y la relación R = "es menor que" definida en A:
> $R = \{(1,2),(1,3),(2,3)\}$

##### 3.2 Propiedades de las Relaciones (definidas en un conjunto A)

| Propiedad | Definición formal | Ejemplo cotidiano | ¿Se cumple en "≤" sobre ℕ? |
|---|---|---|---|
| **Reflexiva** | ∀a∈A: (a,a)∈R | "es igual a" | Sí (a≤a siempre) |
| **Simétrica** | Si (a,b)∈R entonces (b,a)∈R | "es hermano de" | No (si a≤b no implica b≤a) |
| **Antisimétrica** | Si (a,b)∈R y (b,a)∈R entonces a=b | "es menor o igual que" | Sí |
| **Transitiva** | Si (a,b)∈R y (b,c)∈R entonces (a,c)∈R | "es ancestro de" | Sí |

##### 3.3 Relación de Equivalencia vs. Relación de Orden

| Tipo | Propiedades que cumple | Ejemplo |
|---|---|---|
| **Relación de equivalencia** | Reflexiva + Simétrica + Transitiva | "Tiene la misma edad que", "≡ (mod n)" |
| **Relación de orden** | Reflexiva + Antisimétrica + Transitiva | "≤", "es subconjunto de (⊆)" |

> *Ejemplo de clases de equivalencia:* La relación "tiene el mismo resto al dividir por 3" sobre los números enteros divide a todos los enteros en exactamente 3 clases: {...,-3,0,3,6,...}, {...,-2,1,4,7,...}, {...,-1,2,5,8,...}

##### 3.4 Funciones

Una **función** $f: A \to B$ asigna a **cada** elemento de A **exactamente un** elemento de B (no puede faltar ninguno, ni tener dos imágenes).

| Tipo | Definición | Verificación visual | Ejemplo |
|---|---|---|---|
| **Inyectiva (1 a 1)** | Elementos distintos del dominio tienen imágenes distintas | Ningún elemento de B recibe dos flechas | $f(x)=x+1$ en ℝ |
| **Sobreyectiva (sobre)** | Todo elemento de B tiene al menos una preimagen | Todos los elementos de B son alcanzados | $f(x)=x^3$ en ℝ |
| **Biyectiva** | Es inyectiva y sobreyectiva a la vez | Correspondencia exacta uno a uno | $f(x)=2x$ en ℝ |

> *Ejemplo:* $f(x) = x^2$ definida de ℝ a ℝ **NO es inyectiva** porque $f(2)=f(-2)=4$ (dos elementos del dominio tienen la misma imagen), y **NO es sobreyectiva** porque ningún número negativo de B tiene preimagen real.

##### 3.5 Composición de Funciones

$$(f \circ g)(x) = f(g(x))$$

> *Ejemplo resuelto:* Si $f(x) = x+1$ y $g(x) = x^2$, entonces:
> $(f \circ g)(3) = f(g(3)) = f(9) = 10$
> $(g \circ f)(3) = g(f(3)) = g(4) = 16$
>
> Nótese que $f \circ g \neq g \circ f$ en general — la composición **no es conmutativa**.

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