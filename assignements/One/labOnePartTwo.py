def lab_two_part_two(text, letter):
    result = []
    for idx, char in enumerate(text):
        if char == letter:
            result.append(idx) 
    return result