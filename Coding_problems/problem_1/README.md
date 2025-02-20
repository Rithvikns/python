# Clash of Clans Builder Assignment Simulation

## problem Statement 
I was playing clash of clans game and wanted to upgrade my town hall from 16 to 17 , but i want to first finish my archer tower and canon upgrade to level 21. So i wanted to calculate the least amount of time taken to upgrade all the neccessary upgrades required for the townhall 
## Overview
This Python script simulates a builder assignment and upgrade system similar to the one found in Clash of Clans. It helps determine the optimal way to assign builders, manage upgrade times, and estimate the minimum time required to max out all buildings to level 21.

## Features
- Assign builders to available buildings.
- Calculate upgrade time based on building levels.
- Manage free builders dynamically.
- Simulate the full upgrade process until all buildings reach level 21.
- Track total time taken for upgrades.

## Functions
### `upgrade_time(level)`
Calculates the time required to upgrade a building based on its current level.
- Below level 16: Each level reduces upgrade time by 2 hours.
- Level 16: Fixed 24 hours.
- Level 17: Fixed 48 hours.
- Level 18-20: Each level takes 12 hours more.
- Level 21: No further upgrades needed.

### `assign(no_of_builders, buildings, current_upgrades)`
Assigns builders to buildings that need upgrades.
- Selects buildings that are not at max level (21).
- Prioritizes buildings with lower levels.
- Updates the current upgrade list with new upgrade times.

### `free_builders(k, current_upgrades)`
Calculates the number of free builders available.
- Returns the number of builders that can still be assigned.
- Checks for incorrect builder input.

### `check_max_level(buildings)`
Checks if any buildings still require upgrades.
- Returns `True` if at least one building is below level 21.
- Returns `False` if all buildings have reached level 21.

### `current_construction(k, buildings, current_upgrade)`
Simulates a single round of construction.
- Assigns builders to available buildings.
- Finds the minimum upgrade time.
- Updates building levels and ongoing upgrade times.
- Prints the status of buildings after each upgrade cycle.

### `Building_progress(k, buildings, current_upgrade)`
Simulates the full upgrade process until all buildings reach level 21.
- Iterates through upgrade cycles.
- Tracks total time taken.
- Prints progress after each round.

## Usage
```python
# Define initial values
k = 4  # Number of builders
buildings = [19, 16, 16, 13, 17]  # Current levels of buildings
current_upgrade = [(1, 0), (2, 24), (3, 20), (4, 24), (5, 13)]  # Ongoing upgrades

# Run the simulation
print("Minimum completion time:", Building_progress(k, buildings, current_upgrade))
```

## Example Output
```
[19, 16, 16, 13, 17]
[(1, 0), (2, 24), (3, 20), (4, 24), (5, 13)]
after 13 hrs : The current buildings level [19, 16, 16, 13, 18]
time taken till now 0.5416666666666666
after 7 hrs : The current buildings level [19, 16, 17, 13, 18]
time taken till now 0.8333333333333334
after 4 hrs : The current buildings level [19, 17, 17, 14, 18]
time taken till now 1.0
after 20 hrs : The current buildings level [19, 17, 17, 15, 18]
time taken till now 1.8333333333333333
after 22 hrs : The current buildings level [19, 17, 17, 16, 18]
time taken till now 2.75
after 2 hrs : The current buildings level [19, 17, 18, 16, 18]
time taken till now 2.8333333333333335
after 4 hrs : The current buildings level [19, 18, 18, 16, 18]
time taken till now 3.0
after 1 hrs : The current buildings level [19, 18, 18, 16, 19]
time taken till now 3.0416666666666665
after 17 hrs : The current buildings level [19, 18, 18, 17, 19]
time taken till now 3.75
after 38 hrs : The current buildings level [19, 18, 19, 17, 19]
time taken till now 5.333333333333333
after 4 hrs : The current buildings level [19, 19, 19, 17, 19]
time taken till now 5.5
after 6 hrs : The current buildings level [19, 19, 19, 18, 19]
time taken till now 5.75
after 7 hrs : The current buildings level [20, 19, 19, 18, 19]
time taken till now 6.041666666666667
after 53 hrs : The current buildings level [20, 19, 19, 19, 19]
time taken till now 8.25
after 2 hrs : The current buildings level [20, 19, 20, 19, 19]
time taken till now 8.333333333333334
after 4 hrs : The current buildings level [20, 20, 20, 19, 19]
time taken till now 8.5
after 13 hrs : The current buildings level [20, 20, 20, 19, 20]
time taken till now 9.041666666666666
after 53 hrs : The current buildings level [20, 20, 20, 20, 20]
time taken till now 11.25
after 14 hrs : The current buildings level [21, 20, 20, 20, 20]
time taken till now 11.833333333333334
after 4 hrs : The current buildings level [21, 21, 20, 20, 20]
time taken till now 12.0
after 13 hrs : The current buildings level [21, 21, 21, 20, 20]
time taken till now 12.541666666666666
after 53 hrs : The current buildings level [21, 21, 21, 21, 20]
time taken till now 14.75
after 14 hrs : The current buildings level [21, 21, 21, 21, 21]
time taken till now 15.333333333333334
Minimum completion time: 15.333333333333334

```

## Conclusion
This script efficiently assigns builders and manages upgrade progression in a simulated Clash of Clans environment. It ensures the fastest possible upgrade completion time based on given constraints.
