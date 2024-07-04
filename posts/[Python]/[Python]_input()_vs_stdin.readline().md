<p><a href="https://velog.io/@yje9802/Python-input-vs-stdin.readline" target="blank">원본 링크</a></p><br><p><img alt="" src="https://velog.velcdn.com/images/yje9802/post/ede53220-881e-400e-a764-084b3c72eea3/image.png" /></p>
<p>코테 문제를 풀다보면 백준 같은 사이트에서는 입력값을 받아오는 부분부터 구현해야 하는 경우가 많습니다. </p>
<p>지금까지는 그냥 내장 함수인 <code>input</code>을 사용했는데 최근 소프티어에서 풀었던 문제는 <code>input</code>을 쓰면 시간 초과가 나서 <code>sys</code>모듈의 <code>stdin.readline</code>을 써야 했습니다. </p>
<p>둘 다 입력을 받는 건데 어떤 차이가 있길래 <code>stdin.readline</code>이 더 빠른 것일까요? 이참에 한 번 정리하고 넘어가고자 합니다.</p>
<h3 id="input">input()</h3>
<h4 id="기본적인-사용법">기본적인 사용법</h4>
<p>기본 내장 함수로, 인자로 주어진 프롬프트 문자열이 있다면 화면에 출력해주고 사용자의 입력(키보드 입력)을 받습니다. </p>
<pre><code class="language-python">answer = input(&quot;정답을 입력하세요: &quot;)
print(answer)

&gt;&gt; 정답을 입력하세요: apple
apple</code></pre>
<p>개행 문자(Enter, <code>\n</code>)를 입력의 종료로 간주하기 때문에 엔터 치면 입력 종료라고 생각하면 됩니다. 만약 입력이 없다면 EOF 에러 발생하기 때문에 try-except 구문을 통해 처리하거나 해야 합니다. </p>
<h4 id="특징">특징</h4>
<p>문자가 하나씩 입력될 때마다 하나씩 버퍼에 들어갑니다. 만약 <code>apple</code>을 입력하고 엔터를 치면 개행 문자 포함 총 6번(<code>a</code>, <code>p</code>, <code>p</code>, <code>l</code>, <code>e</code>, <code>\n</code>) 버퍼에 들어가는 것입니다. </p>
<p>최종 입력값은 <strong>문자열로 변환되며, 자체적으로 rstrip() 함수를 실행해 마지막 줄바꿈 문자를 제거한 뒤에 값을 반환합니다.</strong></p>
<hr />
<h3 id="sysstdinreadline">sys.stdin.readline()</h3>
<h4 id="기본적인-사용법-1">기본적인 사용법</h4>
<p>sys 모듈 함수로, input 함수와 유사하나 프롬프트 문자열을 인자로 받아 출력해주는 기능은 없습니다.</p>
<pre><code class="language-python">import sys

answer = list(sys.stdin.readline())
print(answer)
jump = list(sys.stdin.readline())
print(jump)

&gt;&gt; hello
['h', 'e', 'l', 'l', 'o', '\n']

['\n']</code></pre>
<p>최종 입력값은 문자열로 저장되며, 입력이 없다면 빈 문자열을 반환하고, control+z를 눌러 종료시킬 수 있습니다. </p>
<p>참고로 아래 예시처럼 인자를 통해 입력값의 일부만 받아올 수 있습니다.</p>
<pre><code class="language-python">import sys

answer = sys.stdin.readline(2)
print(answer)

&gt;&gt; hello
he</code></pre>
<h4 id="특징-1">특징</h4>
<p>위의 hello 예시처럼 개행 문자까지 그대로 저장합니다. 그렇기 때문에 자동으로 개행 문자를 제거하는 작업을 거치는 input() 보다 빠릅니다. </p>
<p>또한 한 번에 읽어와서 버퍼에 저장하기 때문에 키보드 입력 하나하나 마다 버퍼에 저장시키는 input() 보다 빠릅니다.</p>
<hr />
<h3 id="결론">결론</h3>
<p>입력값이 한 두 줄 정도라면 input과 readline 간에 특별한 차이가 없겠지만 입력값이 많거나 입력이 언제 끝날지 모를 경우에는 readline을 쓰는 것이 훨씬 빠릅니다. </p>
<p>다만 readline을 쓸 때는 <code>\n</code>도 결과값에 포함된다는 것을 잊으면 안 되겠죠!</p>
<hr />
<h3 id="참고-자료">참고 자료</h3>
<ul>
<li><a href="https://100s.tistory.com/5">https://100s.tistory.com/5</a></li>
<li><a href="https://buyandpray.tistory.com/7">https://buyandpray.tistory.com/7</a></li>
</ul>