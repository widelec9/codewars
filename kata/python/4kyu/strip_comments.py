def solution(string, markers):
    string = string.split('\n')
    for i, line in enumerate(string):
        for m in markers:
            if m in string[i]:
                string[i] = string[i][:string[i].index(m)].rstrip()
    return '\n'.join(string)
