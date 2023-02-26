## Еще про ядра и образы линейных отображений

---

**Утверждение:**<a name="statement-0"></a> Пусть $\varphi$ - линейное отображение векторных пространств $U$ и $W$, $e_1, \ldots, e_n$ - базис в $U$. Тогда
$$\operatorname{img} \varphi = < \varphi(e_1), \ldots, \varphi(e_n) >$$

*Доказательство:* $\forall u \in U \,\,\,\, \exists \lambda_1, \ldots, \lambda_n: \,\,\,\, u = \lambda_1 e_1 + \ldots + \lambda_n e_n \Rightarrow \forall w \in W:$

$\exists u \in U: \,\,\,\, \varphi(u) = w \,\,\,\, w \in < \varphi(e_1), \ldots, \varphi(e_n) > \,\,\,\,\blacksquare$

**Определение:**<a name="definition-0"></a> Пусть $\varphi$ - линейное отображение векторных пространств $U$ и $W$. $\dim \operatorname{img} \varphi$ - это *ранг линейного отображения* $\varphi$.

**Утверждение:**<a name="statement-1"></a> Пусть $\varphi$ - линейное отображение векторных пространств $U$ и $W$. Тогда $$\dim \operatorname{img} \varphi + \dim \ker \varphi = \dim U$$

*Доказательство:* Пусть $e_1, \ldots, e_m$ - базис $\ker \varphi$, дополним его до базиса $U \Rightarrow e_1, \ldots, e_m, e_{m + 1}, \ldots, e_n$ - базис $U$. По [предыдущему утверждению](#statement-0) $\operatorname{img} \varphi = < \varphi(e_1), \ldots, \varphi(e_m), \varphi(e_{m + 1}), \ldots, \varphi(e_n) >$. $\varphi(e_1) = 0, \ldots, \varphi(e_m) = 0$, так как $e_1, \ldots, e_m \in \ker \varphi \Rightarrow \operatorname{img} \varphi = < \varphi(e_{m + 1}), \ldots, \varphi(e_n) >$. Докажем, что векторы $\varphi(e_{m + 1}), \ldots, \varphi(e_n)$ линейно независимы, то есть образуют базис $\operatorname{img} \varphi$. Рассмотрим их линейную комбинацию равную нулю: $\lambda_{m + 1} \varphi(e_{m + 1}) + \ldots + \lambda_n\varphi(e_n) = \varphi(\lambda_{m + 1} e_{m + 1} + \ldots + \lambda_n e_n) = 0 \Rightarrow$

$\Rightarrow \lambda_{m + 1} e_{m + 1} + \ldots + \lambda_n e_n \in \ker \varphi \Rightarrow \exists \lambda_1, \ldots, \lambda_m:$

$\lambda_{m + 1} e_{m + 1} + \ldots + \lambda_n e_n = \lambda_1 e_1 + \ldots + \lambda_m e_m$, так как векторы $e_1, \ldots, e_n$ линейно независимы $\lambda_{m + 1} = 0, \ldots, \lambda_{n} = 0 \,\,\,\,\blacksquare$

## Линейные операторы и их матрицы

---

**Определение:**<a name="definition-1"></a> Пусть $\varphi$ - линейное отображение векторного пространства $V$ в себя. Тогда $\varphi$ - это *линейный оператор* пространства $V$.

Пусть $V$ - векторное пространство над полем $F$, $\varphi$ - линейный оператор на $V$, $B = \{e_1, \ldots, e_n\}$ - базис $V$. 

$$\varphi(e_1) = \lambda_{11} e_1 + \ldots + \lambda_{n1} e_n$$
$$\vdots$$
$$\varphi(e_n) = \lambda_{1n} e_1 + \ldots + \lambda_{nn} e_n$$
$$\Downarrow$$
$$A = \left(\begin{array}{ccc}
\lambda_{11} & \dots & \lambda_{1n}\\
\vdots & \ddots & \vdots\\
\lambda_{n1} & \dots & \lambda_{nn}
\end{array}\right)$$
$$\left(\begin{array}{c}
\varphi(e_1)\\
\vdots\\
\varphi(e_n)
\end{array}\right) = A^T \left(\begin{array}{c}
x_1\\
\vdots\\
x_n
\end{array}\right)$$
$$\left(\begin{array}{ccc}
\varphi(e_1) & \dots & \varphi(e_n)
\end{array}\right) = \left(\begin{array}{ccc}
e_1 & \dots & e_n
\end{array}\right)A$$

Пусть $x \in V$ имеет координаты $x_1, \ldots, x_n$, а $y = \varphi(x)$ имеет координаты $y_1, \ldots, y_n$. 
$$\left(\begin{array}{ccc}
e_1 & \dots & e_n
\end{array}\right)\left(\begin{array}{c}
y_1\\
\vdots\\
y_n
\end{array}\right) = \varphi(x) = \varphi(x_1 e_1 + \ldots + x_n e_n)=$$
$$= x_1 \varphi(e_1) + \ldots + x_n \varphi(e_n) = \left(\begin{array}{ccc}
\varphi(e_1) & \dots & \varphi(e_n)
\end{array}\right) \left(\begin{array}{c}
x_1\\
\vdots\\
x_n
\end{array}\right)$$
$$\Downarrow$$
$$\left(\begin{array}{c}
y_1\\
\vdots\\
y_n
\end{array}\right) = A \left(\begin{array}{c}
x_1\\
\vdots\\
x_n
\end{array}\right)$$
**Определение:**<a name="definition-2"></a> $A$ - *матрица линейного оператора* $\varphi$ относительно базиса $e_1, \ldots, e_n$.

**Утверждение:**<a name="statement-2"></a> Пусть $V$ - векторное пространство, $\varphi$ - линейный оператор на $V$, $B, \tilde{B}$ - базисы $V$, $A, \tilde{A}$ - матрицы линейного оператора $\varphi$ относительно $B, \tilde{B}$ соответственно. Тогда $$\tilde{A} = C^{-1}_{B \to \tilde{B}}A C_{B \to \tilde{B}}$$

*Доказательство:* [следует отсюда](https://mech-math-msu.github.io/lections/linear-algebra/lection-20.02.23#statement-3) $\,\,\,\,\blacksquare$

**Утверждение:**<a name="statement-3"></a> 

1. Ранг матрицы линейного оператора не зависит от базиса.
2. Определитель матрицы линейного оператора не зависит от базиса.

*Доказательство:* Пусть $V$ - векторное пространство, $\varphi$ - линейный оператор на $V$, $B, \tilde{B}$ - базисы $V$, $A, \tilde{A}$ - матрицы линейного оператора $\varphi$ относительно $B, \tilde{B}$ соответственно. 

1. $\tilde{A} = C^{-1}_{B \to \tilde{B}}A C_{B \to \tilde{B}} \Rightarrow$ строки матрицы $A$ линейно выражаются через строки матрицы $\tilde{A} \,\,\,\,\blacksquare$
2. $|\tilde{A}| = |C^{-1}_{B \to \tilde{B}}A C_{B \to \tilde{B}}| = |C^{-1}_{B \to \tilde{B}}||C_{B \to \tilde{B}}||A| = |A| \,\,\,\,\blacksquare$ 

**Утверждение:**<a name="statement-4"></a> Матрица $A$ линейного оператора $\varphi$ на векторном пространстве $V$ невырождена $\Leftrightarrow$ $\varphi$ - обратимо.

*Доказательство:*

**Утверждение:**<a name="statement-5"></a> Пусть $\varphi$ - линейное отображение векторных пространств $U$ и $W$. $\ker \varphi = \{0\}$ и $\operatorname{img} \varphi = W$ $\Leftrightarrow$ $\varphi$ - обратимо.

*Доказательство:* $$\Rightarrow$$
$\varphi$ - [биекция](https://mech-math-msu.github.io/lections/linear-algebra/lection-20.02.23#statement-5)
$$\Leftarrow$$
$\varphi$ - обратимо, следовательно инъекция и сюръекция $\Rightarrow \ker \varphi = \{0\}$ и $\operatorname{img} \varphi = W \,\,\,\,\blacksquare$ 

**Утверждение:**<a name="statement-6"></a> Пусть $\varphi$ - линейный оператор пространства $V$. Тогда 

1. $\varphi$ обратимо $\Leftrightarrow \ker \varphi = \{0\}$.
2. $\varphi$ обратимо $\Leftrightarrow \operatorname{img} \varphi = V$.

*Доказательство:* [это](#statement-6) $+$ [это](#statement-1) $\,\,\,\,\blacksquare$

## Определение алгебры, алгебра линейных операторов

---

**Определение:**<a name="definition-3"></a> *Алгебра* над полем $F$ - это множество $\mathfrak{A}$ с операциями сложения $+: \mathfrak{A}\times \mathfrak{A} \to \mathfrak{A}$, умножения $\cdot: \mathfrak{A}\times \mathfrak{A} \to \mathfrak{A}$ и умножения на числа из поля $F$ $\cdot: F\times \mathfrak{A} \to \mathfrak{A}$, удовлетворяющих:

1. Относительно сложения и умножения $\mathfrak{A}$ - кольцо.
2. Относительно сложения и умножения на число $\mathfrak{A}$ - векторное пространство над $F$.
3. $\forall x, y \in \mathfrak{A}, \,\,\,\, \lambda \in F, \,\,\,\, \lambda(xy) = (\lambda x)y = x (\lambda y)$.

**Определение:**<a name="definition-4"></a> Множество всех линейных операторов на векторном пространстве $V$ обозначается $\operatorname{end} V$.

**Утверждение:**<a name="statement-7"></a> Пусть $V$ векторное пространство над полем $F$. Тогда $\operatorname{end} V$ - алгебра над полем $F$ относительно операций:

1. $\forall \mathcal{A}, \mathcal{B} \in \operatorname{end} V,\,\,\,\, \forall v \in V \,\,\,\, (\mathcal{A} + \mathcal{B})(x) = \mathcal{A}(x) + \mathcal{B}(x)$.
2. $\forall \mathcal{A}, \mathcal{B} \in \operatorname{end} V,\,\,\,\, \forall v \in V \,\,\,\, (\mathcal{A} \mathcal{B})(x) = \mathcal{A}(\mathcal{B}(x))$.
3. $\forall \mathcal{A} \in \operatorname{end} V,\,\,\,\, \forall \lambda \in F, \,\,\,\, \forall v \in V \,\,\,\, \lambda\mathcal{A}(x) = \mathcal{A}(\lambda x)$.

*Доказательство:* очев $\,\,\,\,\blacksquare$

**Определение:**<a name="definition-5"></a> Алгебра $\mathfrak{C}$ над $F$ *изоморфна* алгебре $\mathfrak{B}$ над $F$, если $\mathfrak{C}$ изоморфно $\mathfrak{B}$, как кольцо и как векторное пространство над $F$. Обозначается $\mathfrak{C} \cong \mathfrak{B}$.

**Определение:**<a name="definition-6"></a> Множество всех матриц $n \times n$ с элементами из поля $F$ обозначается $\mathbf{M}_{n}(F)$.

**Утверждение:**<a name="statement-8"></a> $M_{n}(F)$ - алгебра над полем $F$ относительно операций матричного сложения, матричного умножения и умножения каждого элемента матрицы на элемент из поля $F$.

*Доказательство:* очев $\,\,\,\,\blacksquare$

**Утверждение:**<a name="statement-9"></a> Пусть $V$ - векторное пространство над полем $F$. Тогда $$\operatorname{end} V \cong \mathbf{M}_{n}(F)$$

*Доказательство:* Построим биекцию $\varphi: \mathcal{A} \in \operatorname{end} V \mapsto A \in \mathbf{M}_{n}(F)$, где $A$ - матрица линейного оператора $\mathcal{A} \,\,\,\,\blacksquare$

## Инвариантные подпространства

---

**Определение:**<a name="definition-7"></a> Пусть $U$ подпространство векторного пространства $V$ над полем $F$, $\mathcal{A}$ - линейный оператор на $V$. $U$ *инвариантное (пространство)* остносительно $\mathcal{A}$, если $\forall u \in U \,\,\,\, \mathcal{A}(u) \in U$.

**Определение:**<a name="definition-8"></a> Если $U$ инвариантное пространство относительно линейного оператора $\mathcal{A}$, то ограничение $\mathcal{A}$ на $U$ обозначается $\mathcal{A}_{\vert U}$.

**Утверждение:**<a name="statement-10"></a> $\mathcal{A}_{\vert U}$ - линейный оператор $U$.
