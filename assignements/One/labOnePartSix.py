def lab_one_part_six(number):
    number=input("enter * number:")
    number=int(number)
    i=1
    while i <= number:
        space= number -i 
        return(" " * space + "*" * i)
        i+=1
       
