One of the most common question asked in the assesment test are water storage problem in between buildings. To solve this problem I use a two pointer method, This same approach can be used to solve problems such as snow capped mountains and trapping lava problem

First let's undertstand the question , you have to find the number of water blocks that can be stored in between the buildings.

![image](https://github.com/user-attachments/assets/c0d801ad-020a-4084-869b-b89764e600dc)


Here is an example of the buildings which is provided in a form of list. In this example the input list is [ 3 , 1 , 0 , 2 , 0 , 2]

![image](https://github.com/user-attachments/assets/15b4657d-3183-45a9-b76c-99e786e8efee)


The output is the number of water blocks that can be collected in between the buildings without any overflow. 

https://github.com/user-attachments/assets/8e8f62df-d8ca-4eb5-a3a7-0cefa3d9cff4


Here is the animation of overflow blocks .

Solution : We are using a two pointer method to solve this problem.

step 1 : Take two variables 'left_pointer' and 'right_pointer' , assign left pointer at the beggining of the list and right pointer at the end of the list .

step 2 : Take two more variables to store the height of thge tallest building . I use 'left_max_building' and 'right_max_building'.

step 3 : In most of the problems when you are using left_pointer and right-pointer you have to use a while loop to check if left pointer is less than or equal to right pointer which significes that we have looped all the elements in the input array/list .

step 4 :check if left buildingf block height is less than right building block , this i done to not count overflow blocks.

step 5 ; compare the current pointer value with the max height , if the max height is less update the max height to the value or else update the count of the water stored variable.

step 4 : print out the waater stored variable .
