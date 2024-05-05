import random
import time
import statistics

import moon_lists


def main():

    start_time = time.time()

    # pick which moon to gather data on based off of three character shorthands
    # (First three letters of the moon)
    moon = "art"
    print(moon)
    moon_to_use = moon_lists.pick_moon(moon)

    # move lists from moon_to_use into their own lists / better names
    moon_items = moon_to_use[0]
    moon_weights = moon_to_use[1]
    moon_scrapamounts = moon_to_use[2]
    moon_values = moon_to_use[3]

    # number of theoretical runs of scrap
    number_of_runs = 10000000

    # list of every individual run's scrap
    total_scrap = []

    # all scrap from total_scrap added together
    total_scrap_total = 0

    for i in range(number_of_runs):

        # stores the value of each individual piece of scrap from one run
        individual_scrap = []

        # takes the values from individual_scrap and adds them all together
        individual_scrap_total = 0

        # decides on all moon's scrap
        for i in range(random.randint(moon_scrapamounts[0], moon_scrapamounts[1])):

            # selects one of the moons possible scrap options using the weighted table
            choice = random.choices(moon_items, weights=moon_weights, k=1)

            # adds the value of the selected scrap item to the individual_scrap list
            individual_scrap.append(moon_values[choice[0]])

        # adds all scrap into one number
        for i in range(len(individual_scrap)):

            # adds the value of all items in individual_scrap together
            individual_scrap_total += individual_scrap[i]

        # adds each moons total scrap amount to total_scrap
        total_scrap.append(individual_scrap_total)

    # finds average and stdev for all scrap from every run
    total_scrap_total_average = statistics.mean(total_scrap)
    total_scrap_total_stdev = statistics.stdev(total_scrap)

    # print the average scrap
    print('Average scrap value: ' + str(total_scrap_total_average))
    print('Standard Deviation: ' + str(total_scrap_total_stdev))

    print('Computation time: ' + str(time.time() - start_time) + ' seconds')


if __name__ == "__main__":
    main()
