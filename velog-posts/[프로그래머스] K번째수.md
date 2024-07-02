<blockquote>
<p>프로그래머스 Lv.1 🌱
<a href="https://school.programmers.co.kr/learn/courses/30/lessons/42748">K번째수</a>
파이썬으로 풀어보기</p>
</blockquote>
<h3 id="문제-설명">문제 설명</h3>
<p>배열 <code>array</code>의 <code>i</code>번째 숫자부터 <code>j</code>번째 숫자까지 자르고 정렬했을 때, <code>k</code>번째에 있는 수를 구하려 합니다.</p>
<p>예를 들어 <code>array</code>가 <code>[1, 5, 2, 6, 3, 7, 4]</code>, <code>i = 2</code>, <code>j = 5</code>, <code>k = 3</code>이라면</p>
<p><code>array</code>의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
2에서 나온 배열의 3번째 숫자는 5입니다.
배열 <code>array</code>, <code>[i, j, k]</code>를 원소로 가진 2차원 배열 <code>commands</code>가 매개변수로 주어질 때, <code>commands</code>의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.</p>
<h3 id="제한-사항">제한 사항</h3>
<ul>
<li><code>array</code>의 길이는 1 이상 100 이하입니다.</li>
<li><code>array</code>의 각 원소는 1 이상 100 이하입니다.</li>
<li><code>commands</code>의 길이는 1 이상 50 이하입니다.</li>
<li><code>commands</code>의 각 원소는 길이가 3입니다.</li>
</ul>
<hr />
<h3 id="내가-작성한-정답">내가 작성한 정답</h3>
<pre><code class="language-python">def solution(array, commands):
    answer = []
    for c in commands:
        new_array = sorted(array[c[0]-1:c[1]])
        answer.append(new_array[c[2]-1])

    return answer</code></pre>
<h3 id="⭐️-추천-가장-많이-받은-정답">⭐️ 추천 가장 많이 받은 정답</h3>
<pre><code class="language-python">def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))</code></pre>
<p>이 문제는 이 추천 정답이 재밌어서 가져왔다. </p>
<p>내가 작성한 코드와 정확히 같은 내용을 map과 lambda를 활용하여 작성하였다. </p>