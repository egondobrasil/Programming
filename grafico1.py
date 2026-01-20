#pip install matplotlib numpy plotext
import matplotlib.pyplot as plt
import numpy as np
import plotext as pt

x = ['PHP', 'Python', 'JavaScript', 'Banco de Dados']
y = [50, 80, 30, 40]
mylabels = ["PHP", "Python", "JavaScript", "Banco de Dados"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]
ax = plt.gca()  
ax.set_facecolor("gray")
#plt.bar(x, y, color=['navy', 'green', 'rebeccapurple', 'red'])
plt.title('Quantidade de Alunos')
plt.xlabel('Cursos')
plt.ylabel('Alunos')
plt.pie(y, labels = mylabels,colors = mycolors)
plt.show()