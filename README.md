# OttermapTask
1. So this project is part of the task given to me by Ottermap for the position of Python Developer Intern.
2. I have tried to complete this project as much as i can on 27th February 2025 only, because i have an on campus interview on 28th February 2025.
3. So the project can be run as:
   1. Clone the repository
   2. Set up and activate virtual environment
   3. Install all the dependencies
   4. Setup Postman
   5. http://127.0.0.1:8000/home/, this is the endpoint , method=POST that will be used to create the user for the application:
      The required format for post request is:
      {"username":"","password":"","email":"" }
      After sending the request a token will be generated that will be used to perform crud operations for specific users.
   6. http://127.0.0.1:8000/shops/ this is the endpoint, method=POST that will be used to create shops for vendors
      The required format for post request is { "Shopname": "","Businesstype": "","Latitude": 26.8467,"Longitude": 80.9462}
      The latitude and longitude are mentioned for understanding.
      The token generated in previous step ensures that user can acces the role to create the shop.
      Token will be used as :
      1. Open headers tab in postman in this request only
      2. In the key add Authorization and in value add Token followed by token
      3. Send the request , the returned response should be the one you sent along with id in it.
    7. Similarly, end points like http://127.0.0.1:8000/shops/1 where 1 is the id of the created entry in the database with methods like PUT and DELETE will be used to update and delete the entry from the database.
    8. Catch: A user can only perform read, update and delete operations on shops created by the user only.
    9. http://127.0.0.1:8000/nearby-shops/ this is the public endpoint, method=POST that will be used to find the nearby shops within the specified radius. Token is not required for this endpoint.
        The format of POST request should be : {"latitude": 26.8467,"longitude": 80.9462,"radius": 5}, where the mentioned attributes are for understanding purposes only.
4. I got to learn a lot from this assignment, worked on permissions, authentication, ensuring user authenticated crud operations and docker as well.
5. If you read it till here, i hope you must have understoood the project and the use of endpoints as well. 

    

