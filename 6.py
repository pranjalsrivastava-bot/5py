import matplotlib.pyplot as plt

# defining labels
activities = ['eat', 'play', 'study', 'hobbies']

# portion covered by each label
slices = [3, 7, 5, 9]

#color for each label
colors = ['aqua', 'maroon', 'teal', 'blue']

#plotting the pie chart
plt.pie(slices, labels = activities, colors=colors, startangle=30, shadow= False, explode = (0, 0, 0, 0), radius = 2.3, autopct = '%9.9f%%')

# plotting legend
plt.legend()

# showing the plot
plt.show()