# Tema 6: Máquinas de Estado y Lenguajes Formales
## 🏫 Materia: Álgebra y Lógica Formal (ALF-100)

---

### 📚 Apuntes y Conceptos Clave
##### 6.1 Autómatas Finitos

Un **autómata finito** es un modelo matemático con un número finito de estados, usado para reconocer patrones en cadenas (lenguajes formales).

**Definición formal:** $M = (Q, \Sigma, \delta, q_0, F)$
- $Q$: conjunto finito de estados
- $\Sigma$: alfabeto de entrada
- $\delta$: función de transición ($Q \times \Sigma \to Q$)
- $q_0$: estado inicial
- $F$: conjunto de estados de aceptación

| Tipo | Característica |
|---|---|
| **DFA** (Determinista) | Para cada estado y símbolo, exactamente una transición posible |
| **NFA** (No determinista) | Puede haber cero, una o varias transiciones posibles para el mismo símbolo |

> *Ejemplo:* Autómata que reconoce cadenas binarias que terminan en "1":
> - Estados: $\{q_0, q_1\}$, donde $q_0$ es inicial y $q_1$ es de aceptación.
> - Transiciones: desde $q_0$ con "0" se queda en $q_0$; con "1" va a $q_1$. Desde $q_1$ con "0" vuelve a $q_0$; con "1" se queda en $q_1$.
> - La cadena "1101" termina en $q_1$ (acepta), la cadena "1100" termina en $q_0$ (rechaza).

##### 6.2 Gramáticas Formales y Jerarquía de Chomsky

Una **gramática** $G=(V,T,P,S)$ define las reglas de producción que generan las cadenas válidas de un lenguaje.

| Tipo | Nombre | Reconocida por |
|---|---|---|
| Tipo 0 | Sin restricciones | Máquina de Turing |
| Tipo 1 | Sensible al contexto | Autómata linealmente acotado |
| Tipo 2 | Libre de contexto | Autómata de pila |
| Tipo 3 | Regular | Autómata finito |

> *Ejemplo de gramática regular* que genera cadenas con cualquier número de "a" seguidas de una "b":
> $S \to aS \mid b$
> Genera: b, ab, aab, aaab, ...

##### 6.3 Expresiones Regulares

| Símbolo | Significado | Ejemplo |
|---|---|---|
| `*` | Cero o más repeticiones | `a*` → "", "a", "aa", "aaa"... |
| `+` | Una o más repeticiones | `a+` → "a", "aa", "aaa"... |
| `?` | Cero o una repetición (opcional) | `a?` → "" o "a" |
| `\|` | Alternancia (o) | `a\|b` → "a" o "b" |
| `.` | Cualquier carácter | `a.c` → "abc", "axc"... |

> *Ejemplo práctico:* la expresión regular para validar un número de teléfono boliviano simple podría ser `[67][0-9]{7}` (empieza con 6 o 7, seguido de 7 dígitos).

> Las expresiones regulares son equivalentes en poder de reconocimiento a los autómatas finitos (Tipo 3): todo lo que reconoce un DFA puede expresarse como expresión regular, y viceversa.

---

##### 📑 Banco de Preguntas (Auto-Evaluación)
1. **¿Qué diferencia hay entre un DFA (Autómata Finito Determinista) y un NFA (No Determinista)?**
   * *Respuesta:* En un DFA, para cada estado y símbolo de entrada hay una única transición posible; en un NFA, puede haber múltiples transiciones posibles, transiciones vacías ($\epsilon$) o ninguna transición para un mismo par de estado y símbolo.
2. **Describa la Jerarquía de Chomsky de lenguajes y gramáticas formales.**
   * *Respuesta:* Clasifica las gramáticas en 4 niveles de restricciones crecientes: Tipo 0 (Sin restricciones / Máquina de Turing), Tipo 1 (Sensibles al contexto), Tipo 2 (Libres de contexto / Autómata de pila) y Tipo 3 (Regulares / Autómata finito).
3. **Dada la expresión regular $a^*b$, ¿cuál de las siguientes cadenas NO es aceptada por ella?**
   * A) "b"
   * B) "ab"
   * C) "aaab"
   * D) "aba"
   * *Respuesta correcta:* D) "aba" (la cadena debe terminar estrictamente en un único carácter "b").
4. **Mencione los 5 componentes formales de un autómata finito.**
   * *Respuesta:* $M = (Q, \Sigma, \delta, q_0, F)$ donde $Q$ son los estados, $\Sigma$ el alfabeto, $\delta$ la función de transición, $q_0$ el estado inicial y $F$ los estados de aceptación.

---

### ✍️ Mis Resúmenes y Notas de Clase
*Haz doble clic en este archivo para registrar tus notas, fórmulas o resúmenes de las clases del docente.*

---

### 📂 Archivos y Tareas de esta Unidad
*Arrastra tus prácticas, códigos o diapositivas a esta carpeta para organizarlas aquí.*

---
*Documento autogenerado para el control de estudios del Ing. José Luis Choquevilca - UNIOR*