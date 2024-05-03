# 백준 2512번 : 예산 (실버 II) original model

from sys import stdin, stdout

input = stdin.readline
print = stdout.write

# 요청한 에산의 합이 총예산보다 작다면 최댓값 출력
# 총예산보다 크다면 매개 변수 탐색으로 상한액 탐색

gov = int(input().rstrip())
# 지자체 개수
require = list(map(int, input().split()))
# 지자체 요청 예산 리스트
total = int(input().rstrip())
# 총예산

if sum(require) > total:
    start = 0
    end = max(require)
    while start <= end:
        sigma = 0
        # 상한 설정 후의 총합
        mid = (start + end) // 2
        for i in require:
            if i > mid:
                # 지자체 요청 예산이 상한액보다 크다면
                sigma += mid
                # 상한액으로 처리
            else:
                sigma += i
                # 지자체 요청 예산이 상한액보다 작다면 그대로
        if sigma > total:
            end = mid - 1
        else:
            result = mid
            # 상한 설정 후 총합이 총예산보다 작다면 그 값을 저장 후 다시 이분 탐색
            # 이분 탐색이 끝나면 상한액의 최솟값이 result
            start = mid + 1

    print('{0}'.format(result))
    # 상한액 = 최댓값
else:
    print('{0}'.format(max(require)))