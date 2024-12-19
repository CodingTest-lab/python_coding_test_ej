# [level 2] JadenCase 문자열 만들기 - 12951 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12951) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.02 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 12월 19일 19:02:04

### 문제 설명

<p>JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)<br>
문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.</p>

<h5>제한 조건</h5>

<ul>
<li>s는 길이 1 이상 200 이하인 문자열입니다.</li>
<li>s는 알파벳과 숫자, 공백문자(" ")로 이루어져 있습니다.

<ul>
<li>숫자는 단어의 첫 문자로만 나옵니다.</li>
<li>숫자로만 이루어진 단어는 없습니다.</li>
<li>공백문자가 연속해서 나올 수 있습니다.</li>
</ul></li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>s</th>
<th style="text-align: center">return</th>
</tr>
</thead>
        <tbody><tr>
<td>"3people unFollowed me"</td>
<td style="text-align: center">"3people Unfollowed Me"</td>
</tr>
<tr>
<td>"for the last week"</td>
<td style="text-align: center">"For The Last Week"</td>
</tr>
</tbody>
      </table>
<hr>

<p>※ 공지 - 2022년 1월 14일 제한 조건과 테스트 케이스가 추가되었습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 참고
1. 리스트 컴프리헨션 주의점
  ```
    [word[0].upper()+word[1:].lower() if word else "" for word in words]
  ```
- 이것은 조건부 표현식(conditional expression)을 리스트 컴프리헨션 내부에서 사용
- 모든 word에 대해 실행되며, word가 있으면 대문자 변환을, 없으면 빈 문자열 반환
- 결과 리스트의 길이는 words와 동일
  
```
  [word[0].upper()+word[1:].lower() for word in words if word else ""]

  # 이것은 가능합니다:
  [word[0].upper()+word[1:].lower() for word in words if word]
  # 빈 문자열을 제외하고 대문자 변환만 수행
```
- 이것은 문법적으로 잘못된 코드
- 리스트 컴프리헨션에서 if 절은 필터링 용도로만 사용되며 else를 가질 수 없음
- 이 코드는 SyntaxError를 발생시킴

2. 빈 문자열과 공백 문자열
   ```
   empty = ''      # 길이가 0인 빈 문자열
   space = ' '     # 길이가 1인 공백 문자가 있는 문자열

   print(len(empty))    # 0
   print(len(space))    # 1

   print(bool(empty))   # False
   print(bool(space))   # True

   print(empty == space)  # False

   //////////////////////////////////////////
   answer = ['Hello', 'World']

   # 구분자 없이 붙이기
   print(''.join(answer))    # HelloWorld

   # 공백으로 구분하여 붙이기
   print(' '.join(answer))   # Hello World
   ```
