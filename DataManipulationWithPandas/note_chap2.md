# Aggregating DataFrames

## Mean
- 일반적인 평균값 계산 공식
- (전체총합)/(총개수)

## Median
- 중앙값
1. 전체 수 정렬
2. 홀수인 경우: (n+1)/2의 위치의 값
    짝수인 경우: (가운데 두 수의 합)/2

## .agg()
- method allows you to apply your own custom functions to a DataFrame
- df['column'].agg(function)

## cumulative Values
- .cumsum()
- .cummax()

## .drop_duplicates()
- Removing duplicates

## .value_counts(0)
- <...>.value_counts(sort=True, normalize=True)

## .groupby
- SQL의 group by와 같은 기능

## 피벗 테이블(pivot table)
- Pivot tables are another way of calculating grouped summary statistics. 
- 커다란 표(예: 데이터베이스, 스프레드시트, 비즈니스 인텔리전스 프로그램 등)의 데이터를 요약하는 통계표이다. 이 요약에는 합계, 평균, 기타 통계가 포함될 수 있으며 피벗 테이블이 이들을 함께 의미있는 방식으로 묶어준다.
- 피벗 테이블은 데이터 처리의 한 기법이다. 유용한 정보에 집중할 수 있도록 하기 위해 통계를 정렬 또는 재정렬(피벗)한다.

### .pivot_table(values="...", index="...", aggfunc=<...>, columns=..)
- values: 나타내려는 컬럼
- index: groupby할 컬럼
- aggfunc: 적용하려는 함수
- fill_value: replaces missing values with a real value (known as imputation). What to replace missing values with is a topic big enough to have its own course (Dealing with Missing Data in Python), but the simplest thing to do is to substitute a dummy value.
- margins: a shortcut for when you pivoted by two variables, but also wanted to pivot by each of those variables separately: it gives the row and column totals of the pivot table contents.