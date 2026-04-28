def solution(letter):
    answer = ''
    morse = [
        ".-","-...","-.-.","-..",".","..-.","--.","....",
        "..",".---","-.-",".-..","--","-.","---",".--.",
        "--.-",".-.","...","-","..-","...-",".--","-..-",
        "-.--","--.."
    ]
    
    result = letter.split()
    
    for i in range(0, len(result), 1):
        for j in range(0, len(morse), 1):
            if morse[j] == result[i]:
                answer += chr(j+97)
    
    return answer