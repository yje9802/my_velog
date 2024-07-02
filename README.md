# my_velog 레포지토리

<p align="center">
  <img src="./assets/velog_capture.png" align="center" width="30%"> 
  <img src="./assets/github_capture.png" align="center" width="30%"> 
</p>

<h3 align=center>🌱 Velog 글 깃허브로 모아보기 🌱</h3>

## 👋 Introduction
<h4> 🥲 Velog의 단점 - 지금까지 작성한 게시글 목록을 쭉 모아보기가 어렵다. </h4>

<h4> 😎 그럼 Velog로 작성한 게시글을 깃허브에 자동으로 정리될 수 있게 하자! 깃허브 잔디는 덤~ </h4>

<br>

### 🧐 기획 의도
옵시디언에 깃허브를 연동해 일정 시간 마다 레포지토리에 commit 하는 기능을 애용하고 있었다. 그러다 보니 블로그 포스트를 작성해도 옵시디언 처럼 commit 될 수 있다면 좋지 않을까? 생각이 들었다. 

그래서 그 유명한 백준허브처럼 Velog에서 출간하기 버튼을 누르면 깃허브에 바로 반영될 수 있으면 좋겠다 생각했지만...현실적으로 쉽지 않아 보였다.😭 

이거 말고도 해야할 게 많았기 때문에 결국 Github Actions로 정해진 기간마다 Velog 포스트를 깃허브에 저장하는 스크립트를 실행시키는 것으로 타협했다.

### 📌 사용 기술
- ![python](https://img.shields.io/badge/Python-3.8-3776AB.svg?style=flat&logo=python&logoColor=white)
  - 스크립트 작성
  - RSS를 사용해 Velog 포스트를 scraping & parsing 하는 작업이 필요했기 때문에 parsing 작업에 적합한 Python으로 스크립트를 작성하기로 결정했다.
  - `feedparser` 라이브러리 
  
- ![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=flat&logo=githubactions&logoColor=white)
  - 스크립트 실행

### 🔧 에러 로그
- _The following actions uses node12 which is deprecated and will be forced to run on node16: actions/checkout@v2._
  - `checkout@v2`가 node12를 사용하는데 node12는 더이상 지원하지 않는 상황
  - 해결 방법
    - `checkout@v3`로 바꿔주면 된다.
- 블로그의 모든 게시글을 가져오지 못 하는 문제
  - Velog RSS로 한 번에 가져올 수 있는 게시글의 수가 총 20개로 제한되어 있는 것 같다.

<br> 

---
### 🔗 참고 자료
- [velog와 github 연동 : 벨로그 글쓰고 잔디심기 🌱](https://velog.io/@sooozi/velog%EC%99%80-github-%EC%97%B0%EB%8F%99-%EB%B2%A8%EB%A1%9C%EA%B7%B8-%EA%B8%80%EC%93%B0%EA%B3%A0-%EC%9E%94%EB%94%94%EC%8B%AC%EA%B8%B0)
- [feedparser Documentation](https://feedparser.readthedocs.io/en/latest/common-rss-elements.html)