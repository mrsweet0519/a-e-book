# 시각자료 에셋 폴더 (visuals)

전자책 본문에 삽입될 15개의 시각자료 원본을 저장하는 폴더입니다.
최종 PDF 생성 전에 아래 파일명 기준에 맞추어 이미지를 준비해주세요.

## 시각자료 목록

| 번호 | 파일명 | 들어갈 장 | 제작 방식 | 직접 캡처 필요 | 캔바 제작 가능 | 모자이크 필요 | 우선순위 |
|:---|:---|:---|:---|:---|:---|:---|:---|
| 01 | `01_prologue_playlist_example.png` | 프롤로그 | AI / 캔바 | X | O | X | Mid |
| 02 | `02_monetization_pipeline.png` | 1장 | 캔바 / 다이어그램 | X | O | X | **High (7)** |
| 03 | `03_playlist_concept_comparison.png` | 1장 | AI / 캔바 | X | O | X | Mid |
| 04 | `04_reused_content_risk_card.png` | 2장 | 캔바 안내 카드 | X | O | X | Mid |
| 05 | `05_copyright_check_flow.png` | 2장 | 캔바 / 다이어그램 | X | O | X | **High (4)** |
| 06 | `06_channel_concept_funnel.png` | 3장 | 캔바 / 다이어그램 | X | O | X | **High (6)** |
| 07 | `07_ai_music_creation_flow.png` | 4장 | 캡처 / 다이어그램 | O | O | O (계정) | **High (2)** |
| 08 | `08_commercial_license_check.png` | 4장 | 캡처 / 안내 카드 | O | O | X | **High (9)** |
| 09 | `09_pexels_video_search.png` | 5장 | 직접 캡처 | O | X | X | Low |
| 10 | `10_video_timeline_structure.png` | 5장 | 캔바 / 다이어그램 | X | O | X | **High (1)** |
| 11 | `11_youtube_upload_seo_screen.png` | 6장 | 직접 캡처 | O | X | O (계정) | **High (8)** |
| 12 | `12_youtube_check_no_issue.png` | 6장 | 직접 캡처 | O | X | X | **High (5)** |
| 13 | `screenshot-shorts-related-video.png` | 7장 | 직접 캡처 | O | X | O (계정) | **High (3)** |
| 14 | `14_30day_upload_calendar.png` | 8장 | 캔바 (달력) | X | O | X | **High (10)**|
| 15 | `15_template_mockup.png` | 9장 | 캔바 (목업) | X | O | X | Mid |

## 주의사항
- 실제 캡처 시 이메일, 채널명, 개인정보는 반드시 모자이크 처리해주세요.
- 파일명과 확장자(`.png` 또는 `.jpg`)를 정확히 지켜주세요.

## 2026-05-11 삽입 작업 상태

현재 `index.html`에는 아래 실제 캡처 파일명이 연결되어 있습니다. 숏츠 관련 동영상 연결 화면은 `screenshot-shorts-related-video.png`로 삽입되었습니다.

| 최종 파일명 | HTML 삽입 위치 |
|:---|:---|
| `01_prologue_playlist_example.png` | 유튜브 플레이리스트 채널 성공 예시 |
| `02_monetization_pipeline.png` | 수익화 파이프라인 개념도 |
| `03_playlist_concept_comparison.png` | 타깃 세분화 전후 비교 |
| `04_reused_content_risk_card.png` | 재사용된 콘텐츠 / 반복적인 콘텐츠 거절 화면 |
| `05_copyright_check_flow.png` | 상업적 이용 가능(Commercial Use) 약관 확인법 |
| `06_channel_concept_funnel.png` | 채널 콘셉트 기획표 |
| `07_ai_music_creation_flow.png` | AI 음원 제작 흐름 |
| `08_commercial_license_check.png` | Soundraw 메인 화면 및 요금제 |
| `09_pexels_video_search.png` | Pexels 검색 팁 화면 |
| `10_video_timeline_structure.png` | 1시간 플레이리스트 조립 타임라인 구조 |
| `11_youtube_upload_seo_screen.png` | 업로드 제목/설명란 작성 화면 |
| `12_youtube_check_no_issue.png` | 저작권 발견된 문제 없음 화면 |
| `screenshot-shorts-related-video.png` | 숏츠 관련 동영상 링크 연결 화면 |
| `14_30day_upload_calendar.png` | 4주차 30일 플랜 표, 템플릿 미리보기: 30일 실행 플랜 |
| `15_template_mockup.png` | 템플릿 미리보기: 채널 콘셉트 기획표 |

README 목록 외 추가 placeholder 이미지는 `extra_*.png` 파일명으로 정리했고, 기존 `임시*` 원본은 `backup/` 폴더에 보관했습니다.
