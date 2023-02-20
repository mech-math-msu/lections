## Матрица перехода сопряженного базиса

---

**Теорема:**<a name="theorem-0"></a> Пусть $V$ - векторное пространство, $B = \{e_1, \ldots, e_n\}$ и $\tilde{B} = \{\tilde{e}_1, \ldots, \tilde{e}_n\}$ - базисы $V$. $B^{*} = \{\varepsilon^1, \ldots, \varepsilon^n\}$ и $\tilde{B}^{*} = \{\tilde{\varepsilon}^1, \ldots, \tilde{\varepsilon}^n\}$ - сопряженные к $B$ и $\tilde{B}$ базисы. Тогда $C_{B \to \tilde{B}}^T = C_{B^{*} \to \tilde{B}^{*}}$.

*Доказательство:* 
$$\tilde{e}_1 = \lambda_{11}e_1 + \ldots + \lambda_{n1}e_n$$
$$\tilde{e}_2 = \lambda_{12}e_1 + \ldots + \lambda_{n2}e_n$$
$$\vdots$$
$$\tilde{e}_n = \lambda_{1n}e_1 + \ldots + \lambda_{nn}e_n$$
$$C_{B \to \tilde{B}} = \left(\begin{array}{ccc}
    \lambda_{11} & \dots & \lambda_{1n}\\
    \vdots & \ddots & \vdots\\
    \lambda_{n1} & \dots & \lambda_{nn}\\
\end{array}\right)$$

$$\tilde{\varepsilon}^1 = \mu_{11}\varepsilon^1 + \ldots + \mu_{n1}\varepsilon^n$$
$$\tilde{\varepsilon}^2 = \mu_{12}\varepsilon^1 + \ldots + \mu_{n2}\varepsilon^n$$
$$\vdots$$
$$\tilde{\varepsilon}^n = \mu_{1n}\varepsilon^1 + \ldots + \mu_{nn}\varepsilon^n$$
$$C_{B^{*} \to \tilde{B}^{*}} = \left(\begin{array}{ccc}
    \mu_{11} & \dots & \mu_{1n}\\
    \vdots & \ddots & \vdots\\
    \mu_{n1} & \dots & \mu_{nn}\\
\end{array}\right)$$

$$\delta_i^j = \tilde{\varepsilon}_i(\tilde{e}_j) = (\mu_{1i}\varepsilon^1 + \ldots + \mu_{ni}\varepsilon^n)(\lambda_{1j}e_1 + \ldots + \lambda_{nj}e_n) = \displaystyle \sum_{k = 1}^{n}\mu_{ki}\lambda_{kj} =$$
$$=\displaystyle \sum_{k = 1}^{n}\lambda_{kj}\mu_{ik}^T \Rightarrow C_{B \to \tilde{B}}\cdot C_{B^{*} \to \tilde{B}^{*}}^T = E \,\,\,\,\blacksquare$$

## Ядро линейной функции(линейного функционала)

---

**Определение:**<a name="definition-0"></a> Пусть $\varphi$ - линейная функция на  векторном пространстве $V$. Тогда *ядро* $\varphi$ - это $\ker \varphi = \{v \in V: \,\,\,\, \varphi(v) = 0\}$.

**Утверждение:**<a name="statement-1"></a> Пусть $\varphi$ - линейная функция на  векторном пространстве $V$. Тогда $\ker \varphi$ - подпространство $V$.

*Доказательство:* 

1. $0 \in \ker \varphi$, так как $\varphi(0) = \varphi(0 + 0) = \varphi(0) + \varphi(0) \Rightarrow \varphi(0) = 0$.
2. Пусть $u, v \in \ker \varphi \Rightarrow \varphi(u) + \varphi(v) = 0 + 0 = 0 = \varphi(u + v) \Rightarrow u + v \in \ker \varphi$.
3. $\,\,\,\,\blacksquare$

**Утверждение:**<a name="statement-0"></a> Пусть $V$ векторное пространство, тогда любое его подпространство $U$ может быть представлено как конечное пересечение ядер некоторых линейных функций на $V$.

*Доказательство:* Пусть $B = \{e_1, \ldots, e_m\}$ - базис в $U$. Дополним его до базиса $V$: $B’ = \{e_1, \ldots, e_m, e_{m + 1} \ldots, e_n\}$.<br>
Пусть $v \in V$, разложим его по базису: $v = \lambda_1e_1 + \ldots + \lambda_n e_n$.<br>Рассмотрим значение $i$-ого вектора базиса сопряженного к $B’$: $\varepsilon^i(v) = \varepsilon^i(\lambda_1e_1 + \ldots + \lambda_n e_n) = \lambda_i$, то есть $v \in \ker \varepsilon^i \Rightarrow i$-я координата $v$ равна $0$($\lambda_i = 0$).<br>
Пусть $u \in U, \,\,\,\, u = \mu_1e_1 + \ldots + \mu_m e_m \Rightarrow \mu_{m + 1}, \ldots, \mu_n = 0$, иначе векторы базиса будут линейно зависимы, следовательно $u \in \ker\varepsilon^{m + 1}, \ldots, \ker\varepsilon^n \Rightarrow \displaystyle\bigcap\limits_{i = m + 1}^{n}\ker \varepsilon^i = U \,\,\,\,\blacksquare$

**Утверждение:**<a name="statement-2"></a> Пусть $V$ - векторное пространство, $B = \{e_1, \ldots, e_m, e_{m + 1}, \ldots, e_n\}$ - базис $V$, $U$ - попространство $V$, $B’ = \{e_1, \ldots, e_m\}$ - базис $U$. Тогда $U$ - это множество решений некоторой однородной системы линейных уравнений.

*Доказательство:* Рассмотрим некоторой базис $\tilde{B} = \{\tilde{e}_1, \ldots, \tilde{e}_n\}$.<br>
Тогда координаты вектора в базисе $B$ выражаются через координаты в базисе $\tilde{B}$ так: $\left(\begin{array}{c}
x_1\\
x_2\\
\vdots\\
x_n
\end{array}\right) = C_{B \to \tilde{B}}\left(\begin{array}{c}
\tilde{x}_1\\
\tilde{x}_2\\
\vdots\\
\tilde{x}_n
\end{array}\right)$.<br>
Пусть $C_{B \to \tilde{B}}^{*}$ - это матрица, содержащая строки матрицы $C_{B \to \tilde{B}}$ c $m + 1$ до $n$.
$\forall u \in U \left(\begin{array}{c}
x_1\\
\vdots\\
x_{m + 1}\\
\vdots\\
x_n
\end{array}\right) = C_{B \to \tilde{B}}\left(\begin{array}{c}
\tilde{x}_1\\
\vdots\\
\tilde{x}_{m + 1}\\
\vdots\\
\tilde{x}_n
\end{array}\right)$, где $x_{m + 1}, \ldots, x_n = 0$. Значит $u \in U \Leftrightarrow C_{B \to \tilde{B}}^{*}\left(\begin{array}{c}
\tilde{x}_{m + 1}\\
\vdots\\
\tilde{x}_n
\end{array}\right) = 0 \,\,\,\,\blacksquare$

## Линейные отображения

---

**Определение:**<a name="definition-1"></a> Пусть $U$ и $W$ - векторные пространства над полем $F$. $\varphi: \,\,\,\, V \to W$ - *линейное отображение*, если:

1. $\forall u_1, u_2 \in V \,\,\,\, \varphi(u_1 + u_2) = \varphi(u_1) + \varphi(u_2)$
2. $\forall u \in U, \,\,\,\, \lambda \in F \,\,\,\, \varphi(\lambda u) = \lambda \varphi(u)$

### Матрицы линейных отображений

---

**Определение:**<a name="definition-2"></a> Пусть $U$ и $W$ - векторные пространства над полем $F$, $\varphi: U \to W$ - линейное отображение. Пусть $B = \{e_1, \ldots, e_n\}$ - базис $U$, $B’ = \{f_1, \ldots, f_m\}$ - базис $W$.

$$u \in U \,\,\,\, u = \lambda_1 e_1 + \ldots \lambda_n e_n$$
$$\varphi(u) = \lambda_1 \varphi(e_1) + \ldots + \lambda_n \varphi(e_n)$$
$$w_1 = \varphi(e_1), \ldots, w_n = \varphi(e_n)$$
$$w_1 = \mu_{11} f_1 + \ldots + \mu_{m1} f_m$$
$$\vdots$$
$$w_n = \mu_{1n} f_1 + \ldots + \mu_{mn} f_m$$
$$\Downarrow$$
$$\mathcal{A} = \left(\begin{array}{ccc}
\mu_{11} & \dots & \mu_{1n}\\
\vdots & \ddots & \vdots\\
\mu_{m1} & \dots & \mu_{mn}
\end{array}\right)$$ - *матрица линейного отображения* $\varphi$ относительно базисов $B$ и $B’$.

**Утверждение:**<a name="statement-3"></a> Пусть $U$ и $W$ - векторные пространства над полем $F$, $\varphi: U \to W$ - линейное отображение. Пусть $B, \tilde{B}$ - базисы $U$, $B’, \tilde{B}’$ - базисы $W$. $\mathcal{A}$ - матрица $\varphi$ относительно $B$ и $B’$, $\mathcal{A}’$ - матрица $\varphi$ относительно $\tilde{B}$ и $\tilde{B}’$. Тогда $$\mathcal{A}’ = C_{\tilde{B} \to \tilde{B}’}^{-1}\mathcal{A}C_{B \to B’}$$

*Доказательство:* записать все в матричном виде ($Y = \mathcal{A}X$, $Y$ - координаты вектора в $W$, $X$ - координаты вектора в $U$) $\,\,\,\,\blacksquare$

## Ядро и образ линейного отображения

---

**Определение:**<a name="definition-3"></a> Пусть $U$ и $W$ - векторные пространства над полем $F$, $\varphi: U \to W$ - линейное отображение. *Ядро* $\varphi$ - это $\ker \varphi = \{u \in U: \,\,\,\, \varphi(u) = 0\}$.

**Определение:**<a name="definition-4"></a> Пусть $U$ и $W$ - векторные пространства над полем $F$, $\varphi: U \to W$ - линейное отображение. *Образ* $\varphi$ - это $\operatorname{Img} \varphi = \{w \in W: \,\,\,\,\exists u \in U \,\,\,\, \varphi(u) = w\}$.

**Утверждение:**<a name="statement-4"></a> Пусть $U$ и $W$ - векторные пространства над полем $F$, $\varphi: U \to W$ - линейное отображение. Тогда $\ker \varphi$ подпространство в $U$ и $\operatorname{Img} \varphi$ подпространство в $W$.

*Доказательство:* очев $\,\,\,\,\blacksquare$

**Утверждение:**<a name="statement-5"></a> Пусть $U$ и $W$ - векторные пространства над полем $F$, $\varphi: U \to W$ - линейное отображение.

$\varphi$ - сюръективно $\Leftrightarrow \operatorname{Img} \varphi = W$

$\varphi$ - инъективно $\Leftrightarrow \ker \varphi = \{0\}$

*Доказательство:* ну, почти очев $\,\,\,\,\blacksquare$


