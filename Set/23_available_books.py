available_books = {"Python", "Java", "C++", "HTML", "SQL"}

requested_books = {"Python", "Java", "CSS", "SQL"}

available_requested = available_books & requested_books

print("Requested books that are available:", available_requested)