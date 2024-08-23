<p><a href="https://velog.io/@yje9802/Java-%EC%9E%90%EB%B0%94-%EB%A9%B4%EC%A0%91-%EB%8C%80%EB%B9%84-%EA%B0%9C%EB%85%90-%EC%A0%95%EB%A6%AC-2" target="blank">원본 링크</a></p><br><h2 id="어노테이션annotation">어노테이션(Annotation)</h2>
<blockquote>
<p>✅ <strong>Annotation</strong></p>
</blockquote>
<ul>
<li>주석과 비슷하게 특정 코드를 사용하는 프로그램에게 정보를 전달하는 기능을 하는 일종의 메타데이터</li>
<li>작성한 코드에 대해 추가적인 정보를 제공하면서 컴파일 타임 혹은 런타임 시점에서 해당 코드에 필요한 추가적인 처리를 해 주는 역할</li>
</ul>
<h4 id="어노테이션-등장-배경">어노테이션 등장 배경</h4>
<ul>
<li>주석이 없던 시절에는, 소스 코드와 문서화가 별도로 진행되었다.
➡️ 소스 코드만 변경하고 문서를 변경하지 않는 일이 자주 발생하였고, 코드와 문서의 버전 불일치 문제를 해결하고자 어노테이션 탄생</li>
</ul>
<h4 id="어노테이션의-역할">어노테이션의 역할</h4>
<ul>
<li>컴파일러에게 문법 에러를 체크하도록 정보 제공</li>
<li>프로그램을 빌드할 때 코드를 자동으로 생성할 수 있도록 정보 제공</li>
<li>런타임 동안에도 특정 기능을 실행하도록 정보 제공 (Java Reflection)</li>
</ul>
<h4 id="어노테이션의-특징">어노테이션의 특징</h4>
<blockquote>
<p><em>Annotations <strong>do not directly affect program semantics</strong>, but they do <strong>affect the way programs are treated by tools and libraries</strong>, which can in turn affect the semantics of the running program. Annotations can be read from source files, class files, or <strong>reflectively at run time</strong>.</em>
<a href="https://docs.oracle.com/javase/8/docs/technotes/guides/language/annotations.html">https://docs.oracle.com/javase/8/docs/technotes/guides/language/annotations.html</a></p>
</blockquote>
<ul>
<li>어노테이션 자체는 프로그램 코드의 동작에 영향을 끼치지 않는다.</li>
<li>프로그램이 처리되는 방식에는 영향을 끼친다.</li>
<li>런타임 시점에 반사적으로 어노테이션을 읽어올 수 있다.<ul>
<li>리플렉션</li>
</ul>
</li>
</ul>
<h4 id="어노테이션의-장점">어노테이션의 장점</h4>
<ul>
<li>어노테이션을 통해 소스 코드와 설정 정보를 같이 관리할 수 있어서 편하다.</li>
<li>비지니스 로직을 방해하지 않고, 필요한 정보를 제공할 수 있다.</li>
</ul>
<h4 id="어노테이션의-종류">어노테이션의 종류</h4>
<ul>
<li><p><strong>표준 어노테이션</strong>
  자바에서 기본적으로 제공하는 어노테이션
  @Override, @Deprecated, @FunctionalInterface, @SuppressWarning, @SafeVarargs</p>
</li>
<li><p><strong>메타 어노테이션</strong>
  어노테이션을 정의하는 데에 사용하는 어노테이션
  @Target, @Documented, @Inherited, @Retention, @Repeatable</p>
</li>
<li><p><strong>사용자 정의 어노테이션</strong>
  사용자가 직접 정의하여 사용하는 어노테이션</p>
</li>
</ul>
<hr />
<h2 id="리플렉션reflection">리플렉션(Reflection)</h2>
<p><img alt="" src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZWQwNGhveDNmeWRjOWM5ODBmeXlhOXlqNnp1M2d5N2hkdGJoeWN0NyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wfETXXGtH2lDW/giphy.gif" /></p>
<blockquote>
<p>✅ <strong>Reflection</strong></p>
</blockquote>
<ul>
<li><p>구체적인 클래스 타입을 알지 못하더라도 그 클래스의 메서드, 타입, 변수들에 접근할 수 있도록 해주는 자바 API</p>
</li>
<li><p>런타임 중에 동적으로 특정 클래스의 정보를 추출할 수 있다.</p>
</li>
<li><p>개발자가 작성 시점에는 어떠한 클래스를 사용해야 할지 모르지만 런타임 시점에서 클래스를 가져와서 실행해야하는 경우 사용한다.</p>
<ul>
<li>런타임 환경의 자바 클래스가 다른 자바 클래스의 정보를 확인 할 수 있게 해준다.</li>
<li>➡️ 어노테이션이 리플렉션을 이용하여 프로그램 실행 도중 동적으로 클래스의 정보를 가져와서 사용한다.</li>
<li>➡️ IntelliJ의 자동완성 기능도 리플렉션을 이용한다고 한다.</li>
</ul>
</li>
<li><p>리플렉션을 통해 Class, Constructor, Method, Field 정보를 가져올 수 있다.</p>
</li>
</ul>
<h4 id="리플렉션의-단점">리플렉션의 단점</h4>
<ul>
<li><code>Field.setAccessible()</code> 메서드를 사용하면 외부에서 접근할 수 없는 private 멤버 변수에도 접근할 수 있다.<ul>
<li>캡슐화가 깨질 수 있다.</li>
</ul>
</li>
<li>컴파일 에러가 아닌 런타임 에러가 발생한다.</li>
</ul>
<hr />
<h2 id="string-객체">String 객체</h2>
<h3 id="string-literal-vs-string-object">String Literal vs. String Object</h3>
<p><strong>String literal</strong></p>
<pre><code class="language-java">String str = &quot;Jieun&quot;;</code></pre>
<p>이렇게 생성된 변수는 JVM의 Heap 영역 내부에 있는 <strong>String Constant Pool</strong>에 할당된다.
➡️ Constant, 즉 상수로 사용되기 때문에 가변성(immutable)이 허용되지 않는다.</p>
<p>두 문자열 변수가 동일한 값(리터럴)을 갖게 되면 두 변수는 서로 같은 주소값을 갖게 된다.
➡️ <strong><code>new String()</code> 방식보다 메모리를 절약할 수 있다.</strong></p>
<p><strong>String Object</strong></p>
<pre><code class="language-java">String str = new String(&quot;Jieun&quot;);</code></pre>
<p>매번 새로운 String 인스턴스를 Heap 메모리에 할당한다.</p>
<pre><code class="language-java">// 주소값 확인 예시

String literalStr01 = &quot;Jieun&quot;;
String literalStr02 = &quot;Jieun&quot;;

System.out.println(&quot;literalStr01 주소값 : &quot;+System.identityHashCode(literalStr01));
System.out.println(&quot;literalStr02 주소값 : &quot;+System.identityHashCode(literalStr02));

String objStr01 = new String(&quot;hello&quot;);
String objStr02 = new String(&quot;hello&quot;);

System.out.println(&quot;objStr01 주소값 : &quot;+System.identityHashCode(objStr01));
System.out.println(&quot;objStr02 주소값 : &quot;+System.identityHashCode(objStr02));</code></pre>