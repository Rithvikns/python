def can_complete_circuit(gas, cost, start=0, tank=0, visited=0):
    if visited == len(gas):  # Base case: If we visited all stations
        return start  # Successful journey
    
    n = len(gas)
    curr_station = (start + visited) % n  # Ensure circular indexing
    tank += gas[curr_station] - cost[curr_station]  # Update gas tank
    
    if tank < 0:  # If gas runs out, journey fails from this start point
        return -1
    
    return can_complete_circuit(gas, cost, start, tank, visited + 1)  # Move to the next station

def find_starting_station(gas, cost):
    for i in range(len(gas)):
        if can_complete_circuit(gas, cost, i) != -1:  # Try each station as a start
            return i
    return -1  # No valid start found

# Example Usage
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(find_starting_station(gas, cost))  # Output: 3
