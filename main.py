import pandas
from prettytable import PrettyTable
import statistics


def main():
    form_responses = pandas.read_csv("data.csv")

    last_numbers = form_responses['Last digit of your phone number (type numerics only)'].tolist(
    )
    heights = form_responses["Height (in cm only, include decimals. Do not type 'cm'. Just the number please)"].tolist(
    )
    last_numbers = list(map(int, last_numbers))
    heights = list(map(float, heights))
    # Discrete Distribution of Phone Number
    discrete_distribution = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for number in last_numbers:
        discrete_distribution[number] += 1
    sum_of_last_numbers = sum(discrete_distribution)
    discrete_distribution = list(
        map(lambda x: x/sum_of_last_numbers, discrete_distribution))

    discrete_table = PrettyTable()
    discrete_table.field_names = ['x'] + list(range(0, 10))
    discrete_table.add_row(
        ["p(x)"] + list(map(lambda x: "{:.4f}".format(x), discrete_distribution)))
    print("Here is the discrete distribution of the last digit of phone numbers: ")
    print(discrete_table)

    discrete_distribution_mean = sum(last_numbers)/len(last_numbers)
    discrete_distribution_variance = statistics.variance(last_numbers)

    print("The mean is: ", discrete_distribution_mean)
    print("The Variance is: ", discrete_distribution_variance)
    print("The Standard Deviation is: ", discrete_distribution_variance**0.5)

    # Continuous Distribution Of Heights
    cont_distribution_mean = sum(heights)/len(heights)
    cont_distribution_variance = statistics.variance(heights)
    print("\n\nData for continuous distribution of heights: ")
    print("The mean is: ", cont_distribution_mean)
    print("The Variance is: ", cont_distribution_variance)
    print("The Standard Deviation is: ", cont_distribution_variance**0.5)
    show_heights = 'no'

    show_heights = input("Do you want to show height data? (yes/no) ")
    if show_heights == "yes":
        print("Heights: ", heights)


if __name__ == "__main__":
    main()
