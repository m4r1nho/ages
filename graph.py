import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def create_graph(people):
    # Extract ages from people
    ages = [x.age for x in people]

    # Sort ages in ascending order
    ages = sorted(ages)

    # Initialize an empty list to store counts
    age_count = []

    # Iterate through the sorted ages and count the occurrences of each age
    current_age = ages[0]
    count = 1

    for age in ages[1:]:
        if age == current_age:
            count += 1
        else:
            age_count.append((current_age, count))
            current_age = age
            count = 1

    # Add the last count to the list
    age_count.append((current_age, count))

    # Prepare data for the chart
    age_labels = [str(age) for age, _ in age_count]  # Convert ages to strings

    counts = [count for _, count in age_count]

    # Create a bar chart with the sorted ages
    fig, ax = plt.subplots()
    ax.bar(age_labels, counts)

    # Set the Y-axis to display only integer values
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    # Add labels to the axes
    plt.xlabel("Age")
    plt.ylabel("Number of People")

    # Add a title to the chart
    plt.title("Number of People by Age")

    # Show the chart
    plt.show()

