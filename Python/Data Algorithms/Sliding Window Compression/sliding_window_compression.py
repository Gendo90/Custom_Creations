def getStartIndex(window, curr_selection):
    poss_matches = []
    max_count = 0
    
    for i in range(len(window)):
        arr = [a for a in window][i:]
        j = 0
        count = 0
        # print(arr, curr_selection)
        while(count < min(len(arr), len(curr_selection)) and arr[j] == curr_selection[j]):
            # print(count, j)
            count += 1
            j += 1
            
        if(count > 0):
            poss_matches.append([i, count])
            max_count = max(max_count, count)  
            
        # print(poss_matches)
            
    if(max_count == 0):
        return None  
        
    while(len(poss_matches) > 0):
        val = poss_matches.pop(0)
        if(val[1] == max_count):
            return val


def solution(inputString, width):
    result = ""
    i = 0
    while (i < len(inputString)):
        if(i == 0):
            result += inputString[i]
            i += 1
            continue
            
        if(i < width):
            window = inputString[:i]
        else:
            window = inputString[i-width:i]
            
        if(width + i < len(inputString)):
            curr_selection = inputString[i:i + width]
        else:
            curr_selection = inputString[i:]
            
        curr_result = getStartIndex(window, curr_selection)
        # print(i, curr_result)
        if(curr_result == None):
            result += inputString[i]
            i += 1
        else:
            if(i > width):
                curr_result[0] += i - width
            result += "({},{})".format(curr_result[0], curr_result[1])
            i += curr_result[1]
            
        # print(result)
            
    return result
