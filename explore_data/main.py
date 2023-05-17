import numpy as np
import pandas as pd


def calculateMean(data: int) -> float:
    amount = len(data)
    sum = 0
    for grade in data:
        sum += grade
    
    return sum / amount

def repeat(word, repeat_word) -> str:
 
    # if number of characters greater than length of word.
    # set number of characters = length of word
    m = len(word)

    result = ""
 
    for i in range(m):
        result = result+repeat_word
    return result

data = [50,50,47,97,49,3,53,42,26,74,82,62,37,15,70,27,36,35,48,52,63,64]

grades = np.array(data)

print("Grades manual mean: " + '{0:.2f}'.format(calculateMean(data)))
print("Grades NumPy mean: " + '{0:.2f}'.format(grades.mean()))

# Define an array of study hours
study_hours = [10.0,11.5,9.0,16.0,9.25,1.0,11.5,9.0,8.5,14.5,15.5,
               13.75,9.0,8.0,15.5,8.0,9.0,6.0,10.0,12.0,12.5,12.0]

# Create a 2D array (an array of arrays)
student_data = np.array([study_hours, grades])

# display the array
print("\n" + str(student_data))
print(student_data[1][0])

avg_study = student_data[0].mean()
avg_grade = student_data[1].mean()

print("\n" + 'Average study hours: {0:.2f} \nAverage grade: {1:.2f}'.format(avg_study, avg_grade))

panda_message = 'PANDA TIME!'
print("\n\n{0}\n{1}\n{0}\n".format(repeat(panda_message, "-"), panda_message))

df_students = pd.DataFrame({'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic', 'Jimmie', 
                                     'Rhonda', 'Giovanni', 'Francesca', 'Rajab', 'Naiyana', 'Kian', 'Jenny',
                                     'Jakeem','Helena','Ismat','Anila','Skye','Daniel','Aisha'],
                            'StudyHours':student_data[0],
                            'Grade':student_data[1]})

passes = pd.Series(df_students['Grade'] >= 60)
df_students = df_students.sort_values('Grade', ascending=False)

print(df_students)

