# marks = [45, 78, 86, 77]
# percentage = (sum(marks)/400 )*100
# print(percentage)
def percent(marks):
    return((marks[0] + marks[1] + marks[2] + marks[3])/400)*100
marks1 = [45, 78, 86, 77]
percentage1 = percent(marks1)
print(percentage1)