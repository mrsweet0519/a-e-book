# -*- coding: utf-8 -*-
import os

filepath = r'c:\안티그래비티\전자책\ebook\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    '<h2>1. 초보자가 선택하기 좋은 음악 채널 주제 (장르별 차이)</h2>': '<h2>1. 초보자가 선택하기 좋은<br>음악 채널 주제 (장르별 차이)</h2>',
    '<h2>1. 제작 전 필수 확인: 저작권과 라이선스 기준</h2>': '<h2>1. 제작 전 필수 확인:<br>저작권과 라이선스 기준</h2>',
    '<h2>2. 초보자를 위한 AI 음원 도구 선택 (Soundraw 중심)</h2>': '<h2>2. 초보자를 위한 AI 음원 도구 선택<br>(Soundraw 중심)</h2>',
    '<h2>4. 플레이리스트 구성 및 &quot;반복 콘텐츠&quot; 피하는 법</h2>': '<h2>4. 플레이리스트 구성 및<br>&quot;반복 콘텐츠&quot; 피하는 법</h2>',
    '<h2>1. 무료 영상 소스 찾기 (Pexels, Pixabay 등)</h2>': '<h2>1. 무료 영상 소스 찾기<br>(Pexels, Pixabay 등)</h2>',
    '<h2>2. 초보자용 영상 편집 툴 선택 (Filmora, CapCut 등)</h2>': '<h2>2. 초보자용 영상 편집 툴 선택<br>(Filmora, CapCut 등)</h2>',
    '<h2>3. &#39;반복 콘텐츠&#39;를 피하는 편집 기술 (가장 중요!)</h2>': '<h2>3. &#39;반복 콘텐츠&#39;를 피하는 편집 기술<br>(가장 중요!)</h2>',
    '<h2>1. 검색 노출과 클릭을 유도하는 제목 짓기</h2>': '<h2>1. 검색 노출과 클릭을 유도하는<br>제목 짓기</h2>',
    '<h2>3. 태그(Tag)와 해시태그(#)의 차이 완벽 이해</h2>': '<h2>3. 태그(Tag)와 해시태그(#)의 차이<br>완벽 이해</h2>',
    '<h2>1. 음악 채널에서 만들 수 있는 숏츠 주제 예시</h2>': '<h2>1. 음악 채널에서 만들 수 있는<br>숏츠 주제 예시</h2>',
    '<h2>3. 외부 플랫폼(짤스튜디오, 쇼츠뮤직 등) 활용 시 주의사항</h2>': '<h2>3. 외부 플랫폼(짤스튜디오, 쇼츠뮤직 등)<br>활용 시 주의사항</h2>',
    '<h2>4. 숏츠에서 롱폼 영상으로 유입시키는 비법</h2>': '<h2>4. 숏츠에서 롱폼 영상으로<br>유입시키는 비법</h2>'
}

count = 0
for old, new in replacements.items():
    if old in content:
        content = content.replace(old, new)
        count += 1
    else:
        print(f'Not found: {old}')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Successfully replaced {count} titles.')
