import feedparser
import git
import os

# Velog RSS 피드 URL
rss_url = 'https://api.velog.io/rss/@yje9802'

# 작업을 반영할 깃허브 레포지토리 경로
repo_path = '.'

# 'velog-posts' 폴더 경로
posts_dir = os.path.join(repo_path, 'posts')

# 'posts' 폴더가 없다면 생성
if not os.path.exists(posts_dir):
    os.makedirs(posts_dir)

# 레포지토리 로드
repo = git.Repo(repo_path)

# RSS 피드 파싱
feed = feedparser.parse(rss_url)

# 각 글을 파일로 저장하고 커밋
for entry in feed.entries:
    # 파일 이름에서 유효하지 않은 문자 제거 또는 대체
    file_name = entry.title
    file_name = file_name.replace('/', '-')  # 슬래시를 대시로 대체
    file_name = file_name.replace('\\', '-')  # 백슬래시를 대시로 대체
    
    # 카테고리별 하위 폴더 생성 
    if file_name[0] == '[':
        for i in range(len(file_name)):
            if file_name[i] == ']':
                folder_name = file_name[:i+1]
                break
    else:
        folder_name = '[ETC.]'
    
    specified_posts_dir = posts_dir + '/' + folder_name # 하위 폴더까지 추가된 경로
    if not os.path.exists(specified_posts_dir):
        os.makedirs(specified_posts_dir)
    
    file_name += '.md'
    file_path = os.path.join(specified_posts_dir, file_name)

    # 파일이 존재하지 않으면 생성
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            contents = f'<p><a href="{entry.link}" color="black">원본 링크</a></p><br>'
            contents += entry.description
            file.write(entry.description)  # 글 내용을 파일에 작성
            

        # 깃허브 커밋
        repo.git.add(file_path)
        repo.git.commit('-m', f'포스트 업데이트: {entry.title}')

# 변경 사항을 깃허브에 푸시
repo.git.push()