for tc in range(1,int(input())+1):
    a,b=map(int,input().split())
    if a>b:
        print("#"+str(tc)+" >")
    elif a<b:
        print("#"+str(tc)+" <")
    else:
        print("#"+str(tc)+" =")