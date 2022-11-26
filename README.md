# Next read

## Overview

The idea behind this website is to allow the user to search for a book recommendation
based on their latest reading experience. On the main page, they input a title and 
fetch the recommendation based on a genre from the book. 

For now it works only if you enter a title that is in the database. The database should be created locally and then updated with books. Each position should contain:  
:ballot_box_with_check: ```title```  
:ballot_box_with_check: ```author```  
:ballot_box_with_check: ```genre```  

Additionaly it pulls 20 recommendations from ```lubimyczytac.pl``` which is the largest book database in Poland at the moment. The search is based on the books' tags.

## How to access the website

### Running for the first time

Clone the repository:  
```git clone https://github.com/PiotrPietrz/book_search.git```

Setting up the database

In ```warehouse``` create ```archive```.

Change to dev:  
```git checkout dev```

Spin up the docker container:  
```docker build --tag book .```

```docker compose up -d```

Access the website:  
```http://localhost:5001```

### Update for changes

Save all the changes in the repository.   

Stop the current container:  
```docker compose down```

Clear the existing images:  
```docker image prune -a```

Spin up the docker container again:  
```docker build --tag book .```

```docker compose up -d```

Refresh the website:  
```http://localhost:5001```

## Notes

This project is focused mainly on the backend as part of development towards Python programming. If you're interested in creating a front-end styling, feel free to fork the repo and create pull request. 
