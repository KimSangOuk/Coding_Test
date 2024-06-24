from collections import deque

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def bfs(rectangle,visited,cX,cY):
    global result

    q=deque()
    q.append((cX,cY))
    visited[cX][cY]=0

    while q:
        now=q.popleft()
        for i in range(4):
            nx=now[0]+dx[i]
            ny=now[1]+dy[i]
            # 영역을 벗어나는지
            if nx<1 or ny<1 or nx>50 or ny>50:
                continue
            if visited[nx][ny]!=-1:
                continue
            inside=False
            for left_down_x,left_down_y,right_up_x,right_up_y in rectangle:
                if left_down_x<nx<right_up_x and left_down_y<ny<right_up_y:
                    inside=True
                    break
                if left_down_y<ny<right_up_y and now[1]==ny and ((left_down_x==nx and right_up_x==now[0]) or (left_down_x==now[0] and right_up_x==nx)) and abs(left_down_x-right_up_x)==1:
                    inside=True
                    break
                if left_down_x<nx<right_up_x and now[0]==nx and ((left_down_y==ny and right_up_y==now[1]) or (left_down_y==now[1] and right_up_y==ny)) and abs(left_down_y-right_up_y)==1:
                    inside=True
                    break


            # 다른 사각형 안으로 향하는지
            if inside:
                continue
            # 영역 벗어나지 않고, 다른 사각형 안으로 향하지 않으면서 다른 사각형의 선 위에 있으면 됨, 대신 현재 있는 사각형이랑 같은 사각형 이어야 함
            now_on_rect=set()
            for left_down_x,left_down_y,right_up_x,right_up_y in rectangle:
                if (left_down_x==now[0] or right_up_x==now[0]) and left_down_y<=now[1]<=right_up_y:
                    now_on_rect.add((left_down_x,left_down_y,right_up_x,right_up_y))
                if (left_down_y==now[1] or right_up_y==now[1]) and (left_down_x<=now[0]<=right_up_x):
                    now_on_rect.add((left_down_x,left_down_y,right_up_x,right_up_y))
            on_line=False
            for left_down_x,left_down_y,right_up_x,right_up_y in list(now_on_rect):
                if (left_down_x==nx or right_up_x==nx) and left_down_y<=ny<=right_up_y:
                    on_line=True
                    break
                if (left_down_y==ny or right_up_y==ny) and (left_down_x<=nx<=right_up_x):
                    on_line=True
                    break
            if on_line:
                visited[nx][ny]=visited[now[0]][now[1]]+1
                q.append((nx,ny))


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    visited=[[-1]*51 for _ in range(51)]
    bfs(rectangle,visited,characterX,characterY)
    answer=visited[itemX][itemY]
    return answer