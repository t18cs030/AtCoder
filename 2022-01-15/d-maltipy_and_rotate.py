"""def division(x,y):
    return x/y
def queue(x):
    return int(str(x)[1:]+str(x)[0])
def rotate(x,a):
    for _ in range(len(str(x))):
        x = queue(x)
        if x%a == 0:
            return int(x)
        else:
            x = queue(x)
    return 0

a,N = list(map(int,input().split()))
def saiki(num):
    print(num)
    if num == 1:
        return True
    if num%a == 0:
        if(saiki(int(num/a))):
            return True
    if rotate(num,a) != 0:
        return saiki(rotate(num,a))
    #print("rotate true")
    #print(r)
    return False
   
    
        



    

print(saiki(N))
"""
# 本問題を再帰処理で解こうとすると大変。
# queue を用いることで再起処理を省略, 
# また, 一度見たものを記録することで無限ループを防ぐ
from collections import deque # 両端からの要素の追加・削除を高速に行う


dq=deque([])
a,sN = input().split()
a=int(a)
seen={sN} #一度見たものを記録

dq.append((0,sN))
while dq: #キューが空になったら終了
    cost,now = dq.popleft()
    # 1 なら現在のコストを出力して終了
    if now == '1':
        print(cost)
        exit()
    # それ以外なら次の候補をキューに追加
    tmp = int(now)
    next = str(tmp//a)
    # 割り切れる && 一度も見たことがない数字ならキューに追加
    if tmp%a == 0 and next not in seen:
        dq.append((cost+1,next))
        seen.add(next)
    # 二桁以上ある数字 && 変更後の先頭が0にならない数字なら入れ替える
    if len(now)>1 and now[1] != '0':
        n = now[1:]+now[0]
        if n not in seen:
            seen.add(n)
            dq.append((cost+1,n))
print(-1)