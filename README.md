# Data in Api View

apidata = using https://jobs.github.com/positions.json url retriving the data using GET.method

- sqlite3 database created with the same fields which is derived from the url

- post = post the data using post method to the http://127.0.0.1:8000/index

**function name id_api:**

filter the serialized data in ApiViewSerializer. 

- search the id :- id(SlugField): ?id123xcsc-cxscd-cssdw21

**function name list_out:**

- list out the whole data in db as apiview

**function name about:**

- Values_list: filter the field (title) from database 

**function name search_api**

- ApiViewFilters: filter the data using title, location field using filters in filters.py 

**class name UserListView:**

- filter the data using search field using filters
