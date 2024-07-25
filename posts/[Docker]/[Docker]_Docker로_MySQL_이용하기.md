<p><a href="https://velog.io/@yje9802/Docker%EB%A1%9C-MySQL-%EC%9D%B4%EC%9A%A9%ED%95%98%EA%B8%B0" target="blank">원본 링크</a></p><br><p><img alt="" src="https://velog.velcdn.com/images/yje9802/post/46af4918-f720-43d6-aef2-dc2c98ef561f/image.png" /></p>
<blockquote>
<p><strong>💫 도커에 대해서 아무 것도 모르는 상태에서 MySQL을 다운받고 사용하기 위해 온갖 고생을 하다 눈물을 흘리며🥲 깨달은 방법을 정리해서 공유하기 위해 이 포스트를 작성합니다. 💫</strong></p>
</blockquote>
<h3 id="개인적인-하소연">개인적인 하소연</h3>
<p>개인 프로젝트를 하다보면 MySQL이나 PostgreSQL 같은 데이터베이스를 설치해서 사용해야 할 일이 많다. </p>
<p>예전에는 그냥 로컬에 설치해서 사용했다. 데이터베이스 강의도 다 로컬에 DB 설치하는 단계부터 시작하기도 하고.</p>
<p>근데 이번에 프로젝트를 하는데 이미 로컬에 MariaDB가 설치된 환경에서 MySQL을 설치하려 하다가 DB 설정부터 아주 고생했다. 그래서 해결 방법을 찾아보는데 다들 로컬에 DB 설치하지 말고 도커를 이용하라고 하는 거다! </p>
<p>그동안 도커 어려워 보여서 나중으로 미뤄왔는데 요즘은 폐쇄망 환경의 기업에서도 많이 쓴다고 하고, 무엇보다 이번엔 DB 때문에 머리가 너무 아파서 무작정 도커를 시도해봤다. </p>
<p>결론 : 진작에 도커 쓸 걸🤣🤣🤣</p>
<hr />
<p>아래 내용은 이미 Docker를 설치했다는 전제 하에  Docker에 MySQL을 내 입맛대로 설치하는 과정을 담았다. </p>
<p>혹시 도커 설치됐나 긴가민가 한 사람들은 터미널에 <code>docker -v</code> 명령어 결과로 도커 버전이 잘 나오는 지 확인하면 된다.
¡Vamos!</p>
<h2 id="🐳-docker에-mysql-다운받고-실행하기까지">🐳 Docker에 MySQL 다운받고 실행하기까지</h2>
<h3 id="mysql-이미지-다운로드">MySQL 이미지 다운로드</h3>
<pre><code class="language-bash">docker pull mysql
docker pull mysql:8.0.22</code></pre>
<p>버전 지정 없이 다운 받는다면 MySQL 최신 버전이 다운된다. Docker Desktop 이용 중이면 검색해서 다운이 가능하다.</p>
<p>다운된 이미지 목록은 아래 명령어로 확인이 가능하다.</p>
<pre><code class="language-bash">docker images</code></pre>
<h3 id="mysql-도커-컨테이너-생성-및-실행">MySQL 도커 컨테이너 생성 및 실행</h3>
<pre><code class="language-bash">docker run 
--name mysql-container 
-e MYSQL_ROOT_PASSWORD=0000 
-d 
-p 3307:3307 
mysql:latest 
--character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci --lower_case_table_names=1</code></pre>
<p>도커는 이미지를 실행하는 것이 아니라 다운받은 이미지에서 컨테이너를 만들어 컨테이너를 실행한다. 실질적으로 내가 프로젝트에서 사용하게될 MySQL은 이미지에서 만든 컨테이너라고 생각하면 된다. </p>
<p>위 명령어가 복잡해 보이니 하나씩 뜯어보면 (터미널에 작성할 때는 한 줄로 작성하는 거 아시죠?)</p>
<ul>
<li><p><code>docker run</code> : 이미지에서 컨테이너 생성</p>
</li>
<li><p><code>--name</code> : 컨테이너 이름 설정</p>
</li>
<li><p><code>-e</code> : environment를 의미하며, 보통 루트 계정의 비밀번호를 설정하기 위해 사용</p>
</li>
<li><p><code>-d</code> : detach를 의미하며, 컨테이너를 백그라운드로 실행시켜 실행을 유지해주는 역할을 하는데 거의 대부분 이 -d를 사용</p>
</li>
<li><p><code>-p</code> : 포트 설정, <code>&lt;Host Port&gt;:&lt;Container Port&gt;</code> 형식으로 작성 
호스트 시스템에서 <code>&lt;Host Port&gt;</code>번 TCP 포트로 유입되는 트래픽은 모두 도커 컨테이너의 <code>&lt;Container Port&gt;</code>번 TCP 포트로 전달된다.</p>
</li>
<li><p><code>mysql:latest</code> : 사용할 이미지의 이름 
<code>:latest</code>라고 작성하지 않아도 자동으로 최신 버전을 가져온다.</p>
</li>
<li><p>이미지 이름 뒤에 오는 내용은 전부 MySQL 설정</p>
<ul>
<li><code>—character-set</code>은 문자 인코딩을 위한 설정으로 한글 깨짐을 방지하기 위해서는 utf8로 설정해줘야 한다. mb4는 4 byte를 지원하는 설정이다. </li>
<li><code>—collation</code> 역시 utf8로 설정한다. <code>_unicode_ci</code>는 유니코드에 정의된 규칙을 따르면서 대소문자를 구분하지 않는다는 의미를 갖고 있다. </li>
<li><code>--lower_case_table_names=1</code>는 입력값을 전부 소문자로 인식하게 하는 설정이다.</li>
</ul>
</li>
</ul>
<blockquote>
<p>💡 MySQL의 기본 포트 번호는 3306이지만 로컬에 이미 DB가 설치되어 있거나 하면 포트 충돌이 일어날 수 있어 나는 보통 도커용 MySQL은 3307이나 3308 처럼 다른 포트 번호를 사용하는 편이다. </p>
</blockquote>
<hr />
<h4 id="참고-character-set은-뭐고-collation은-뭐죠">참고) character-set은 뭐고 collation은 뭐죠?</h4>
<p>character set은 문자를 어떤 코드로 저장할 지 정한 규칙, collation은 저장된 character set을 데이터베이스 작업에 사용할 때 어떤 기준으로 비교 작업을 할 지 정한 규칙이라고 보면 된다. </p>
<p><a href="https://velog.io/@mooh2jj/MySQL-Character-Set-Collation-%ED%99%95%EC%9D%B8">이 블로그</a>를 참고해보면 좋을 것 같다!</p>
<hr />
<p>생성한 컨테이너 목록은 다음 명령어로 확인 가능하다.</p>
<pre><code class="language-bash">docker ps -a</code></pre>
<h3 id="생성된-컨테이너-실행접속삭제">생성된 컨테이너 실행/접속/삭제</h3>
<h4 id="기존에-생성했던-컨테이너-실행중지재실행">기존에 생성했던 컨테이너 실행/중지/재실행</h4>
<pre><code class="language-bash">docker start 컨테이너 이름
docker stop 컨테이너 이름
docker restart 컨테이너 이름</code></pre>
<h4 id="컨테이너-접속">컨테이너 접속</h4>
<pre><code class="language-bash">docker exec -it 컨테이너 이름 bash</code></pre>
<p>지금처럼 MySQL 컨테이너에 접속하는 거라면</p>
<pre><code class="language-bash">docker exec -it mysql 컨테이너 이름 bash</code></pre>
<p>이후에는 터미널에서 MySQL 접속하는 것처럼 해주면 된다.</p>
<pre><code class="language-bash">&gt; mysql -u root -p
&gt; 루트 비밀번호 입력</code></pre>
<h4 id="컨테이너-삭제">컨테이너 삭제</h4>
<pre><code class="language-bash">docker rm 컨테이너 ID</code></pre>
<p>당연히 컨테이너 삭제하면 DB에 저장된 데이터도 싹 날아가는 것이므로 항상 주의! 
특히 Docker Desktop에선 휴지통 아이콘 한 번 누르면 끝이라 주의 또 주의! </p>
<hr />
<h2 id="🐳-추가적으로">🐳 추가적으로</h2>
<h3 id="docker-desktop-이용해도-괜찮을까">Docker Desktop 이용해도 괜찮을까?</h3>
<p>개인적으로 기존에 생성한 컨테이너를 실행하거나 중지하거나 삭제하는 작업은 Docker Desktop을 이용하는 것이 더 편리하게 느껴졌다. GUI 환경이라 터미널에 귀찮게 하나하나 입력할 일도 없고 Actions 버튼 딸깍 한 번으로 간편하게 컨테이너 상태를 관리할 수 있다. </p>
<p>그렇지만 이상하게 Docker Desktop 잔오류도 많고 가끔 실행 안 될 때도 있어서 터미널 방식이랑 Docker Desktop을 번갈아가며 이용하는 것이 더 좋다고 생각한다. </p>
<p>일단 컨테이너 생성하는 건 터미널 방식이 100배 낫다. </p>
<h3 id="mysql-workbench-연결이-안-돼요ㅠㅠ">MySQL Workbench 연결이 안 돼요ㅠㅠ</h3>
<p>이 문제는 보통 컨테이너 생성할 때 MySQL 기본 포트인 3306이 아닌 다른 포트를 할당했을 때 발생하는 문제이다. </p>
<p>DBeaver나 MySQL Workbench 같은 DB툴을 이용하기 위해서는 포트 번호를 통해 DB를 DB툴에 연결해줘야 하는데, 컨테이너 생성할 때 할당한 포트 번호가 정작 MySQL 설정에는 적용이 안 돼서 DB툴이 보기에는 내가 작성한 포트 번호와 실제로 MySQL이 이용하는 포트 번호가 맞지 않다고 인식되기 때문에 문제가 생긴다. </p>
<p>도커로 MySQL에 접속한 다음 </p>
<pre><code class="language-sql">SHOW GLOBAL VARIABLES LIKE ‘PORT’;</code></pre>
<p>명령어로 MySQL 설정에는 어떤 포트 번호가 할당되어 있는지 확인할 수 있다. </p>
<p>만약 내가 설정한 포트 번호가 아닌 3306이라고 나온다면, my.cnf를 수정해야 한다. </p>
<p>Docker Desktop에서 my.cnf 파일을 다음과 같이 수정할 수 있다.</p>
<ul>
<li>컨테이너 이름을 클릭</li>
<li>이때 컨테이너는 실행 중인 상태</li>
<li>Files 탭에 들어가서 쭉 내려보면</li>
<li>my.cnf 파일이 있는데 우클릭 하면 편집할 수 있다.</li>
<li><code>user=mysql</code> 아래에 <code>port=포트번호</code> 이렇게 추가</li>
</ul>
<hr />
<h4 id="참고-기존-컨테이너의-포트를-변경하고-싶어요">참고) 기존 컨테이너의 포트를 변경하고 싶어요</h4>
<p>불가능하다.</p>
<p><code>docker commit</code> 명령어를 통해 기존 컨테이너를 새로운 이미지에 복사하고 이 이미지에서 컨테이너를 새롭게 생성하는 수 밖에 없다.</p>
<hr />
<h3 id="📚-reference">📚 Reference</h3>
<ul>
<li><a href="https://hackmd.io/@bonjugi/BkxMuegyS">run 시점에 옵션으로 설정 추가 (추천)</a></li>
<li><a href="https://hy-ung.tistory.com/82">Docker에 mysql 설치 후 workbench 연결 오류!?</a></li>
</ul>