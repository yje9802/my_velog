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


def check_posts(path):
    folder_file_list = {}
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if item != "README.md" and os.path.isdir(item_path) is True:
            # 폴더면
            sub_files = []
            for sub_item in os.listdir(item_path):
                sub_files.append(sub_item)
            
            if len(sub_files) == 0:
                # 빈 폴더면 삭제
                os.rmdir(item_path)
            else:
                folder_file_list[item] = sub_files
    folders_sorted = folder_file_list.items()
    folders_sorted.sort(key=lambda x: x[0])
    return folders_sorted

readme_path = os.path.join(posts_dir, "README.md")
# if is_added:
# 추가된 게시글이 존재한다면 README 업데이트
with open(readme_path, "w", encoding='utf-8') as f:
    f.write("# Velog 게시글 목록 한 눈에 보기\n")
    for key, value in check_posts(posts_dir):
        f.write(f"{key} - {value} \n")

# 변경 사항을 깃허브에 푸시
repo.git.push()