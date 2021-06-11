# write your code here
with open('salary.txt') as f_month, open('salary_year.txt', 'w') as f_year:
    salaries = f_month.readlines()
    for salary in salaries:
        f_year.write(str(int(salary.strip('\n')) * 12) + '\n')
