def q14563():
    # 완전수
    n = int(input())
    nums = list(map(int, input().split()))
    result = []
    for num in nums:
        div = 1
        sum_val = 0
        while div != (num // 2) + 1:
            if num % div == 0:
                sum_val += div
            div += 1
        if sum_val == num:
            result.append('Perfect')
        elif sum_val > num:
            result.append('Abundant')
        else:
            result.append('Deficient')
    for answer in result:
        print(answer)


def q1773():
    # 폭죽쇼
    n, c = map(int, (input().split()))
    dp = [0] * 2000001
    for _ in range(n):
        time = int(input())
        for i in range(time, c + 1, time):
            dp[i] = 1
    print(sum(dp))


def q2775():
    # 부녀회장이 될테야
    t = int(input())
    result = []
    for _ in range(t):
        k = int(input())
        n = int(input())
        dp = [[0] * (n + 1) for _ in range(k + 1)]
        for i in range(1, n + 1):
            dp[0][i] = i
        for i in range(1, k + 1):
            for j in range(1, n + 1):
                dp[i][j] = sum(dp[i - 1][:j + 1])
        result.append(dp[k][n])
    for answer in result:
        print(answer)


def q2609():
    # 최대공약수와 최소공배수
    n1, n2 = map(int, input().split())
    for_lcm = n1 * n2
    for_gcd = 0
    if n1 >= n2:
        while n2 != 0:
            r = n1 % n2
            n1 = n2
            n2 = r
        for_gcd = n1
    else:
        while n1 != 0:
            r = n2 % n1
            n2 = n1
            n1 = r
        for_gcd = n2
    gcd = for_gcd
    lcm = for_lcm // gcd
    print(gcd)
    print(lcm)


def q1157():
    # 단어 공부
    s = input().upper()
    dp = [0] * 26
    for char in s:
        dp[ord(char) - 65] += 1
    if dp.count(max(dp)) >= 2:
        print('?')
    else:
        print(chr(dp.index(max(dp)) + 65))


def q4344():
    # 평균은 넘겠지
    c = int(input())
    result = []
    for _ in range(c):
        lst = list(map(int, input().split()))
        count = 0
        average = sum(lst[1:]) / lst[0]
        for i in range(1, len(lst)):
            if lst[i] > average:
                count += 1
        answer = str(round((count / lst[0] * 100), 3))
        if answer[-1] == '0':
            answer += '00%'
        else:
            answer += '%'
        result.append(answer)
    for answer in result:
        print(answer)


def q1032():
    # 명령 프롬프트
    n = int(input())
    files = []
    for _ in range(n):
        files.append(input())
    string = ''
    index = 0

    for j in range(len(files[0])):
        temp = True
        for i in range(1, n):
            if files[i - 1][j] != files[i][j]:
                temp = False
        if temp:
            string += files[0][index]
            index += 1
        else:
            string += '?'
            index += 1
    print(string)


def q2562():
    # 최댓값
    lst = []
    for _ in range(9):
        lst.append(int(input()))
    print(max(lst))
    print(lst.index(max(lst)) + 1)


def q10872():
    # 팩토리얼
    n = int(input())

    def factor(num):
        if num <= 1:
            return 1
        else:
            return num * factor(num - 1)

    print(factor(n))


def q23971():
    # ZOAC 4
    import math
    h, w, n, m = map(int, input().split())
    print(math.ceil(h / (n + 1)) * math.ceil(w / (m + 1)))


def q5073():
    # 삼각형과 세 변
    result = []
    while 1:
        lst = list(map(int, input().split()))
        if sum(lst) == 0:
            break
        lst_temp1 = lst.copy()
        max_temp1 = lst_temp1.pop(lst_temp1.index(max(lst_temp1)))
        if sum(lst_temp1) <= max_temp1:
            result.append("Invalid")
        elif len(set(lst)) == 1:
            result.append("Equilateral")
        elif len(set(lst)) == 2:
            result.append("Isosceles")
        else:
            result.append("Scalene")
    for answer in result:
        print(answer)


def q2292():
    # 벌집
    n = int(input())
    index = 1
    first = 1
    prod = 6
    while first < n:
        first += prod * index
        index += 1
    print(index)


def q13458():
    # 시험 감독
    import math

    n = int(input())
    a = list(map(int, input().split()))
    b, c = map(int, input().split())
    result = 0
    for i in range(n):
        if a[i] >= b:
            a[i] -= b
        else:
            a[i] = a[i] // b
        result += math.ceil(a[i] / c) + 1
    print(result)


def q10926():
    # ??!
    s = input()
    print(s + '??!')


def q18108():
    # 1998년생인 내가 태국에서는 2541년생?!
    y = int(input())
    print(str(y - 543))


def q11382():
    # 꼬마 정민
    a, b, c = map(int, input().split())
    print(str(a + b + c))


def q10171():
    # 고양이
    l1 = "\\    /\\"
    l2 = " )  ( ')"
    l3 = "(  /  )"
    l4 = " \\(__)|"
    lst = [l1, l2, l3, l4]
    for i in lst:
        print(i)


def q10172():
    # 개
    l1 = "|\\_/|"
    l2 = "|q p|   /}"
    l3 = '( 0 )"""\\'
    l4 = '|"^"`    |'
    l5 = "||_/=\\\\__|"
    lst = [l1, l2, l3, l4, l5]
    for i in lst:
        print(i)


def q2739():
    # 구구단
    n = int(input())
    for i in range(1, 10):
        s = str(n) + f' * {i} = {n * i}'
        print(s)


def q10950():
    # A+B - 3
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        print(a + b)


def q8393():
    # 합
    n = int(input())
    result = 0
    for i in range(1, n + 1):
        result += i
    print(result)


def q25304():
    # 영수증
    x = int(input())
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        x -= a * b
    if x:
        print('No')
    else:
        print('Yes')


def q25314():
    # 코딩은 체육과목 입니다
    n = int(input())
    result = ''
    if n % 4 == 0:
        f = n // 4
    else:
        f = n // 4 + 1
    for _ in range(f):
        result += 'long '
    print(result + 'int')


def q15552():
    # 빠른 A+B
    import sys

    t = int(input())
    for _ in range(t):
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)


def q2438():
    # 별 찍기 - 1
    n = int(input())
    for i in range(1, n + 1):
        print('*' * i)


def q2439():
    # 별 찍기 - 2
    n = int(input())
    for i in range(1, n + 1):
        result = ' ' * (n - i) + '*' * i
        print(result)


def q10952():
    # A+B - 5
    while 1:
        a, b = map(int, input().split())
        if a == b == 0:
            break
        else:
            print(a + b)


def q10951():
    # A+B - 4
    import sys

    while 1:
        s = sys.stdin.readline().rstrip()
        if not s:
            break
        else:
            a, b = int(s[0]), int(s[-1])
            print(a + b)


def q10807():
    # 개수 세기
    n = int(input())
    lst = list(map(int, input().split()))
    v = int(input())
    print(lst.count(v))


def q10871():
    # X보다 작은 수
    n, x = map(int, input().split())
    lst = list(map(int, input().split()))
    result = []
    for i in lst:
        if i < x:
            result.append(i)
    print(*result)


def q10818():
    # 최소, 최대
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    print(str(lst[0]) + ' ' + str(lst[-1]))


def q10810():
    # 공 넣기
    n, m = map(int, input().split())
    lst = [0] * (n + 1)
    for _ in range(m):
        i, j, k = map(int, input().split())
        for l in range(i, j + 1):
            lst[l] = k
    print(*lst[1:n + 1])


def q10813():
    # 공 바꾸기
    n, m = map(int, input().split())
    lst = [i for i in range(1, n + 1)]
    for _ in range(m):
        i, j = map(int, input().split())
        temp = lst[i - 1]
        lst[i - 1], lst[j - 1] = lst[j - 1], temp
    print(*lst)


def q5597():
    # 과제 안 내신 분..?
    lst = [i for i in range(1, 31)]
    for _ in range(28):
        lst.remove(int(input()))
    for result in lst:
        print(result)


def q3052():
    # 나머지
    lst = []
    for _ in range(10):
        n = int(input())
        lst.append(n % 42)
    lst = list(set(lst))
    print(len(lst))


def q10811():
    # 바구니 뒤집기
    n, m = map(int, input().split())
    lst = [i for i in range(1, n + 1)]
    for _ in range(m):
        i, j = map(int, input().split())
        lst[i - 1:j] = list(reversed(lst[i - 1:j]))
    print(*lst)


def q1546():
    # 평균
    n = int(input())
    lst = list(map(int, input().split()))
    max_val = max(lst)
    for i in range(len(lst)):
        lst[i] = lst[i] / max_val * 100
    print(sum(lst) / n)


def q27866():
    # 문자열
    s = input()
    i = int(input())
    print(s[i - 1])


def q2743():
    # 단어 길이 재기
    print(len(input()))


def q9086():
    # 문자열
    t = int(input())
    for _ in range(t):
        s = input()
        print(s[0] + s[-1])


def q11654():
    # 아스키 코드
    print(ord(input()))


def q11720():
    # 숫자의 합
    n = int(input())
    s = input()
    result = 0
    for i in range(n):
        result += int(s[i])
    print(result)


def q10809():
    # 알파벳 찾기
    s = input()
    alphabet = [chr(i) for i in range(97, 123)]
    result = [-1 for _ in range(len(alphabet))]
    for i in range(len(s)):
        if s[i] in alphabet:
            result[alphabet.index(s[i])] = s.index(s[i])
    print(*result)


def q1152():
    # 단어의 개수
    s = list(map(str, input().split()))
    print(len(s))


def q2908():
    # 상수
    a, b = map(str, input().split())
    new_a, new_b = '', ''
    for i in range(2, -1, -1):
        new_a += a[i]
        new_b += b[i]
    print(max(int(new_a), int(new_b)))


def q5622():
    # 다이얼
    s = input()
    dic = {3: ['A', 'B', 'C'], 4: ['D', 'E', 'F'], 5: ['G', 'H', 'I'], 6: ['J', 'K', 'L'], 7: ['M', 'N', 'O'],
           8: ['P', 'Q', 'R', 'S'], 9: ['T', 'U', 'V'], 10: ['W', 'X', 'Y', 'Z']}
    result = 0
    for i in range(len(s)):
        for key, item in dic.items():
            if s[i] in item:
                result += key
    print(result)


def q11718():
    # 그대로 출력하기
    import sys

    count = 0
    while count < 100:
        print(sys.stdin.readline().rstrip())
        count += 1


def q25083():
    # 새싹
    print(
        "         ,r'\"7" + "\n"
        "r`-_   ,'  ,/" + "\n"
        " \\. \". L_r'" + "\n"
        "   `~\\/" + "\n"
        "      |" + "\n"
        "      |"
    )


def q3033():
    # 킹, 퀸, 룩, 비숍, 나이트, 폰
    lst = list(map(int, input().split()))
    answer = [1, 1, 2, 2, 2, 8]
    result = []
    for i in range(6):
        result.append(answer[i] - lst[i])
    print(*result)


def q2444():
    # 별 찍기 - 7
    n = int(input())
    for i in range(n - 1, 0, -1):
        print((' ' * i) + ('*' * (2 * (n - i) - 1)))
    print('*' * (2 * n - 1))
    for i in range(1, n):
        print((' ' * i) + ('*' * (2 * (n - i) - 1)))


def q2738():
    # 행렬 덧셈
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    for i in range(n):
        b = list(map(int, input().split()))
        for j in range(m):
            a[i][j] += b[j]
    for i in range(n):
        print(*a[i])


def q2566():
    # 최댓값
    max_val = 0
    index = [1, 1]
    for i in range(1, 10):
        temp = list(map(int, input().split()))
        temp_max = max(temp)
        if max_val < temp_max:
            max_val = temp_max
            index[0] = i
            index[1] = temp.index(temp_max) + 1
    print(max_val)
    print(*index)


def q10798():
    # 세로읽기
    lst = []
    result = ''
    for _ in range(5):
        temp = list(input())
        for _ in range(15 - len(temp)):
            temp.append('')
        lst.append(temp)
    for i in range(15):
        for j in range(5):
            result += lst[j][i]
    print(result)


def q2745():
    # 진법 변환
    n, b = input().split()
    print(int(n, int(b)))


def q11005():
    # 진법 변환 2
    import sys

    n, b = map(int, sys.stdin.readline().split())
    dic = {}
    for i in range(10, 36):
        dic[i] = str(chr(55 + i))
    dic[0] = '0'
    result = ''
    while n > 0:
        remainder = n % b
        if b == 10:
            print(n)
            break
        elif remainder < 10:
            result = str(remainder) + result
        else:
            result = dic[remainder] + result
        n //= b
    print(result)


def q2720():
    # 세탁소 사장 동혁
    t = int(input())
    for _ in range(t):
        c = int(input())
        lst = [0, 0, 0, 0]
        while c:
            if c // 25 != 0:
                lst[0] += 1
                c -= 25
            elif c // 10 != 0:
                lst[1] += 1
                c -= 10
            elif c // 5 != 0:
                lst[2] += 1
                c -= 5
            else:
                lst [3] += 1
                c -= 1
        print(*lst)


def q2903():
    # 중앙 이동 알고리즘
    n = int(input())
    dp = [0] * 16
    dp[0] = 2
    for i in range(1, 16):
        dp[i] = dp[i - 1] + dp[i - 1] - 1
    print(dp[n] * dp[n])


def q2869():
    # 달팽이는 올라가고 싶다
    import math

    a, b, v = map(int, input().split())
    v -= a
    print(math.ceil(v / (a - b)) + 1)


def q2501():
    # 약수 구하기
    n, k = map(int, input().split())
    lst = []
    d = 1
    if n % 2 == 0:
        while n // 2 >= d:
            if n % d == 0:
                lst.append(d)
            d += 1
        lst.append(n)
    else:
        while n // 3 >= d:
            if n % d == 0:
                lst.append(d)
            d += 1
        lst.append(n)
    if len(lst) >= k:
        print(lst[k - 1])
    else:
        print(0)


def q1978():
    # 소수 찾기
    n = int(input())
    lst = list(map(int, input().split()))
    result = 0
    dp = [0] * 1001
    dp[1] = 1
    for i in range(2, 500):
        for j in range(2, 500):
            if i * j > 1000:
                continue
            dp[i * j] = 1
    for num in lst:
        if not dp[num]:
            result += 1
    print(result)


def q2581():
    # 소수
    m = int(input())
    n = int(input())
    dp = [0] * 10001
    dp[1] = 1
    s = []
    for i in range(2, 5001):
        for j in range(2, 5001):
            if i * j > 10000:
                continue
            dp[i * j] = 1
    for i in range(m, n + 1):
        if not dp[i]:
            s.append(i)
    if s:
        print(sum(s))
        print(min(s))
    else:
        print(-1)


def q27323():
    # 직사각형
    a = int(input())
    b = int(input())
    print(a * b)


def q1085():
    # 직사각형에서 탈출
    x, y, w, h = map(int, input().split())
    print(min(abs(w - x), abs(h - y), x, y))


def q15894():
    # 수학은 체육과목 입니다
    n = int(input())
    print(n * 4)


def q9063():
    # 대지
    n = int(input())
    xs = []
    ys = []
    for _ in range(n):
        x, y = map(int, input().split())
        xs.append(x)
        ys.append(y)
    print((max(ys) - min(ys)) * (max(xs) - min(xs)))


def q10101():
    # 삼각형 외우기
    lst = []
    for _ in range(3):
        lst.append(int(input()))

    if lst[0] + lst[1] + lst[2] == 180:
        if lst[0] == lst[1] == 60:
            print('Equilateral')
        elif lst[0] == lst[1] or lst[1] == lst[2] or lst[0] == lst[2]:
            print('Isosceles')
        else:
            print('Scalene')
    else:
        print('Error')


def q14215():
    # 세 막대
    lst = list(map(int, input().split()))
    lst.sort()
    result = 0
    if lst[0] + lst[1] > lst[2]:
        result = sum(lst)
    else:
        result = (lst[0] + lst[1]) * 2 - 1
    print(result)


def q24262():
    # 알고리즘 수업 - 알고리즘의 수행 시간 1
    print(1)
    print(0)


def q24263():
    # 알고리즘 수업 - 알고리즘의 수행 시간 2
    print(input())
    print(1)


def q24264():
    # 알고리즘 수업 - 알고리즘의 수행 시간 3
    n = int(input())
    print(n * n)
    print(2)


def q24265():
    # 알고리즘 수업 - 알고리즘의 수행 시간 4
    n = int(input())
    result = 0
    for i in range(1, n):
        result += i
    print(result)
    print(2)


def q24266():
    # 알고리즘 수업 - 알고리즘의 수행 시간 5
    n = int(input())
    print(n * n * n)
    print(3)


def q24267():
    # 알고리즘 수업 - 알고리즘의 수행 시간 6
    n = int(input())
    result = 0
    s = 0
    for i in range(1, n - 1):
        s += i
        result += s
    print(result)
    print(3)


def q2798():
    # 블랙잭
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    max_val = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if max_val < lst[i] + lst[j] + lst[k] <= m:
                    max_val = lst[i] + lst[j] + lst[k]
    print(max_val)


def q2231():
    # 분해합
    n = int(input())
    if n in [2, 4, 6, 8]:
        print(n // 2)
        return
    if n > 19:
        length = len(str(n)) * 9
    else:
        length = (len(str(n)) - 1) * 9
    result = 0
    for i in range(n - length, n):
        temps = []
        for j in str(i):
            temps.append(int(j))
        if i + sum(temps) == n:
            result = i
            break
    print(result)


def q19532():
    # 수학은 비대면강의입니다
    a, b, c, d, e, f = map(int, input().split())
    for x in range(-999, 1000):
        for y in range(-999, 1000):
            if a * x + b * y == c and d * x + e * y == f:
                print(x, y)


def q2750():
    # 수 정렬하기
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(int(input()))
    lst.sort()
    for num in lst:
        print(num)


def q2587():
    # 대표값2
    lst = []
    for _ in range(5):
        lst.append(int(input()))
    lst.sort()
    print(sum(lst) // 5)
    print(lst[2])


def q25303():
    # 커트라인
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort(reverse=True)
    print(lst[k - 1])


def q10989():
    # 수 정렬하기 3
    import sys

    n = int(sys.stdin.readline())
    dic = {}
    for _ in range(n):
        temp = int(sys.stdin.readline())
        if temp in dic:
            dic[temp] += 1
        else:
            dic[temp] = 1
    dic = sorted(dic.items())
    for key, val in dic:
        for _ in range(val):
            print(key)


def q15439():
    # 베라의 패션
    n = int(input())
    print(n ** 2 - n)


def q24723():
    # 녹색거탑
    n = int(input())
    print(2 ** n)


def q11050():
    # 이항 계수 1
    n, k = map(int, input().split())
    fact_n = 1
    fact_k = 1
    fact_kn = n - k
    if not fact_kn:
        fact_kn = 1
    for i in range(1, n + 1):
        fact_n *= i
    for i in range(1, k + 1):
        fact_k *= i
    for i in range(1, fact_kn + 1):
        fact_k *= i
    print(fact_n // fact_k)


def q1037():
    # 약수
    n = int(input())
    lst = list(map(int, input().split()))
    if n > 1:
        print(max(lst) * min(lst))
    else:
        print(lst[0] ** 2)


def q27433():
    # 팩토리얼 2
    n = int(input())

    def fact(a):
        if a <= 1:
            return 1
        else:
            return a * fact(a - 1)

    print(fact(n))


def q10870():
    # 피보나치 수 5
    n = int(input())

    def fibo(a):
        if a <= 0:
            return 0
        elif a == 1:
            return 1
        else:
            return fibo(a - 2) + fibo(a - 1)
    print(fibo(n))


def q25501():
    # 재귀의 귀재
    n = int(input())

    def recursion(s, l, r, c):
        c += 1
        if l >= r:
            return 1, c
        elif s[l] != s[r]:
            return 0, c
        else:
            return recursion(s, l + 1, r - 1, c)

    def is_palindrome(s, c):
        return recursion(s, 0, len(s) - 1, c)

    for _ in range(n):
        string = input()
        count = 0
        print(*is_palindrome(string, count))


def q2748():
    # 피보나치 수 2
    n = int(input())
    dp = [0] * 91
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]
    print(dp[n])


def q17202():
    # 핸드폰 번호 궁합
    a = list(map(int, input()))
    b = list(map(int, input()))
    dp = [[] for _ in range(16)]
    lst = []
    for i in range(8):
        lst.append(a.pop(0))
        lst.append(b.pop(0))
    for i in range(len(lst) - 1):
        dp[0].append((lst[i] + lst[i + 1]) % 10)
    for i in range(1, 16):
        for j in range(len(dp[i - 1]) - 1):
            dp[i].append((dp[i - 1][j] + dp[i - 1][j + 1]) % 10)
    print(''.join(map(str, dp[13])))


def q17608():
    # 막대기
    import sys

    n = int(sys.stdin.readline())
    lst = []
    count = 1
    for _ in range(n):
        lst.append(int(sys.stdin.readline()))
    lst.reverse()
    max_val = lst[0]
    for i in range(n):
        if lst[i] > max_val:
            max_val = lst[i]
            count += 1
    print(count)


def q2605():
    # 줄 세우기
    n = int(input())
    lst = list(map(int, input().split()))
    order = []
    for i in range(1, n + 1):
        order.insert(lst[i - 1], i)
    order.reverse()
    print(*order)


def q12605():
    # 단어순서 뒤집기
    n = int(input())
    words = []
    for _ in range(n):
        lst = list(map(str, input().split()))
        lst.reverse()
        words.append(lst)
    for i in range(n):
        print(f'Case #{i + 1}:', *words[i])


def q27160():
    # 할리갈리
    n = int(input())
    dic = {}
    for _ in range(n):
        fruit, ea = input().split()
        if fruit in dic.keys():
            dic[fruit] += int(ea)
        else:
            dic[fruit] = int(ea)
    print('YES' if 5 in dic.values() else 'NO')


def q11531():
    # ACM 대회 채점
    dic = {}
    while 1:
        lst = input().split()
        if int(lst[0]) == -1:
            break
        if lst[1] not in dic.keys():
            dic[lst[1]] = [False, 0]
        if lst[2] == 'right':
            dic[lst[1]][0] = True
            dic[lst[1]][1] += int(lst[0])
        else:
            dic[lst[1]][1] += 20
    solved = 0
    penalties = 0
    for _, item in dic.items():
        if item[0]:
            solved += 1
            penalties += item[1]
    print(solved, penalties)


def q29701():
    # 모스 부호
    n = int(input())
    lst = input().split()
    dic = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
        '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
        '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
        '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
        '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0',
        '--..--': ',', '.-.-.-': '.', '..--..': '?', '---...': ':', '-....-': '-', '.--.-.': '@'
    }
    for char in lst:
        print(dic[char], end='')


def q30034():
    # Slice String
    n = int(input())
    slice_char = input().split()
    m = int(input())
    slice_num = input().split()
    slices = slice_char + slice_num
    k = int(input())
    merge = input().split()
    for char in merge:
        while char in slices:
            slices.remove(char)
    s = int(input())
    string = input().split()
    for char in slices:
        index = 0
        while index < len(string):
            if char in string[index]:
                temp = list(string[index].split(char))
                string.pop(index)
                for i in range(len(temp)):
                    string.insert(index + i, temp[i])
            index += 1
    for char in string:
        if char:
            print(char)


def q15098():
    # No Duplicates
    lst = input().split()
    dic = {}
    is_dup = True
    while lst:
        current = lst.pop()
        if current in dic.keys():
            is_dup = False
            break
        else:
            dic[current] = 1
    print('yes' if is_dup else 'no')


def q25593():
    # 근무 지옥에 빠진 푸앙이 (Small)
    n = int(input())
    dic = {}
    lst = [4, 6, 4, 10]
    for _ in range(n):
        for time in lst:
            workers = input().split()
            for worker in workers:
                if worker != '-':
                    if worker in dic.keys():
                        dic[worker] += time
                    else:
                        dic[worker] = time
    if dic:
        print('Yes' if max(dic.values()) - min(dic.values()) <= 12 else 'No')
    else:
        print('Yes')


def q31562():
    # 전주 듣고 노래 맞히기
    n, m = map(int, input().split())
    music = {}
    for _ in range(n):
        lst = input().split()
        music[lst[1]] = lst[2:5]
    for _ in range(m):
        lst = input().split()
        count = 0
        result = ''
        for key, val in music.items():
            if val == lst:
                result = key
                count += 1
        if count > 1:
            print('?')
        elif count:
            print(result)
        else:
            print('!')


def q9933():
    # 민균이의 비밀번호
    n = int(input())
    dic = {}
    for _ in range(n):
        s = input()
        lst = list(s)
        lst.reverse()
        reverse = ''
        for char in lst:
            reverse += char
        dic[s] = reverse
    result = ''
    key, val = list(dic.keys()), list(dic.values())
    for i in range(n):
        if key[i] == val[i]:
            result = key[i]
            break
        for j in range(i, n):
            if key[i] == val[j]:
                result = key[i]
                break
    print(len(result), result[len(result) // 2])


def q1009():
    # 분산처리
    import sys

    t = int(sys.stdin.readline())
    for _ in range(t):
        a, b = map(int, sys.stdin.readline().split())
        a = a % 10

        if a == 0:
            print(10)
        elif a == 1 or a == 5 or a == 6:
            print(a)
        elif a == 4 or a == 9:
            b = b % 2
            if b == 1:
                print(a)
            else:
                print((a * a) % 10)
        else:
            b = b % 4
            if b == 0:
                print((a ** 4) % 10 % 10 % 10)
            else:
                print((a ** b) % 10 % 10 % 10)
q1009()