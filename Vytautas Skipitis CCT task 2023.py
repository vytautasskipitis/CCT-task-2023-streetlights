import matplotlib.pyplot as plt

print('task nr1. (find the darkest lamp in the street) : ')

# calculates how much light we get from the neighboring flashlight
def illumination_intensity(distance):
    return 3 ** (-(distance / 100) ** 2)


# # creates a list with the final flashlight strengths and return darkest streetlight index
def find_index_of_darkest_street_light(road_length: int, not_working_street_lights: list[int]) -> int:
    list_of_lights_on = []
    for i in range(road_length // 20 + 1):

        # creates a list in which 1 means that the lamp is on, and 0 is off
        if i not in not_working_street_lights:
            list_of_lights_on.append(1)
        else:
            list_of_lights_on.append(0)

    list_of_lights_strengths = []
    final_light_intensity = 0

    # for each street light, it finds the distances to the neighboring lightning
    for i in range(len(list_of_lights_on)):
        for number in range(len(list_of_lights_on)):
            # finds distances
            distance = number - i
            # (>0.01 -> ignore (10 neighboring flashlight is suitable))
            if abs(distance) < 11:
                # let's convert the distance to meters
                distance = abs(distance * 20)
                # "if the neighboring lamp is lit, then we add its light, and if it's not lit, then we let it pass."
                if list_of_lights_on[number] == 1:
                    final_light_intensity += illumination_intensity(distance)

        # Create a list containing the final intensities of the lamps
        list_of_lights_strengths.append(final_light_intensity)
        final_light_intensity = 0

    # visual diagrams of road lighting levels
    # hide this code if you don't want to see the diagrams
    ###
    plt.plot(list_of_lights_strengths)
    plt.xlabel('street lighting index')
    plt.ylabel('lighting intensity')
    plt.title('lighting of the entire street')
    plt.grid(True)
    plt.show()
    ###

    # Returns the index of the darkest lamp
    return list_of_lights_strengths.index(min(list_of_lights_strengths))


if __name__ == "__main__":
    # to check which lamp receives the least amount of light:
    assert find_index_of_darkest_street_light(road_length=200, not_working_street_lights=[8, 9, 10]) == 10
    assert find_index_of_darkest_street_light(road_length=100, not_working_street_lights=[3, 4, 5]) == 5
    assert find_index_of_darkest_street_light(road_length=1000, not_working_street_lights=[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 14
    print("ALL TESTS PASSED")

###############################################################################################################
print('task nr2. (optimal number of working lights according to the given road length) : ')
print('*note. Function "optimal amount_of_light" calculates the minimum amount of flashlights to get the light of each '
      'street light at least 1.0, but places them not accurately enough. Excess light is accumulated at the end of the road.')
###############################################################################################################

def optimal_amount_of_light(road_length: int):
    list_of_street_lights = []
    for i in range(road_length // 20 + 1):
        list_of_street_lights.append(0)

    # if the road is shorter than 80m is calculated separately
    if len(list_of_street_lights) < 4:
        list_of_street_lights[0] = 1
        list_of_street_lights[-1] = 1
        print('lights that need to be switched on are indicated by 1: ', list_of_street_lights)
        return 2

    # 80m+ calculation
    if len(list_of_street_lights) >= 4:
        list_of_street_lights[1] = 1
        list_of_street_lights[-2] = 1

    list_of_non_working_street_lights = []
    count = 0
    how_much_to_turn_on = 0
    # create a list indicating which street lights to turn on
    for i in range(len(list_of_street_lights)):
        if list_of_street_lights[i] == 0:
            count += 1
            list_of_non_working_street_lights.append(i)
        if list_of_street_lights[i] == 1:
            if count >= 7:
                how_much_to_turn_on = count // 6
            count = 0
    for i in range(1, len(list_of_street_lights) - 2, 7):
        list_of_street_lights[i] = 1

    # visual diagrams of road lighting levels
    # hide this code if you don't want to see the diagrams:
###############################################################################################################
    list_of_lights_strengths = []
    final_light_intensity = 0

    # for each street light, it finds the distances to the neighboring lightning
    for i in range(len(list_of_street_lights)):
        for number in range(len(list_of_street_lights)):
            # finds distances
            distance = number - i
            # (>0.01 -> ignore (10 neighboring flashlight is suitable))
            if abs(distance) < 11:
                # let's convert the distance to meters
                distance = abs(distance * 20)
                # "if the neighboring lamp is lit, then we add its light, and if it's not lit, then we let it pass."
                if list_of_street_lights[number] == 1:
                    final_light_intensity += illumination_intensity(distance)

        # Create a list containing the final intensities of the lamps
        list_of_lights_strengths.append(final_light_intensity)
        final_light_intensity = 0

    plt.plot(list_of_lights_strengths)
    plt.xlabel('street lighting index')
    plt.ylabel('lighting intensity')
    plt.title('(OPTIMAL) lighting of the entire street')
    plt.grid(True)
    plt.show()
###############################################################################################################

    # the list with working and non-working lights turns into a list with indexes that indicate which lamp should be turned on
    count = 0
    for i in list_of_street_lights:
        if i == 1:
            count += 1
    whitch_lights_to_turn_on = []
    for index, reiksme in enumerate(list_of_street_lights):
        if reiksme == 1:
            whitch_lights_to_turn_on.append(index)
    print('print('index of street lights that need to be turned on : ', whitch_lights_to_turn_on)', whitch_lights_to_turn_on)

    how_much_to_turn_on = count
    return how_much_to_turn_on


if __name__ == "__main__":
    # the test checks how many flashlights will be needed for the given road length, so that the minimum illumination level is more than 1.0:
    assert optimal_amount_of_light(road_length=20) == 2
    assert optimal_amount_of_light(road_length=40) == 2
    assert optimal_amount_of_light(road_length=60) == 2
    assert optimal_amount_of_light(road_length=180) == 2
    assert optimal_amount_of_light(road_length=200) == 3
    assert optimal_amount_of_light(road_length=5000) == 37
    print("ALL TESTS PASSED")
























