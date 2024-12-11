# [level 0] 짝수의 합 - 120831 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120831) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.02 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 12월 11일 20:14:59

### 문제 설명

<p>정수 <code>n</code>이 주어질 때, <code>n</code>이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.</p>

<hr>

<h5>제한사항</h5>

<p>0 &lt; <code>n</code> ≤ 1000</p>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>10</td>
<td>30</td>
</tr>
<tr>
<td>4</td>
<td>6</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li><code>n</code>이 10이므로 2 + 4 + 6 + 8 + 10 = 30을 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li><code>n</code>이 4이므로 2 + 4 = 6을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

---
### 참고
- sum() : iterable(예: 리스트, 튜플 등)의 모든 요소를 더하는 데 사용되는 내장 함수, 주로 숫자들의 합계를 계산하는 데 사용, 문자열이나 다른 데이터 타입이 포함된 iterable을 사용하면 TypeError가 발생
  ```
  numbers = [1, 2, 3, 4, 5]
  result = sum(numbers)
  print(result)  # 출력: 15

  numbers = [1, 2, 3]
  result = sum(numbers, 10)  # 10을 초기값으로 추가
  print(result)  # 출력: 16
  
  float_numbers = [1.5, 2.5, 3.5]
  result = sum(float_numbers)
  print(result)  # 출력: 7.5

  ```
