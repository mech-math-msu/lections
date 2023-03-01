## Собственные векторы

---

**Определение:**<a name="definition-0"></a> Пусть $V$ - векторное пространство над полем $F$, $\mathcal{A}$ - линейный оператор на $V$. $v \ne 0 \in V$ - *собственный вектор* линейного оператора $\mathcal{A}$, если $\exists \lambda \in F: \,\,\,\, \mathcal{A}(v) = \lambda v$.

$\lambda$ - *собственное значение* оператора $\mathcal{A}$.(вектор $v$ *отвечает* собственному значению $\lambda$).

**Утверждение:**<a name="statement-0"></a> Пусть $V$ - векторное пространство над полем $F$, $\mathcal{A}$ - линейный оператор на $V$. Если в $V$ существует базис из собственных векторов $\{e_1, \ldots, e_n\}$ оператора $\mathcal{A}$, отвечающих собственным значениям $\lambda_1, \ldots, \lambda_n$, то матрица $A$ линейного оператора $\mathcal{A}$ в этом базисе имеет вид:
 $$A = \left(\begin{array}{cccc}
    \lambda_1 & 0 & \dots & 0\\
    0 & \lambda_2 & \ldots & 0\\
    \vdots & \vdots & \ddots & \vdots\\
    0 & 0 & \dots & \lambda_n
 \end{array}\right)$$

 *Доказательство:* $\,\,\,\,\blacksquare$

### Характеристическое уравнение и многочлен

---

**Определение:**<a name="definition-1"></a> $\mathcal{I}$ - *тождественный линейный оператор*, то есть $\forall v \in V: \,\,\,\, \mathcal{I}(v) = v$.

**Определение:**<a name="definition-2"></a> Пусть $V$ - векторное пространство над полем $F$, $\mathcal{A}$ - линейный оператор на $V$, $A$ - матрица $\mathcal{A}$ в некотором базисе.

$\chi(t) = \det \left(\mathcal{A} - t E\right)$ - *характеристический многочлен* линейного оператора $\mathcal{A}$.

Уравнение $\chi(t) = 0$ - *характеристическое уравнение* линейного оператора $\mathcal{A}$.

**Определение:**<a name="definition-3"></a> (определение корректно) [Определение](#definition-2) корректно, то есть характеристический многочлен и характеристическое уравнение не зависят от выбора базиса.

*Доказательство:* Пусть $V$ - векторное пространство над полем $F$, $\mathcal{A}$ - линейный оператор на $V$, $A$ - матрица $\mathcal{A}$ в базисе $B$, $\tilde{A}$ - матрица $\mathcal{A}$ в базисе $\tilde{B}$.

$$|\tilde{A} - t E| = |C_{B \to \tilde{B}}^{-1}A C_{B \to \tilde{B}} - t C_{B \to \tilde{B}}^{-1}C_{B \to \tilde{B}}| = |A - t E| \,\,\,\,\blacksquare$$

**Утверждение:**<a name="statement-1"></a> Пусть $V$ - векторное пространство над полем $F$, $\mathcal{A}$ - линейный оператор на $V$. Тогда $\lambda \in F$ - собственное значение $\mathcal{A} \Leftrightarrow \lambda$ - корень характеристического уравнения $\mathcal{A}$.

*Доказательство:* $$\Leftarrow$$
$\lambda$ - корень $\chi(t) \Rightarrow \det(A - \lambda E) = 0 \Rightarrow$
$$\Rightarrow \exists x = \left(\begin{array}{c}
x_1^0\\
\vdots\\
x_n^0
\end{array} \right) \in V: \,\,\,\, (A - \lambda E)\left(\begin{array}{c}
x_1^0\\
\vdots\\
x_n^0
\end{array} \right) = 0 \Rightarrow$$
$$\Rightarrow (\mathcal{A} - \lambda \mathcal{I})(x) = 0 \Rightarrow \mathcal{A}(x) = \lambda x$$
$$\Rightarrow$$
Те же рассуждения в обратную сторону $\,\,\,\,\blacksquare$

## Собственные подпространства

---

**Определение:**<a name="definition-4"></a> Пусть $V$ - векторное пространство над полем $F$, $\mathcal{A}$ - линейный оператор на $V$, $\lambda$ - собственное значение $\mathcal{A}$. $V_{\lambda}$ - это множество собственных векторов, отвечающих значению $\lambda$ и нулевой вектор.

**Утверждение:**<a name="statement-2"></a> $V_{\lambda}$ - подпространство векторного пространства $V$.

*Доказательство:* очев $\,\,\,\,\blacksquare$

**Определение:**<a name="definition-5"></a> $V_{\lambda}$ - *собственное подпространство*.

**Утверждение:**<a name="statement-3"></a> Пусть $V$ - векторное пространство над полем $F$, $\mathcal{A}$ - линейный оператор на $V$, $\lambda$ - собственное значение $\mathcal{A}$. Тогда
$$V_{\lambda} = \ker (\mathcal{A} - \lambda \mathcal{I})$$

*Доказательство:* $V_{\lambda} = \{v \in V: \,\,\,\, \mathcal{A}(v) = \lambda v\} \,\,\,\,\blacksquare$

**Утверждение:**<a name="statement-4"></a> Пусть $V$ - векторное пространство над полем $F$ размерности $n$, $\mathcal{A}$ - линейный оператор на $V$, $\lambda$ - собственное значение $\mathcal{A}$. $\dim V_{\lambda} = \dim \ker (\mathcal{A} - \lambda \mathcal{I}) = n - \dim \operatorname{img} (\mathcal{A} - \lambda \mathcal{I})$.

*Доказательство:* [следует отсюда](https://mech-math-msu.github.io/lections/linear-algebra/lection-25.02.23#statement-1) $\,\,\,\,\blacksquare$

**Утверждение:**<a name="statement-5"></a> Пусть $V$ - векторное пространство над полем $F$ размерности $n$, $\mathcal{A}$ - линейный оператор на $V$, $\lambda$ - корень кратности $k$ характеристического многочлена $\chi(t) = |\mathcal{A} - t E|$. Тогда $\dim V \le k$.

*Доказательство:* 

**Утверждение:**<a name="statement-6"></a> Пусть $\mathcal{A}$ - линейный оператор на $V$, $\lambda_1, \ldots, \lambda_s$ - его различные собственные значения. Тогда векторы $v_1, \ldots, v_s$, отвечающие собственным значениям $\lambda_1, \ldots, \lambda_s$ - линейно независимы.

*Доказательство:* (индукция по $s$) 
$$\alpha_1 v_1 + \ldots + \alpha_s v_s = 0 \,\,\,\, (1)$$
$$\alpha_1 \lambda_1 v_1 + \ldots + \alpha_s \lambda_s v_s = 0 \,\,\,\, (2)$$
Пусть $\lambda_1 \ne 0$ 
$$(2) - \lambda * (1):\,\,\,\,\,\,\,\, \alpha_2 (\lambda_2 - \lambda_1) v_2 + \ldots + \alpha_s (\lambda_s - \lambda_1) v_s = 0$$
По предположению индукции $v_2, \ldots, v_s$ линейно независимы $\Rightarrow$
$$\begin{cases}
    \alpha_2 (\lambda_2 - \lambda_1) = 0\\
    \vdots\\
    \alpha_s (\lambda_s - \lambda_1) = 0
\end{cases} \Rightarrow \begin{cases}
    \alpha_2 = 0\\
    \vdots\\
    \alpha_s = 0
\end{cases} \Rightarrow \alpha_1 v_1 = 0$$
Противоречие $\,\,\,\,\blacksquare$

**Следствие:**<a name="corollary-0"></a> Сумма собственных подпространств отвечающих различным значениям $\lambda$ - прямая.

*Доказательство:* 

**Следствие:**<a name="corollary-1"></a> Пусть $V$ - векторное пространство над полем $F$ размерности $n$, $\mathcal{A}$ - линейный оператор на $V$. Если $\chi(t) = 0$ имеет $n$ различных корней, то в $V$ существует базис, состоящий из собственных векторов.

*Доказательство:* очев $\,\,\,\,\blacksquare$

**Теорема:**<a name="theorem-0"></a> (критерий диагонализируемости линейного оператора) Пусть $V$ - векторное пространство над полем $F$ размерности $n$, $\mathcal{A}$ - линейный оператор на $V$. Тогда существование базиса $V$, состоящего из собственных векторов $\mathcal{A} \Leftrightarrow \chi(t)$ - разлагается на линейные множители над полем $F$ и $\dim V_{\lambda} = k$, где $k$ - кратность $\lambda$ для любого корня $\lambda$.

*Доказательство:* Пусть $\lambda_1, \ldots, \lambda_s$ - все корни характеристического многочлена $\chi(t)$, $k_1, \ldots, k_s$ - кратности этих корней.

$$\Rightarrow$$
В $V$ существует базис $B = \{e_1, \ldots, e_n\}$ из собственных векторов линейного оператора $\mathcal{A}$. Рассмотрим множество $V_1$ из всех векторов $B$, отвечающих собственному значению $\lambda_1$, оно является подмножеством собственного подпространства $V$, отвечающего значению $\lambda_1 \,\,\,\, V_1 \subset V_{\lambda_1}$. Аналогично для $V_1, \ldots,  V_s$. Тогда $V = V_1 \oplus \ldots \oplus V_s \subset V_{\lambda_1} \oplus \ldots \oplus V_{\lambda_s} \subset V \Rightarrow V = V_{\lambda_1} \oplus \ldots \oplus V_{\lambda_s}$. $\dim V = \displaystyle \sum_{i = 1}^{s}\dim V_{\lambda_i} \le \displaystyle \sum_{i = 1}^{s}k_i \le n \Rightarrow \dim V_{\lambda_i} = k_i \,\,\,\, \forall i \in \{1, \ldots, s\}$. (что-то непонятно)

$$\Leftarrow$$
$\dim V_{\lambda_1} \oplus \ldots \oplus \dim V_{\lambda_s} = \displaystyle \sum_{i = 1}^{s}\dim V_{\lambda_i} = \displaystyle \sum_{i = 1}^{s}k_i = n = \dim V \Rightarrow$ можем взять базис, состоящий из базисов $V_{\lambda_i} \,\,\,\,\blacksquare$

