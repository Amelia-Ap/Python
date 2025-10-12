#it is a callBack example. customer in restaurant put order and Waiter deliver food


##--
#  PS code (beachten Sie arr_length is definiern in linie 12)
# def food_exists = 0
#  // i ist Array Index 
# FOR i IST 0 BIS i <= arr_length i PLUS 1
#    WENN food_name = arr_foods[i] 
#       food_exists=1 
#    END IF
# RETURN food_exist   
##--
def checkFoodExistence(food_name:str)->bool:
    arr_foods=["Pizza", "Pasta","Dönner", "Eis"]
    if food_name in arr_foods:
       return True
    else:
        return False
      
def orderFood(food_name:str, checkFoodExistence):
    is_food_exists = checkFoodExistence(food_name)
    if is_food_exists == True:
        print(f"your {food_name} deliver soon!")
    else:
        print(f"sorry, we have no such a food so called {food_name}")

#-- actual PROGRAM use upper defined methods --#
order_string = input("what is your order?")
orderFood(order_string,checkFoodExistence)