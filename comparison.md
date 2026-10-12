# 라이브러리 비교



|비교 항목|라이브러리 X|라이브러리 O|차이|
|-|-|-|-|
|코드 줄 수 |28줄|5줄|23줄 감소 |
|처리하기 어려웠던 부분|점수가 빈 줄 때문에 float()에서 ValueError가 나서 if문과 try/except로 직접 걸러야 했고, 카테고리별 합계와 개수도 딕셔너리로 직접 관리해야 했다.|to\_numeric의 errors="coerce" 철자만 맞게 쓰면 빈 값이 NaN이 되고 mean()이 알아서 제외해 줘서 따로 처리할 게 없었다.|예외 처리와 집계를 직접 구현하던 부분을 pandas 함수 몇 개(read\_csv, to\_numeric, groupby, mean, round)가 대신해 준다.|
|실행 결과|국어 75.78<br />수학 82.83<br />영어 82.0|category<br />국어    75.78<br />수학    82.83<br />영어    82.00<br />Name: score, dtype: float64|카테고리별 평균값은 같고, 출력 형식만 다르다 (pandas는 표 형태로 출력).|

# 



