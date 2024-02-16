'''
Calculate the total distance of the drive.
Convert time in hours to time in minutes.
Calculate one-quarter of distance to find distance traveled.
Calculate time already traveled in minutes.
Calculate distance and time left to travel.
Calculate miles per hour needed to travel distance left with time remaining.

'''
# Collect user input for speed and time
speed = int(input('Enter your usual speed in miles per hour: '))
time = float(input('Enter how many hours the drive would usually take: '))

# Calculate total distance of the drive
total_distance = int(speed * time)

# Convert time in hours to time in minutes
time_minutes = time * 60

# Calculate distance traveled and time traveled
distance_traveled = total_distance / 4
time_traveled = (distance_traveled / speed * 60) + 20

# Calculate distance and time left to travel
distance_left = total_distance - distance_traveled
time_left = time_minutes - time_traveled

# Calculate speed needed to cover remaining distance with time remaining
new_speed = distance_left / time_left * 60


print(f'You would have to drive at {
      new_speed:.2f} miles per hour for the remaining distance.')
