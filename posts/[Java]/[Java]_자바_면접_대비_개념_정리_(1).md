<p><a href="https://velog.io/@yje9802/%ED%85%8C%ED%81%AC-%EC%9E%90%EB%B0%94-%EB%A9%B4%EC%A0%91-%EB%8C%80%EB%B9%84-%EA%B0%9C%EB%85%90-%EC%A0%95%EB%A6%AC-1" target="blank">원본 링크</a></p><br><h2 id="java의-특징">Java의 특징</h2>
<ul>
<li><strong>운영체제에 독립적</strong><ul>
<li>자바 응용 프로그램은 JVM과만 통신</li>
<li>자바로 작성된 프로그램은 운영체제와 하드웨어에 관계없이 실행 가능하다.</li>
<li>WORA(Write Once Read Anywhere)</li>
</ul>
</li>
<li><strong>객체지향 언어</strong></li>
<li><strong>Garbage Collection</strong><ul>
<li>가비지 컬렉터가 있어 이를 통해 자동적으로 메모리 관리가 가능</li>
</ul>
</li>
<li><strong>네트워크와 분산처리 지원</strong></li>
<li><strong>멀티스레드 지원</strong></li>
<li><strong>동적 로딩 지원</strong><ul>
<li>실행 시에 모든 클래스가 로딩되지 않고, 필요한 시점에 클래스를 로딩하여 사용할 수 있다.</li>
<li>➡️ 일부 클래스가 변경되어도 전체 애플리케이션을 다시 컴파일하지 않아도 된다.</li>
</ul>
</li>
</ul>
<h2 id="java의-실행-과정">Java의 실행 과정</h2>
<p><img alt="" src="https://velog.velcdn.com/images/yje9802/post/8337a6c3-d74c-40f3-92e2-0ae519dbeefe/image.png" /></p>
<p><a href="https://pienguin.tistory.com/m/entry/JAVA-%EC%9E%90%EB%B0%94-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8-%EC%8B%A4%ED%96%89-%EA%B3%BC%EC%A0%95-%EB%B0%8F-%EA%B8%B0%EB%B3%B8-%EA%B5%AC%EC%A1%B0">이미지 출처</a></p>
<p>Java로 작성된 파일을 Java컴파일러가 가상 기계어 파일인 Java클래스 파일(*.class)로 만든다. 다시 말해, 소스 코드를 Java 바이트 코드로 번역한다. </p>
<p>이후 Java 바이트 코드를 JVM이 읽고 실행하게 된다.</p>
<p>JVM 에 있는 .class 파일들을 Execution Engine 이 명령어 단위로 하나씩 실행하는데, 이 때 내부적으로는 Interpreter와 JIT Complier 를 통해 해석한다.</p>
<p>해석된 바이트 코드는 Runtime Data Area에 배치되어 실질적인 수행이 이루어진다.</p>
<h3 id="👩💻-바이트-코드">👩‍💻 바이트 코드?</h3>
<ul>
<li>JVM이 이해할 수 있는 언어로 변환된 자바 소스 코드<ul>
<li>기계어는 아니고 기계어와 자바 코드 사이의 중간 단계</li>
<li>확장자는 .class이며 자바 바이트 코드는 자바 가상 머신만 설치되어 있으면, 어떤 운영체제에서 라도 실행될 수 있다.</li>
</ul>
</li>
<li>자바 컴파일러에 의해 변환되는 코드의 명령어 크기가 1바이트라서 자바 바이트 코드라고 부름</li>
<li>바이너리 코드와 다르게 환경에 종속적이지 않고 실행가능</li>
</ul>
<h3 id="👩💻-인터프리터와-컴파일러">👩‍💻 인터프리터와 컴파일러?</h3>
<ul>
<li><strong>인터프리터</strong><ul>
<li>소스코드의 각 행을 한 줄 한 줄 분석해 바이트코드를 기계어로 변환</li>
<li>컴파일러 방식보다 느림</li>
</ul>
</li>
<li><strong>JIT 컴파일러</strong><ul>
<li>Just In Time</li>
<li>JRE 안에 존재하며, JVM이 호출되는 메서드 각각에 대해 호출마다 호출 횟수를 누적해서 그 횟수가 특정 수치를 초과 할 때 컴파일</li>
<li>컴파일 방식은 전체 소스코드를 보고 명령어를 해석해 기계어로 변환하는 방식</li>
<li>컴파일 임계치<ul>
<li>얼마나 자주 호출되는지 검사한 후 '이제는 컴파일이 필요한 시점이다'라고 판단하는 어떠한 기준</li>
</ul>
</li>
</ul>
</li>
</ul>
<h3 id="👩💻-java-실행-과정을-통해-알-수-있는-java의-단점">👩‍💻 Java 실행 과정을 통해 알 수 있는 Java의 단점</h3>
<ul>
<li>JVM을 반드시 한 번 거쳐야 하는 구조이므로 상대적으로 실행 속도가 느리다.<ul>
<li>➡️ 개선하기 위해 JIT 컴파일러 도입, 그래도 C언어 보다는 느리다.</li>
</ul>
</li>
</ul>
<h2 id="java-주요-버전">Java 주요 버전</h2>
<p>일반적으로 Java 8, 11, 17이 중요하다.</p>
<ul>
<li>Java 8<ul>
<li>오라클 인수 후 첫번째 버전<ul>
<li>이후 Oracle JDK, Open JDK로 나뉜다.</li>
</ul>
</li>
<li>Lambda 및 함수형 프로그래밍, 메소드 참조 기능, Stream API, 새로운 날짜와 시간 API 추가</li>
<li>2014년 공개되어 2019년 1월에 일반 지원 종료</li>
</ul>
</li>
<li>Java 11<ul>
<li>Oracle JDK의 기능이 OpenJDK에 통합되어 두 JDK가 동일해짐</li>
<li>오라클이 제공하는 Oracle JDK는 유료화, Open JDK를 기반으로 하는 다른 서드파티 JDK가 대안으로 등장</li>
<li>2018년 공개되어 2023년 9월 일반 지원 종료</li>
</ul>
</li>
<li>Java 17<ul>
<li>의사난수 생성기를 통해 난수 생성하는 API 추가</li>
<li>2021년 공개</li>
</ul>
</li>
</ul>
<p>더 알아보고 싶다면 <a href="https://garonguri.tistory.com/143">이 블로그</a> 참고! (shout out to my friend🤣)</p>
<h2 id="jdk-jre-그리고-jvm">JDK, JRE, 그리고 JVM</h2>
<p><img alt="" src="https://velog.velcdn.com/images/yje9802/post/412611bf-6ae1-4aa8-89d1-7e39117bd7a8/image.png" /></p>
<p><a href="https://www.geeksforgeeks.org/differences-jdk-jre-jvm/">이미지 출처</a></p>
<ul>
<li><strong>JDK</strong><ul>
<li>Java Development Kit</li>
<li>자바 언어 기반의 소프트웨어를 개발하기 위한 도구</li>
<li>JRE와 컴파일러를 포함</li>
</ul>
</li>
<li><strong>JRE</strong><ul>
<li>Java Runtime Environment</li>
<li>자바 코드를 실행하기 위해 필요한 라이브러리, API를 담고 있는 패키지</li>
<li>JVM, Java 클래스 라이브러리를 포함</li>
</ul>
</li>
<li><strong>JVM</strong><ul>
<li>Java Virtual Machine</li>
<li>OS에 상관없이 자바를 실행시킬 수 있는 프로그램</li>
<li><strong>JVM만 있으면 운영체제가 리눅스든, 맥이든 관계없이 운영체제로부터 독립적으로 프로그램을 제약없이 실행할 수 있다는 의미</strong></li>
</ul>
</li>
</ul>
<h2 id="동일성과-동등성">동일성과 동등성</h2>
<ul>
<li><strong>동일성</strong><ul>
<li>두 개의 객체가 완전히 같은 경우</li>
<li>주소 값이 같기 때문에 두 변수가 같은 객체를 가리킴</li>
<li>변수의 동일성은 <code>==</code> 연산자로 판별</li>
</ul>
</li>
<li><strong>동등성</strong><ul>
<li>두 개의 객체가 같은 정보를 갖고 있는 경우</li>
<li>변수가 참조하고 있는 객체의 주소가 서로 다르더라도 내용만 같으면 두 변수는 동등</li>
<li><code>equals</code> 연산자로 판별 가능</li>
</ul>
</li>
</ul>
<h2 id="java에서-메인-메서드가-static인-이유">Java에서 메인 메서드가 static인 이유</h2>
<p>메인 메서드는 JVM이 사용하는 프로그램의 시작점이기에 가장 먼저 실행되어야 한다. 그래서 메인 메서드를 호출할 객체가 존재해야 하지만 static이 아니라면 JVM이 시작하는 순간에 생성되어 있는 객체는 없을 것이다. 따라서 static 키워드를 사용하여 프로그램이 시작되는 순간 메모리에 올라가 객체 없이도 호출할 수 있게 하는 것이다.</p>
<p>static 키워드가 붙게 되면 JVM이 시작될 때 가장 먼저 메모리의 Static 영역에 저장되고 프로그램이 종료될 때까지 메모리에 남아있다.</p>
<h2 id="constant--literal">constant &amp; literal</h2>
<pre><code class="language-java">final int MAX_VALUE = 1000;
// MAX_VALUE : 상수
// 1000 : 리터럴</code></pre>
<ul>
<li><strong>constant</strong><ul>
<li>값을 한 번만 저장할 수 있는 공간으로, 한 번 값을 정하면 변경할 수 없음</li>
<li>리터럴에 의미있는 이름을 붙인 것이 상수</li>
<li>final 키워드로 선언할 수 있음</li>
</ul>
</li>
<li><strong>literal</strong><ul>
<li>변하지 않는 데이터 그자체</li>
</ul>
</li>
</ul>
<h2 id="primitive-type--reference-type">Primitive Type &amp; Reference Type</h2>
<p><strong>자바 데이터 타입</strong></p>
<ul>
<li><strong>Primitive Type</strong><ul>
<li>정수, 실수, 문자, 논리 리터럴 등의 <strong>실제 데이터 값을 저장</strong>하는 타입</li>
<li>int, long, double, float, boolean, byte, short, char</li>
<li>반드시 <strong>사용하기 전에 선언(Declared)</strong> 되어야하며, 자료형의 <strong>길이는 운영체제에 독립적</strong>이며 변하지 않음</li>
<li>stack에 저장</li>
</ul>
</li>
<li><strong>Reference Type</strong><ul>
<li>객체(Object)를 참조(주소를 저장)하는 타입으로 메모리 <strong>번지 값을 통해 객체를 참조</strong>하는 타입</li>
<li>String, Array, Class, …</li>
<li>java.lang.Object 클래스를 상속하는 모든 클래스들</li>
<li><strong>실제 객체</strong>는 <strong>힙(heap) 메모리에 저장</strong>되며 <strong>참조 타입 변수</strong>는 <strong>스택에 실제 객체들의 주소를 저장</strong>하여, 객체를 사용할때 마다 참조 변수에 저장된 객체의 주소를 불러와 사용</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/yje9802/post/6e222761-2024-4c67-a4ad-c0a34a41760c/image.png" /></p>
<p><a href="https://raw.githubusercontent.com/ParkJiwoon/PrivateStudy/master/java/images/screen_2022_01_30_20_51_33.png">이미지 출처</a></p>
<h3 id="primitive-vs-reference">Primitive vs. Reference</h3>
<ul>
<li>primitive type은 입력값으로 null을 담을 수 없다.</li>
<li>primitive type은 제네릭 타입에서 사용할 수 없다.</li>
<li>reference type은 최소 2번 메모리에 접근해야 하므로 상대적으로 속도가 느리다.</li>
</ul>
<h2 id="call-by-value-vs-call-by-reference">call by value vs. call by reference</h2>
<p><strong>메소드 파라미터 호출 방식</strong></p>
<ul>
<li><strong>Call by Value(Pass by Value)</strong><ul>
<li>값을 넘겨주는 방식</li>
<li>메서드를 호출하는 호출자(Caller)의 변수와 호출 당하는 수신자(Callee)의 파라미터는 복사된 <strong>서로 다른 변수</strong><ul>
<li>stack 영역에 동일한 값을 가지는 새로운 변수가 생성된다.</li>
</ul>
</li>
<li><strong>Java는 Call by Value</strong></li>
</ul>
</li>
<li><strong>Call by Reference(Pass by Reference)</strong><ul>
<li>주소를 직접 넘겨주는 방식</li>
<li>주소를 직접 넘기기 때문에 호출자의 변수와 수신자의 파라미터는 <strong>완전히 동일한 변수</strong><ul>
<li>➡️ 메소드 내에서 파라미터를 수정하면 원본 변수도 그대로 수정됨</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h2 id="객체지향">객체지향</h2>
<h3 id="다형성polymorphism">다형성(Polymorphism)</h3>
<ul>
<li>하나의 메서드나 클래스가 있을 때 그것이 다양한 방법으로 동작하는 것</li>
<li>자바에서는 일반적으로 오버로딩과 오버라이딩을 통해 가능</li>
<li>객체의 재사용이 쉬워지고, 기능 확장과 변경이 용이해진다.</li>
</ul>
<h3 id="오버로딩-vs-오버라이딩">오버로딩 vs. 오버라이딩</h3>
<ul>
<li><strong>오버로딩(Overloading)</strong><ul>
<li>한 클래스 내에 같은 이름의 메서드를 여러 개 정의하는 것</li>
<li>메서드 이름은 동일하지만 반드시 매개변수의 개수나 타입이 달라야한다.</li>
</ul>
</li>
<li><strong>오버라이딩(Overriding)</strong><ul>
<li>상위 클래스가 갖고 있는 메서드를 하위 클래스에서 재정의하여 사용하는 것</li>
<li>메서드의 이름과 매개변수의 개수와 타입도 동일해야 한다.</li>
<li>메서드의 내용만 변경하는 것</li>
</ul>
</li>
</ul>
<h3 id="상속inheritance">상속(Inheritance)</h3>
<ul>
<li>기존의 클래스를 재사용해 새로운 클래스를 작성할 수 있는 것<ul>
<li>➡️ 코드의 재사용성을 높이고 코드의 중복을 제거해 프로그램의 생산성과 유지보수에 기여한다.</li>
</ul>
</li>
<li>상속해 주는 클래스를 Parent Clas(조상 클래스), 상속 받는 클래스를 Child Class(자식 클래스)라고 한다.<ul>
<li>Child Class는 Parent Class로 부터 모든 멤버를 상속받는다.</li>
<li>Parent Class가 변경되면 그 변경 사항이 Child Class에도 반영된다.</li>
</ul>
</li>
</ul>