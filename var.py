# 변수에 값을 할당함으로써 자동으로 변수 생성
# 자료형을 지정하거나 변수를 선언할 필요가 없다.
i = 5
print(i)
i = i + 1
print(i)
i += 1
print(i)

s = '''This is a multi-line string.
This is the second line.'''
print(s)

# 물리적 명령행이란 프로그램 코드 내에 직접 표현된 한 줄
# 논리적 명령행이란 파이썬 인터프리터 관점에서의 한 명령 단위

# ;을 사용하여 한 물리적 명령행에 둘 이상의 논리적 명령행을 강제로 이을 수 있다.
# 아래의 모든 예제는 같다.
i = 5
print(i)
i = 5;
print(i);
i = 5; print(i);
i = 5; print(i);
#

# \를 사용하여 한 논리적 명령행을 여러 물리적 명령행으로 나눌 수 있다.
# 명시적 행간 결합
# 대괄호나 중괄호를 열었을 경우 괄호를 닫을 때 까지 \ 없이도 모두 같은 명령으로 간주된다.
# 이를 비명시적 행간 결합이라고 부른다.
s = 'This is a string. \
This is continues the string.'
print(s)
# 아래의 모든 예제는 같다.
print \
    (i)
print(\
    i)
print(i\
      )
#

# 파이썬에서 공백은 중요한 역할이며 한 행의 앞에 붙어있는 공백은 정말 중요하다.
# 이를 들여쓰기라 부르며 같은 들여쓰기 단계에 있는 명령들은 반드시 같은 들여쓰기를 사용해아한다.
# 같은 들여쓰기를 사용하고 있는 명령들의 집합을 블록(block)이라고 부른다.

