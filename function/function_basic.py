
'''
* 함수 (function)

- 함수는 지속적으로 사용되는 코드 블록에 이름을 붙여놓은 형태입니다.

- 함수는 한 번 정의해 두면 지정된 함수 이름을 통해
언제든지 해당 코드 블록을 실행할 수 있습니다.

- 함수를 정의할 때 사용하는 키워드는 def 입니다.

- 정의해 놓은 함수를 사용하는 것을 호출(call) 이라고 부릅니다.

- 파이썬에서는 함수를 호출하려면 반드시 호출문보다 상단부에
함수를 먼저 정의해야 합니다.
'''

# 함수의 정의 (1~X까지의 누적합을 구하는 로직)

def calc_sum(end):
    sum = 0
    for n in range(1,end+1):
        sum += n
        return sum

# 함수의 호출
print(f'함수의 호출 결과: {calc_sum(100)}')

def add(n1, n2):
    return n1 + n2

result = add(10, 5)

# 리턴이 있는 함수는 다른 함수의 매개값으로도 사용이 가능합니다.
print(add(add(5,7), add(9,8))) # add(12, 17)
# n = int(input('정수: ')) -> n = int('3')

def operate_all(n1, n2):
    return n1 + n2, n1-n2, n1*n2, n1/n2 # tuple
    # return n1 - n2
    # return n1 * n2
    # return n1 / n2

print(type(operate_all(10, 5)))

def multi(n1, n2):
    result = n1 * n2
    print(f'{n1} x {n2} = {result}')

abc = multi(9, 6)
print(abc)  
