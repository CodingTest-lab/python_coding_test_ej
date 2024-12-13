# [level 0] 배열의 유사도 - 120903 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120903) 

### 성능 요약

메모리: 9.97 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 12월 13일 17:44:08

### 문제 설명

<p>두 배열이 얼마나 유사한지 확인해보려고 합니다. 문자열 배열 <code>s1</code>과 <code>s2</code>가 주어질 때 같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>s1</code>, <code>s2</code>의 길이 ≤ 100</li>
<li>1 ≤ <code>s1</code>, <code>s2</code>의 원소의 길이 ≤ 10</li>
<li><code>s1</code>과 <code>s2</code>의 원소는 알파벳 소문자로만 이루어져 있습니다</li>
<li><code>s1</code>과 <code>s2</code>는 각각 중복된 원소를 갖지 않습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>s1</th>
<th>s2</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>["a", "b", "c"]</td>
<td>["com", "b", "d", "p", "c"]</td>
<td>2</td>
</tr>
<tr>
<td>["n", "omg"]</td>
<td>["m", "dot"]</td>
<td>0</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>"b"와 "c"가 같으므로 2를 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>같은 원소가 없으므로 0을 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

---
### 참고
- set(집합) : 중복되지 않는 고유한 요소들의 모음, 중복 요소 자동 제거, 순서 없음, 해시 가능한(immutable) 요소만 포함 가능
  ```
  # 빈 집합 만들기
  s1 = set()
  # 리스트로부터 집합 생성
  s2 = set([1, 2, 3, 4, 4, 5])  # {1, 2, 3, 4, 5}
  # 직접 요소 입력
  s3 = {1, 2, 3, 4, 5}

  # 추가
  s = {1, 2, 3}
  s.add(4)  # {1, 2, 3, 4}

  # 여러 요소 추가
  s.update([5, 6, 7])  # {1, 2, 3, 4, 5, 6, 7}

  # 삭제
  s.remove(3)  # 요소 없으면 에러 발생
  s.discard(3)  # 요소 없어도 에러 없음

  # 교집합
  s1 = {1, 2, 3}
  s2 = {3, 4, 5}
  print(s1 & s2)  # {3}
  print(s1.intersection(s2))  # {3}

  # 합집합
  print(s1 | s2)  # {1, 2, 3, 4, 5}
  print(s1.union(s2))  # {1, 2, 3, 4, 5}

  # 차집합
  print(s1 - s2)  # {1, 2}
  print(s1.difference(s2))  # {1, 2}

  # 길이
  len(s)

  # 포함 여부
  2 in s  # True/False

  # 복사
  s_copy = s.copy()

  # 모든 요소 제거
  s.clear()
  ```
