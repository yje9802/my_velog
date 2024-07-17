<p><a href="https://velog.io/@yje9802/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-2021-KAKAO-BLIND-RECRUITMENT-%ED%95%A9%EC%8A%B9-%ED%83%9D%EC%8B%9C-%EC%9A%94%EA%B8%88" target="blank">원본 링크</a></p><br><p><img alt="" src="https://velog.velcdn.com/images/yje9802/post/535b831c-311f-42fe-9d6f-32dcb3f832a8/image.jpg" /></p>
<blockquote>
<p>프로그래머스 Lv.3 🌲
<a href="https://school.programmers.co.kr/learn/courses/30/lessons/72413">2021 KAKAO BLIND RECRUITMENT &gt; 합승 택시 요금</a>
파이썬으로 풀어보기</p>
</blockquote>
<h3 id="문제-설명">문제 설명</h3>
<p><img alt="" src="https://velog.velcdn.com/images/yje9802/post/23261e6a-e2a9-433c-b7b0-6f9bef3df1b0/image.png" /></p>
<p>위 예시 그림은 택시가 이동 가능한 반경에 있는 6개 지점 사이의 이동 가능한 택시노선과 예상요금을 보여주고 있습니다.
그림에서 A와 B 두 사람은 출발지점인 4번 지점에서 출발해서 택시를 타고 귀가하려고 합니다. A의 집은 6번 지점에 있으며 B의 집은 2번 지점에 있고 두 사람이 모두 귀가하는 데 소요되는 예상 최저 택시요금이 얼마인 지 계산하려고 합니다.</p>
<ul>
<li>그림의 원은 지점을 나타내며 원 안의 숫자는 지점 번호를 나타냅니다.<ul>
<li>지점이 n개일 때, 지점 번호는 1부터 n까지 사용됩니다.</li>
</ul>
</li>
<li>지점 간에 택시가 이동할 수 있는 경로를 간선이라 하며, 간선에 표시된 숫자는 두 지점 사이의 예상 택시요금을 나타냅니다.<ul>
<li>간선은 편의 상 직선으로 표시되어 있습니다.</li>
<li>위 그림 예시에서, 4번 지점에서 1번 지점으로(4→1) 가거나, 1번 지점에서 4번 지점으로(1→4) 갈 때 예상 택시요금은 <code>10</code>원으로 동일하며 이동 방향에 따라 달라지지 않습니다.</li>
</ul>
</li>
</ul>
<p>지점의 개수 n, 출발지점을 나타내는 s, <code>A</code>의 도착지점을 나타내는 a, <code>B</code>의 도착지점을 나타내는 b, 지점 사이의 예상 택시요금을 나타내는 fares가 매개변수로 주어집니다. 이때, <code>A</code>, <code>B</code> 두 사람이 s에서 출발해서 각각의 도착 지점까지 택시를 타고 간다고 가정할 때, 최저 예상 택시요금을 계산해서 return 하도록 solution 함수를 완성해 주세요.</p>
<p>📌 <strong>만약, 아예 합승을 하지 않고 각자 이동하는 경우의 예상 택시요금이 더 낮다면, 합승을 하지 않아도 됩니다.</strong></p>
<p>위 그림 예시에 해당하는 입력값은 다음과 같습니다.</p>
<table>
<thead>
<tr>
<th>n</th>
<th>s</th>
<th>a</th>
<th>b</th>
<th>fares</th>
<th>result</th>
</tr>
</thead>
<tbody><tr>
<td>6</td>
<td>4</td>
<td>6</td>
<td>2</td>
<td>[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]</td>
<td>82</td>
</tr>
</tbody></table>
<br />

<h3 id="제한-사항">제한 사항</h3>
<ul>
<li>지점갯수 n은 3 이상 200 이하인 자연수입니다.</li>
<li>지점 s, a, b는 1 이상 n 이하인 자연수이며, 각기 서로 다른 값입니다.<ul>
<li>📌 <strong>즉, 출발지점, <code>A</code>의 도착지점, <code>B</code>의 도착지점은 서로 겹치지 않습니다.</strong></li>
</ul>
</li>
<li>fares는 2차원 정수 배열입니다.</li>
<li>fares 배열의 크기는 2 이상 <code>n x (n-1) / 2</code> 이하입니다.<ul>
<li>예를들어, n = 6이라면 fares 배열의 크기는 2 이상 15 이하입니다. (<code>6 x 5 / 2 = 15</code>)</li>
<li>fares 배열의 각 행은 [c, d, f] 형태입니다.</li>
<li>c지점과 d지점 사이의 예상 택시요금이 <code>f</code>원이라는 뜻입니다.</li>
<li>지점 c, d는 1 이상 n 이하인 자연수이며, 각기 서로 다른 값입니다.</li>
<li>요금 f는 1 이상 100,000 이하인 자연수입니다.</li>
<li>fares 배열에 두 지점 간 예상 택시요금은 1개만 주어집니다. 즉, [c, d, f]가 있다면 [d, c, f]는 주어지지 않습니다.</li>
</ul>
</li>
<li>📌 <strong>출발지점 s에서 도착지점 a와 b로 가는 경로가 존재하는 경우만 입력으로 주어집니다.</strong></li>
</ul>
<blockquote>
<p><strong>문제가 너무 길어서 중요한 부분만 가져왔습니다. 나머지는 문제 사이트에서 직접 확인해주세요!</strong></p>
</blockquote>
<hr />
<h3 id="내가-작성한-정답">내가 작성한 정답</h3>
<pre><code class="language-python">from heapq import heappop, heappush

INF = int(1e9) # 무한대 설정
connected = [[]] # connected[i] : [[i번 노드와 연결된 노드, 비용], []]

def dijkstra(n, src, dest):
    global connected

    costs = [INF for _ in range(n+1)] # src와의 비용을 저장하는 배열
    costs[src] = 0 # src와 src 사이의 비용은 0
    pq = [[0, src]] # pq[i] : [src와의 비용, 노드]

    while pq:
        w, x = heappop(pq) # w는 x -&gt; src 최소 비용, x는 해당 노드

        # costs 저장된 값이 pq에서 pop한 값(최솟값) 보다 이미 더 작다면 넘어감
        if costs[x] &lt; w:
            continue

        for item in connected[x]: # x와 연결된 노드들 확인
            nx, ncost = item[0], item[1]
            ncost += w

            # src에서 nx로 바로 갈 때보다 x를 거쳐서 nx로 가는게 비용이 더 적게 들면 업데이트
            # 문제에서 경로를 요구하지는 않아서 이렇게 해도 됨
            if ncost &lt; costs[nx]:
                costs[nx] = ncost
                heappush(pq, [ncost, nx]) # src -&gt; nx 최소 비용 갱신될 때만 push

    return costs[dest]

def solution(n, s, a, b, fares):
    global connected
    connected = [[] for _ in range(n+1)]
    # connected 설정
    for fare in fares:
        src, dest, each_cost = fare
        connected[src].append([dest, each_cost])
        connected[dest].append([src, each_cost])

    answer = dijkstra(n, s, a) + dijkstra(n, s, b) # A와 B가 출발지점부터 따로 갔을 경우의 비용

    for i in range(1, n+1):
        if s != i: # 출발점 아님
            curr_cost = dijkstra(n, s, i) + dijkstra(n, i, a) + dijkstra(n, i, b) # A와 B가 i번 노드부터 따로 갔을 때 비용
            answer = min(answer, curr_cost)

    return answer</code></pre>
<p>사실상 가중치가 있는 그래프에서 최단 거리를 구하는 문제라고 보면 되기 때문에 다익스트라 알고리즘을 활용하는 문제라고 할 수 있다.</p>
<h4 id="✏️-그럼-다익스트라를-어떻게-적용해야할까">✏️ 그럼 다익스트라를 어떻게 적용해야할까?</h4>
<p>제한 사항을 보면 A와 B의 도착지점이 겹치지 않는다고 명시했기 때문에 이 둘이 갈라지는 지점이 반드시 존재한다. </p>
<p>그렇기 때문에 경로가 겹치는 지점까지 다익스트라로 비용을 구하고 갈라진 이후부터는 각자 경로를 따라 다익스트라로 비용을 구해 마지막에 다 더해주면 될 것이다.</p>
<p>참고로 문제 조건에서 처음부터 아예 합승을 하지 않아도 괜찮다 라고 명시했기 때문에 </p>
<ul>
<li>시작 지점 <code>S</code>부터 따로 가는 경우 
  <code>dijkstra(n, s, a) + dijkstra(n, s, b)</code></li>
<li><code>S</code>가 아닌 특정 지점 <code>i</code>부터 따로 가는 경우
  <code>dijkstra(n, s, i) + dijkstra(n, i, a) + dijkstra(n, i, b)</code></li>
</ul>
<p>이런 식으로 경우가 나눠진다.</p>
<p>따지고 보면 n개의 지점 별로 다 한 번씩 검사하는 거랑 똑같다. 근데 시작 지점부터 따로 가면 다익스트라 함수를 두 번만 호출하면 되니까 저렇게 경우를 나눈 것.</p>
<br />

<h4 id="✏️-connected-변수-설명">✏️ <code>connected</code> 변수 설명</h4>
<p>헷갈릴까봐 미리 말하지만 <code>connected</code>의 크기는 n+1이다. 각 지점 번호는 1부터 시작하지만 리스트 인덱스는 0부터 시작하기 때문. 그래서 1번 지점에 대해 알고 싶으면 <code>connected[1]</code>을 해야한다.</p>
<p>그럼 <code>connected</code>는 무엇을 담는 리스트인가 하면, <code>i</code>번 지점과 연결된 지점 번호와 비용을 배열로 저장하는 역할을 한다. 결과적으로 3차원 리스트이다.</p>
<p>위의 그림 예시를 connected로 구성한 결과이다.</p>
<pre><code class="language-python">connected = [
    [],
    [[3, 41], [4, 10], [5, 24], [6, 25]], # 1번 지점 연결 정보
    [[3, 22], [4, 66]], # 2번 지점 연결 정보
    [[1, 41], [2, 22], [5, 24]], # 3번 지점 연결 정보
    [[1, 10], [2, 66], [6, 50]], # 4번 지점 연결 정보
    [[1, 24], [3, 24], [6, 2]], # 5번 지점 연결 정보
    [[1, 25], [4, 50], [5, 2]] # 6번 지점 연결 정보
]</code></pre>
<br />

<h4 id="✏️-dijkstra-함수-설명">✏️ <code>dijkstra</code> 함수 설명</h4>
<ul>
<li><p><code>dijkstra</code> 함수의 매개변수는 <code>n</code>(전체 지점 개수), <code>src</code>(출발 지점), <code>dest</code>(목표 도착 지점)로 구성된다.</p>
</li>
<li><p>함수 내에서 <code>costs</code>라는 새로운 리스트가 등장하는데 이 리스트는 <code>src</code>에서 특정 지점 <code>i</code>로 가는 최소 비용을 저장한다. 그래서 처음에는 최소 비용을 모르기 때문에 전체를 INF로 초기화 하고, <code>costs[src]</code>는 0으로 초기화 한다. </p>
</li>
<li><p>그 다음 <code>pq</code>는 <code>[src와의 거리 비용, 지점 번호]</code>를 원소로 갖는 2차원 배열이자 최소힙이다. <code>pq</code>에 저장되는 경우는 <code>costs</code>가 업데이트 되어서 추가로 확인이 필요한 지점이며, 맨처음에 <code>costs[src] = 0</code>으로 초기화 되기 때문에 <code>pq</code> 역시 <code>[[0, src]]</code>로 시작한다.</p>
</li>
<li><p>while문에서는 <code>pq</code>를 heappop 하여 최종적으로 <code>pq</code>에 더이상 원소가 없을 때, 즉 더이상 그 어떤 지점에도 최소 비용 업데이트가 이루어지지 않을 때까지 체크하게 된다. </p>
</li>
<li><p>while문 내부에서는 우선 현재 <code>pq</code>에서 <code>src</code>와의 거리 비용이 가장 작은 지점이 pop 될 것이다. 여기서 <code>w</code>를 거리 비용, <code>x</code>를 지점 번호로 뒀을 때, <code>costs[x]</code>를 확인해본다. </p>
<p>만약 이미 <code>costs[x]</code>가 <code>w</code>보다 작으면 <code>costs</code>를 업데이트할 필요가 없으므로 넘어간다.</p>
<p>그게 아니라면 <code>connected[x]</code>를 통해 지점<code>x</code>와 연결된 다른 노드들을 확인한다. 지점<code>x</code>와 연결된 다른 노드를 <code>nx</code>라고 한다면 <code>src -&gt; x -&gt; nx (ncost + w)</code>의 경로 비용과 <code>src -&gt; nx (costs[nx])</code> 경로 비용을 비교해 <code>x</code>를 거쳐 가는게 더 비용이 적게 든다면 <code>costs[nx]</code>를 갱신한다. </p>
<p>이 경우 <code>costs</code>가 업데이트 되었으므로 <code>pq</code>에 <code>[ncost, nx]</code>를 heappush 한다.</p>
</li>
</ul>
<br />

<h4 id="✏️-그렇다면-solution-함수에서는">✏️ 그렇다면 <code>solution</code> 함수에서는?</h4>
<p>우선 <code>connected</code> 리스트를 설정해준다음,</p>
<p><code>answer</code>는 출발 지점 S부터 A와 B가 갈라지는 경우의 비용으로 초기화 해준다. </p>
<p>그 다음 for문을 돌며 각 지점에서 갈라졌을 때는 비용이 어떤지 <code>answer</code>와 비교해 최솟값으로 <code>answer</code>를 갱신한다. </p>
<br />

<hr />
<p>개인적으로 다익스트라는 너무 머리 속으로 그려지지 않아서 함수 진행 과정을 몇 번이고 손으로 직접 써가며 정리했다.😭 </p>
<p>그렇지만 문제 자체는 딱 레벨 3에 적합한 문제였다고 생각한다. 대신 문제가 너무 길어서 여기에 집중을 좀 해야할 것 같은?</p>
<p>그리고 문제 조건을 잘 살펴봐야했던 문제였다. 실제로 문제 푸는데 중요한 역할을 한 조건은 위에서 📌로 표시해뒀으므로 주목해서 보기를! </p>
<hr />
<h3 id="📚-reference">📚 Reference</h3>
<p><a href="https://velog.io/@new_wisdom/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%95%A9%EC%8A%B9-%ED%83%9D%EC%8B%9C-%EC%9A%94%EA%B8%88-%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC">[프로그래머스] 합승 택시 요금 - 다익스트라</a></p>