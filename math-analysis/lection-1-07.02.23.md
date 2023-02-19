## Неопределенный интеграл

---

**Определение:**<a name="definition-0"></a> Пусть $f(x)$ определена на $(a, b)$. Пусть $F(x)$, такова что $F’(x) = f(x) \,\,\,\, \forall x \in (a, b)$. Тогда $F(x)$ *первообразная* $f(x)$ на $(a, b)$.

**Определение:**<a name="definition-1"></a> *Неопределенный интеграл* $f(x)$ на $(a, b)$ - это множество всех первообразных $f(x)$ на $(a, b)$. Обозначается $\displaystyle \int f(x)dx$.

Замечание: $f(x)dx = F’(x)dx = dF(x)$. То есть интеграл - это множество всех функций, дифференциал которых равен некоторой заданной функции $f(x)$.

**Теорема:**<a name="theorem-0"></a> Пусть $F(x)$ первообразная $f(x)$ на $(a, b)$. Тогда 
$$\displaystyle \int f(x)dx = \{F(x) + g(x), \,\,\,\, g(x) = C, \,\,\,\, C \in \mathbb{R}\}$$

*Доказательство:* Докажем, что $F(x) + C$ - это первообразная $f(x)$ на $(a, b)$. $(F(x) + C)’ = F’(x) + C’ = f(x)$.<br>
Докажем, что любая первообразная представима в виде $F(x) + g(x), \,\,\,\, g(x) = C \,\,\,\, C \in \mathbb{R}$. Пусть $G(x)$ первообразная $f(x)$ на $(a, b)$. Рассмотрим $F(x) - G(x)$. $(F(x) - G(x))’ = F’(x) - G’(x) = f(x) - f(x) = 0$. Следовательно [по следствию из теоремы Лагранжа](https://calculus-with-cats.github.io/lections/#corollary-4) $F(x) - G(x) = const \Rightarrow G(x) = F(x) + C \,\,\,\,\blacksquare$

Далее пишем $\displaystyle \int f(x) dx = F(x) + C$, подразумевая множество всех первообразных.

### Свойства неопределенного интеграла

---

**Утверждение:**<a name="statement-0"></a> (Свойства неопределенного интеграла)

1. $\displaystyle \int k \cdot f(x) dx = k \cdot \displaystyle \int f(x) dx$ (Множество умножить на число - это каждый элемент множества умножить на число)

2. $\displaystyle \int (f(x) + g(x)) dx = \displaystyle \int f(x) dx + \displaystyle \int g(x) dx$

3. $\displaystyle \int f(\varphi(x)) \varphi’(x) dx = F(\varphi(x)) + C$, если $F(x)$ первообразная $f(x)$.

4. $\displaystyle \int f’(x) g(x) dx = f(x)g(x) - \displaystyle \int f(x) g’(x) dx$

*Доказательство:*

1. -- 3. очев $\,\,\,\,\blacksquare$
4. Проинтегрировать производную суммы функций $\,\,\,\,\blacksquare$

### Таблица неопределенных интегралов

---

Смэрть

### Интегрирование рациональных функций

---

Хотим интегрировать функции вида: $\frac{P(x)}{Q(x)}$, где $P(x), Q(x) \in \mathbb{R}[x]$, то есть многочлены от одной пременной над полем $\mathbb{R}$.

Из алгебры любая такая дробь представима в виде:

$$\frac{P(x)}{Q(x)} = S(x) + \displaystyle \sum_{i = 0}^{n} \frac{A_i}{(x - a_i)^{\alpha_i}} + \displaystyle \sum_{j = 0}^{m}\frac{B_j + C_jx}{(x^2 + p_jx + q_j)^{\beta_j}},$$ где $x^2 + p_jx + q_j = 0$ не имеет действительных корней, а $S(x)$ многочлен.

То есть нужно уметь искать интегралы трех видов:

1. $S(x) = a_0 + a_1x + a_2x^2 + \ldots + a_nx^n$
2. $\frac{A}{(x - a)^{\alpha}}$
3. $\frac{B + Cx}{(x^2 + px + q)^{\beta}}$

Найдем эти интегралы:

1. $\displaystyle \int S(x)dx = \displaystyle \int (a_0 + a_1x + a_2x^2 + \ldots + a_nx^n)dx=$ 
$= \displaystyle \int a_0 dx + \displaystyle \int a_1x dx + \ldots + \displaystyle \int a_nx^n dx= a_0 x + a_1 \frac{x^2}{2} + \ldots + a_n \frac{x^{n + 1}}{n + 1}$

2. $\frac{A}{(x - a)^{\alpha}}$ Пусть $\alpha \ne 1$. Тогда 
$$\displaystyle \int \frac{A}{(x - a)^{\alpha}}dx = \displaystyle \int A(x - a)^{-\alpha}dx = A\frac{(x - a)^{-\alpha + 1}}{-\alpha + 1} + C.$$
Пусть $\alpha = 1$. Тогда
$$\displaystyle \int \frac{A}{(x - a)}dx = \displaystyle \int \frac{A}{(x - a)}d(x - a) = A\ln|x - a| + C.$$

3. $$\frac{B + Cx}{(x^2 + px + q)^{\beta}} = 
\frac{C(x + \frac{p}{2}) + s}{((x + \frac{p}{2})^2 + e^2)^{\beta}} = \frac{C t}{(t^2 + e^2)^{\beta}} + \frac{s}{(t^2 + e^2)^{\beta}}$$
То есть $\displaystyle\int \frac{B + Cx}{(x^2 + px + q)^{\beta}} dx = \displaystyle\int \frac{C t}{(t^2 + e^2)^{\beta}} dt + \displaystyle\int \frac{s}{(t^2 + e^2)^{\beta}} dt$

a. $$\displaystyle\int \frac{C t}{(t^2 + e^2)^{\beta}} dt = \frac{C}{2}\displaystyle\int \frac{d(t^2 + e^2)}{(t^2 + e^2)^{\beta}} = \ldots$$

b. $$I_{\beta} = \displaystyle\int \frac{dt}{(t^2 + e^2)^{\beta}} = \frac{t}{(t^2 + e^2)^{\beta}} + \displaystyle\int \frac{2t^2\beta}{(t^2 + e^2)^{\beta + 1}} dt =$$
$$= \frac{t}{(t^2 + e^2)^{\beta}} + 2\beta\displaystyle\int \frac{(t^2 + e^2) - e^2}{(t^2 + e^2)^{\beta + 1}} dt = \frac{t}{(t^2 + e^2)^{\beta}} + 2\beta I_{\beta} - 2\beta e^2 I_{\beta + 1}$$
Получили рекуррентную формулу для вычисления интеграла:
$$I_{\beta + 1} = \frac{t}{2\beta e^2 (t^2 + e^2)^{\beta}} + \frac{2\beta - 1}{2\beta e^2}I_{\beta}$$

При $\beta = 1$ имеем $$\displaystyle\int \frac{dt}{t^2 + e^2} = \frac{1}{e}\displaystyle\int \frac{d(\frac{t}{e})}{(\frac{t}{e})^2 + 1} = \frac{1}{e}\tan^{-1}\frac{t}{e} + C$$

### Метод Остроградского

---

![](img/blah-blah.png)