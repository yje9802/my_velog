<p><a href="https://velog.io/@yje9802/%EC%97%90%EB%9F%AC-%ED%95%B4%EA%B2%B0-Spring-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%8B%A4%ED%96%89-%EC%8B%A4%ED%8C%A8%ED%95%98%EB%8A%94-%EA%B2%BD%EC%9A%B0-%ED%95%B4%EA%B2%B0" color="black">원본 링크</a></p><br><h2 id="문제-상황">문제 상황</h2>
<p>Spring 기반 웹서비스 협업 프로젝트를 하고 있는 중인데 
다른 분이 작업하신 브랜치와 merge 한 이후로 프로젝트 실행이 안 되는 문제가 발생했다. </p>
<p>분명 혼자 작업할 때는 잘만 되던 것이 아예 실행조차 안 되는 것이다. 더군다나 내가 한 부분은 특별히 의존성 추가도 없고 정말 간단한 CRUD 기능 추가였어서 의존성 충돌이라거나 이런 것이 원인일리도 없었다.</p>
<p>당시 내가 만난 문제 상황은 다음과 같다. </p>
<h3 id="📌-문제-1">📌 문제 1</h3>
<blockquote>
<p>*<em>Process finished with exit code 0 *</em></p>
</blockquote>
<p>프로젝트 main 메소드를 실행하면 아무런 에러 로그 없이 종료되어 버렸다. 서버는 이렇게 실행하자마자 종료되어 버리면 안 된다. </p>
<p>build.gradle에 </p>
<pre><code>implementation 'org.springframework.boot:spring-boot-starter-web'</code></pre><p>도 잘 추가 되어 있었다. </p>
<h3 id="📌-문제-2">📌 문제 2</h3>
<blockquote>
<p><strong>org.springframework.beans.factory.CannotLoadBeanClassException</strong></p>
</blockquote>
<p>프로젝트 시작 시 빈을 찾을 수 없다는 문제 발생하는 경우 나타나는 에러이다.</p>
<p>보통 이 에러는 문제가 되는 파일이 존재하지 않거나, 경로가 잘못 되었거나, 또는 오타 등의 문제가 존재할 때 발생한다. 그러나 나의 경우 문제가 되는 Bean 파일은 아무런 문제 없이 프로젝트 내에 잘 존재했다. </p>
<h3 id="📌-문제-3">📌 문제 3</h3>
<blockquote>
<p><strong>java.lang.ClassNotFoundException</strong></p>
</blockquote>
<p>이 경우가 가장 문제였다. </p>
<p>실제 에러 코드는 다음과 같다.</p>
<pre><code>Caused by: java.io.FileNotFoundException: class path resource [jakarta/servlet/Filter.class] cannot be opened because it does not exist</code></pre><p>문제가 된 jakarta/servlet/Filter는 JWT 검사를 위해 반드시 필요한 의존성이라 애초에 내가 따로 파일을 작성하는 것이 아니었다. </p>
<p>즉, Gradle이 build 할 때 알아서 갖고 오는 거라 내가 경로를 잘못 작성했거나 할 리가 없다는 것! </p>
<p>디버그 모드로 하나하나 확인해봤지만 실수나 문제점은 발견할 수 없었다.😭</p>
<h2 id="해결하기-위해-시도한-것">해결하기 위해 시도한 것</h2>
<p>위 세가지 에러 상황은 보통 빌드가 꼬였거나 빌드가 제대로 안 되었기 때문에 발생하는 상황이다. 따라서 구글링 해도 해결법은 항상 똑같았다.</p>
<blockquote>
<ol>
<li>build.gradle에 <code>implementation 'org.springframework.boot:spring-boot-starter-web'</code> 의존성 추가</li>
<li>프로젝트에서 out 패키지 삭제</li>
<li>Gradle clean</li>
<li>Project Rebuild </li>
<li>그래도 안 되면 Invalidate Caches에서 캐시 삭제</li>
</ol>
</blockquote>
<p>1번은 애초에 추가되어 있었기에 해당 사항이 없었고, 2<del>5번을 정말 스무 번은 넘게 했지만 전혀 해결되지 않았다. ~</del>(험한 말🤬)~~</p>
<p>정말 어떻게 해야하나 막막했다. </p>
<h2 id="💡-의외의-해결-방법">💡 의외의 해결 방법</h2>
<p>그러다 문득 '나 설마 build.gradle에서 <code>providedRuntime 'org.springframework.boot:spring-boot-starter-tomcat'</code> 주석 처리 안 했나...?'라는 생각이 들었다. </p>
<p>그렇다... 이게 정답이었다.😇</p>
<blockquote>
<p><strong>정확히 말하면 IntelliJ 무료 버전에서 프로젝트 빌드를 Gradle 대신 IntelliJ IDEA를 사용할 경우 build.gradle에서 저 부분을 주석처리 해야 한다.</strong></p>
</blockquote>
<p>혹시 이해 안 되면 <a href="https://www.inflearn.com/questions/167473/%EC%98%A4%EB%A5%98-%EA%B4%80%EB%A0%A8%ED%95%B4%EC%84%9C-%EC%A7%88%EB%AC%B8%EB%93%9C%EB%A6%BD%EB%8B%88%EB%8B%A4">여기서 👈🏻</a> 김영한님 답변을 참고해보자.</p>
<h3 id="gradle-대신-intellij-idea-사용">Gradle 대신 IntelliJ IDEA 사용</h3>
<p>IntelliJ 무료 버전에서 Settings &gt; Build, Execution, Deployment &gt; Build Tools &gt; Gradle &gt; Build and run using: 이
<img alt="" src="https://velog.velcdn.com/images/yje9802/post/a60d2e59-a72b-42bd-bbc2-e016b840cd2b/image.png" /></p>
<p>다음 사진처럼 되어 있으면 </p>
<pre><code>Deprecated Gradle features were used in this build, making it incompatible with Gradle 9.0.</code></pre><p>이런 메시지를 띄우면서 프로젝트 빌드에 실패한다. </p>
<p>해결 방법은 두 가지인데 하나는 Gradle 버전 업데이트를 해주는 것이다. 그러나 협업 중인 프로젝트에서 함부로 버전을 업데이트 하고 싶지는 않았다. </p>
<p>그래서 IntelliJ 무료 버전의 경우에는 저 세팅을 다음 사진처럼 수정해서 사용한다. 
<img alt="" src="https://velog.velcdn.com/images/yje9802/post/4c0e5543-d95c-4582-8d0b-22428d82bae1/image.png" /></p>
<p>이렇게 Build and run using과 Run tests using을 Gradle 대신 IntelliJ IDEA로 바꿔주고 아래 Apply 버튼을 눌러 적용해주면 된다. </p>
<blockquote>
<p>본인 세팅 확인했을 때 이렇게 IntelliJ IDEA 사용 중이라면 build.gradle에서 <code>providedRuntime 'org.springframework.boot:spring-boot-starter-tomcat'</code>은 주석 처리하거나 빼버려야 tomcat 정상 작동한다. </p>
</blockquote>
<h2 id="마무리">마무리</h2>
<p>거의 일주일 가까이 혼자 로컬에서 프로젝트 따로 파서 작업하고 결과물은 깃허브에 수작업으로 옮겨주는 작업을 했는데...</p>
<p>생각보다 해결법이 간단하면서도 어처구니 없어서... 이걸 웃어야 할 지 울어야 할 지 모르겠다. 하하</p>
<p>괜히 JWT 욕만 했던 지난 날들이 스쳐 지나가지만... 그래도 이렇게 해결했을 때의 도파민이 짜릿해서 이 맛에 개발자 하나보다 오늘도 생각하게 된다.💪</p>
<blockquote>
<p>오늘의 결론: 빨리 취업해서 IntelliJ 유료 버전 쓰고 싶다.</p>
</blockquote>
<hr />
<h3 id="부록-javalangclassnotfoundexception-기타-해결-방법">부록) java.lang.ClassNotFoundException 기타 해결 방법</h3>
<p><a href="https://study-easy-coding.tistory.com/86">https://study-easy-coding.tistory.com/86</a>
이 블로그 참고.</p>
<h3 id="부록-deprecated-gradle-features-were-used-in-this-build-making-it-incompatible-with-gradle-90-다른-해결-방법">부록) Deprecated Gradle features were used in this build, making it incompatible with Gradle 9.0. 다른 해결 방법</h3>
<p><a href="https://firstws.tistory.com/23">https://firstws.tistory.com/23</a>
이 블로그 참고.</p>