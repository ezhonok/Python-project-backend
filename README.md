![GA-Logo](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png)

# Unit 4: Second language 

We'll provide you a client (unless you've gotten approval from us to use one of your own). Using the second language you chose, you will build a RESTful API will be consumed by the client. You will update the client as necessary to implement the expected behavior. 

This is a partner Project. 

## Deliverables & Requirements

- A RESTful API that supports consuption by this application [react-client](https://git.generalassemb.ly/WebDev-Connected-Classroom/react-movie-client) (or another of your group's previous projects) 
- A (Movie) model that has at least two fields, with full CRUD implemented on that model.
- A User model (if your framework comes with one, you can use/adapt that) that allows that user to perform those CRUD actions.
- Correctly implemented relations (and table SQL, if you chose Ruby) between the User and the other (Movie) model. Additional relations/models are optional, and should only be implemented after you complete the requirements.
- Proper login, logout, and registration functionality
- Create proper error messages on the client if the user does not have access, or if the username or password is already taken.
- The API/server/back end repo should be a _completely separate_ repo from the React/client/front end repo **from the very beginning**, and there should be several commits in the API as you build each route and test it (Postman!).
- Proper CORS implementation in your API, so that...
- ...your deployed React app can consume your deployed API.

## Not quite a stretch goal

* Try to make your front end and back end "work" both on your local machine ("development") **and** when deployed ("production").  This will likely involve careful researching of both CORS and environment variables. There is extensive documentation and a panopoly of articles about this online.

## Stretch Goals

* Add a third party API from the back end 
* Add json web tokens to secure your api further [token auth python](https://flask-httpauth.readthedocs.io/en/latest/)
  * This might involve finding a module/gem/package to do HTTP requests from the back end
    * [request module-python](http://docs.python-requests.org/en/master/)
    * [Net::HTTP — make HTTP requests w/ Ruby](https://ruby-doc.org/stdlib-2.5.3/libdoc/net/http/rdoc/Net/HTTP.html) (or find your own at https://rubygems.org)
  * If you used something like [OMDB or TMDB](https://medium.com/@mcasciato/no-imdb-api-check-out-these-options-75917d0fe923), you could...
    * Make it so that only actual movies that are validated via a third party movie API can be added, and only one time
    * (i.e. update your model to contain the 3rd party API ID, or something similarly unique, to be sure you're only referring to exactly the correct movie)


* Add pagination to your API. For example, if your user had 126 movies in the database, this HTTP request should return movies 21-40:
  ```
  GET 'https://your-deployed-api.herokuapp.com/api/movies?resultsPerPage=20&page=2
  ```
  
* You could then implement pagination in your front end as well.

* Add animations to the front end



