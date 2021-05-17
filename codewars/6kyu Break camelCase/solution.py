def solution(string):
    return ''.join(f' {ch}' if ch.isupper() else ch for ch in string)