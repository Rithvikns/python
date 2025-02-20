
def upgrade_time(level):
    if level < 16:
        return max(0, 24 - ((16 - level)*2))  # Below 16, each level reduces by 2 hours
    elif level == 16:
        return 24
    elif level == 17:
        return 48
    elif level >= 21:
        return 0
    else:
        return 48 + (level - 17) * 12  # Above 16, each level takes 12 hours more

def assign( no_of_builders ,buildings, current_upgrades):
    if no_of_builders == 0:
        return current_upgrades
    else:
        selected_building = []
        result = [x for x, y in current_upgrades if y == 0]
        for k in result:
            if buildings[k-1] == 21:
                continue
            else:
                selected_building.append((buildings[k-1] , k))
        selected_building.sort(key = lambda x :x[0])
        selected_building = selected_building[0:no_of_builders]
        output = []
        for i ,k in selected_building:
            output.append((k,upgrade_time(i)))
        replacement_dict = {x: y for x, y in output}
        updated_current_upgrade = [(x, replacement_dict[x]) if x in replacement_dict else (x, y) for x, y in current_upgrades]

        return updated_current_upgrade

def free_builders(k , current_upgrades):
    zero_count = sum(1 for pair in current_upgrades if 0 in pair)
    no_of_builders = len(current_upgrades) - zero_count
    if  no_of_builders == k :
        return 0
    elif  no_of_builders  < k :
        return k - no_of_builders 
    else:
        print(" Number of builders provided is wrong")
        KeyError 

def check_max_level(buildings):
    for i in range(len(buildings)):
        if buildings[i] != 21:
            return True
    return False

def current_construction(k , buildings , current_upgrade):
    free_build = free_builders(k,current_upgrade)
    current_upgrade = assign(free_build, buildings,current_upgrade)
        
    min_value = min([t for t in current_upgrade if t[1] != 0], key=lambda x: x[1])
    curr_upgrade_time = min_value[1]
                    
    for i in range(len(current_upgrade)):
        if current_upgrade[i][1] == 0:
            continue
        else:
            if current_upgrade[i][1] - curr_upgrade_time == 0:
                buildings[i] +=1
            current_upgrade[i] = (current_upgrade[i][0], current_upgrade[i][1] - curr_upgrade_time)
    print(f"after { curr_upgrade_time} hrs : The current buildings level {buildings}")
    return buildings , current_upgrade , curr_upgrade_time


def Building_progress( k ,buildings , current_upgrade):
    total_time = 0
    while check_max_level(buildings):
        buildings , current_upgrade , time_required = current_construction(k , buildings , current_upgrade)
        total_time += time_required
        print("time taken till now",total_time/24)


    return total_time/24
    
    print(current_upgrade)
    print(buildings)
             


# Example usage
k = 4
buildings = [19, 16, 16, 13,17]  # Current levels, all targeting level 21
current_upgrade = [(1,0),(2,24),(3,20),(4,24),(5,13)]
print(buildings)
print(current_upgrade)
print("Minimum completion time:", Building_progress(k , buildings , current_upgrade))
