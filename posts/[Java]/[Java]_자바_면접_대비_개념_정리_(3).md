<p><a href="https://velog.io/@yje9802/Java-%EC%9E%90%EB%B0%94-%EB%A9%B4%EC%A0%91-%EB%8C%80%EB%B9%84-%EA%B0%9C%EB%85%90-%EC%A0%95%EB%A6%AC-2-6kapjiyy" target="blank">원본 링크</a></p><br><h1 id="jcfjava-collection-framework">JCF(Java Collection Framework)</h1>
<blockquote>
<p>✅ <strong>JCF란?</strong></p>
</blockquote>
<ul>
<li>자바에서 제공하는 자료구조 클래스 모음</li>
<li>자료구조를 활용하기 위한 표준 인터페이스로 JDK 1.2부터 추가되었다.</li>
<li>사용 빈도가 높은 자료 구조와 데이터 처리 알고리즘을 구조화하여 클래스로 구현해 놓았다.</li>
</ul>
<h4 id="jcf-장점">JCF 장점</h4>
<ul>
<li>별도로 필요한 자료 구조를 구현하는 것보다 이미 구현되어 있는 것을 사용함으로써 생산성이 향상되고 유지보수를 용이해진다.</li>
<li>컬렉션 인터페이스들은 제네릭(Generics)으로 표현되어 컴파일 시점에서 객체의 타입을 체크하기 때문에 런타임 에러를 줄이는 데 도움이 된다.</li>
</ul>
<h2 id="jcf-계층구조">JCF 계층구조</h2>
<p>크게 Collection 인터페이스와 Map 인터페이스로 나눌 수 있다.</p>
<h3 id="🔎-iterable을-상속하는-인터페이스">🔎 Iterable을 상속하는 인터페이스</h3>
<p><img alt="" src="https://velog.velcdn.com/images/yje9802/post/955bce62-5c52-4859-89d1-35c600245530/image.svg" /></p>
<h4 id="🔖-여기서-iterable-인터페이스는">🔖 여기서 Iterable 인터페이스는?</h4>
<pre><code class="language-java">// java.lang.Iterable
public interface Iterable&lt;T&gt; {
         /**
     * Returns an iterator over elements of type {@code T}.
     *
     * @return an Iterator.
     */
    Iterator&lt;T&gt; iterator();

    ...</code></pre>
<blockquote>
<p><strong>&lt;<a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html">Java 공식 문서 中</a>&gt;</strong>
<em>Implementing this interface allows an object to be the target of the &quot;for-each loop&quot; statement.</em>
<em>해당 인터페이스를 구현함으로써 객체를 for-each 루프의 대상으로 만들 수 있다.</em></p>
</blockquote>
<p>default 메소드인 <code>forEach()</code>, <code>spliterator()</code>가 있고 상속받은 클래스에서 구체화해주어야 하는 <code>iterator()</code> 추상 메소드를 갖고 있다.</p>
<h4 id="🔖-여기서-collection-인터페이스는">🔖 여기서 Collection 인터페이스는?</h4>
<pre><code class="language-java">// java.util.Collection
public interface Collection&lt;E&gt; extends Iterable&lt;E&gt;</code></pre>
<p>List, Set, Map의 상위 인터페이스이다.</p>
<p>주요 메소드로는 <code>add()</code>, <code>clear()</code>, <code>contain()</code>, <code>equals()</code>, <code>isEmpty()</code>, <code>iterator()</code>, <code>remove()</code>, <code>stream()</code> 등을 갖고 있다. </p>
<br />

<hr />
<h4 id="참고-iterable과-iterator의-차이">참고) Iterable과 Iterator의 차이</h4>
<ul>
<li><strong>Iterable</strong></li>
</ul>
<p>Iterable은 Collection 인터페이스의 상위 인터페이스로, <code>iterator()</code> 메소드를 추상 메소드로 선언하고 있다.</p>
<p>따라서 Iterable을 상속하는 하위 클래스에서 <code>iterator()</code> 메소드를 무조건 구현하도록 만든다.</p>
<ul>
<li><strong>Iterator</strong></li>
</ul>
<p>Collection과는 별개로 존재하는 인터페이스로, 컬렉션 클래스에 담긴 데이터를 하나씩 읽어올 때 사용한다. </p>
<p>Iterator가 없다면 컬렉션 클래스의 데이터를 읽어올 때마다 해당 클래스의 데이터를 꺼내오는 메소드들을 다 따로 구현해야 한다.
➡️ 코드의 일관성을 유지하여 재사용성을 극대화할 수 있다.</p>
<hr />
<br />

<h3 id="🔎-map을-상속하는-인터페이스">🔎 Map을 상속하는 인터페이스</h3>
<p><img alt="" src="https://velog.velcdn.com/images/yje9802/post/72eb7673-a1e5-47d2-bbe7-998fa492c913/image.svg" /></p>