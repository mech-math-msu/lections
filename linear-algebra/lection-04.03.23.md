## Комплексификация

---

**Определение:**<a name="definition-0"></a> Пусть $V$ - векторное пространство над $\mathbb{R}$. Рассмотрим множество $V_(\mathbb{C}) = \{(v_1, v_2)| v_1, v_2 \in V\}$. Определим 

сложение: $\forall (v_1, v_2), (\tilde{v_1}, \tilde{v_2}) \in V_(\mathbb{C}) \,\,\,\,\,\,\,\, (v_1, v_2) + (\tilde{v_1}, \tilde{v_2}) = (v_1 + \tilde{v_1}, v_2 + \tilde{v_2})$,

умножение на числа из $\mathbb{C}$:
$\forall (\alpha + i \beta) \in \mathbb{C}, \,\,\,\, \alpha, \beta \in \mathbb{R},\,\,\,\, (v_1, v_2) \in V_(\mathbb{C}) \,\,\,\,\,\,\,\, (\alpha + i \beta)(v_1, v_2) = (\alpha v_1 - \beta v_2, \beta v_1 + \alpha v_2)$.

Будем обозначать пару $(v, 0) \in V_(\mathbb{C})$, как $v$. Заметим, что $i(v, 0) = (0, v)$, а следовательно $(v_1, v_2)$ записывается так: $v_1 + i v_2$.

**Утверждение:**<a name="statement-0"></a> Пусть $V$ - векторное пространство над $\mathbb{R}$. Тогда $V_(\mathbb{C})$ - векторное пространство над $\mathbb{C}$.

*Доказательство:* очев $\,\,\,\,\blacksquare$

**Утверждение:**<a name="statement-1"></a> Пусть $V$ - векторное пространство над $\mathbb{R}$. Тогда любой базис $V$ является базисом в $V_(\mathbb{C})$.

*Доказательство:* не очев $\,\,\,\,\blacksquare$

**Утверждение:**<a name="statement-2"></a> Пусть $V$ - векторное пространство над $\mathbb{R}$, $\mathcal{A}$ - линейный оператор на $V$. Определим отображение $\mathcal{A}_{\mathbb{C}}: V_(\mathbb{C}) \to V_(\mathbb{C}) \,\,\,\,\,\,\,\, v_1 + i v_2 \in V_(\mathbb{C}) \mapsto \mathcal{A}(v_1) + i \mathcal{A}(v_2)$. Тогда $\mathcal{A}_{\mathbb{C}}$ линейный оператор на $V_(\mathbb{C})$.

*Доказательство:* очев $\,\,\,\,\blacksquare$

**Утверждение:**<a name="statement-3"></a> Пусть $V$ - векторное пространство над $\mathbb{R}$, $\mathcal{A}$ - линейный оператор на $V$, $B$ - базис в $V$. Тогда матрица линейного оператора $\mathcal{A}_{\mathbb{C}}$ в базисе $B$ совпадает с матрицей линейного оператора $\mathcal{A}$ в базисе $B$.

*Доказательство:* очев $\,\,\,\,\blacksquare$

**Утверждение:**<a name="statement-4"></a> Пусть $V$ - векторное пространство над $\mathbb{R}$, $\mathcal{A}$ - линейный оператор на $V$. Тогда линейный оператор $\mathcal{A}_{\mathbb{C}}$ имеет собственный вектор $x + i y$ с собственным значением $\lambda = \alpha + i \beta$
$$\Downarrow$$
$$\begin{cases}
    \mathcal{A}(x) = \alpha x - \beta y\\
    \mathcal{A}(y) = \beta x + \alpha y
\end{cases}$$

*Доказательство:* $$\Rightarrow$$
$$\mathcal{A}_{\mathbb{C}}(x + i y) = (\alpha + i \beta)(x + i y) = \alpha x - \beta y + i (\beta x + \alpha y) = \mathcal{A}(x) + i \mathcal{A}(y) \,\,\,\,\blacksquare$$
$$\Leftarrow$$
То же самое в обратную сторону.

**Следствие:**<a name="corollary-0"></a> Пусть $V$ - векторное пространство над $\mathbb{R}$, $\mathcal{A}$ - линейный оператор на $V$. Линейный оператор $\mathcal{A}_{\mathbb{C}}$ имеет собственный вектор $x + i y$ с собственным значением $\lambda = \alpha + i \beta$. Тогда $<x , y >$ - двумерное инвариантное подпространство линейного оператора $\mathcal{A}$.

*Доказательство:*

## Приведение матрицы линейного оператора к треугольному виду

---

**Определение:**<a name="definition-1"></a> Поле $F$ *алгебраически замкнуто*, если любой многочлен над $F$ имеет хотя бы один корень.

**Теорема:**<a name="theorem-0"></a> Пусть $V$ - векторное пространство размерности $n$ над алгебраически замкнутым полем $F$, $\mathcal{A}$ - линейный оператор на $V$, $A$ - матрица $\mathcal{A}$ в некотором базисе. Тогда $\exists$ такой базис, что матрица линейного оператора $\mathcal{A}$ в нем верхнетреугольная. 

**Эквивалентная формулировка:** Пусть $F$ - алгебраически замкнуто, $A \in M_n(F)$. Тогда $$\exists C \in M_n(F), \,\,\,\, \det(C) \ne 0: \,\,\,\, C^{-1}AC = \left(\begin{array}{cccc}
\star & \star & \dots & \star\\
0 & \star & \dots & \star\\
\vdots & \ddots & \ddots & \vdots\\
0 & \dots & 0 & \star
\end{array}\right)$$

*Доказательство:* (индукция по $n$)
Пусть утверждение верно для $n - 1$, докажем, что оно верно для $n$. $F$ - алгебраически замкнуто, то есть характеристический многочлен $\chi(t)$ имеет хотя бы одни корень, а значит у $\mathcal{A}$ существует собственный вектор $e_1 \ne 0$, отвечающий собственному значению $\lambda$. Дополним его до базиса $V \Rightarrow \mathcal{e} = \{e_1, \ldots, e_n\}$. Матрица $\mathcal{A}$ в базисе $\mathcal{e}$ имеет вид $A_{\mathcal{e}} = \left(\begin{array}{c|ccc}
\lambda & \star & \dots & \star\\
\hline
0\\
\vdots & \,\,\,\, & B\\
0\\
\end{array}\right)$, где $B$ - матрица размера $n - 1$, а значит по предположению индукции существует $S: \,\,\,\, S^{-1}BS$ - верхнетреугольная матрица. Рассмотрим матрицу $C = \left(\begin{array}{c|ccc}
1 & 0 & \dots & 0\\
\hline
0\\
\vdots & \,\,\,\, & S\\
0\\
\end{array}\right)$.
$$C^{-1}AC = \left(\begin{array}{c|ccc}
1 & 0 & \dots & 0\\
\hline
0\\
\vdots & \,\,\,\, & S^{-1}\\
0\\
\end{array}\right)\left(\begin{array}{c|ccc}
\lambda & \star & \dots & \star\\
\hline
0\\
\vdots & \,\,\,\, & B\\
0\\
\end{array}\right)\left(\begin{array}{c|ccc}
1 & 0 & \dots & 0\\
\hline
0\\
\vdots & \,\,\,\, & S\\
0\\
\end{array}\right)=$$
$$= \left(\begin{array}{c|ccc}
\lambda & \star & \dots & \star\\
\hline
0\\
\vdots & \,\,\,\, & S^{-1}BS\\
0\\
\end{array}\right) \,\,\,\,\blacksquare$$

## Теорема Гамильтона-Кэли

---

**Теорема:**<a name="theorem-1"></a> (Теорема Гамильтона-Кэли) Пусть $\mathcal{A}$ линейный оператор на векторном пространстве $V$ размерности $n$ над полем $F$. Тогда $A$ является корнем своего характеристического многочлена.

*Доказательство:* 

1. Пусть $F$ - алгебраически замкнуто. Тогда в $V$ существует базис, в котором матрица линейного оператора $A$ является верхнетреугольной. 
$$A = \left(\begin{array}{cccc}
a_{11} & \star & \dots & \star\\
0 & a_{22} & \dots & \star\\
\vdots & \ddots & \ddots & \vdots\\
0 & \dots & 0 & a_{nn}
\end{array}\right)$$
$$\chi_{\mathcal{A}}(t) = \det (A - tE) = (a_{11} - t)\cdot \ldots \cdot (a_{nn} - t)$$
$$\chi_{\mathcal{A}}(A) = (-1)^n(A - a_{11}E)\cdot \ldots \cdot (A - a_{nn}E)=$$
$$= \left(\begin{array}{c|ccc}
0 & \star & \dots & \star\\
\hline
0\\
\vdots & C - a_{11}E\\
0\\
\end{array}\right)\cdot\ldots\cdot\left(\begin{array}{c|ccc}
a_{11} - a_{nn} & \star & \dots & \star\\
\hline
0\\
\vdots & C - a_{nn}E\\
0\\
\end{array}\right)=$$
$(C - a_{22}E)\cdot\ldots\cdot(C - a_{nn}E) = 0$ по предположению индукции (многочлен степени $n - 1$).

$$=\left(\begin{array}{c|ccc}
0 & \star & \dots & \star\\
\hline
0\\
\vdots & \,\,\,\, & C - a_{11}E\\
0\\
\end{array}\right)\cdot\left(\begin{array}{c|ccc}
\displaystyle \prod_{i = 2}^{n}(a_{11} - a_{ii}) & \star & \dots & \star\\
\hline
0\\
\vdots & \,\,\,\, & 0\\
0\\
\end{array}\right) = \left(0\right)$$

2. Пусть поле $F$ алгебраически не замкнуто. Тогда по теореме, которая будет доказана в неопределенном будущем у $F$ является подполем некоторого алгебраически замкнутого поля $F’$. $\,\,\,\,\blacksquare$


