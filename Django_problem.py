""" 
1,"no such table" I thing the problem have faced approximately in 10m/11d/2024y
I have manually deleted the migration files and so I have faced the problem
and then I have runs the command of migration and migrate but didn't work so I have to run python manage.py migrate --run-syncdb
solution: python manage.py migrate --run-syncdb
"""
""" 
2, Data not saving in database 11/16/2024
Solution: After 1 day sepending finally I got solution of this problem which is I was rendered 
the form with the help of every field like this " {{form.First_Name}} , {{form.Last_Name}}, {{form.Email}}, {{form.Password}}, {{form.Confirm_Password}}" and then I have tried to save the data in the database. No error showed at the time in terminal and broswer but the data is not saved in the database.When I rendered the form like this "{{form.as_p}}" then the data is saved successfully in the database.so keep in mind that we have to render the form in this way "{{form.as_p}}" otherwise the data is not saved in the database.
"""
