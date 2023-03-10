## Деревья

---

**Определение:**<a name="definition-0"></a> *Дерево* - это связный граф без циклов.

**Теорема:**<a name="theorem-0"></a> Пусть $G = \{V, E\}$ - граф, $|V| = n, \,\,\,\, |E| = m$. Следующие утверждения эквивалентны.

1. $G$ - дерево.
2. $G$ связный и $n = m + 1$.
3. $G$ не содержит циклов и $n = m + 1$.
4. В $G$ между любыми двумя вершинами сущесвует единственный маршрут.
5. $G$ не содержит циклов и в графе, содержащем ребро между двумя несмежными вершинами $G$, существует ровно один цикл.

*Доказательство:*

$$1 \Rightarrow 2$$
Докажем индукцией по количеству вершин. База: $n = 1$ тогда ребер $0$, так как нет петель, то есть $n = 1 = 0 + 1$ что и требовалось. Пусть $n \ge 2$ и для деревьев с меньшим, чем $n$ числом вершин верно $n = m + 1$. Тогда возьмем произвольное ребро $e$(множество ребер непусто, так как граф связный) и рассмотрим $G\\e$.

**Лемма:**<a name="lemma-0"></a> Пусть $G$ - дерево, $e$ - произвольное ребро в нем. Тогда граф $G$ без ребра $e$ содержит $2$ компоненты связности, каждая из которых - дерево.

*Доказательство:* Пусть $e$ соединяет $v_1$ и $v_2$. $G$ - связный, значит, убрав одно ребро получим $1$ или $2$ компоненты связности. Если получим одну компоненту, то существует маршрут из $v_1$ в $v_2$. Следовательно, в $G$ был цикл. Противоречие. Получили две компоненты связности, каждая из которых не содержит циклов, так как циклов нет в $G \,\,\,\,\blacksquare$

Для $2$-ух полученных компонент связности - деревьев верно предположение индукции. Пусть в первом и втором деревьях $n_1, n_2, m_1, m_2$ вершин и ребер соответственно. Тогда $n_1 = m_1 + 1, \,\,\,\, n_2 = m_2 + 1$. $n = n_1 + n_2 = m_1 + 1 + m_2 + 1 = (m_1 + m_2 + 1) + 1 \,\,\,\,\blacksquare$ (в $G$ $m_1 + m_2 + 1$ - ребер)

$$2 \Rightarrow 3$$

Пусть $G$ содержит цикл.

**Лемма:**<a name="lemma-1"></a> Пусть простой граф $G$ содержит $n$ вершин, $m$ ребер и $k$ компонент связности. Тогда $n - m \le k$.

*Доказательство:* Докажем индукцией по количеству ребер. Для $m = 0 \,\,\,\, n = k$, что и требовалось. Пусть ребер $m \ge 1$ и для всех графов с меньшим числом вершин утверждение выполнено. Тогда выберем произвольное ребро $e$ и рассмотрим граф без него. Убрав ребро, получим либо $k$ компонент связности либо $k + 1$. Для графа $G \\ e$ верно $n’ - m’ \le k’$, $m’, \,\,\,\, n’, k’$ - количество ребер, вершин и компонент связности $G\\e \,\,\,\,\blacksquare$

Рассмотри граф $G$ без произвольного ребра $e$, входящего в цикл. $G\\e$ связный, так как $e$ входило в цикл. То есть в $G$ $n$ вершин и $n - 2$ ребер, что противоречит [лемме](#lemma-1) $\,\,\,\,\blacksquare$

$$3 \Rightarrow 4$$
Единственность маршрута при его существовании очевидна. Маршрут существует между любыми двумя вершинами $G$, так как, предположив, что в $G$ $k$ компонент связности(которые не содержат циклов, а следовательно деревья) получим, что $n =$ сумма количества вершин в каждой компоненте = сумма количества ребер в каждой компоненте + $k$(по $1 \Rightarrow 2$) $= m + 1 \,\,\,\,\blacksquare$

$$4 \Rightarrow 5$$

Если в $G$ есть цикл, то нарушается условие о единственности маршрута. Добавив ребро, получим цикл, так как маршрут существует между любыми двумя вершинами. Если получим больше одного цикла, то они оба содержат добавленное ребро, а следовательно сущесвует цикл в $G \,\,\,\,\blacksquare$ 

$$5 \Rightarrow 1$$

$G$ - связный, так как для каждой пары вершин существует маршрут между ними, либо это ребро, соединяющее их, либо цикл, полученный добавлением ребра соединяющего их, без этого ребра (то есть уже не цикл)$\,\,\,\,\blacksquare$
