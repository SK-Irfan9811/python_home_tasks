def check_positions(original,created):
    return len(set(original)-set(created))

def solution(buckets):
    # Implement your solution here
    b_count=buckets.count("B")
    e_count=buckets.count(".")
    indexes=[idx for idx,ele in enumerate(buckets) if ele=='B']
    min_num=min(indexes)
    max_num=max(indexes)
    min_positions=10
    while True:
        lst=[min_num+i for i in range(0,b_count*2,2)]
        if(max(lst)>10):
            break
        min_num+=1

        if(check_positions(indexes,lst)<min_positions):
            min_positions=check_positions(indexes,lst)
    print(min_positions)

solution("..B....B.BB")
solution("BB.B.BBB...")
solution(".BBB.B")
solution("......B.B")
