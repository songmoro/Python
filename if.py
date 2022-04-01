number = 23
guess = int(input('Enter an integer : ')) # 파이썬3 에서는 raw_input이 아니라 input을 사용

if guess == number:
    # new block starts here
    print('Congratulations, you guessed it.')
    print('but you do not win any prizes!')
    # new block ends here
elif guess < number:
    # another block
    print('No, it is a little higher than that')
    # you can do whatever you want in a block ...
else:
    print('No, it is a little lower than that')
    # you must have guessed > number to reach here

print('Done')
# This last statement is always executed,
# after the if statement is executed.
