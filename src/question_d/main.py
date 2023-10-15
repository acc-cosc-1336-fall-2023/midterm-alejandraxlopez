#add import
import question_d

def d_local_variable():
    num = 100
    question_d.use_local_variable(num)
    print (num)
# 10 should display
d_local_variable()