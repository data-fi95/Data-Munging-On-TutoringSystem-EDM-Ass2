# no of seconds per user
import pandas as ps

file=open('Andes-2009-csv.csv','r') # Open the log file (Andes log file)

# Create 2 empty arrays to store end-time and student id's

stu_id=[]
end_time=[]
for line in file:
    wrd=line.split(',')

    if wrd[1][11:18]=="student":       # Append into student id array all student id's
        stu_id.append(wrd[1][26:34])


files1=open('Andes-2009-csv.csv','r')
for passage in files1:
    pasd=passage.split(',')
    if pasd[1][0:7]=="END-LOG":
        a=pasd[0]
        b=a.split(':')
        c=int(b[0])
        d=int(b[1])
        e=(c*60)+d
        end_time.append(e)              # Append into end time array the no of seconds for that session

stu_id.append("b")

result=list(zip(stu_id,end_time))     # Create a data structure which has one column as student id and other as end time.

df=ps.DataFrame(result)

sum1=df.groupby([0])[1].sum()         # Add the end time (in seconds) grouping by student id's
print(sum1)
sum1.to_csv("C:/Users/harik/Documents/fall.csv")  # Store the output in csv format on local system to visualize in RStudio.

