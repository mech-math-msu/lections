$$\mathcal{I}$$

## Аннулирующй и минимальный многочлены

---

**Определение:**<a name="definition-0"></a> Пусть $V$ векторное пространство над полем $F$, $\mathcal{A}$ - линейный оператор на $V$. $f \in F[t]$ - *аннулирующий многочлен* для $\mathcal{A}$, если $f(\mathcal{A}) = 0$.

По теореме Гамильтона-Кэли характеристический многочлен является аннулирующим.

Для $\mathcal{A} = \mathcal{I}$ аннулирющим многочленом является $t - 1$, т.к. $\mathcal{A} - 1 \mathcal{I} = 0$.

**Определение:**<a name="definition-1"></a> Пусть $V$ векторное пространство над полем $F$, $\mathcal{A}$ - линейный оператор на $V$. Аннулирующий многочлен $\mathcal{A}$ минимальной степени со старшим коэффицентом равным $1$ - *минимальный многочлен* для $\mathcal{A}$.

Обозначается: $\mu_{\mathcal{A}}(t)$.

### Простейшие свойства аннулирующего многочлена

**Утверждение:**<a name="statement-0"></a> Пусть $V$ векторное пространство над полем $F$, $\mathcal{A}$ - линейный оператор на $V$. Тогда

1. Минимальный многочлен делит любой аннулирующий.
2. $\mu_{\mathcal{A}}$ - единственный.
3. Множество корней $\mu_{\mathcal{A}}$ совпадает с множеством корней характеристического многочлена.

*Доказательство:* 

1. Пусть $\zeta(t)$ - аннулирующий многочлен оператора $\mathcal{A}$. Разделим с остатком $\zeta(t)$ на $\mu_{\mathcal{A}}(t) \Rightarrow \zeta(t) = \xi(t)\mu_{\mathcal{A}}(t) + r(t)$, где степень $r(t)$ меньше степени $\mu_{\mathcal{A}}(t)$, если $r(t) \ne 0$, то получим противоречие с минимальностью степени $\,\,\,\,\blacksquare$
2. Пусть $\mu_{\mathcal{A}}(t)$ и $\tilde{\mu}_{\mathcal{A}}(t)$ - минимальные многочлены $\mathcal{A}$. Тогда по $1$-му свойству $\mu_{\mathcal{A}}(t)$ делит $\tilde{\mu}_{\mathcal{A}}(t)$. То есть $\mu_{\mathcal{A}}(t) = \lambda\tilde{\mu}_{\mathcal{A}}(t)$, а следовательно эти многочлены совпадают, так как коэффицент при старшем члене о минимального многочлена $1 \,\,\,\,\blacksquare$ 
3. По свойству $1$ множество корней минимального многочлена является подмножеством корней характеристического. Пусть $\lambda$ корень $\chi_{\mathcal{A}}(t)$. Значит существует собственный вектор $e$ оператора $\mathcal{A}$, отвечающий значению $\lambda$. Для любого $f(t) \in F[t] \,\,\,\, f(\mathcal{A})(e) = f(\lambda)e \Rightarrow 0 = \mu_{\mathcal{A}}(\mathcal{A})(e) = \mu_{\mathcal{A}}(\lambda)e \Rightarrow (e \ne 0) \,\,\,\, \mu_{\mathcal{A}}(\lambda) = 0 \,\,\,\,\blacksquare$

## Жорданова нормальная форма

---

### Определения

**Определение:**<a name="definition-2"></a> Квадратная матрица вида $\operatorname{J}_k(\lambda) = \left(\begin{array}{ccccc}
\lambda & 1 & 0 & \dots & 0\\
0 & \lambda & 1 & \dots & 0\\
\vdots & \ddots & \ddots & \ddots & \vdots\\
0 & \dots & 0 & \lambda & 1\\
0 & \dots & 0 & 0 & \lambda\\
\end{array}\right)$ - *жорданова клетка* с $\lambda$ на диагонали размера $k$.

Обозначение: $\operatorname{J}_k(\lambda)$.

**Определение:**<a name="definition-3"></a> Квадратная матрица размера $n \times n$, состоящая из жордановых клеток на диагонали и нулей на остальных местах - это *жорданова матрица* размера $n \times n$.

**Определение:**<a name="definition-4"></a> Пусть $V$ - векторное пространство, $\mathcal{A}$ - линейный оператор на $V$. Если существует базис, в котором матрица $\mathcal{A}$ жорданова, то такой базис - *жорданов*, а сама матрица *жорданова нормальная форма* линейного оператора $\mathcal{A}$.

### Простейшие свойства

**Утверждение:**<a name="statement-1"></a> Пусть матрица линейного оператора $\mathcal{A}$ имеет жорданову нормальную форму размера $n \times n$ и состоит из жордановых клеток $\operatorname{J}_{k_1}(\lambda_1), \ldots, \operatorname{J}_{k_s}(\lambda_s)$. Тогда

1. $\chi_{\mathcal{A}}(t) = (-1)^n \displaystyle \prod_{i = 1}^{s}(t - \lambda_i)^k_i$.
2. Жорданов базис $\mathcal{A}$ состоит из объединения жордановых базисов клеток $\operatorname{J}_{k_1}(\lambda_1), \ldots, \operatorname{J}_{k_s}(\lambda_s)$.

*Доказательство:*

1. очев $\,\,\,\,\blacksquare$
2. не очев $\,\,\,\,\blacksquare$

**Утверждение:**<a name="statement-2"></a> 

1. $\operatorname{J}_{k}(0)^m = \begin{cases}
    m,\,\,\,\, m < k\\
    0,\,\,\,\, m \ge k
\end{cases}$
2. $\mu_{\operatorname{J}_{k}(\lambda)}(t) = (t - \lambda)^k$
3. $\mu_{\operatorname{J}_n}$ - это наименьшее общее кратное всех минимальных многочленов ее жордановых клеток.
4. $\operatorname{rk}(\operatorname{J}_k(\lambda) - \alpha E)^m = \begin{cases}
    k,\,\,\,\, \lambda \ne \alpha\\
    k - m,\,\,\,\, \lambda = \alpha, k \ge m\\
    0,\,\,\,\, \lambda = \alpha, k < m
\end{cases}$

*Доказательство:* все кроме $3$ очевидно $\,\,\,\,\blacksquare$
3. 

**Утверждение:**<a name="statement-3"></a> Пусть $V$ - векторное пространство размерности $n$. Пусть матрица линейного оператора $\mathcal{A}$ в некотором базисе имеет жорданову нормальную форму $\operatorname{J}_n$. Тогда $\dim V_{\lambda}$ равно количеству жордановых клеток в матрице $\mathcal{A}$ с $\lambda$ на диагонали.

*Доказательство:* $V_{\lambda} = \{v \in V: \,\,\,\, \mathcal{A}(v) = \lambda v\}$, а это множество решений $\mathcal{A} - \lambda \mathcal{I} = 0$ или $\operatorname{J}_n - \lambda E = 0$. Следовательно, $\dim V_{\lambda} = n - \operatorname{rk}\operatorname{J}_n$. Ранг жордановой матрицы - это сумма рангов составляющих ее клеток $J_{k_1}(\lambda_1), \ldots, J_{k_s}(\lambda_s)$, а ранг жордановой клетки $\operatorname{J}_k(\lambda) = \begin{cases}
    k, \lambda \ne 0\\
    k - 1, \lambda = 0
\end{cases}$. То есть $n - \operatorname{rk}\operatorname{J}_n = \displaystyle \sum_{i = 1}^{s}k_i - \displaystyle \sum_{i = 1}^{s}\operatorname{rk}J_{k_i}(\lambda_i)$ значение этого выражения равно $1$ на всех клетках с $\lambda$ на диагонали и $0$ на остальных $\,\,\,\,\blacksquare$

