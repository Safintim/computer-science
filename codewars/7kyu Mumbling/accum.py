def accum(s):
    
    def repeat_and_capitalize_char(ch, i):
        return (ch * i).capitalize()
    
    strings = (repeat_and_capitalize_char(ch, i)
               for i, ch in enumerate(s.lower(), start=1))
    
    return '-'.join(strings)