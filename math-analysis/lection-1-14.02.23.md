## Суммы Дарбу

---

**Определение:**<a name="definition-0"></a> 
Пусть $f(x)$ ограничена на отрезке $[a, b]$. $\mathcal{T}_{[a, b]}^{+}$ - некоторое разбиение отрезка $[a, b]$.
Пусть 
$m_i = \displaystyle \inf_{x\in \Delta_i}f(x)$ (точная нижняя грань $f(x)$ на $i$-ом отрезке разбиения $\mathcal{T}_{[a, b]}^{+}$), $M_i = \displaystyle \sup_{x\in \Delta_i}f(x)$.

$s(\mathcal{T}) = \displaystyle \sum_{i = 1}^{n} m_i\cdot (x_{i} - x_{i - 1})$ - это *нижняя сумма Дарбу* функции $f(x)$ по разбиению $\mathcal{T}_{[a, b]}^{+}$.

$S(\mathcal{T}) = \displaystyle \sum_{i = 1}^{n} M_i\cdot (x_{i} - x_{i - 1})$ - это *верхняя сумма Дарбу* функции $f(x)$ по разбиению $\mathcal{T}_{[a, b]}^{+}$.

## Свойства сумм Дарбу

---

**Лемма:**<a name="lemma-0"></a> Пусть $\{X_i: \,\,\,\, X_i \subset \mathbb{R}\}_{i = 1}^n$, $X_i$ - ограничено $\forall i \in \{1, \ldots, n\}$. $\{a_i: \,\,\,\, a_i \ge 0\}_{i = 1}^n$. Тогда 
$$\displaystyle\sup_{x_i \in X_i}\left\{\sum_{i = 1}^{n}a_ix_i\right\} = \displaystyle \sum_{i = 1}^{n}a_i \displaystyle\sup\left(X_i\right)$$
$$\displaystyle\inf_{x_i \in X_i}\left\{\sum_{i = 1}^{n}a_ix_i\right\} = \displaystyle \sum_{i = 1}^{n}a_i \displaystyle\inf\left(X_i\right)$$

Точная верхняя грань сумм - это точная верхняя грань множества всех сумм вида $\displaystyle \sum_{i = 1}^{n}a_ix_i$, где $x_i \in X_i$.

*Доказательство:* $$\forall \varepsilon \,\,\,\, \forall i \,\,\,\, \exists x_i \in X_i:\,\,\,\, x_i > \sup X_i - \varepsilon$$
Домножая каждую сумму неравенства на $a_i$ и суммируя по $i$, получаем:

$$\forall \varepsilon > 0 \,\,\,\, \exists \{x_i \in X_i\}_{i = 1}^n:\,\,\,\,\displaystyle \sum_{i = 1}^{n}a_ix_i > \displaystyle \sum_{i = 1}^{n}a_i\sup X_i - \varepsilon \displaystyle \sum_{i = 1}^{n}a_i$$

Так как утверждение верно для любого $\varepsilon > 0$, то домножение $\varepsilon$ на положительную константу ничего не меняет, то есть:  
$$\forall \varepsilon > 0 \,\,\,\, \exists \{x_i \in X_i\}_{i = 1}^n:\,\,\,\,\displaystyle \sum_{i = 1}^{n}a_ix_i > \displaystyle \sum_{i = 1}^{n}a_i\sup X_i - \varepsilon$$

Значит $$\displaystyle\sup_{x_i \in X_i}\left\{\sum_{i = 1}^{n}a_ix_i\right\} = \displaystyle \sum_{i = 1}^{n}a_i \displaystyle\sup\left(X_i\right) \,\,\,\,\blacksquare$$

**Теорема:**<a name="theorem-0"></a> (Свойства сумм Дарбу)

1. Пусть разбиение $\mathcal{T}_2$ измельчение $\mathcal{T}_1$. Тогда $S(\mathcal{T}_1) > S(\mathcal{T}_2)$ и $s(\mathcal{T}_1) < s(\mathcal{T}_2)$.

2. Пусть $\mathcal{T}_2$ и $\mathcal{T}_1$ некоторые разбиения $[a, b]$. Тогда $s(\mathcal{T}_1) < S(\mathcal{T}_2)$

3. $$S(\mathcal{T}) = \displaystyle\sup_{\xi}\left\{\sigma_f(\mathcal{T}(\xi))\right\}$$
$$s(\mathcal{T}) = \displaystyle\inf_{\xi}\left\{\sigma_f(\mathcal{T}(\xi))\right\}$$

*Доказательство:*

1. Пусть $\mathcal{T}_2 = \mathcal{T}_1 \cup \{t\}, \,\,\,\, t \in [x_{j - 1}, x_j]$. Тогда 
$$S(\mathcal{T}_2) - S(\mathcal{T}_1) = \displaystyle\sup_{[x_{j - 1}, t]}(f(x))\cdot (t - x_{j - 1}) + \displaystyle\sup_{[t, x_j]}(f(x))\cdot (x_j - t) - \displaystyle\sup_{[x_{j - 1}, x_j]}(f(x))\cdot (x_j - x_{j - 1})=$$
$$=\displaystyle\sup_{[x_{j - 1}, t]}(f(x))\cdot (t - x_{j - 1}) + \displaystyle\sup_{[t, x_j]}(f(x))\cdot (x_j - t) - \displaystyle\sup_{[x_{j - 1}, x_j]}(f(x))\cdot ((t - x_{j - 1}) + (x_j - t))\le 0 \,\,\,\,\blacksquare$$

2. Пусть $\mathcal{T} = \mathcal{T}_1 \cup \mathcal{T}_2$. Тогда по свойству $1$: 
$$s(\mathcal{T}_1) < s(\mathcal{T}) < S(\mathcal{T}) < S(\mathcal{T}_2) \,\,\,\,\blacksquare$$

3. [По лемме](#lemma-0) $$\displaystyle\sup_{\xi}\left\{\sigma_f(\mathcal{T}(\xi))\right\} = \displaystyle\sup_{\xi}\left\{\displaystyle \sum_{i = 1}^{n}f(\xi_i)\cdot (x_{i} - x_{i - 1})\right\} = \displaystyle \sum_{i = 1}^{n}\displaystyle\sup_{\Delta x_i}\left(f(x)\right)\cdot(x_i - x_{i-1})$$Множеством $X_i$ здесь будет отрезок $\Delta x_i = [x_i, x_{i - 1}]$, так как точная верхняя грань ищется по множеству всех разметок и, следовательно, $\xi_i$ пробегает весь отрезок $\Delta x_i \,\,\,\,\blacksquare$

## Критерий интегрируемости функции по Риману

---

**Определение:**<a name="definition-1"></a> 

$I^{*} = \displaystyle\inf_{\mathcal{T}}S(\mathcal{T})$ - *верхний интеграл Дарбу*.

$I_{*} = \displaystyle\sup_{\mathcal{T}}s(\mathcal{T})$ - *нижний интеграл Дарбу*.

Замечание: определение верхнего и нижнего интеграла Дарбу корректно, так как выполняется [свойство 2](#theorem-0).

**Теорема:**<a name="theorem-1"></a> (критерий интегрируемости)

$$f(x) \in R[a, b] \Leftrightarrow \forall \varepsilon > 0 \,\,\,\, \exists \delta: \,\,\,\, \forall \mathcal{T}(\xi) \left(d(\mathcal{T}) < \delta\right) \,\,\,\, S(\mathcal{T}) - s(\mathcal{T}) < \varepsilon$$

*Доказательство:* $$\Rightarrow$$

$f(x) \in R[a, b]$, то есть $\exists I \in \mathbb{R}:\,\,\,\,\forall \varepsilon > 0 \,\,\,\, \exists \delta >0: \,\,\,\, \forall \mathcal{T}(\xi) \left(d(\mathcal{T}) < \delta\right) \,\,\,\, |\sigma_f(\mathcal{T}(\xi)) - I| <\varepsilon$. Следовательно

$$I + \varepsilon < s(\mathcal{T}) < \sigma_f(\mathcal{T}(\xi)) < S(\mathcal{T}) < I + \varepsilon \,\,\,\,\blacksquare$$

$$\Leftarrow$$

Из определения верхнего и нижнего интегралов Дарбу следует, что $s(\mathcal{T}) \le I_{*} \le I^{*} \le S(\mathcal{T}) \Rightarrow I_{*} = I^{*} = I$. 

Имеем $$\begin{cases}
s(\mathcal{T}) \le I \le S(\mathcal{T})\\
S(\mathcal{T}) - s(\mathcal{T}) < \varepsilon\\
s(\mathcal{T}) \le \sigma_f(\mathcal{T}(\xi)) \le S(\mathcal{T})
\end{cases} \Rightarrow |\sigma_f(\mathcal{T}(\xi)) - I| <\varepsilon \,\,\,\,\blacksquare$$
