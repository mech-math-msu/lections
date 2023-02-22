## Свойства интеграла Римана

---

4. **Утверждение:**<a name="statement-0"></a> Пусть $f(x) \in R[a, b]$. Тогда $$\displaystyle\int\limits_a^b f(x)dx \le \displaystyle\sup_{[a, b]} |f(x)| |b - a|$$

*Доказательство:* $\forall \mathcal{T}(\xi) \,\,\,\, |\sigma_f(\mathcal{T}(\xi))| = |\displaystyle \sum_{i = 1}^{n}f(\xi_i)(x_{i} - x_{i - 1})| \le \displaystyle\sup_{[a, b]} |f(x)| |b - a| \,\,\,\,\blacksquare$

5. **Утверждение:**<a name="statement-1"></a> Пусть $f(x) \in R[a, b], \,\,\,\, a > b$. Тогда $|f(x)| \in R[a, b]$ и $$\left|\displaystyle\int\limits_a^b f(x)dx\right| \le \displaystyle\int\limits_a^b |f(x)|dx$$

*Доказательство:* $$||f(x_2)| - |f(x_1)|| \le |f(x_2) - f(x_1)| \,\,\,\,\blacksquare$$

6. **Утверждение:**<a name="statement-2"></a> $$f(x) \ge 0 \Rightarrow \displaystyle\int\limits_a^b f(x)dx \ge 0$$

*Доказательство:* $$\forall \mathcal{T}(\xi) \,\,\,\, \sigma_f(\mathcal{T}(\xi)) \ge 0 \,\,\,\,\blacksquare$$

7. **Утверждение:**<a name="statement-3"></a> Пусть $f(x) \in R[a, b], \,\,\,\, f(x) \ge 0 \,\,\,\, \forall x \in [a, b], \,\,\,\, \exists c \in [a, b]: \,\,\,\, f(c) > 0$ и $f(x)$ непрерывна в точке $c$. Тогда $$\displaystyle\int\limits_a^b f(x)dx > 0$$

*Доказательство:* $$\forall \varepsilon > 0 \,\,\,\, \exists \delta > 0: \,\,\,\, \forall x: 0 < |x - c| < \delta \,\,\,\, |f(x) - f(c)| < \varepsilon$$
Пусть $\varepsilon = \frac{f(c)}{2} \Rightarrow \forall x \in (c - \delta, c + \delta) \,\,\,\, f(x) > \frac{f(c)}{2} \Rightarrow \displaystyle\int\limits_{c - \delta}^{c + \delta} f(x)dx > \frac{f(c)}{2} > 0 \Rightarrow \displaystyle\int\limits_a^b f(x)dx > 0 \,\,\,\,\blacksquare$

8. **Утверждение:**<a name="statement-4"></a> $$f(x), g(x) \in R[a, b] \Rightarrow f(x)g(x) \in R[a, b]$$

*Доказательство:* $|f(x_2)g(x_2) - f(x_1)g(x_1)| = |f(x_2)||g(x_2) - g(x_1)| + |g(x_1)||f(x_2) - f(x_1)| \,\,\,\,\blacksquare$

9. **Утверждение:**<a name="statement-5"></a> Пусть $f(x) \in R[a, b]$ и $\exists \delta > 0: \,\,\,\, \forall x \in [a, b] \,\,\,\, f(x) > \delta$. Тогда $\frac{1}{f(x)} \in R[a, b]$.

*Доказательство:* $$\frac{1}{f(x)} \le \frac{1}{\delta}$$
$$\left|\frac{1}{f(x_2)} - \frac{1}{f(x_1)}\right| \le \frac{1}{\delta^2}|f(x_2) - f(x_1)| \,\,\,\,\blacksquare$$

## Первая теорема о среднем

---

**Теорема:**<a name="theorem-0"></a> Пусть $f(x), g(x) \in R[a, b], \,\,\,\, g(x) \ge 0, \,\,\,\, m = \displaystyle\inf_{[a, b]} f(x), \,\,\,\, M = \displaystyle\sup_{[a, b]} f(x)$. Тогда $$\exists \mu \in [m, M]: \,\,\,\, \displaystyle\int\limits_a^b f(x)g(x)dx = \mu\displaystyle\int\limits_a^b g(x)dx$$

*Доказательство:* $$m g(x) \le g(x)f(x) \le M g(x) \Rightarrow$$
$$m \displaystyle\int\limits_a^b g(x)dx \le \displaystyle\int\limits_a^b f(x)g(x)dx \le M\displaystyle\int\limits_a^b g(x)dx$$
Если $\displaystyle\int\limits_a^b g(x)dx \ne 0$, то возьме в качестве $\mu = \,\,\,\, \frac{\displaystyle\int\limits_a^b f(x)g(x)dx}{\displaystyle\int\limits_a^b g(x)dx}$.

Иначе, любое $\mu$ подходит $\,\,\,\,\blacksquare$

