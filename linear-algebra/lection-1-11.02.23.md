## Векторное пространство

---

**Определение:**<a name="definition-0"></a> *Векторное пространство* $V$ над полем $F$ - это множество с операциями сложения $+: \,\,\,\, V \times V \to V$ и умножения $\cdot: \,\,\,\, F \times V \to V$, удовлетворяющими аксиомам:<br>

$\forall a, b, c \in V, \,\,\,\, \forall \lambda, \mu \in F$

1. $a + (b + c) = (a + b) + c$ (ассоциативность)
2. $a + b = b + a$ (коммутативность)
3. $\exists \vec{0}:\,\,\,\, a + \vec{0} = a$ (существование *нулевого вектора*)
4. $\exists (-a) \in V: \,\,\,\, a + (-a) = \vec{0}$

5. $\lambda (\mu \cdot a) = (\lambda \mu) \cdot a$
6. $(\lambda + \mu)\cdot a = \lambda\cdot a + \mu\cdot a$
7. $\lambda \cdot (a + b) = \lambda \cdot a + \lambda\cdot b$
8. $\exists 1 \in F: \,\,\,\, 1 \cdot a = a$

**Определение:**<a name="definition-1"></a> элементы векторного пространства $V$ - *векторы*.

Примеры:

!()[]

**Определение:**<a name="definition-2"></a> Пусть $V$ - векторное пространство над $F$ с операциями сложения $+$ и умножения $-$. *Векторное подпространство* $V$ - это $U \subset V$, такое что:

1. $\vec{0} \in U$ (нулевой вектор $V$ принадлежит $U$)
2. $\forall u, v \in U \,\,\,\, u + v \in U$ (замкнуто относительно сложения $V$)
3. $\forall u \in U, \lambda \in F \,\,\,\, \lambda \cdot u \in U$ (замкнуто относительно умножения $V$)

**Утверждение:**<a name="statement-0"></a> Пусть $V$ - векторное пространство над $F$. Векторное подпространство $U$ пространства $V$ является векторным пространством над полем $F$ относительно операций сложения и умножения, определенных для $V$.

*Доказательство:* Проверить аксиомы $\,\,\,\,\blacksquare$

## Линейная зависимость векторов

---

**Определение:**<a name="definition-3"></a> Пусть в векторном пространстве $V$ над полем $F$ заданa система векторов $U = (v_1, \ldots, v_n)$. Выражение $\lambda_1 \cdot v_1 + \ldots + \lambda_n \cdot v_n, \,\,\,\, \lambda_i \in F$ - это *линейная комбинация* системы векторов $U$.<br>

Если $\forall i \in \{1, \ldots, n\} \,\,\,\, \lambda_i = 0$, то линейная комбинация *тривиальная*, иначе *нетривиальная*.

**Определение:**<a name="definition-4"></a> Пусть в векторном пространстве $V$ над полем $F$ заданa система векторов $U = (v_1, \ldots, v_n)$. Если $\exists$ их нетривиальная линейная комбинация равная $0$, то система векторов $U$ *линейно зависима*.

**Определение:**<a name="definition-5"></a> Пусть в векторном пространстве $V$ над полем $F$ заданa система векторов $U = (v_1, \ldots, v_n)$. Если только тривиальная линейная комбинация векторов $U$ равна $0$, то система векторов $U$ *линейно независима*.

**Определение:**<a name="definition-6"></a> Пусть задана система векторов $V = (v_1, \ldots, v_n)$. Множество всех линейных комбинаций векторов системы $V$ - это *линейная оболочка* $V$. Обозначается: $<V> = <v_1, \ldots, v_n>$.<br>

$V$ называется *порождающей  (системой)* линейной оболочки $V$.

**Утверждение:**<a name="statement-1"></a> Линейная оболочка $<U> = <u_1, \ldots, u_n>, \,\,\,\, u_i \in V$($V$ векторное пространство) - это векторное подпространство $V$.

*Доказательство:* $\,\,\,\,\blacksquare$

**Лемма:**<a name="lemma-0"></a> Система векторов линейно зависима $\Leftrightarrow$ существует вектор этой системы линейно выражающийся через остальные.

*Доказательство:* $\,\,\,\,\blacksquare$

**Лемма:**<a name="lemma-1"></a> (Основная лемма о линейной зависимости) Пусть $\{v_1, \ldots, v_m\} \subset <u_1, \ldots, u_n>, \,\,\,\, m > n$. Тогда векторы $v_1, \ldots, v_m$ линейно зависимы.

*Доказательство:* $\,\,\,\,\blacksquare$

## Базис

---

**Определение:**<a name="definition-7"></a> *Базис* векторного пространства $V$ - это:

1. Максимальная по включению линейно независимая система векторов $V$.
2. Система векторов, такая что любой вектор $V$ линейно выражается через векторы этой системы единственным образом.
3. Линейно независимая система векторов, такая что любой вектор $V$ линейно выражается через векторы этой системы.

**Утверждение:**<a name="statement-2"></a> Все определения базиса эквивалентны. 

**Определение:**<a name="definition-8"></a> Векторное пространство, порождающее множество которого конечно, называется *конечномерным*, иначе векторное пространство *бесконечномерно*.

**Утверждение:**<a name="statement-4"></a> В любом конечномерном векторном пространстве существует базис.

*Доказательство:* $\,\,\,\,\blacksquare$

**Утверждение:**<a name="statement-3"></a> Количество векторов в любом базисе конечномерного векторного пространства одинаково.

*Доказательство:* $\,\,\,\,\blacksquare$

**Теорема:**<a name="theorem-0"></a> Любую линейно независимую систему векторов в векторном пространстве можно дополнить до базиса.

*Доказательство:* Будем добавлять векторы до тех пор пока система остается линейно независимой $\Rightarrow$ получим максимальную по включению линейно независимую систему $\,\,\,\,\blacksquare$

**Теорема:**<a name="theorem-1"></a> В $n$-мерном векторном пространстве любые $n$ линейно независимых вектора образуют базис.

*Доказательство:* Любые $n + 1$ вектора в $n$-мерном пространстве линейно зависимы, так как размерность - это количество векторов в базисе. То есть любые $n$ векторов -это максимальная по включению линейно независимая система. Осталось доказать, что любой вектор пространства представим линейной комбинацией этих векторов. Но если это не так, то линейно независимы $n + 1$ вектор $\,\,\,\,\blacksquare$

**Утверждение:**<a name="statement-5"></a> Пусть $U$ подпространство векторного пространства $V$. Тогда $\dim U \le \dim V$, при этом $\dim U = \dim V \Leftrightarrow U = V$.

*Доказательство:* Основная лемма о линейной зависимости $\,\,\,\,\blacksquare$

**Определение:**<a name="definition-9"></a> Векторное пространство $U$ над полем $F$ *изоморфно* векторному пространству $V$ над полем $F$, если существует биекция $\varphi: \,\,\,\, U \to V$, такая что:

1. $\forall u_1, u_2 \in U \,\,\,\, \varphi(u_1 + u_2) = \varphi(u_1) + \varphi(u_2)$
2. $\forall u \in U, \lambda \in F \,\,\,\, \varphi(\lambda u) = \lambda \varphi(u)$

$\varphi$ называется *изоморфизм*.
Обозначается $U \cong V$.

**Теорема:**<a name="theorem-2"></a> Пусть $U$ и $V$ конечномерные векторные пространства над полем $F$.
Тогда $$U \cong V \Leftrightarrow \dim U = \dim V$$

*Доказательство:* Изоморфизм переводит вектор базиса одного пространства в соответствующий вектор базиса другого $\,\,\,\,\blacksquare$
