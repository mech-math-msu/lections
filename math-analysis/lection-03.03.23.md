## Вторая теорема о средних

---

**Теорема:**<a name="theorem-0"></a> Пусть $f(x) \in C[a, b], \,\,\,\, g(x) \in C^1[a, b], \,\,\,\, g(x)$ - монотонно возрастает. Тогда $\exists c \in [a, b]$:

$$\displaystyle\int\limits_a^b f(x)g(x)dx = g(a)\displaystyle\int\limits_a^c g(x)dx + g(b)\displaystyle\int\limits_c^b f(x)dx$$

*Доказательство:* $F(x) = \displaystyle\int\limits_x^b f(t)dt$

$$\displaystyle\int\limits_a^b f(x)g(x)dx = -\displaystyle\int\limits_a^b g(x)dF(x) = -\left.g(x)F(x)\right|_{a}^{b} + \displaystyle\int\limits_a^b F(x)g’(x)dx=$$
$$= g(a) \displaystyle\int\limits_a^b f(x)dx + F(c) \displaystyle\int\limits_a^b g’(x)dx=$$
$$= g(a) \displaystyle\int\limits_a^b f(x)dx + \displaystyle\int\limits_c^b f(x)dx (g(b) - g(a))=$$
$$= g(a)\displaystyle\int\limits_a^c g(x)dx + g(b)\displaystyle\int\limits_c^b f(x)dx \,\,\,\,\blacksquare$$

## Кривые

---

**Определение:**<a name="definition-1"></a> Отображение $\gamma: [a, b] \to \mathbb{R}^n, \,\,\,\, \gamma(t): t \in [a, b] \mapsto (x_1(t), \ldots, x_n(t))$ - *непрерывно* на $[a, b]$, если $x_i(t)$ - непрерывно на $[a, b] \,\,\,\, \forall i \in \{1, \ldots, n\}$.

**Определение:**<a name="definition-0"></a> Непрерывное отображение $\gamma: [a, b] \to \mathbb{R}^n$ - это *(непрерывная) кривая*.

$t \in [a, b] \,\,\,\, \gamma(t) = (x_1(t), \ldots, x_n(t))$, где $x_1(t)$ - *первая координата*...

$\forall t \in [a, b] \,\,\,\, M = \gamma(t)$ - *точка* кривой $\gamma$.

Если $\exists t_1 \ne t_2 (t_1, t_2 \in [a, b]): \,\,\,\, M = \gamma(t_1) = \gamma(t_2)$, то $M$ *точка самопересечения* кривой $\gamma$.

$\operatorname{card}\{t: \,\,\,\, M = \gamma(t), \,\,\,\, t \in [a, b]\}$ - *кратность* точки $M$.

Если точек самопересечения нет, то кривая $\gamma$ - *простая*.

Если существует единственная точка самопересечения и ее кратность равна $2$, то кривая $\gamma$ - *простая замкнутая*.

**Определение:**<a name="definition-2"></a> Пусть $\mathcal{T} = \{t_i\}_{i = 0}^k$ разбиение $[a, b]$, $\gamma$ - кривая.

$|l_{\gamma}(\mathcal{T})| = \displaystyle \sum_{i = 1}^{k}|\gamma(t_i) - \gamma(t_{i - 1})|$ - *длина ломаной*, отвечающей разметке $\mathcal{T}$.

**Лемма:**<a name="lemma-0"></a> Если $\mathcal{T}_1 \subset \mathcal{T}_2$, то 
$$|l_{\gamma}(\mathcal{T}_1)| \le |l_{\gamma}(\mathcal{T}_2)|$$

*Доказательство:* $\mathcal{T}_2 \setminus \mathcal{T}_1 = \{t^{*}\}, \,\,\,\, t_{j - 1} < t^{*} < t_j$. <br>$|l_{\gamma}(\mathcal{T}_2)| - |l_{\gamma}(\mathcal{T}_1)| \ge 0$ - неравенство треугольника в плоскости $\{\gamma(t_{j - 1}), \gamma(t^{*}), \gamma(t_{j})\} \,\,\,\,\blacksquare$

**Определение:**<a name="definition-3"></a> Пусть $\gamma$ - кривая. Если множество $\{|l_{\gamma}(\mathcal{T})|\}_{\mathcal{T}}$ ограничено сверху, то $\gamma$ *спрямляемая* и $\sup \{|l_{\gamma}(\mathcal{T})|\}_{\mathcal{T}} = |\gamma|$ - *длина кривой* $\gamma$.

**Теорема:**<a name="theorem-1"></a> Пусть $\gamma(t) \in C^1[a, b]$. Тогда $\gamma$ - спрямляемая и
$$|\gamma| = \displaystyle\int\limits_a^b \sqrt{\displaystyle \sum_{i = 1}^{n} x_i’^2(t)} dt$$

*Доказательство:* Докажем, что $\gamma$ спрямляемая, то есть $\{|l_{\gamma}(\mathcal{T})|\}_{\mathcal{T}}$ ограничено сверху.
$$|l_{\gamma}(t)| = \displaystyle \sum_{j = 1}^{m} \sqrt{\displaystyle \sum_{i = 1}^{n}(x_i(t_j) - x_i(t_{j - 1}))^2} =$$
$$=\displaystyle \sum_{j = 1}^{m} \sqrt{\displaystyle \sum_{i = 1}^{n}x_i’^2(\xi_{ij}) (t_j - t_{j - 1})^2} = \displaystyle \sum_{j = 1}^{m} \sqrt{\displaystyle \sum_{i = 1}^{n}x_i’^2(\xi_{ij})} |t_j - t_{j - 1}|\le$$
$$\le M \sqrt{n} (b - a)$$
Следовательно, $\gamma$ спрямляемая.

**Лемма:**<a name="lemma-1"></a> $$\sqrt{\displaystyle \sum_{i = 1}^{n}x_i^2} - \sqrt{\displaystyle \sum_{i = 1}^{n}y_i^2} \le \displaystyle \sum_{i = 1}^{n}|x_i - y_i|$$

*Доказательство:* домножить на сопряженное и поколдовать $\,\,\,\,\blacksquare$

$f(t) = \sqrt{\displaystyle \sum_{i = 1}^{n} x_i’^2(t)}$ - композиция суммы непрерывных функций непрерывна, а следовательно $$\exists \displaystyle\int\limits_a^b \sqrt{\displaystyle \sum_{i = 1}^{n} x_i’^2(t)} dt = I$$

1. $$\forall \varepsilon > 0 \,\,\,\, \exists \delta_1 > 0: \,\,\,\, \forall \mathcal{T} (d(\mathcal{T}) < \delta_1) \,\,\,\, |\sigma_f(\mathcal{T}) - I| < \varepsilon$$
2. $$||l_{\gamma}(\mathcal{T})| - \sigma_f(\mathcal{T})| = \left|\displaystyle \sum_{j = 1}^{m} \sqrt{\displaystyle \sum_{i = 1}^{n}x_i’^2(\xi_{ij})} |t_j - t_{j - 1}| - \sigma_f(\mathcal{T})\right|=$$
$$=\left|\displaystyle \sum_{j = 1}^{m} \sqrt{\displaystyle \sum_{i = 1}^{n}x_i’^2(\xi_{ij})} |t_j - t_{j - 1}| - \displaystyle \sum_{j = 1}^{m}\sqrt{\displaystyle \sum_{i = 1}^{n} x_i’^2(\xi_j)}|t_j - t_{j - 1}|\right| \le$$
$$\le \left|\displaystyle \sum_{j = 1}^{m} \displaystyle \sum_{i = 1}^{n}|x_i’(\xi_{ij}) - x_i’(\xi_j)| |t_j - t_{j - 1}|\right|$$ 
$$\forall \varepsilon > 0 \,\,\,\, \exists \delta_2 > 0: \,\,\,\, \forall \xi_{ij}, \xi_j: \,\,\,\, |\xi_{ij} - \xi_j| < \delta \,\,\,\, |x_i’(\xi_{ij}) - x_i’(\xi_j)| < \varepsilon \Rightarrow$$
$$\forall \frac{\varepsilon}{n(b - a)} \,\,\,\, ||l_{\gamma}(t)| - \sigma_f(\mathcal{T})| < \varepsilon$$
3. $$|\gamma| = \sup_{\mathcal{T}}\{|l_{\gamma}(\mathcal{T})|\} \Rightarrow |\gamma| - |l_{\gamma}(\mathcal{T})| < \varepsilon$$

$$\Downarrow$$

$$|\gamma| - I < \varepsilon \Rightarrow I = |\gamma| \,\,\,\,\blacksquare$$


