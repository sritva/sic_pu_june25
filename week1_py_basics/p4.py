# Farmer Problem
total_land = 80 #acres

# dividing equally among 5 segments
tomato_land = 16 #acres
potato_land = 16 #acres
cabbage_land = 16 #acres
sunflower_land = 16 #acres
sugarcane_land = 16 #acres

# calculating yield per crop (tonnes per acre of land)
tomato_yield_1 = 0.3*16*10
tomato_yield_2 = 0.7*16*12
potato_yield = 16*10
cabbage_yield = 16*14  
sunflower_yield = 16*0.7 
sugarcane_yield = 16*45

# calculating total yeild (adjusted from tonnes -> kg ) [1 ton = 1000 kg]
total_yield = 1000 * (tomato_yield_1 + tomato_yield_2 + potato_yield + cabbage_yield + sunflower_yield + sugarcane_yield)
print("total yeild from all crops: ", total_yield, "kg")

# price per crop (in rupees per kg)
tomato_price = 7 
potato_price = 20
cabbage_price = 24
sunflower_price = 200
sugarcane_price = 4000 # per tonne 

#calculating revenue per crop
tomato_revenue = 1000 * (tomato_yield_1 + tomato_yield_2) * tomato_price 
potato_revenue = 1000 * potato_yield * potato_price
cabbage_revenue = 1000 * cabbage_yield * cabbage_price
sunflower_revenue = 1000 * sunflower_yield * sunflower_price
sugarcane_revenue = sugarcane_yield * sugarcane_price
 
#calculating total revenue
total_revenue = tomato_revenue + potato_revenue + cabbage_revenue + sunflower_revenue + sugarcane_revenue
print("overall sales i.e total revenue from all crops: ", total_revenue, "rupees")

'''chemical free cops in 11 months time include all vegetables(tomator, potato, cabbage) and sunflower'''
chemical_free_crops_revenue = tomato_revenue + potato_revenue + cabbage_revenue + sunflower_revenue
print("revenue from chemical free crops: ", chemical_free_crops_revenue, "rupees")