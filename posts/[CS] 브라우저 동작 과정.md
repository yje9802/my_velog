<h2 id="관련-질문">관련 질문</h2>
<blockquote>
<p><strong><a href="http://www.naver.com%EC%9D%84">www.naver.com을</a> 주소창에 치면 무슨 일이 일어날까요?</strong></p>
</blockquote>
<h3 id="요약">요약</h3>
<p>브라우저 캐시와 공유 캐시를 확인하여 해당 요청이 이미 전에 캐싱된 요청인지 확인합니다. 만약 캐시에서 확인할 수 없다면 웹 서버의 IP 주소를 찾는 과정을 거치게 됩니다. DNS에 질의하기 전 우선 OS에 저장된 hosts 파일과 DNS 결과 캐시를 확인하고 여기서 IP 주소를 가져올 수 없다면 그때 DNS 서버에 질의하는 과정을 거칩니다. </p>
<p>이렇게 IP 주소를 획득했다면, 해당 IP를 기반으로 라우터를 통해 서버까지의 경로를 알아내고, ARP를 통해 IP 주소를 물리적 네트워크 장치의 주소인 MAC 주소로 변환하여 서버와의 연결을 수립합니다. 그 다음 TCP 연결을 수립하고 만약 HTTPS 프로토콜이라면 TLS 핸드쉐이킹도 수행합니다. </p>
<p>최종적으로 웹 서버와 연결이 수립되면 HTTP Request를 통해 원하는 파일을 요청하고 서버는 그에 맞는 Response를 보내게 됩니다. 이후에는 브라우저 렌더링 과정을 거쳐 사용자가 요청한 화면을 출력합니다.</p>
<hr />
<h2 id="웹-브라우저">웹 브라우저</h2>
<blockquote>
<p><strong>웹 서버에서 양방향으로 통신을 하며 HTML 문서, 멀티미디어 등의 컨텐츠를 열람할 수 있게 해주는 GUI 기반의 소프트웨어 프로그램</strong></p>
</blockquote>
<p><em>브라우저는 화면을 띄우기 위해 응용 계층의 HTTP 프로토콜을 이용해 데이터를 송신/수신한다.</em></p>
<h3 id="웹-브라우저의-구조">웹 브라우저의 구조</h3>
<p><img alt="" src="https://velog.velcdn.com/images/yje9802/post/146ae2db-90b0-4a8f-8576-890fc4edb3a8/image.png" /></p>
<p><a href="https://www.browserstack.com/guide/browser-rendering-engine">출처) Understanding the Role of Rendering Engine in Browsers</a></p>
<ul>
<li>사용자 인터페이스 : 주소표시줄, 이전/다음 버튼, 홈버튼, 새로고침/정지 버튼 등 요청한 페이지를 보여주는 창 외에 사용자가 컨트롤 할 수 있는 부분</li>
<li>브라우저 엔진 : 사용자 인터페이스와 렌더링 엔진 사이의 동작을 제어한다.(webkit, blink)</li>
<li>렌더링 엔진 : 요청한 URI(리소스)를 브라우저 엔진에게 받아서 server에게 요청한다(통신). server로 부터 URI에 해당하는 데이터(HTML, CSS, JavaScript)를 받아서 파싱한 후 렌더링한다.(화면에 출력한다.)(chrome webkit)</li>
<li>통신 : 렌더링 엔진으로부터 HTTP 요청 등을 받아서 네트워크 처리 후 응답을 전달한다.(OS 단에서 실행)</li>
<li>자바스크립트 해석기 : JavaScript를 해석하고 실행한다.(chrome V8)</li>
<li>UI 백엔드 : render tree를 browser 에 그리는 역할을 담당한다</li>
<li>자료 저장소 : 쿠키 등의 자료를 컴퓨터 하드디스크에 저장한다. (HTML5 부터 Web Database에 저장가능) 로컬 스토리지 + 세션 스토리지</li>
</ul>
<hr />
<h2 id="브라우저-동작-과정">브라우저 동작 과정</h2>
<blockquote>
<p>브라우저에 URL을 입력했을 때 화면에 페이지가 나타나기까지 어떤 과정을 거치는 지를 설명한다.</p>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/yje9802/post/eba12d0b-a3f6-4bfc-9214-e49ec2fd3b22/image.png" /></p>
<p><a href="https://w3c.github.io/resource-timing/#attribute-descriptions">출처) W3C Editor's Draft 08 February 2024 -  Resource Timing</a></p>
<h3 id="✅-리다이렉트">✅ 리다이렉트</h3>
<p>서버는 클라이언트로부터 요청을 받은 후, 클라이언트에게 특정 URL을 이동하라고 요청 + 상태코드 302</p>
<p>리다이렉트가 있다면 그 리다이렉트를 진행, 없다면 해당 요청에 대한 과정을 진행</p>
<hr />
<h3 id="✅-캐싱">✅ 캐싱</h3>
<p><img alt="" src="https://velog.velcdn.com/images/yje9802/post/16fbc110-8f71-4506-9eeb-ff778aad60bc/image.png" /></p>
<p><a href="https://medium.com/codex/methods-to-optimize-your-node-js-application-a5261ccc9b9">참고 사이트) https://medium.com/codex/methods-to-optimize-your-node-js-application-a5261ccc9b9</a></p>
<p>해당 요청이 캐시를 사용할 수 있는지 파악</p>
<p>캐싱이 이미 된 요청이라면 캐싱된 값을 반환하여 빠르게 렌더링, 캐시가 없는 새로운 요청이라면 그 다음 단계로 진행</p>
<p>web server에 대한 부하도 줄이고, 응답 속도도 빠르게 하기 위해 사용</p>
<h4 id="👉🏻-캐시-종류">👉🏻 캐시 종류</h4>
<ul>
<li><p><strong>브라우저 캐시</strong></p>
</li>
<li><p>쿠키, 로컬 스토리지 등 브라우저에 저장된 캐시*</p>
</li>
<li><p>브라우저 자체가 HTTP를 통해 다운 받은 모든 문서를 보유하는 것*</p>
</li>
<li><p>상태코드 304*</p>
</li>
<li><p><strong>공유 캐시</strong></p>
</li>
<li><p>클라이언트와 서버 사이에 위치하며, 사용자 간에 공유할 수 있는 응답을 저장하는 캐시*</p>
</li>
<li><p>리버스 프록시(서버 앞단에 프록시 서버를 둬서 캐싱)*</p>
</li>
<li><p>서버의 부하를 줄일 수 있다.*</p>
</li>
<li><p>예) NginX를 프록시 서버로 둬서 캐싱, cloudflare, …*</p>
</li>
</ul>
<hr />
<h3 id="✅-dns-질의">✅ DNS 질의</h3>
<p>입력한 URL의 웹서버로 요청하기 위해서는 해당 웹서버의 IP 주소를 알아야 한다.</p>
<ol>
<li><p><code>hosts 파일 검색</code>
 ip 주소와 hostname 을 매칭시켜놓은 텍스트 파일</p>
</li>
<li><p><code>DNS 캐시 검색</code>
 DNS 조회 결과를 저장하는 캐시</p>
<p> 다음의 순서로 캐시를 조회한다.</p>
<ol>
<li><p>브라우저 캐시
 기존에 방문한 적이 있다면 브라우저가 결과를 일정 기간 동안 캐싱
 <code>chrome://net-internals/#dns</code></p>
</li>
<li><p>OS 캐시
 system call 필요
 local DNS cache</p>
</li>
<li><p>라우터 캐시</p>
</li>
<li><p>ISP 캐시</p>
</li>
</ol>
</li>
<li><p><code>DNS 서버에 질의</code>
 hosts 파일과 캐시에서 알아낼 수 없다면 최종적으로 DNS 서버에 질의한다.</p>
</li>
</ol>
<h4 id="👉🏻-fqdn">👉🏻 FQDN</h4>
<p><em>Fully Qualified Domain Name</em>
<em>호스트와 도메인이 합쳐진 완전한 도메인 이름</em></p>
<h4 id="👉🏻-dns">👉🏻 DNS</h4>
<p><em>Domain Name System; FQDN을 IP 주소로 바꿔주는 시스템</em></p>
<h4 id="👉🏻-isp">👉🏻 ISP</h4>
<p><em>Internet Service Provider; KT처럼 인터넷 서비스를 제공하는 주체</em></p>
<h4 id="👉🏻-cdn">👉🏻 CDN</h4>
<ul>
<li><em>Content Delivery Network; 컨텐츠 전송 네트워크</em></li>
<li><em>최종 사용자와 가까운 곳에 컨텐츠를 캐시하는 지리적으로 분산된 서버 그룹으로, 서버와 사용자 사이의 물리적 거리를 줄여 컨텐츠 로딩에 소요되는 시간을 최소화한다.</em><h4 id="👉🏻-gslb">👉🏻 GSLB</h4>
</li>
<li><em>Global Server Load Balancing; 글로벌 서버 부하 분산</em></li>
<li><a href="https://www.samsungsds.com/kr/network-gslb/gslb.html"><em>https://www.samsungsds.com/kr/network-gslb/gslb.html</em></a></li>
</ul>
<hr />
<h3 id="✅-ip-라우팅">✅ IP 라우팅</h3>
<p>IP 주소를 획득했다면, 해당 IP를 기반으로 <code>라우팅</code>, <code>ARP 과정</code>을 거쳐 실제 서버를 찾는다.</p>
<p>라우터를 통해 서버까지의 경로를 알아내고, ARP를 통해 IP 주소를 물리적 네트워크 장치의 주소인 MAC 주소로 변환하여 서버와의 연결을 수립한다.</p>
<p>라우터는 IP네트워크, 서브넷을 관리하면서 다른 네트워크를 거쳐 패킷을 전송하는 역할을 하는 장비이고, 라우팅은 그 패킷을 보낼 경로를 선택하는 과정이다. </p>
<p>ARP는 Address Resolution Protocol의 약자로, IP 주소에 맞는 물리적인 주소 MAC 주소를 가지고 오는 프로토콜이다. ARP 프로토콜을 통해 정확한 주소(MAC 주소)를 알아내어 정확한 위치를 찾아 통신해야 한다.</p>
<p><a href="https://images.app.goo.gl/wNFRaFKwMEjXfXwZ8"><img alt="" src="https://velog.velcdn.com/images/yje9802/post/3e4da43e-165c-4246-a2b4-3d70ab669a5c/image.png" /></a></p>
<hr />
<h3 id="✅-tcp-연결">✅ TCP 연결</h3>
<p>IP의 특징인 비신뢰성과 비연결성으로 인해 IP주소 만으로는 통신을 할 수 없어 브라우저가 HTTP 통신을 위해 <code>TCP 연결</code>을 구축한다.</p>
<ul>
<li>HTTPS라면 <code>SSL/TLS 핸드쉐이킹</code>도 일어난다. </li>
<li>HTTP/3은 TCP가 아닌 <code>QUIC 연결</code>이 일어난다.</li>
</ul>
<hr />
<h3 id="✅-서버로부터-컨텐츠-다운로드">✅ 서버로부터 컨텐츠 다운로드</h3>
<p><code>HTTP Request</code> → <code>HTTP Response</code></p>
<p>최초에는 html 파일만 브라우저가 받아오고 이후 필요한 파일을 만날 때마다 <code>HTTP Request</code>를 보내 받아온다.</p>
<h4 id="👉🏻-ttfb">👉🏻 TTFB</h4>
<p><a href="https://stackoverflow.com/questions/69116839/does-ttfb-include-the-time-for-the-request-that-redirects-to-my-page"><img alt="" src="https://velog.velcdn.com/images/yje9802/post/2f24fa45-dc96-4fc4-a224-358b54d0f2e0/image.png" /></a></p>
<ul>
<li><em>Time to First Byte; 서버의 성능을 보여주는 척도</em></li>
<li><em>HTTP 요청을 보내고 HTML의 첫 패킷(일반적으로 14kB)을 받는데 걸린 시간</em></li>
<li><em>the duration from the user or client making an HTTP request to the first byte of the page being received by the client's browser</em></li>
</ul>
<h4 id="👉🏻-tcp-슬로우-스타트">👉🏻 TCP 슬로우 스타트</h4>
<ul>
<li><em>첫 응답 패킷은 14kB, 이후 네트워크의 최대 대역폭을 파악할 수 있을 때까지 점진적으로 데이터의 전송량을 증가 (14kB rule)</em></li>
<li><em>혼잡을 피하기 위해서 네트워크의 용량에 적당한 전송 속도를 찾고자 점진적으로 속도를 높여나간다.</em></li>
<li>[MDN 공식 문서] (<a href="https://developer.mozilla.org/ko/docs/Web/Performance/How_browsers_work#tcp_%EC%8A%AC%EB%A1%9C%EC%9A%B0_%EC%8A%A4%ED%83%80%ED%8A%B8_tcp_slow_start_14kb_rule">https://developer.mozilla.org/ko/docs/Web/Performance/How_browsers_work#tcp_%EC%8A%AC%EB%A1%9C%EC%9A%B0_%EC%8A%A4%ED%83%80%ED%8A%B8_tcp_slow_start_14kb_rule</a>)</li>
<li><a href="https://velog.io/@sejinkim/%EC%9B%B9-%EC%82%AC%EC%9D%B4%ED%8A%B8%EC%9D%98-%ED%81%AC%EA%B8%B0%EA%B0%80-14KB-%EB%AF%B8%EB%A7%8C%EC%9D%B4%EC%96%B4%EC%95%BC-%ED%95%98%EB%8A%94-%EC%9D%B4%EC%9C%A0">더 알아보기</a></li>
</ul>
<hr />
<h3 id="✅-브라우저-렌더링">✅ 브라우저 렌더링</h3>
<p>응답받은 데이터를 바탕으로 브라우저 엔진의 렌더링 과정을 거쳐 사용자가 요청한 화면을 표시한다.</p>
<p>이때 응답받은 데이터들은 브라우저가 자체적으로 캐싱한다.(브라우저 캐시)</p>
<hr />
<h2 id="참고자료">참고자료</h2>
<h4 id="유튜브-영상">유튜브 영상</h4>
<ul>
<li>[What happens when you type a URL into your browser?] (<a href="https://youtu.be/AlkDbnbv7dk?si=2MqjYeojpNdEmJQ4">https://youtu.be/AlkDbnbv7dk?si=2MqjYeojpNdEmJQ4</a>)</li>
<li><a href="https://youtu.be/GAyZ_QgYYYo?si=Mixces4U4ThgYx5k">웹 브라우저에 URL 입력하면 일어나는 일 - 인프라 위주</a></li>
<li><a href="https://youtu.be/YahjHM9UNCA?si=MJ1zeiC74_pivtDl">www.naver.com을 주소창에 치면 무슨 일이 일어날까요?</a></li>
<li><a href="https://www.youtube.com/watch?v=ipwfEUslfQA">크롬 브라우저에 URL을 입력하면 어떤 과정이 진행될까?</a></li>
</ul>
<h4 id="블로그">블로그</h4>
<ul>
<li><a href="https://velog.io/@wlwl99/%EB%B8%8C%EB%9D%BC%EC%9A%B0%EC%A0%80-%EB%8F%99%EC%9E%91-%EC%9B%90%EB%A6%AC-%EA%B5%AC%EC%A1%B0">브라우저 동작 원리 &amp; 구조</a></li>
<li><a href="https://study-ihl.tistory.com/206">크롬 브라우저 작동원리2 - 페이지 이동</a></li>
<li><a href="https://davidhwang.netlify.app/Developments/browser-rendering-process/">browser elements</a></li>
<li><a href="https://brunch.co.kr/@seungjoonlernnx/100">브라우저에 google.com을 치면 일어나는 일들</a></li>
</ul>