# importing the required libraries
import matplotlib.pyplot as plt
import numpy as np
import random
import math

def create_random_data(x_range: int, slope: int) -> dict:
    offset = random.randrange(1, 15)
    x = np.arange(0, x_range)
    feature_points = []

    for i in x:
        variance = random.randrange(1, 50)
        feature_val = i * slope
        start_range = 0

        # Replicated values cannot be negative
        if feature_val - variance >= 0:
            start_range = feature_val - variance
        
        feature_y = random.uniform(start_range, feature_val + variance)
        feature_points.append(feature_y)
    return {
        "x": x,
        "y": np.array(feature_points) + offset
    }
    

def calculate_loss(points, slope, offset) -> float:
    return np.sum(np.square(np.subtract(points, np.arange(len(points)) * slope + offset))) / len(points)


def find_minimum_loss(learning_rate: int, points: list, actual_slope: int):
    x_list = np.arange(len(points))
    slope = 0
    loss_1 = calculate_loss(points, slope, points[0])
    print("Itintial loss: " + str(loss_1))
    min = loss_1
    minimum_found = False
    i = 0
    avg_y_intercept = find_avg_y_intercept(points)
    avg_slope = find_avg_slope(points)
    print("Average intercept: " + str(avg_y_intercept))
    print("Average slope: " + str(avg_slope))

    plt.plot(x_list, x_list * avg_slope + avg_y_intercept, color='blue')
    actual_line = np.arange(len(points)) * avg_slope + avg_y_intercept
    
    while not minimum_found:
        slope += (math.sqrt(loss_1) * learning_rate) / 2
        print("slope: " + str(slope))
        loss_2 = calculate_loss(points, slope, points[0])
        if loss_2 > loss_1:
            learning_rate = learning_rate * -1
        elif loss_2 == loss_1:
            minimum_found = True
            min = loss_2
            plt.plot(np.arange(len(points) + 1), np.arange(len(points) + 1) * slope + points[0], color='red')
        else:
            loss_1 = loss_2
        min = loss_2 if loss_2 < min else min
        i += 1
    print("\nfinal slope: " + str(slope) + "\nActual slope: " + str(avg_slope))
    print("\nLoss of slope: " + str(min) + "\nLoss of actual slope " + str(calculate_loss(points, avg_slope, avg_y_intercept)))
    print("\n\nIterations: " + str(i))

def find_avg_slope(points: list) -> float:
    slope_list = []
    for y in range(len(points) -1):
        slope_list.append(points[y+1] - points[y])
    
    return np.mean(slope_list)

def find_avg_y_intercept(points: list) -> float:
    intercept_list = []
    for x in range(len(points) -1):
        slope = points[x+1] - points[x]
        intercept_list.append(points[x] - ((x+1) * slope))
    
    return np.mean(intercept_list)

def plot_loss_parabola(range: int, points: list, increment: float):
    x_values = np.arange(range)
    y_values = []
    slope = 0
    y_intercept = points[0]
    for i in x_values:
        y_values.append(calculate_loss(points, slope, y_intercept))
        slope += increment
    
    plt.plot(x_values, y_values)

def find_standard_form(points: list) -> dict:
    c = points[0]
    


slope = 5
points = create_random_data(20, slope)
# plt.plot(points["x"], points["y"], color='green')

plot_loss_parabola(50, points["y"], 0.3)



plt.show()  # display