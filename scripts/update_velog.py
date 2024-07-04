import feedparser
import git
import os

# Velog RSS 피드 URL
rss_url = 'https://api.velog.io/rss/@yje9802'

# 작업을 반영할 깃허브 레포지토리 경로
repo_path = '.'

# 'posts' 폴더 경로
posts_dir = os.path.join(repo_path, 'posts')

# 'posts' 폴더가 없다면 생성
if not os.path.exists(posts_dir):
    os.makedirs(posts_dir)

# 레포지토리 로드
repo = git.Repo(repo_path)

# RSS 피드 파싱
feed = feedparser.parse(rss_url)

is_added = False # 추가된 게시글 존재 여부

# 각 글을 파일로 저장하고 커밋
for entry in feed.entries:
    # 파일 이름에서 유효하지 않은 문자 제거 또는 대체
    file_name = entry.title
    file_name = file_name.replace('/', '-')  # 슬래시를 대시로 대체
    file_name = file_name.replace('\\', '-')  # 백슬래시를 대시로 대체
    file_name = file_name.replace(' ', '_') # 띄어쓰기는 언더바로 대체
    
    # 카테고리별 하위 폴더 생성 
    if file_name[0] == '[':
        for i in range(len(file_name)):
            if file_name[i] == ']':
                folder_name = file_name[:i+1]
                break
    else:
        folder_name = '[ETC.]'
    
    specified_posts_dir = os.path.join(posts_dir, folder_name) # 하위 폴더까지 추가된 경로
    if not os.path.exists(specified_posts_dir):
        os.makedirs(specified_posts_dir)
    
    file_name += '.md'
    file_path = os.path.join(specified_posts_dir, file_name)

    # 파일이 존재하지 않으면 생성
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            is_added = True
            contents = f'<p><a href="{entry.link}" target="blank">원본 링크</a></p><br>'
            contents += entry.description
            file.write(contents)  # 글 내용을 파일에 작성
            

        # 깃허브 커밋
        repo.git.add(file_path)
        repo.git.commit('-m', f'포스트 업데이트: {entry.title}')

# posts 폴더 아래 하위 폴더들의 파일 목록을 딕셔너리에 저장하여 반환하는 함수
def check_posts(path):
    folder_file_list = {} # 폴더 이름: [파일1, 파일2, ...]
    
    for item in os.listdir(path): # path 경로의 하위 폴더 및 파일 순회
        item_path = os.path.join(path, item)
        if item != "README.md" and os.path.isdir(item_path) is True:
            # 폴더 내부 파일들 리스트에 저장
            # 폴더 안에 또다른 하위 폴더가 없는 구조이기에 가능 
            sub_files = []
            for sub_item in os.listdir(item_path): 
                sub_item_path = "./" + item + "\/" + sub_item
                
                sub_item = sub_item.replace('_', ' ') # 기존에 언더바로 대체되었던 띄어쓰기 복구
                break_point = 0 # ] 부분 위치
                for i in range(len(sub_item)):
                    if sub_item[i] == "]":
                        break_point = i+2
                        break
                title = sub_item[break_point:-3] # 파일 이름에서 앞에 []부분과 뒤에 .md 제거
                
                sub_files.append([title, sub_item_path])
            
            if len(sub_files) == 0: # 빈 폴더면 삭제
                os.rmdir(item_path)
            else: # 그게 아니면 딕셔너리에 저장
                folder_file_list[item] = sub_files
    return folder_file_list

readme_path = os.path.join(posts_dir, "README.md") # /posts/README.md
if is_added: # 추가된 게시글이 존재한다면 README 업데이트
    folders_files = check_posts(posts_dir)
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("# 📌 Velog 게시글 목록 한 눈에 보기\n")
        for folder in folders_files.keys():
            f.write(f"### 📁 {folder}\n")
            for file_info in folders_files[folder]:      
                f.write(f"- [{file_info[0]}]({file_info[1]})  \n")
    # 깃허브 커밋
    repo.git.add(readme_path)
    repo.git.commit('-m', f'포스트 업데이트: README.md')

# 변경 사항을 깃허브에 푸시
repo.git.push()