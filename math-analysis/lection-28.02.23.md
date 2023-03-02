## Интеграл с переменным верхним пределом

---

**Теорема:**<a name="theorem-0"></a> Пусть $f(x) \in R[a, b]$. Тогда $F(x) = \displaystyle\int\limits_a^x f(t)dt$ непрерывна на отрезке $[a, b]$.

*Доказательство:* $f(x) \in R[a, b] \Rightarrow \exists c > 0: \,\,\,\, |f(x)| < c \,\,\,\, \forall x \in [a, b]$.
$|F(x + \Delta) - F(x)| = \left|\displaystyle\int\limits_a^{x + \Delta x} f(t)dt - \displaystyle\int\limits_a^{x} f(t)dt\right|=$
$= \left|\displaystyle\int\limits_{x}^{x + \Delta x} f(t)dt\right| \le \left|\displaystyle\int\limits_{x}^{x + \Delta x} |f(t)|dt \right| \le |\Delta x|c \,\,\,\,\blacksquare$

**Теорема:**<a name="theorem-1"></a> Пусть $f(x) \in R[a, b]$, $f(x)$ непрерывна в точке $x_0 \in [a, b]$. Тогда $F(x) = \displaystyle\int\limits_a^x f(t)dt$ дифференцируема в точке $x_0$ и $F’(x_0) = f(x_0)$.

*Доказательство:* $\forall \varepsilon > 0 \,\,\,\, \exists \delta > 0: \,\,\,\, \forall t: 0 < |t - x_0| < \delta \,\,\,\, |f(t) - f(x_0)| < \varepsilon$.
$\left|\frac{1}{\Delta x}(F(x + \Delta x) - F(x)) - f(x_0)\right| = \left|\frac{1}{\Delta x}\left(\displaystyle\int\limits_a^{x + \Delta x} f(t)dt - \displaystyle\int\limits_a^{x} f(t)dt\right) - f(x_0)\right|=$

$= \left|\frac{1}{\Delta x}\displaystyle\int\limits_x^{x + \Delta x} f(t)dt - \frac{1}{\Delta x}\displaystyle\int\limits_x^{x + \Delta x} f(x_0)dt\right| = \left|\frac{1}{\Delta x}\displaystyle\int\limits_x^{x + \Delta x} (f(t) - f(x_0))dt\right|\le$

$\le \left|\frac{1}{\Delta x}\right|\left|\displaystyle\int\limits_x^{x + \Delta x} |f(t) - f(x_0)|dt\right| \le \varepsilon \left|\frac{1}{\Delta x}\right|\left|\Delta x\right| = \varepsilon \,\,\,\,\blacksquare$

**Следствие:**<a name="corollary-0"></a> Пусть $f(x) \in R[a, b]$ и $f(x) \in C(a, b)$. Тогда $F(x) = \displaystyle\int\limits_a^x f(t)dt$ - первообразная $f(x)$ на $(a, b)$ и $F(x) \in C[a, b]$.

### Формула Ньютона-Лейбница

---

**Теорема:**<a name="theorem-2"></a> (формула Ньютона-Лейбница) Пусть $f(x) \in R[a, b]$, $\Phi(x)$ - первообразная $f(x)$ на $(a, b)$. Тогда $$\displaystyle\int\limits_a^b f(x)dx = \Phi(b) - \Phi(a)$$

*Доказательство:* $\displaystyle\int\limits_a^x f(t)dt = \Phi(x) + C$, так как [один](https://mech-math-msu.github.io/lections/math-analysis/lection-1-07.02.23#theorem-0) и [два](#corollary-0). Подставим $x = a \Rightarrow C = -\Phi(a) \Rightarrow \displaystyle\int\limits_a^x f(t)dt = \Phi(x) - \Phi(a)$, подставляя $x = b$, получаем требуемое равенство $\,\,\,\,\blacksquare$

**Теорема:**<a name="theorem-3"></a> (обобщение формулы Ньютона-Лейбница) Пусть $f(x) \in R[a, b]$ и $f(x) \in C([a, b] \setminus \{x_i\}_{i = 1}^n)$, $\Phi(x) \in C^([a, b])$, $\Phi’(x) = f(x) \,\,\,\, \forall x \in [a, b] \setminus \{x_i\}_{i = 1}^n$. Тогда $$\displaystyle\int\limits_a^b f(x)dx = \Phi(b) - \Phi(a)$$

*Доказательство:* Пусть $x_0 = a, \,\,\,\, x_{n + 1} = b$. Тогда $\displaystyle\int\limits_a^b f(x)dx = \displaystyle \sum_{i = 0}^{n}\displaystyle\int\limits_{x_i}^{x_{i + 1}} f(x)dx = \displaystyle \sum_{i = 0}^{n} \Phi(x_{i + 1}) - \Phi(x_{i}) = \Phi(b) - \Phi(a) \,\,\,\,\blacksquare$

## Интегрирование по частям и замена переменной для определенного интеграла

---

**Теорема:**<a name="theorem-4"></a> (замена переменной при интегрировании определенного интеграла) Пусть $f(x) \in R[a, b], \,\,\,\, \varphi(t) \in C^{1}[\alpha, \beta]$($\varphi(x)$ непрерывна, и ее производная непрерывна), $\varphi([\alpha, \beta]) \subset [a, b], \,\,\,\,\varphi(\alpha) = a, \,\,\,\, \varphi(\beta) = b$. Тогда 
$$\displaystyle\int\limits_a^b f(x)dx = \displaystyle\int\limits_{\alpha}^{\beta} f(\varphi(t))\varphi’(t)dt$$

*Доказательство:* Пусть $\Phi(x)$ - первообразная $f(x)$ на $(a, b) \Rightarrow \Phi(\varphi(t))$ - первообразная для $f(\varphi(t))\varphi’(t)$.
$$\displaystyle\int\limits_{\alpha}^{\beta} f(\varphi(t))\varphi’(t) = \Phi(\varphi(\beta)) - \Phi(\varphi(\alpha)) = \displaystyle\int\limits_a^b f(x)dx \,\,\,\,\blacksquare$$

**Теорема:**<a name="theorem-5"></a> (интегрирование по частям определенного интеграла) Пусть $f(x), g(x) \in R[a, b]$. Тогда $$\displaystyle\int\limits_a^b f(x)g’(x)dx = \left.f(x)g(x)\right\rvert_{a}^{b} - \displaystyle\int\limits_a^b f’(x)g(x)dx$$

*Доказательство:* $$\left.f(x)g(x)\right\rvert_{a}^{b} = \displaystyle\int\limits_a^b \left(f(x)g(x)\right)’dx \,\,\,\,\blacksquare$$

