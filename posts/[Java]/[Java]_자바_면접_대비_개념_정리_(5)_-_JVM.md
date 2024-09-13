<p><a href="https://velog.io/@yje9802/Java-%EC%9E%90%EB%B0%94-%EB%A9%B4%EC%A0%91-%EB%8C%80%EB%B9%84-%EA%B0%9C%EB%85%90-%EC%A0%95%EB%A6%AC-5-JVM" target="blank">원본 링크</a></p><br><h2 id="java-소스코드가-실행되는-전반적인-흐름">Java 소스코드가 실행되는 전반적인 흐름</h2>
<p><img alt="" src="https://velog.velcdn.com/images/yje9802/post/c7da78b2-1430-41ae-ac38-ddffd76a31a0/image.svg" /></p>
<p>Java 소스 코드가 실행되는 과정은 위 그림과 같다. 간략하게 설명해보면, </p>
<ul>
<li>Java 컴파일러에 의해 Java 소스 코드가 JVM이 실행할 수 있는 바이트 코드로 바뀌게 된다. </li>
<li>그 다음 JVM 내부의 클래스 로더에 의해 해당 Java 코드 상의 클래스들(바이트 코드)이 Runtime Data Area에 올려진다.</li>
<li>Execution Engine은 Runtime Data Area에 있는 바이트 코드를 가져와 실제로 실행한다.</li>
</ul>
<hr />
<h3 id="바이트-코드byte-code">바이트 코드(Byte Code)?</h3>
<p>✅ 바이트 코드란 JVM에서 작동하도록 만든 이진 코드이다. </p>
<p>즉, JVM이 이해할 수 있는 언어로 변환된 코드이며 명령어의 크기가 1 바이트라서 자바 바이트 코드라고 불리고, 자바 코드를 배포하는 가장 작은 단위이며, 확장자는 .class이다.</p>
<p>자바 바이트 코드는 자바 가상 머신만 설치되어 있으면, 어떤 운영체제에서라도 실행될 수 있다.</p>
<p>그렇지만 CPU는 바이트코드를 직접 실행할 수 없으므로, 이를 네이티브 코드(기계어)로 변환해주는 과정을 거쳐야 실제로 실행이 가능하다.</p>
<hr />
<h2 id="jvm-구조">JVM 구조</h2>
<p><img alt="" src="https://velog.velcdn.com/images/yje9802/post/6982497f-8bcb-41fc-9530-87c798bc56dd/image.svg" /></p>
<p>이제는 JVM을 좀 더 자세하게 알아보자.</p>