# [level 1] 푸드 파이트 대회 - 134240 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/134240) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.02 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 12월 30일 15:44:06

### 문제 설명

<p>수웅이는 매달 주어진 음식을 빨리 먹는 푸드 파이트 대회를 개최합니다. 이 대회에서 선수들은 1대 1로 대결하며, 매 대결마다 음식의 종류와 양이 바뀝니다. 대결은 준비된 음식들을 일렬로 배치한 뒤, 한 선수는 제일 왼쪽에 있는 음식부터 오른쪽으로, 다른 선수는 제일 오른쪽에 있는 음식부터 왼쪽으로 순서대로 먹는 방식으로 진행됩니다. 중앙에는 물을 배치하고, 물을 먼저 먹는 선수가 승리하게 됩니다.</p>

<p>이때, 대회의 공정성을 위해 두 선수가 먹는 음식의 종류와 양이 같아야 하며, 음식을 먹는 순서도 같아야 합니다. 또한, 이번 대회부터는 칼로리가 낮은 음식을 먼저 먹을 수 있게 배치하여 선수들이 음식을 더 잘 먹을 수 있게 하려고 합니다. 이번 대회를 위해 수웅이는 음식을 주문했는데, 대회의 조건을 고려하지 않고 음식을 주문하여 몇 개의 음식은 대회에 사용하지 못하게 되었습니다.</p>

<p>예를 들어, 3가지의 음식이 준비되어 있으며, 칼로리가 적은 순서대로 1번 음식을 3개, 2번 음식을 4개, 3번 음식을 6개 준비했으며, 물을 편의상 0번 음식이라고 칭한다면, 두 선수는 1번 음식 1개, 2번 음식 2개, 3번 음식 3개씩을 먹게 되므로 음식의 배치는 "1223330333221"이 됩니다. 따라서 1번 음식 1개는 대회에 사용하지 못합니다.</p>

<p>수웅이가 준비한 음식의 양을 칼로리가 적은 순서대로 나타내는 정수 배열 <code>food</code>가 주어졌을 때, 대회를 위한 음식의 배치를 나타내는 문자열을 return 하는 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>2 ≤ <code>food</code>의 길이 ≤ 9</li>
<li>1 ≤ <code>food</code>의 각 원소 ≤ 1,000</li>
<li><code>food</code>에는 칼로리가 적은 순서대로 음식의 양이 담겨 있습니다.</li>
<li><code>food[i]</code>는 i번 음식의 수입니다.</li>
<li><code>food[0]</code>은 수웅이가 준비한 물의 양이며, 항상 1입니다.</li>
<li>정답의 길이가 3 이상인 경우만 입력으로 주어집니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>food</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[1, 3, 4, 6]</td>
<td>"1223330333221"</td>
</tr>
<tr>
<td>[1, 7, 1, 2]</td>
<td>"111303111"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p><strong>입출력 예 #1</strong></p>

<ul>
<li>문제 예시와 같습니다.</li>
</ul>

<p><strong>입출력 예 #2</strong></p>

<ul>
<li>두 선수는 1번 음식 3개, 3번 음식 1개를 먹게 되므로 음식의 배치는 "111303111"입니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 참고
- enumerate() : iterable(반복 가능한 객체)의 요소를 순회하면서 인덱스와 값을 함께 반환하는 내장 함수 <br>
        - 리스트나 튜플의 인덱스와 값을 동시에 필요로 할 때, 행 번호가 필요한 파일 처리, 순차적인 데이터 처리에서 위치 정보가 필요할 때, 인덱스 기반 조건문이 필요할 때 편리
  ```
  fruits = ['apple', 'banana', 'cherry']
  for index, value in enumerate(fruits):
     print(f"Index: {index}, Value: {value}")

  # 출력:
  # Index: 0, Value: apple
  # Index: 1, Value: banana
  # Index: 2, Value: cherry

  # 시작 인덱스를 1로 지정
  for index, value in enumerate(fruits, start=1):
     print(f"Index: {index}, Value: {value}")

  # 인덱스가 짝수인 요소만 선택(리스트 컴프리헨션 사용)
  even_indexed = [v for i, v in enumerate(fruits) if i % 2 == 0]

  # 문자열과 함께 사용
  word = "Python"
  for i, char in enumerate(word):
     print(f"Position {i}: {char}")

  # 리스트의 값을 키로, 인덱스를 값으로 하는 딕셔너리 생성
  dict_from_list = {value: index for index, value in enumerate(fruits)}
  ```
