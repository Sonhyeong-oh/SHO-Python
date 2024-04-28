# 백준 1302번 : 배스트셀러 (실버 IV) original model

from sys import stdin

input = stdin.readline

N = int(input().rstrip())

books = dict()
for _ in range(N):
    name = input().rstrip()
    if name in books:
        books[name] += 1
        # 딕셔너리에 이미 추가된 책이면 밸류 + 1
    else:
        books[name] = 1
        # 딕셔너리에 추가되지 않은 책이면 딕셔너리에 추가

best = max(books.values())
# 최고 판매 수량
best_seller = []
books = sorted(books.items(), key = lambda x: x[1], reverse = True)
# 딕셔너리의 요소들을 책의 수 기준으로 내림차순 정렬
# (book name, number) -> number 기준

for i in books:
    if i[1] == best:
        best_seller.append(i)
        # 책이 최고 판매 수량만큼 판매 되었다면 베스트 셀러에 추가
best_seller = sorted(best_seller)
# 베스트셀러를 이름(오름차순) 기준으로 정렬
print(best_seller[0][0])