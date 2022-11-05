# Next read

## Overview

The idea behind this website is to allow the user to search for a book recommendation
based on their latest reading experience. On the main page, they input a title and 
fetch the recommendation based on a genre from the book. 

For now it work only if you enter a title that is in the database. The database should be created locally and then updated with books. Each position should contain:  
:ballot_box_with_check: ```title```  
:ballot_box_with_check: ```author```  
:ballot_box_with_check: ```genre```  

## Setting up the database

In the project folder, create a folder ```warehouse``` and inside of ```warehouse``` create ```archive```.

The project uses the following python libraries:  
:ballot_box_with_check: ```flask```  
:ballot_box_with_check: ```typing```  
:ballot_box_with_check: ```sqlite3```  
:ballot_box_with_check: ```pandas```

## Notes

This project is focused mainly on the backend as part of development towards Python programming. If you're interested in creating a front-end styling, feel free to fork the repo and create pull request. It will be further developed to provide better functionalities. Should the need arise, the project will be dockerized.
