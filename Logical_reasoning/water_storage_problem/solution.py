def water_stored(buildings_list):
  left_pointer , right_pointer , left_max_building , right_max_building , water_storage = 0 , len(building_list) , 0 , 0 , 0
  while left_pointer <= right_pointer:
    if building_list[left_pointer] < building_list[right_pointer]:
      if left_max_building < building_list[left_pointer]:
        left_max_building = building_list[left_pointer]
      else:
        water_storage += left_max-building - building_list[left_pointer]
      left += 1
    else:
      if right_max_building < building_list[right_pointer]:
        right_max_building = building_list[right_pointer]
      else:
        water_storage += right_max-building - building_list[right_pointer]
        right -= 1
  return water_storage

def main():
  lift_of_buildings = input()
  print(water_stored(list_of_buildings)
