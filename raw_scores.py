raw_scores=[49,50,53,36,88,27,34]

def process_grades(scores):
    passing_list=[]
    passing_count=0

    for s in scores:
        if s>= 50:
            passing_list.append(s)
            passing_count +=1

    sorted_grades = sorted(passing_list) 
    return sorted_grades, passing_count

final_grades, final_count = process_grades(raw_scores)

print ("Processed Passing Grade:",final_grades)
print ("Total Student Passed:", final_count)