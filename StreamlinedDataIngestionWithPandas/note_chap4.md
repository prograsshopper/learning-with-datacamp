# Importing JSON Data and Working with APIs

### read_json()
- pandas가 json을 읽어오기 위한 메서드로, string path 혹은 JSON 데이터를 문자열로 받는다.
- dtype: 데이터 타입을 특정하는 키워드
- orient: 레이아웃에 플래그를 지정하는 키워드

### requests.get(api_url, headers=headers, params=params)
- 위의 메서드로 데이터를 불러온다음, 데이터를 분리하고 싶으면 json 매서드를 사용하면 된다.

## Working with nested JSONs
### pandas.io.json
- JSON을 읽고 쓰는 툴이 있는 서브모듈

### .json_normalize()
- dictionary내의 dictionary를 받는다.
- 평평하게(flatten) 바꾼 데이터프레임을 리턴한다.
    - sep: 점 구분기호는 판다스의 점 표기법에 방해되므로, 해당 인수에 다른 구분기호를 지정하는 것을 권장한다. 주로 _(underscore)를 사용하는듯.
    - record_path: 중첩된 데이터의 문자열 속성의 문자열/리스트 
    - meta: 데이터프레임으로 로드하기 위한 다른 속성의 리스트
    - meta_prefix: 메타 컬럼명의 접두사 문자열

## 데이터의 결합
### .append()
- 데이터프레임 메서드
- df1.append(df2)
- ignore_index: True로 세팅하면 인덱스를 다시 지정한다.

### .merge()
- pandas에서 SQL의 join처럼 사용하는 메서드
- df1.merge(df2, ...)
- on: 같은 이름의 키면 사용
- left_on, right_on: 이름이 다를 경우 사용