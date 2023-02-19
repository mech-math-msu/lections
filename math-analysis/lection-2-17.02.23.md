## Интегрируемость непрерывных и монотонных функций

---

**Теорема:**<a name="theorem-0"></a> Пусть $f(x) \in C[a, b]$, тогда $f(x) \in R[a, b]$.

*Доказательство:* $\forall \varepsilon > 0$ возьмем $\delta = \varepsilon$, тогда $\forall \mathcal{T}(\xi) (d(\mathcal{T}) < \delta = \varepsilon) \,\,\,\, S(\mathcal{T}) - s(\mathcal{T}) = \displaystyle \sum_{i = 1}^{n}(\sup_{\Delta x_i}(f(x)) - \inf_{\Delta x_i}(f(x)))(x_{i} - x_{i - 1})$
$$= \displaystyle \sum_{i = 1}^{n}(\max_{\Delta x_i}(f(x)) - \min_{\Delta x_i}(f(x)))(x_{i} - x_{i - 1})$$
$$= \displaystyle \sum_{i = 1}^{n}(f(x_{max_i}) - f(x_{min_i}))(x_{i} - x_{i - 1}) \le \displaystyle \sum_{i = 1}^{n}\varepsilon (x_{i} - x_{i - 1}) < \varepsilon (b - a) \,\,\,\,\blacksquare$$

**Теорема:**<a name="theorem-1"></a> Пусть $f(x)$ монотонна на $[a, b]$, тогда $f(x) \in R[a, b]$.

*Доказательство:* Пусть $f(x)$ монотонно возрастает. $\forall \varepsilon > 0$ возьмем $\delta = \varepsilon$, тогда $\forall \mathcal{T}(\xi) (d(\mathcal{T}) < \delta = \varepsilon) \,\,\,\, S(\mathcal{T}) - s(\mathcal{T}) = \displaystyle \sum_{i = 1}^{n}(\sup_{\Delta x_i}(f(x)) - \inf_{\Delta x_i}(f(x)))(x_{i} - x_{i - 1}) =$
$$=\displaystyle \sum_{i = 1}^{n}(f(x_i) - f(x_{i - 1}))(x_{i} - x_{i - 1})=$$
$$= \displaystyle \sum_{i = 1}^{n}(f(x_i) - f(x_{i - 1}))\varepsilon < \varepsilon (f(b) - f(a)) \,\,\,\,\blacksquare$$

**Определение:**<a name="definition-0"></a> Множество $A \subset \mathbb{R}$ *имеет лебегову меру* $0$, если $\forall \{(a_i, b_i)\}_i: \,\,\,\, A \subset \displaystyle\cup_i (a_i, b_i) \,\,\,\, \displaystyle\sup_{N < \infty}\displaystyle \sum_{i = 1}^{N}|b_i - a_i| < \varepsilon$.

**Теорема:**<a name="theorem-2"></a> $f(x) \in R[a, b] \Leftrightarrow$ множество предельных точек $f(x)$ на $[a, b]$ имеет лебегову меру $0$.

*Доказательство:* $\,\,\,\,\blacksquare$

## Основные свойства интегрируемых по Риману функций

---

1. (Интегрируемость на подотрезках)

**Утверждение:**<a name="statement-0"></a> Пусть $f(x) \in R[a, b]$, тогда $f(x) \in R[a^{*}, b^{*}]$, если $[a^{*}, b^{*}] \subset [a, b]$.

*Доказательство:* Пусть $\mathcal{T}_{[a, b]}$ некоторое разбиение $[a, b]$, $\mathcal{T}_[a, b]^{*} = \mathcal{T}_{[a, b]} \cup \{a^{*}, b^{*}\}$. 

Тогда $\varepsilon > S(\mathcal{T}_{[a, b]}) - s(\mathcal{T}_{[a, b]}) \ge S(\mathcal{T}_{[a, b]}^{*}) - s(\mathcal{T}_{[a, b]}^{*})$
$$= S(\mathcal{T}_{[a, a^{*}]}) + S(\mathcal{T}_{[a^{*}, b^{*}]}) + S(\mathcal{T}_{[b^{*}, b]}) - s(\mathcal{T}_{[a, a^{*}]}) - s(\mathcal{T}_{[a^{*}, b^{*}]}) - s(\mathcal{T}_{[b^{*}, b]})\ge$$
$$\ge S(\mathcal{T}_{[a^{*}, b^{*}]}) - s(\mathcal{T}_{[a, a^{*}]}) \,\,\,\,\blacksquare$$

Здесь использованы свойства сумм Дарбу. Где и какие?

2. (Аддитивность)

**Утверждение:**<a name="statement-1"></a> Пусть $f(x) \in R[a, b]$ и $f(x) \in R[b, c]$, тогда $f(x) \in R[a, c]$ и $$\displaystyle\int\limits_a^c f(x)dx = \displaystyle\int\limits_a^b f(x)dx + \displaystyle\int\limits_b^c f(x)dx$$

*Доказательство:* Пусть  $b \in \Delta x_j = [x_{j - 1}, x_j]$.
$$S(\mathcal{T}_{[a, c]}) - s(\mathcal{T}_{[a, c]}) = S(\mathcal{T}_{[a, c]} \cap \{b\}) - s(\mathcal{T}_{[a, c]} \cap \{b\})+$$
$$+ \displaystyle\sup_{\Delta_j}f(x)(x_j - x_{j - 1}) - \displaystyle\inf_{\Delta_j}f(x)(x_j - x_{j - 1}) - \displaystyle\sup_{[x_{j - 1}, b]}f(x)(b - x_{j - 1}) - \displaystyle\sup_{[b, x_j]}f(x)(x_j - b)+$$
$$+ \displaystyle\inf_{[x_{j - 1}, b]}f(x)(b - x_{j - 1}) + \displaystyle\inf_{[b, x_j]}f(x)(x_j - b) < 7 \varepsilon \,\,\,\,\blacksquare$$

3. (Линейность)

**Утверждение:**<a name="statement-2"></a> Пусть $f(x), g(x) \in R[a, b], \,\,\,\, \lambda, \mu \in \mathbb{R}$, тогда $$\lambda f(x) + \mu g(x) \in R[a, b]$$

*Доказательство:* $$S_{\lambda f(x) + \mu g(x)}(\mathcal{T}) - s_{\lambda f(x) + \mu g(x)}(\mathcal{T})=$$
$$=\lambda S_{f(x)}(\mathcal{T}) + \mu S_{g(x)}(\mathcal{T}) - \lambda s_{f(x)}(\mathcal{T}) - \mu s_{g(x)}(\mathcal{T})=$$
$$= \lambda (S_{f(x)}(\mathcal{T}) - s_{f(x)}(\mathcal{T})) + \mu (S_{g(x)} - s_{g(x)}(\mathcal{T})) < (\lambda + \mu) \varepsilon \,\,\,\,\blacksquare$$
