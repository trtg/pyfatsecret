pyfatsecret
===========

This library provides a lightweight python wrapper for the fatsecret API with the goal of making it easier to visualize the data retrieved from the API. To that end, this library will usually return lists of identical elements for ease of plotting, discarding extra header fields that the fatsecret API otherwise includes. For example, exercise_entries_get_month() returns a list of dates and calories burned without the 'month','day', 'from_date_int', 'to_date_int' keys that the API normally returns 


The methods provided by the API are grouped according to category:

Foods
---
food_add_favorite()
food_delete_favorite() 
food_get() 
foods_get_favorites() 
foods_get_most_eaten() 
foods_get_recently_eaten() 
foods_search() 

Recipes
---
recipe_add_favorite() 
recipe_delete_favorite() 
recipe_get() 
recipes_get_favorites() 
recipes_search() 

Recipe Types
---
recipe_types_get() 

Saved Meals
---
saved_meal_create() 
saved_meal_delete() 
saved_meal_edit() 
saved_meals_get() 
saved_meal_item_add() 
saved_meal_item_delete() 
saved_meal_item_edit() 
saved_meal_items_get() 

Exercises
---
exercises_get 

Profile - Management
---
profile_create 
profile_get 
profile_get_auth 
profile_request_script_session_key 

Profile - Food Diary
---
food_entries_copy 
food_entries_copy_saved_meal 
food_entries_get 
food_entries_get_month 
food_entry_create 
food_entry_delete 
food_entry_edit 

Profile - Exercise Diary
---
exercise_entries_commit_day 
exercise_entries_get 
exercise_entries_get_month 
exercise_entries_save_template 
exercise_entry_edit 

Profile - Weight Diary
---
weight_update 
weights_get_month

