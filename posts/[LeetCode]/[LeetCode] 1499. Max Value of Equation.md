<p><a href="https://velog.io/@yje9802/LeetCode-1499.-Max-Value-of-Equation" color="black">원본 링크</a></p><br><p><img alt="" src="https://velog.velcdn.com/images/yje9802/post/8019e153-1f8e-49a2-8a78-95ab9661dda3/image.png" /></p>
<blockquote>
<p>LeetCode 🔑
<a href="https://leetcode.com/problems/max-value-of-equation/description/">1499. Max Value of Equation</a>
파이썬으로 풀어보기</p>
</blockquote>
<h3 id="문제-설명">문제 설명</h3>
<p><em>You are given an array points containing the coordinates of points on a 2D plane, sorted by the x-values, where <code>points[i] = [xi, yi]</code> such that <code>xi &lt; xj</code> for all <code>1 &lt;= i &lt; j &lt;= points.length</code>. You are also given an integer <code>k</code>.</em></p>
<p><em>Return the maximum value of the equation <code>yi + yj + |xi - xj|</code> where <code>|xi - xj| &lt;= k</code> and <code>1 &lt;= i &lt; j &lt;= points.length</code>.</em></p>
<p><em>It is guaranteed that there exists at least one pair of points that satisfy the constraint <code>|xi - xj| &lt;= k</code>.</em></p>
<h4 id="💡-문제-해석">💡 문제 해석</h4>
<p>2차원 평면 상의 x, y 좌표 정보를 담은 배열 points 주어진다. i번째 x, y 좌표 정보는 <code>points[i] = [xi, yi]</code> 이렇게 주어지며 배열은 x좌표값을 기준으로 정렬되어있다. </p>
<p>x좌표는 반드시 증가하는 수열이다. 즉, 모든 <code>1 &lt;= i &lt; j &lt;= points.length</code>에 대하여 반드시 <code>xi &lt; xj</code>이다. </p>
<p>주어진 좌표들 중 <code>|xi - xj| &lt;= k</code>를 만족하는 <code>i, j(i &lt; j)</code> 중에서 <code>yi + yj + |xi - xj|</code>의 최댓값을 구하시오. </p>
<p>단, <code>|xi - xj| &lt;= k</code>를 만족하는 <code>i</code>, <code>j</code> 쌍은 반드시 존재한다. </p>
<h3 id="제한-사항">제한 사항</h3>
<ul>
<li>2 &lt;= <code>points.length</code> &lt;= 105</li>
<li><code>points[i].length</code> == 2</li>
<li>-108 &lt;= <code>xi</code>, <code>yi</code> &lt;= 108</li>
<li>0 &lt;= <code>k</code> &lt;= 2 * 108</li>
</ul>
<hr />
<h3 id="내가-작성한-정답">내가 작성한 정답</h3>
<pre><code class="language-python">class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -&gt; int:
        q = [] # deque
        answer = -float('inf')

        for i in range(len(points)):
            x, y = points[i] 
            # |x[i] - x[j]| ≤ k 만족할 때까지 pop
            while q and q[0][0] + k &lt; x:
                q.pop(0)

            diff = y - x
            plus = y + x

            if q:
                eq_v = plus + q[0][1] # yi + yj + |xi - xj|
                answer = max(answer, eq_v)

            # 전에 계산된 diff들이 현재 diff보다 작으면 필요 없으므로 뺀다.(최댓값을 구하는 것이므로)
            while q and q[-1][1] &lt; diff:
                q.pop()

            q.append((x, diff))

        return answer</code></pre>
<p>처음에 시도한 접근법은 2중 for문이었다. 이렇게 해도 답은 나오나 효율성 평가에서 통과하지 못할 가능성이 높다. </p>
<p>이 문제는 dequeue를 활용하면 O(n) 시간 안에 해결할 수 있다. </p>
<p>우선 <code>yi + yj + |xi - xj|</code> 이 식을 정리하고 넘어가보면,</p>
<ul>
<li>x좌표값만 놓고 봤을 때, i &lt; j 일 때 <code>xi &lt; xj</code>인 엄격한 증가 수열이므로 <code>|xi - xj| = xj - xi</code>라고 할 수 있다. </li>
<li>따라서 원래 식을 다시 정리하면 <code>(yj + xj) + (yi - xi)</code>라고 할 수 있다. </li>
<li><code>points[i]</code>에서 <code>yi - xi</code>만 계산하고 <code>points[j]</code>에서 <code>yj + xj</code>만 계산해서 둘이 더해주면 되는 것이다. </li>
</ul>
<p>이렇게 <code>xi - xj</code> 두 좌표에 걸쳐서 계산해야 하는 것을 <code>yi - xi</code>, <code>yj + xj</code> 각 좌표 별로 계산할 수 있게 되므로 구현이 훨씬 간단해진다. </p>
<p>따라서 코드에서 현재 시점에 <code>q</code>에 있는 값들은 모두 현재보다 이전 좌표들, 즉 현재를 <code>j</code>라고 한다면 <code>q</code>에 있는 값들은 <code>i</code>라고 생각하면 쉽다. 여기서 <code>|x[i] - x[j]| ≤ k</code>를 만족하지 못 하는 경우만 <code>q</code>에서 제거해주면 이후부터는 최댓값인지 비교하기만 하면 된다. </p>