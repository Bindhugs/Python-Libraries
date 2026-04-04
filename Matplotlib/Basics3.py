import matplotlib.pyplot as plt
import numpy as np

#SCATTER GRAPHS

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 7, 8]) #Hours
y = np.array([50, 60, 65, 62, 70, 75, 78, 82, 85, 87]) #Grades

x1 = np.array([0,1,2,2,3,4,5,6,7,8,8])
y1 = np.array([50,58,65,70,72,78,83,88,92,95,97])

plt.scatter(x, y,
            color = 'thistle',
            alpha = 0.5,
            s = 200,
            edgecolor = 'black',
            label = 'Class A'
            ) #This is for first scatter graph # alpha is for transparency and s is for size
plt.scatter(x1, y1,
            color = 'yellow',
            alpha = 0.5,
            s = 200,
            edgecolor = 'black',
            label = 'Class B'
            ) #This is for second scatter grph
plt.title("Test Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Grade")
plt.legend() 
plt.show()


#HISTOGRAMS

scores = np.random.normal(loc = 80, scale = 10, size = 100) 
scores = np.clip(scores, 0, 100) 
plt.hist(scores, bins = 10,
         color ="#4ab9d8",
         edgecolor = 'black') 
plt.xlabel("Scores")
plt.ylabel("Number of students")
plt.title("Exam scores")

plt.show()


#Subplots

x = np.array([1, 2, 3, 4, 5])

figure, axes = plt.subplots(2, 2)

axes[0, 0].bar(x, x*2,
                color = 'red')
axes[0, 0].set_title('x*2')

axes[0, 1].plot(x, x**2,
                color = 'blue')
axes[0, 1].set_title('x**2')

axes[1, 0].barh(x, x**3, 
                color = 'orange')
axes[1,0].set_title('x**3')

axes[1, 1].plot(x, x**4,
                color = 'yellow')
axes[1, 1].set_title('x**4')

plt.tight_layout() 
plt.show()