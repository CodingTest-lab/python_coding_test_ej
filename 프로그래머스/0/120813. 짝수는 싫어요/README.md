# [level 0] 짝수는 싫어요 - 120813 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120813) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.02 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 12월 09일 19:21:02

### 문제 설명

<p>정수 <code>n</code>이 매개변수로 주어질 때, <code>n</code> 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>n</code> ≤ 100</li>
</ul>

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
<td>[1, 3, 5, 7, 9]</td>
</tr>
<tr>
<td>15</td>
<td>[1, 3, 5, 7, 9, 11, 13, 15]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 #1</p>

<ul>
<li>10 이하의 홀수가 담긴 배열 [1, 3, 5, 7, 9]를 return합니다.</li>
</ul>

<p>입출력 #1</p>

<ul>
<li>15 이하의 홀수가 담긴 배열 [1, 3, 5, 7, 9, 11, 13, 15]를 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

---
## 참고
- range() : 숫자 시퀀스 생성(순서대로)
  ```
  # 1. range(stop)
  # 0부터 stop-1까지의 숫자 생성
    for i in range(5):
            print(i)  # 0, 1, 2, 3, 4 출력
  
  # 2. range(start, stop)
  # start부터 stop-1까지의 숫자 생성
    for i in range(1, 6):
            print(i)  # 1, 2, 3, 4, 5 출력
  
  # 3. range(start, stop, step)
  # start부터 stop-1까지 step만큼 건너뛰며 생성
    for i in range(0, 10, 2):
            print(i)  # 0, 2, 4, 6, 8 출력
  # 감소하는 순서
    for i in range(10, 0, -1):
            print(i)  # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 출력
  ```
