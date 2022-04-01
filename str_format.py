age = 20
name = 'Swaroop'

print('Quote me on this') # ' '를 이용하여 문자열 지정
print("What's your name?") # " " 를 이용하여 문자열 지정(" " 사이에 ' 사용 가능)
print("""This is a multi-line string. This is the first line.
This is the second line.
"What's your name?, " I asked.
He Said "Bond, James Bond."
""") # """ """, ''' '''를 사용하여 여러 줄에 걸친 문자열 및 문자열 안에서 ', " 사용

print("{0} was {1} years old when he wrote this book".format(name,age)) # format 메소드에 인자는 0부터 시작
print("Why is {0} playing with that python?".format(name))

print("{} was {} years old when he wrote this book".format(name,age)) # format 메소드의 인자에 숫자 생략
print("Why is {} playing with that python?".format(name))

# 소수점 이하 셋 째 자리까지 부동 소숫점 숫자 표기 (0.333)
print('{0:.3f}'.format(1.0/3))
# 밑줄(_)로 11칸을 채우고 가운데 정렬(^)하기 (___hello___)
print('{0:_^11}'.format('hello'))
# 사용자 지정 키워드를 이용해 (Swaroop wrote A Byte of Python) 표기
print('{name} wrote {book}'.format(name = 'Swaroop', book = 'A Byte of Python'))

# print 명령어는 항상 \n을 덧붙인다. print("Statement",end = '\n')
print("a",end = ' ')
print("b")
print("a",end = '')
print("b")

# 이스케이프 문자 사용
print('What\'s your name?')
print('This is first line\nThis is the second line')

# 문자열을 끊김 없이 이어 붙이기 위해 \ 사용
print("This is the first sentence. \
This is the second sentence.")

# 문자열 앞에 r, R을 붙여 순(Raw) 문자열임을 표기
print(r"Newlines are indicated by \n")
# 순 문자열을 사용해 짧게 표기 \\1 = r\1
print('\\1', end = ' ')
print(r'\1')

# 변수 이름은 식별자의 한 예이며 식별자의 첫 문자는 알파벳 문자이거나 밑줄(_)
# 나머지는 알파벳 문자, 밑줄, 숫자
# 식별자는 대/소문자를 구분


