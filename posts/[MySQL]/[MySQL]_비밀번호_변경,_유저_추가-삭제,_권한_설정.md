<p><a href="https://velog.io/@yje9802/MySQL-%EB%B9%84%EB%B0%80%EB%B2%88%ED%98%B8-%EB%B3%80%EA%B2%BD-%EC%9C%A0%EC%A0%80-%EC%B6%94%EA%B0%80%EC%82%AD%EC%A0%9C-%EA%B6%8C%ED%95%9C-%EC%84%A4%EC%A0%95" target="blank">원본 링크</a></p><br><p><img alt="" src="https://velog.velcdn.com/images/yje9802/post/487d4048-dfb3-4bae-921e-10ee3236728e/image.jpg" /></p>
<p>개인 프로젝트에 적용할 수 있는 수준까지만 설명하니 참고.</p>
<h2 id="🐬-root-계정-비밀번호-변경하기">🐬 root 계정 비밀번호 변경하기</h2>
<pre><code class="language-sql">ALTER USER 'root'@'localhost' 
IDENTIFIED WITH mysql_native_password BY '새로운 비밀번호';

FLUSH PRIVILEGES;</code></pre>
<p>MySQL 8.0 버전 이후부터 가능한 구문이다. </p>
<p><code>FLUSH PRIVILEGES</code>는 '설정 적용' 정도로 이해하면 된다.</p>
<h2 id="🐬-유저-생성-및-권한-부여">🐬 유저 생성 및 권한 부여</h2>
<pre><code class="language-sql"># 유저 생성
CREATE USER 유저이름@'%' IDENTIFIED BY '비밀번호';

# 모든 권한 부여
GRANT ALL PRIVILEGES ON 데이터베이스이름.* TO 유저이름@'%';

FLUSH PRIVILEGES;</code></pre>
<p><code>유저이름@</code> 옆에 <code>'%'</code>는 모든 외부 IP에 대해 접속을 허용한다는 의미이다. 만약 특정 IP 대역에서만 접속을 허용하고 싶으면 <code>'172.120.%'</code> 이런식으로 작성하면 된다. </p>
<p><code>GRANT ALL PRIVILEGES ON 데이터베이스이름.*</code> 하면 해당 유저에게 특정 데이터베이스의 <strong>모든</strong> 테이블에 대해 <strong>모든</strong> 권한을 허용한다는 의미이다.</p>
<p><code>ALL PRIVILEGES</code> 부분이나 <code>데이터베이스이름.*</code> 부분을 변경하면 권한 정도를 제한할 수 있다. </p>
<p>예) <code>GRANT ALL PRIVILEGES ON 데이터베이스이름.테이블이름</code> 
특정 테이블에 대해 모든 권한 허용
예) <code>GRANT SELECT, INSERT ON 데이터베이스이름.*</code>
특정 데이터베이스의 모든 테이블에 대해 SELECT, INSERT 권한 허용</p>
<h3 id="유저-삭제">유저 삭제</h3>
<pre><code class="language-sql">DROP USER 유저이름@'%';</code></pre>
<h3 id="유저-권한-정보-확인">유저 권한 정보 확인</h3>
<pre><code class="language-sql">SHOW GRANTS FOR 유저이름@'%';</code></pre>