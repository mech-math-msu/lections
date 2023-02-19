## Линейные функции

---

**Определение:**<a name="definition-0"></a> *Линейная функция* на векторном пространстве $V$ - это отображение $\varphi: \,\,\,\, V \to F$, где $V$ векторное пространство над полем $F$, такое что:

1. $\forall x, y \in V \,\,\,\, \varphi(x + y) = \varphi(x) + \varphi(y)$.
2. $\forall x \in V, \lambda \in F \,\,\,\, \varphi(\lambda x) = \lambda \varphi(x)$.

**Утверждение:**<a name="statement-0"></a> Множество всех линейных функций $V^{*}$ на векторном пространстве $V$ над полем $F$ - это векторное пространство относительно поточечного сложения ($\forall \varphi, \psi \in V^{*} \,\,\,\,\forall v \in V \,\,\,\, (\varphi + \psi)(v) = \varphi(v) + \psi(v)$) и умножения на элементы поля $F$.

*Доказательство:* аксиомы $\,\,\,\,\blacksquare$

**Определение:**<a name="definition-1"></a> $V^{*}$ *сопряженное* к $V$ векторное пространство.

**Утверждение:**<a name="statement-1"></a> 

1. Линейная функция на векторном пространстве $V$ однозначно задается значениями на векторах некоторого базиса $V$.
2. Пусть $V$ векторное пространство над полем $F$ и $\dim V = n$. Тогда любые $n$ чисел из $F$ задают линейную функцию на $V$.
3. Пусть $\varphi$ и $\psi$ линейные функции на векторном пространстве $V$. Тогда $\varphi = \psi \Leftrightarrow$ $\varphi$ принимает на базисных векторах $V$ те же значения, что и $\psi$ (совпадают значения на каждом векторе).
4. какое-то там отображение.

*Доказательство:* Пусть $\varphi$ линейная функция на $V$, а $e_1, \ldots, e_n$ базис в $V$. Тогда $\forall v \in V \,\,\,\, v = \lambda_1 e_1 + \ldots + \lambda_n e_n$ и такое представление единственно.
$\varphi(v) = \varphi(\lambda_1 e_1 + \ldots + \lambda_n e_n) = \lambda_1\varphi(e_1) + \ldots + \lambda_n \varphi(e_n)$. Обозначим $\varphi(e_i) = a_i$. Честно говоря, я не понимаю, что значит задает, а поэтому не знаю, что тут доказывать $\,\,\,\,\blacksquare$ 

## Сопряженные базисы

---

**Утверждение:**<a name="statement-2"></a> Пусть $V$ векторное пространство над полем $F$, $e_1, \ldots, e_n$ базис в $V$. Тогда множество $\{\varepsilon^1, \ldots, \varepsilon^n\}$, где $\varepsilon^j(e_i) = \begin{cases}
    0, i \ne j\\
    1, i = j
\end{cases}$ - базис в $V^{*}$.

*Доказательство:* Докажем, что векторы(линейные функции) $\varepsilon^1, \ldots, \varepsilon^n$ линейно независимы. Рассмотрим их линейную комбинацию равную $0$: $\lambda_1\varepsilon^1+ \ldots + \lambda_n\varepsilon^n = 0$. Чтобы функции (в данном случае тождественный ноль и $\lambda_1\varepsilon^1+ \ldots + \lambda_n\varepsilon^n$) были равны, необходимо совпадение значений на базисных векторах. Значение $\lambda_1\varepsilon^1+ \ldots + \lambda_n\varepsilon^n$ на $e_i$ равно $\lambda_i$, а следовательно $\lambda_i = 0 \,\,\,\,\forall i$. 

Осталось доказать, что любая линейная функция на $V$ задается (😉) через $\varepsilon_i$-е, ну, делается это так: $\varphi = \varphi(e_1)\varepsilon^1 +\ldots + \varphi(e_n)\varepsilon^n \,\,\,\,\blacksquare$

**Следствие:**<a name="corollary-0"></a> $\dim V = \dim V^{*}$ и $V \cong V^{*}$

**Определение:**<a name="definition-2"></a> Базис $\{\varepsilon^1, \ldots, \varepsilon^n\}$ в $V^{*}$ *сопряженный* к базису $e_1, \ldots, e_n$ в $V$.

## Второе сопряженное пространство

---

**Определение:**<a name="definition-3"></a> $V^{**}$ - это $(V^{*})^{*}$, то есть сопряженное к $V^{*}$ и *второе сопряженное к* $V$ векторное пространство ($V^{*}$ сопряжено векторному пространству $V$ 🙄).

**Утверждение:**<a name="statement-3"></a> Пусть $V$ векторное пространство. Каждому вектору $x \in V$ сопоставим отображение $f_x: \,\,\,\, V^{*} \to F$, такое что $f_x(\varphi) = \varphi(x)$. Тогда $f_x \in V^{**}$.

*Доказательство:* 

1. $f_x(\varphi + \psi) = (\varphi + \psi)(x) = \varphi(x) + \psi(x) = f_x(\varphi) + f_x(\psi)$.
2. $f_x(\lambda \varphi) = \lambda \varphi(x) = \lambda f_x(\varphi) \,\,\,\,\blacksquare$

**Теорема:**<a name="theorem-0"></a> (Канонический изоморфизм $V$ и $V^{**}$)
Отображение $\Phi: \,\,\,\, v \mapsto f_v$ - изоморфизм $V$ и $V^{**}$.

*Доказательство:* 

1. Линейность очевидна.
2. Биективность

a. Проверим инъективность. Пусть $\exists x, y \in V: \,\,\,\, x \ne y$ и $\Phi(x) = \Phi(y)$. Пусть $\varepsilon^1, \ldots, \varepsilon^n$ базис в $V^{*}$ сопряженный базису $e_1, \ldots, e_n$ в $V$. Тогда $\Phi(x) = f_x$ на $i$-ом векторе $V^{*} \,\,\,\, f_x(\varepsilon^i) = \varepsilon^i(x) = x_i$, где $x_i$ $i$-я координата вектора $x$ в базисе $e_1, \ldots, e_n$. Аналогично $y_i$ $i$-я координата вектора $y$ в базисе $e_1, \ldots, e_n$, так как $\Phi(x) = \Phi(y)$ эти координаты совпадают, а следовательно $x = y$. Противоречие.
b. Проверим сюрьективность. Пусть $e_1, \ldots, e_n$ - базис в $V$.<br>$\varepsilon_1, \ldots, \varepsilon_n$ - базис в $V^{*}$.<br>$f_{e_1}, \ldots, f_{e_n}$ - базис в $V^{**}$.<br>$f_{e_i}(\varepsilon^j) = \varepsilon^j(e_i) = \begin{cases} 0, \,\,\,\, i \ne j \\ 1, \,\,\,\, i = j \end{cases}$(зачем это?)<br>$\forall v \in V \,\,\,\,\Phi(v) = \Phi(\lambda_1 e_1 + \ldots + \lambda_n e_n) = \lambda_1\Phi(e_1) + \ldots + \lambda_n \Phi(e_n) = \lambda_1 f_{e_1} + \ldots \lambda_n f_{e_n} \,\,\,\,\blacksquare$
(Непонятно)