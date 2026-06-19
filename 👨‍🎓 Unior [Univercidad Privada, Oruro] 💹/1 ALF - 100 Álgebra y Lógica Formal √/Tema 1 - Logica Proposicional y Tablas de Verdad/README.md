# Tema 1: Lógica Proposicional y Tablas de Verdad
## 🏫 Materia: Álgebra y Lógica Formal (ALF-100)

---

### 📚 Apuntes y Conceptos Clave
##### 1.1 Proposiciones

Una **proposición** es un enunciado que puede calificarse como verdadero (V) o falso (F), pero no ambos a la vez.

| Tipo | Descripción | Ejemplo |
|---|---|---|
| **Atómica (simple)** | No contiene conectivos lógicos | "La Paz es la sede de gobierno" |
| **Molecular (compuesta)** | Combina proposiciones con conectivos | "Llueve y hace frío" |

> No son proposiciones las preguntas, órdenes o exclamaciones: "¿Qué hora es?" no es una proposición.

##### 1.2 Conectivos Lógicos

| Conectivo | Símbolo | Nombre | Se lee | Verdadero cuando... |
|---|---|---|---|---|
| Negación | ¬p | NOT | "no p" | p es falso |
| Conjunción | p ∧ q | AND | "p y q" | ambas son verdaderas |
| Disyunción | p ∨ q | OR | "p o q" | al menos una es verdadera |
| Disyunción exclusiva | p ⊕ q | XOR | "p o q, no ambas" | exactamente una es verdadera |
| Implicación (condicional) | p → q | IF...THEN | "si p, entonces q" | excepto cuando p=V y q=F |
| Doble implicación | p ↔ q | IFF | "p si y solo si q" | ambas tienen el mismo valor |

##### 1.3 Tablas de Verdad

**Tabla de los conectivos básicos:**

| p | q | ¬p | p∧q | p∨q | p⊕q | p→q | p↔q |
|---|---|---|---|---|---|---|---|
| V | V | F | V | V | F | V | V |
| V | F | F | F | V | V | F | F |
| F | V | V | F | V | V | V | F |
| F | F | V | F | F | F | V | V |

**Número de filas:** con $n$ proposiciones simples, la tabla tiene $2^n$ filas.

##### 1.4 Tautologías, Contradicciones y Contingencias

| Tipo | Definición | Ejemplo |
|---|---|---|
| **Tautología** | Siempre verdadera, sin importar los valores de verdad | p ∨ ¬p |
| **Contradicción** | Siempre falsa | p ∧ ¬p |
| **Contingencia** | A veces verdadera, a veces falsa | p → q |

##### 1.5 Leyes del Álgebra Proposicional

| Ley | Expresión |
|---|---|
| Doble negación | ¬(¬p) ≡ p |
| Idempotencia | p ∧ p ≡ p ; p ∨ p ≡ p |
| Conmutativa | p ∧ q ≡ q ∧ p ; p ∨ q ≡ q ∨ p |
| Asociativa | (p∧q)∧r ≡ p∧(q∧r) |
| Distributiva | p∧(q∨r) ≡ (p∧q)∨(p∧r) |
| De Morgan | ¬(p∧q) ≡ ¬p∨¬q ; ¬(p∨q) ≡ ¬p∧¬q |
| Implicación material | p→q ≡ ¬p∨q |

##### 1.6 Razonamiento Lógico — Reglas de Inferencia

| Regla | Estructura | Ejemplo |
|---|---|---|
| **Modus Ponens** | p→q, p ⊢ q | Si llueve, me mojo. Llueve. ∴ Me mojo. |
| **Modus Tollens** | p→q, ¬q ⊢ ¬p | Si llueve, me mojo. No me mojé. ∴ No llovió. |
| **Silogismo hipotético** | p→q, q→r ⊢ p→r | Cadena de implicaciones |
| **Silogismo disyuntivo** | p∨q, ¬p ⊢ q | Es A o B. No es A. ∴ Es B. |

---

##### 📑 Banco de Preguntas (Auto-Evaluación)
1. **Diferencie entre una proposición atómica y una molecular.**
   * *Respuesta:* Una proposición atómica es simple y no contiene conectivos lógicos (ej. "La Paz es la sede de gobierno"); una molecular combina dos o más proposiciones atómicas mediante conectivos lógicos (ej. "Llueve y hace frío").
2. **Defina qué son Tautología, Contradicción y Contingencia.**
   * *Respuesta:* Tautología: enunciado que es siempre verdadero bajo cualquier interpretación. Contradicción: enunciado siempre falso. Contingencia: enunciado que puede ser verdadero o falso dependiendo de sus componentes.
3. **¿Cuántas filas tiene una tabla de verdad para un enunciado que contiene 4 proposiciones simples distintas?**
   * A) 8 filas
   * B) 16 filas
   * C) 32 filas
   * D) 4 filas
   * *Respuesta correcta:* B) 16 filas ($2^4 = 16$).
4. **Aplique la Ley de De Morgan para negar la proposición $p \land q$.**
   * *Respuesta:* $\neg(p \land q) \equiv \neg p \lor \neg q$.

---

### ✍️ Mis Resúmenes y Notas de Clase
*Haz doble clic en este archivo para registrar tus notas, fórmulas o resúmenes de las clases del docente.*

---

### 📂 Archivos y Tareas de esta Unidad
*Arrastra tus prácticas, códigos o diapositivas a esta carpeta para organizarlas aquí.*

---
*Documento autogenerado para el control de estudios del Ing. José Luis Choquevilca - UNIOR*