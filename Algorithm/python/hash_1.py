
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

print(participant[-1])

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)) :
        if participant[i] != completion[i] :
            return participant[i]

    return participant[-1]


#print(solution(participant, completion))

















        
    