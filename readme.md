# READABLE #
#### Video Demo:
#### Description:
    
    Thanks to Google Books Api, the application allows you to search for books that interest you.
    The application also allows you to manage your book collections.
    The application provides user service, including the registration and login system.

    I started my project work designing the appearance of the main webpages, using Adobe XD. Projects files in /webdesign.
    ![screen](webdesign/adobe_xd.png)  
)
  	


    The files tree was created by the use of python's framework - Django.
    The app has been divided into two parts: main nad users. 

    /readable/'app_name'/templates/ 
        here are all of the hmtl files created in the project
        list:
        - about.html
        - base.html
        - bookshelf.html
        - contact.html
        - library.html
        - home.html
        - progress.html
        - reco.html
        - base2.html
        - login.html
        - logout.html
        - profile.html
        - register.html

    /readable/main/static/main/
        here are all of the css files created in the project
        - about.css
        - bookshelf.css
        - login.css
        - main_login.css
        - profile.css
        - progress.css  

    Files (created or modified) responsible for the operation of the application:
    urls.py
        files create url patterns and assigne them to corresponding view functions programmed in views.py

    views.py
        files contain all of view functions

    forms.py
        creating forms connected directly to specific models programmed in models.py

    models.py
        files contain definition of all tables in the database

    helpers.py
        function that takes a 'text' as an argument, queries api and returns results
    
    settings.py
        configuration and settings of the app



    There were 4 basic features (views) planned fo this app:
    1.  - Setting and viewing reading goals (yearly, monthly goals)
        - Viewing few currently reading books
    2.  - Viewing and editing all book collections
    3.  - Searching for the books of interest using google books api service
        - Viewing the searching results
    4.  - Viewing book reccomendations based on favourites and already read books

    I managed to accomplish simplier version of app:
    1.  - Setting and viewing years reading goals
    2.  - Viewing and editing all book collections
    3.  - Searching for the books of interest using google books api service
        - Viewing the searching results


    technologies used in the project:
    - django framework
    - sqlite3 database
    - html, css, js
    
    Big thanks to CS50 stuff for their effort and dedication in preparing such an excellent course!