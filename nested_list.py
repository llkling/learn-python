#solution for https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    student_list=dict()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_list[name]=score
score_list=set(student_list.values())
score_list.remove(min(score_list))
result_list=[name for name,score in student_list.items() if score == min(score_list)]
for name in sorted(result_list):
    print(name)

