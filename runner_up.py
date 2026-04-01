#solution for #https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
list1=list(arr)
first=max(set(list1))
runner_up=set(list1)-{first}
print(max(runner_up))