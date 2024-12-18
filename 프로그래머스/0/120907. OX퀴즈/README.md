# [level 0] OX퀴즈 - 120907 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120907) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.04 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 12월 18일 19:50:36

### 문제 설명

<p>덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 형태로 들어있는 문자열 배열 <code>quiz</code>가 매개변수로 주어집니다. 수식이 옳다면 "O"를 틀리다면 "X"를 순서대로 담은 배열을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>연산 기호와 숫자 사이는 항상 하나의 공백이 존재합니다. 단 음수를 표시하는 마이너스 기호와 숫자 사이에는 공백이 존재하지 않습니다.</li>
<li>1 ≤ <code>quiz</code>의 길이 ≤ 10</li>
<li>X, Y, Z는 각각 0부터 9까지 숫자로 이루어진 정수를 의미하며, 각 숫자의 맨 앞에 마이너스 기호가 하나 있을 수 있고 이는 음수를 의미합니다.</li>
<li>X, Y, Z는 0을 제외하고는 0으로 시작하지 않습니다.</li>
<li>-10,000 ≤ X, Y ≤ 10,000</li>
<li>-20,000 ≤ Z ≤ 20,000</li>
<li>[연산자]는 + 와 - 중 하나입니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>quiz</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>["3 - 4 = -3", "5 + 6 = 11"]</td>
<td>["X", "O"]</td>
</tr>
<tr>
<td>["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]</td>
<td>["O", "O", "X", "O"]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>3 - 4 = -3 은 틀린 수식이므로 "X", 5 + 6 = 11 은 옳은 수식이므로 "O" 입니다. 따라서 ["X", "O"]를 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>19 - 6 = 13 은 옳은 수식이므로 "O", 5 + 66 = 71 은 옳은 수식이므로 "O", 5 - 15 = 63 은 틀린 수식이므로 "X", 3 - 1 = 2는 옳은 수식이므로 "O" 따라서 ["O", "O", "X", "O"]를 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 참고
- split() : 문자열을 특정 구분자를 기준으로 나누는 메서드, 결과를 리스트로 나타내기 때문에 인덱스로 각 요소 접근 가능
  ```
  # 인자 없이 사용하면 공백(스페이스, 탭, 줄바꿈)을 기준으로 분리
  text = "hello world python"
  result = text.split()
  print(result)  # ['hello', 'world', 'python']

  # 특정 구분자 지정
  text = "apple,banana,cherry"
  result = text.split(',')
  print(result)  # ['apple', 'banana', 'cherry']

  # 복잡한 문자열 분리
  equation = "19 - 6 = 13"
  parts = equation.split('=')
  print(parts)  # ['19 - 6 ', ' 13']

  # 수식 분리
  left = parts[0].strip()
  right = parts[1].strip()
  left_parts = left.split()
  print(left_parts)  # ['19', '-', '6']

  # 줄바꿈 기준 분리
  multiline = """first line
            second line
            third line"""
  lines = multiline.split('\n')
  print(lines)  # ['first line', 'second line', 'third line']

  # 여러 구분자 동시에 사용
  import re
  text = "apple:banana;cherry,grape"
  result = re.split('[,:;]', text)
  print(result)  # ['apple', 'banana', 'cherry', 'grape']
  ```
