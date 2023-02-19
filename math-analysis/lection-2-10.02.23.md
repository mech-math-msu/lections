## Определенный интеграл

---

**Определение:**<a name="definition-0"></a> *Положительное разбиение* отрезка $[a, b]$ - это множество точек $\{x_i\}_{i = 0}^{n}$, таких что $a = x_0 < x_1 < \ldots < x_{n - 1} < x_n = b$. 
Обозначается: $\mathcal{T}_{[a, b]}^{+}$.

**Определение:**<a name="definition-1"></a> *Отрицательное разбиение* отрезка $[a, b]$ - это множество точек $\{x_i\}_{i = 0}^{n}$, таких что $b = x_0 > x_1 > \ldots > x_{n - 1} > x_n = a$. 
Обозначается: $\mathcal{T}_{[a, b]}^{-}$.

**Определение:**<a name="definition-2"></a> Пусть дано разбиение $\mathcal{T}_{[a, b]} = \{x_i\}_{i = 0}^{n}$ отрезка $[a, b]$.

$i$-й *отрезок разбиения* $\mathcal{T}_{[a, b]}$ - это $\Delta_i = [x_{i - 1}, x_i] \,\,\,\, \forall i \in \{1, \ldots, n\}$.<br>

*длина* $\Delta_i$ равна $|\Delta_i| = |x_{i} - x_{i - 1}|$.<br>

*диаметр разбиения* $d(\mathcal{T}_{[a, b]})$ - это $\displaystyle \max_{i \in \{1, \ldots, n\}}{|\Delta_i|}$.

**Определение:**<a name="definition-3"></a> Пусть дано разбиение $\mathcal{T}_{[a, b]} = \{x_i\}_{i = 0}^{n}$ отрезка $[a, b]$.
*Разметка* $\mathcal{T}_{[a, b]}$ - это множество точек $\xi = \{\xi_1, \xi_2, \ldots, \xi_n\}$, таких что $\xi_i \in \Delta_i$.
Разбиение с заданной разметкой обозначается $\mathcal{T}(\xi)_{[a, b]} = \{\mathcal{T}, \xi\}$.

**Определение:**<a name="definition-4"></a> *Интегральная сумма* - это $\sigma_{f}(\mathcal{T}(\xi)) = \displaystyle \sum_{i = 1}^{n}f(\xi_i)\cdot(x_i - x_{i - 1})$.

**Определение:**<a name="definition-5"></a> Пусть $f(x)$ определена на $[a, b]$. Если $\exists I \in \mathbb{R}$, такое что 
$$\forall \varepsilon > 0 \,\,\,\, \exists \delta > 0: \,\,\,\, \forall \mathcal{T}_{[a, b]}^{+}(\xi) \left(d(\mathcal{T}_{[a, b]}^{+}) < \delta\right) \,\,\,\, |\sigma_{f}(\mathcal{T}(\xi)) - I| < \varepsilon,$$
то функция $f(x)$ *интегрируема по Риману* на отрезке $[a, b]$, а число $I$ - *интеграл* $f(x)$ на отрезке $[a, b]$. Обозначается $I = \displaystyle \int\limits_a^b f(x)dx$.

**Определение:**<a name="definition-6"></a> Пусть $f(x)$ определена на $[a, b]$. Если $\exists I \in \mathbb{R}$, такое что 
$$\forall \varepsilon > 0 \,\,\,\, \exists \delta > 0: \,\,\,\, \forall \mathcal{T}_{[a, b]}^{-}(\xi) \left(d(\mathcal{T}_{[a, b]}^{-}) < \delta\right) \,\,\,\, |\sigma_{f}(\mathcal{T}(\xi)) - I| < \varepsilon,$$
то функция $f(x)$ *интегрируема по Риману* на отрезке $[a, b]$, а число $I$ - *интеграл* $f(x)$ на отрезке $[a, b]$. Обозначается $I = \displaystyle \int\limits_b^a f(x)dx$.

**Утверждение:**<a name="statement-0"></a> $$\displaystyle \int\limits_a^b f(x)dx = -\displaystyle \int\limits_{b}^{a} f(x)dx$$

*Доказательство:* нуу, очев $\,\,\,\,\blacksquare$

**Определение:**<a name="definition-7"></a> Множество всех функций интегрируемых по Риману на отрезке $[a, b]$ обозначается $\mathcal{R}[a, b]$.

**Теорема:**<a name="theorem-0"></a> Если функция $f(x) \in \mathcal{R}[a, b]$, то $f(x)$ ограничена на $[a, b]$.

*Доказательство:* (от противного) Пусть $f(x)$ неограничена на $[a, b]$, то есть $\forall x \in \mathbb{R} \,\,\,\, \exists \xi \in [a, b]: \,\,\,\, f(\xi) > x$.
$\exists \displaystyle\int\limits_a^b f(x)dx = I$. Возьмем $\varepsilon = 1$, имеем
$$\exists \delta > 0: \,\,\,\, \forall \mathcal{T}_{[a, b]}^{+}(\xi) \left(d(\mathcal{T}_{[a, b]}^{+}) < \delta\right) \,\,\,\, |\sigma_{f}(\mathcal{T}(\xi)) - I| < 1$$

$$I - 1 < \displaystyle \sum_{i = 1}^{n}f(\xi_i)\cdot(x_i - x_{i - 1}) < I + 1$$

Зафиксируем разметку $\xi$. $f(x)$ неограничена на одном из $\Delta_i$. Будем менять $\xi_i \in \Delta_i$. $|f(\xi_i)|$ принимает сколь угодно большое значение, а значит сумма не будет ограничена $\,\,\,\,\blacksquare$
