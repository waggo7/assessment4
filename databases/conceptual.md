### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?

 \'''a database managment system 


- What is the difference between SQL and PostgreSQL?
  sql is the baseline programming language that postgresql adds functionality to

- In `psql`, how do you connect to a database?

  psql --databasename--'

- What is the difference between `HAVING` and `WHERE`?

  the WHERE is a pre-filter while HAVING is a post-filter
  this allows for more precision on what the server should return
- What is the difference between an `INNER` and `OUTER` join?
  the directions in which the "join" occurs
  an inner join only join the the condition that match whatever logic is filter through
  an out is all other 'join' types

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?

the directions in which the "join" occurs
  left out matches all the elements on the left and combines those with the matching on the right and viceversa for right outer

- What is an ORM? What do they do?
\'''an ORM - object relation mapping is at it's most basic level a way of mapping ideas about how object/things in an related/interacting 
\'''manner. ie events/people/pathogensetc in a hospital or the comings and goings/procedures/roles in a court building

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?

\'''for the sake of  asynchronization, ajax retrieves and displays info in a live manner to prevent the opening of a new page
 \'''while request will only retrieve what is on the most recent input/load of that page

 \'''how it retuns ajax is json while the requests are python/HTML

- What is CSRF? What is the purpose of the CSRF token?
\'''CROSS SITE REQUEST FORGERY is the attempt to gain unauthorized access/entry to an end user

\'''CSRF token provides authentication for individuals attempting to access this information

- What is the purpose of `form.hidden_tag()`?

\'''remove form from an HTML page
