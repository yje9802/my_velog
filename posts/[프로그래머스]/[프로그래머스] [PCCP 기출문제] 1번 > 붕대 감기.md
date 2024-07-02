<blockquote>
<p>프로그래머스 Lv.1 🌱
<a href="https://school.programmers.co.kr/learn/courses/30/lessons/250137">[PCCP 기출문제] 1번 &gt; 붕대 감기</a>
파이썬으로 풀어보기</p>
</blockquote>
<h3 id="문제-설명">문제 설명</h3>
<p>어떤 게임에는 붕대 감기라는 기술이 있습니다.</p>
<p>붕대 감기는 <code>t</code>초 동안 붕대를 감으면서 1초마다 <code>x</code>만큼의 체력을 회복합니다. <code>t</code>초 연속으로 붕대를 감는 데 성공한다면 <code>y</code>만큼의 체력을 추가로 회복합니다. 게임 캐릭터에는 최대 체력이 존재해 현재 체력이 최대 체력보다 커지는 것은 불가능합니다.</p>
<p>기술을 쓰는 도중 몬스터에게 공격을 당하면 기술이 취소되고, 공격을 당하는 순간에는 체력을 회복할 수 없습니다. 몬스터에게 공격당해 기술이 취소당하거나 기술이 끝나면 그 즉시 붕대 감기를 다시 사용하며, 연속 성공 시간이 0으로 초기화됩니다.</p>
<p>몬스터의 공격을 받으면 정해진 피해량만큼 현재 체력이 줄어듭니다. 이때, 현재 체력이 0 이하가 되면 캐릭터가 죽으며 더 이상 체력을 회복할 수 없습니다.</p>
<p>당신은 붕대감기 기술의 정보, 캐릭터가 가진 최대 체력과 몬스터의 공격 패턴이 주어질 때 캐릭터가 끝까지 생존할 수 있는지 궁금합니다.</p>
<p>붕대 감기 기술의 시전 시간, 1초당 회복량, 추가 회복량을 담은 1차원 정수 배열 <code>bandage</code>와 최대 체력을 의미하는 정수 <code>health</code>, 몬스터의 공격 시간과 피해량을 담은 2차원 정수 배열 <code>attacks</code>가 매개변수로 주어집니다. 모든 공격이 끝난 직후 남은 체력을 return 하도록 solution 함수를 완성해 주세요. 만약 몬스터의 공격을 받고 캐릭터의 체력이 0 이하가 되어 죽는다면 <code>-1</code>을 return 해주세요.</p>
<h3 id="제한-사항">제한 사항</h3>
<p><img alt="" src="https://velog.velcdn.com/images/yje9802/post/8a0eefa7-4a1d-4171-9c55-abe6ce8d3e10/image.png" /></p>
<blockquote>
<p><strong>더 자세한 설명 및 입출력 예시는 문제 사이트에서 확인해주세요!</strong></p>
</blockquote>
<hr />
<h3 id="내가-작성한-정답">내가 작성한 정답</h3>
<pre><code class="language-python">def solution(bandage, health, attacks):
    answer = health

    i = 1 # 현재 시간
    skill = 0 # 기술 연속 성공; 최대 bandage[0]까지

    while len(attacks) &gt; 0:
        if i == attacks[0][0]: # 공격 시점
            answer -= attacks[0][1]
            skill = 0 # 연속 성공 초기화
            attacks.pop(0)
            if answer &lt;= 0: # 체력이 0 이하가 되면 종료
                answer = -1
                break
        else:
            answer += bandage[1]
            if answer &gt;= health: # 최대 체력보다 많이 회복할 수 없다.
                answer = health
            skill += 1
            if skill == bandage[0]: # t초 연속으로 기술 성공 -&gt; 체력 추가 회복
                answer += bandage[2]
                if answer &gt;= health: # 최대 체력보다 많이 회복할 수 없다.
                    answer = health
                skill = 0
        i += 1

    return answer</code></pre>
<p>요구사항을 정확하게 구현해야 하는 문제지만 몇몇 요구사항은 놓치기 쉬워 주의해야 한다. </p>
<p>최대 체력 이상으로 체력을 회복하는 것이 안 되기 때문에 체력 회복 시점에서 항상 이 부분을 체크해야 한다. 체력 회복 시점은 두 가지가 존재한다.</p>
<ul>
<li>공격 받지 않았을 때 초당 회복량 만큼 회복한다.</li>
<li>t초 연속으로 기술을 성공했을 때 추가 회복한다. </li>
</ul>
<p>이 두 시점에 주의해서 구현하면 된다. </p>