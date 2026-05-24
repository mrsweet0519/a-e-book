import glob
import os

files = glob.glob(r"c:\안티그래비티\전자책\*.md")
# don't forget to include index.html in case we missed anything
files.append(r"c:\안티그래비티\전자책\ebook\index.html")

replacements = {
    "숏츠 영상 하단에 내 1시간짜리 플레이리스트 영상 링크를 연결(관련 동영상 기능)해야 합니다.": "숏츠에서 롱폼 영상으로 유입시키려면, 고정 댓글의 링크가 아니라 유튜브 스튜디오의 ‘관련 동영상’ 기능을 중심으로 설계해야 합니다. Shorts 댓글과 설명란의 URL은 클릭 링크로 작동하지 않을 수 있으므로, 실제 클릭 유도는 ‘관련 동영상’ 기능에 연결된 롱폼 영상을 통해 진행하는 것이 좋습니다.",
    "- **제목 예시:** 아침 출근길 기분 좋아지는 팝송 (풀버전은 하단 링크 클릭!)": "- **제목/화면 문구 예시:** 아침 출근길 기분 좋아지는 음악 — 관련 영상에서 1시간 풀버전 이어듣기",
    "- **고정 댓글 예시:** \"📌 1시간 연속 듣기 풀버전이 필요하시다면 아래 링크를 클릭해 주세요! [롱폼 영상 링크]\"": "- **고정 댓글 예시:** \"관련 영상에서 1시간 풀버전을 이어서 들어보세요.\"",
    "- **고정 댓글 예시:** \"1시간 연속 듣기 풀버전이 필요하시다면 아래 링크를 클릭해 주세요! [롱폼 영상 링크]\"": "- **고정 댓글 예시:** \"관련 영상에서 1시간 풀버전을 이어서 들어보세요.\"",
    "- **영상 내 텍스트:** 화면 하단을 가리키는 화살표(⬇️)와 함께 \"1시간 풀버전 듣기\" 텍스트 삽입": "- **영상 내 텍스트:** 관련 영상에서 1시간 풀버전 듣기",
    "- **영상 내 텍스트:** 화면 하단을 가리키는 화살표((아래))와 함께 \"1시간 풀버전 듣기\" 텍스트 삽입": "- **영상 내 텍스트:** 관련 영상에서 1시간 풀버전 듣기",
    "고정 댓글에 롱폼 링크 추가.": "관련 영상에서 1시간 풀버전을 이어서 들어보세요\"처럼 안내 문구를 남깁니다.",
    "- **고정 댓글/텍스트:** 화면 화살표((아래))와 함께 \"1시간 풀버전은 아래 링크 클릭\" 안내 추가.": "- **고정 댓글/텍스트:** 화면 하단에 \"관련 영상에서 1시간 풀버전 듣기\" 텍스트 및 관련 동영상 기능 안내 추가."
}

for filepath in files:
    if not os.path.isfile(filepath): continue
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        modified = False
        for k, v in replacements.items():
            if k in content:
                content = content.replace(k, v)
                modified = True
        
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Modified {os.path.basename(filepath)}")
    except Exception as e:
        print(f"Error on {filepath}: {e}")
