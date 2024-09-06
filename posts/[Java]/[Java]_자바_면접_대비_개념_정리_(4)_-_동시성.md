<p><a href="https://velog.io/@yje9802/Java-%EC%9E%90%EB%B0%94-%EB%A9%B4%EC%A0%91-%EB%8C%80%EB%B9%84-%EA%B0%9C%EB%85%90-%EC%A0%95%EB%A6%AC-4-%EB%8F%99%EC%8B%9C%EC%84%B1" target="blank">원본 링크</a></p><br><h1 id="🔖-멀티스레드-환경에서의-동시성-이슈-해결-in-java">🔖 멀티스레드 환경에서의 동시성 이슈 해결 in Java</h1>
<p><img alt="" src="https://velog.velcdn.com/images/yje9802/post/b99f458a-4641-458d-aab4-1932df371798/image.svg" /></p>
<p>단일 CPU, 멀티 코어 환경에서 스레드의 동작은 일반적으로 위의 그림과 같다.  스레드는 코어 마다 할당이 되고, 또 각 코어 별로 Cache Memory를 두고 있다. 그렇지만 결국에는 모두가 하나의 메인 메모리를 참조하고 있는 구조이다.</p>
<p>이러한 [스레드 - 캐시 - 메인 메모리] 구조로 인해 공유 자원에 여러 스레드가 동시에 접근하게 되면 문제가 발생할 수 있다. </p>
<p>여기서는 동시성 이슈와 관련한 여러 용어와 개념을 정리하고자 한다. 🤓</p>
<br />

<hr />
<h2 id="동시성-병렬성">동시성, 병렬성?</h2>
<p>비슷한 듯 다른 용어이다. '동시에'가 물리적이냐, 논리적이냐 기준을 두고 기억하면 좋을 것 같다. </p>
<ul>
<li><strong>병렬성(Parallelism)</strong><ul>
<li><strong>실제로</strong> 물리적으로 여러 작업이 <strong>동시에</strong>(simultaneously) 처리되는 것</li>
<li>예) 멀티 코어에서 멀티 스레드 동작</li>
</ul>
</li>
<li><strong>동시성(Concurrency)</strong><ul>
<li>각 작업을 빠르게 번갈아가며 수행해서(컨텍스트 스위칭) 논리적으로는 <strong>동시에</strong>(concurrently) <strong>실행되는 것처럼</strong> 보이게 만드는 것</li>
<li>예) 싱글 코어에서 멀티 스레드 동작</li>
<li>적절하게 컨텍스트 스위칭이 일어나서 idle time(남는 시간)을 최소화 하는 것이 목적이다.</li>
</ul>
</li>
</ul>
<br />

<hr />
<h2 id="thread-safe">Thread-Safe?</h2>
<p>간단히 말해서 동시성 이슈가 발생하지 않는 상태.</p>
<p>여러 스레드가 하나의 자원(변수, 객체 등)에 동시에 접근해도 프로그램이 정상적으로 동작하는 상태 / 데이터의 일관성이 보장될 수 있는 상태.</p>
<hr />
<h2 id="가시성-원자성">가시성, 원자성?</h2>
<h3 id="🦄-가시성visibility">🦄 가시성(visibility)</h3>
<p>멀티스레드 환경에서 각각의 스레드가 공유자원에 대해서 모두 같은 상태를 바라보고 있는 것.</p>
<p>그런데 각 스레드는 개별 CPU 코어에서 동작하는데 이 각각의 코어 마다 할당된 캐시가 따로 존재한다. 그렇기 때문에 공유 자원에 변화가 생겨 메인 메모리가 업데이트 되어도 기존의 캐시를 참조하게 되면 스레드들이 서로 다른 상태의 자원을 바라보게 되는 문제가 발생한다.</p>
<p>➡️ 이렇게 각 코어의 Cache 메모리와 메인 메모리의 값이 일치하지 않는 문제를 비가시성이라고 한다.</p>
<p><code>volatile</code> 키워드를 활용해 해결할 수 있다.</p>
<h3 id="🦄-원자성atomicity">🦄 원자성(atomicity)</h3>
<p>하나의 연산이 실제로도 하나의 과정, 하나의 연산으로 처리되는 것.</p>
<p>원자성을 보장하기 위해서는 중간에 어떠한 방해도 받지 않고 어셈블리어 명령어 하나로 실행될 수 있어야 한다. </p>
<p>프로그래밍 코드 상으로는 한 줄이여도 원자적 연산이 아닌 경우도 있다. 예를 들어, <code>problem++</code> 같은 연산은 원자적이지 않다.</p>
<p>다음은 <code>problem++</code>의 어셈블리어 코드이다.</p>
<pre><code class="language-nasm">LOAD problem to R1     # 메모리에서 로드
R1 = R1 + 1            # 더하기 연산 수행
STORE R1 to problem    # 메모리에 업데이트</code></pre>
<p><code>problem++</code> 이 한 줄이 실제로는 총 세 줄의 과정으로 동작한다. </p>
<p>만약 <code>STORE</code> 직전에 다른 스레드로 컨텍스트 스위칭이 된다면 다른 스레드는 앞선 스레드가 <code>LOAD</code>한 problem 값과 동일한(STORE 결과가 반영되지 않은) 값을 <code>LOAD</code>하게 될 것이다.</p>
<p>이렇게 여러 개로 쪼개진 instruction 수행 사이에 다른 스레드가 공유 자원에 접근하게 되면 각 스레드가 서로 다른 상태의 공유 자원을 사용하게 되는 문제가 발생한다.</p>
<p><code>synchronized</code> 키워드를 활용해 해결할 수 있다.</p>
<br />

<hr />
<h2 id="📚-참고-자료">📚 참고 자료</h2>
<ul>
<li>동시성과 병렬성<ul>
<li><a href="https://seamless.tistory.com/42">https://seamless.tistory.com/42</a></li>
</ul>
</li>
<li>Thread-safe<ul>
<li><a href="https://developer-ellen.tistory.com/205">https://developer-ellen.tistory.com/205</a></li>
</ul>
</li>
<li>가시성과 원자성<ul>
<li><a href="https://shuu.tistory.com/57">https://shuu.tistory.com/57</a></li>
<li><a href="https://shuu.tistory.com/58?category=1013667">https://shuu.tistory.com/58?category=1013667</a></li>
</ul>
</li>
</ul>