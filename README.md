<h1 align="center"> FestivCulture <h1>
<h2 align="center"> Welcome to the Cultural Festival World of India <h2>

## Purpose and Targeted Audience
- India is having 28 states and each states are Unique in Celebrating Festivals, speaking Languages, having special foods for the every Festival.

- This Website has made for the people who wants to know Indian Festival and there Culture, how they celebrate it, whats the reason behind every festival.

- This Website blog having Festival's brief information and when its celebrated what foods they preparing for make this festival more special.

<hr>

### The live link is available here [FestivCulture](https://festive-culture-18e558f91174.herokuapp.com/)

## [Content](#content)


 -----

 # User Experience - UX

 ## Site Aims

* 
* 

 ## Agile Methodology

The Agile Methodology was used to plan this project. This was implemented through Github and the Project Board. Through the use of the Kanban board in the projects view in Github, the project was divided into a few different sections: 

* To Do- (All the User stories were initially entered in the 'To Do' column)
* In Progress- (then during development story they were moved into the 'In Progress' column)
* Done- (and then finally they get moved into 'Done' once the development completes)

Please find my Project Board with my user stories [here](https://github.com/users/JyotiHambir-BC/projects/9/views/1)

## User Stories


## Design

* To choose the colour I used [Faltui Colour Picker](https://www.flatuicolorpicker.com/colors/vivid/)

### Typography

* Fonts were imported using Google Fonts. Poppins was used throughout with a backup of sans-serif. It was chosen for easy readability for users.
* Protest Guerrilla font was used for website name **"FestivCulture"**

### Imagery

### Wireframes

**Homepage**

![Home Page](assets/wireframe/homepage.png)

**About Page**

![About Page](assets/wireframe/about%20page.png)

**Festivals Page**

![Festivals Page](assets/wireframe/festivals%20page.png)

**Festivals Blog Page**

![Festivals Blog Page](assets/wireframe/festivals%20blog%20page.png)

**Register Page**

![Register Page](assets/wireframe/register%20page.png)

### Database Diagram

Smart Draw was used to create a database schema to visualise the types of custom models the project requires. This schema was used as a guide to what needed to be added to each model. Below is the Database structure that this project is based on. The relationship between Entities Post and Comment are shown in this diagram.

![ER Diagram](assets/erd_diagram/ERD.png)


# Features

## Home Page

At the very first glimpse, user can see a Navigation menu and carousel-images on the homepage. Homepage provides the user with some quick information about the site and make use of all its features. User do not need to be registered to view a blog post. The responsive navigation bar is featured on all pages. 

![Home Page]()

## Navbar

- The navigation bar is present at the top of every page and navigates all links to the respective pages.
- The options to Register or Log in will change to the option to log out once a user has logged in.
- The navbar is fully responsive, collapsing into a hamburger menu when the screen size becomes smaller.

![Navbar]()

## Footer

- On the website footer, users can see basic information such as my social media, copyright about FestivCulture Website.

## About Page

- The About Page gives, users information about the Incredible India with a brief discription of india and the travel options to reach there.

![About us]()

## Festivals Page

- 

![Festival Page]()

## Festivals blog Details Page

- 

![Festival blog details page]()

- If user is signed-in, following comment box will appear. 

![Comment-Box]()

- When User submit a comment or like/unlike a post, following messages/ alert displays respectively.

![comment-alert]()
![Like-post-alert]()
![Unlike-post-alert]()

- Signed-in users can only edit/delete their own comments.

![Edit-Delet Button]()

- When the user clicks on the delete button to remove his comment, following alert message pops up.

![Delete-comment-alert]()

- When user clicks on update button, a successful update alert message is displayed.

![update-comment-alert]()

## Security
In order to properly interact with the website, the user needs to have an account and sign in. This ensures security of their comments and gives them rights to create, modify and delete them.

### Sign Up

- User is asked to enter username and password to sign up. User will be guided by validation messages if the username exists or password is too small which was created by modifying Django inbuilt templates.

![Signup page]()

- When users sign up to the website they will see a message at the top of the page saying "Successfully signed in as (username)".
![Sign Up alert]()

### Sign In

- User can enter username and password to sign in. User will be guided by validation messages if the username or password is not correct. This was created by modifying Django inbuilt templates.

![Sign In page]()

- When users sign in to the website they will see a message at the top of the page saying "Successfully signed in as (username)".

![Sign In alert]()

### Sign Out

- If the user is signed-in, then only they can see Logout nav-item in navbar. User will be taken to the Sign Out page. This was created by modifying Django inbuilt templates. When the user signs out, they are redirected to homepage.

![Sign out page]()

- When users log out of the website they will see a message at the top of the page saying "You have signed out".

![Sign out alert]()

## Admin Panel/Superuser

- Admin accesses the project via logging into Django admin panel with a superuser id and password. The page appears as shown [here]().
- A superuser "admin" was created for this project to manage the admin panel.
- On the Admin Panel, as an admin I have full access to CRUD functionality so I can view, create, edit and delete the following ones:
  - Posts
  - Comments
  - Author
- As admin I can also approve comments and change the status and give other permissions to the users.

### Admin 'Post' Model Management

- On selecting Blog "Post", a list of blog posts is displayed with its title, slug, status, created_on and author name. Admin can select the post and edit or delete its data.
- When a blog post is submitted by a user, its status is set to Draft by default.
- When the status is set to Publish on Admin Approval, the post starts appearing in the website.

The admin site for post model appears as shown [here]().

### Admin 'Comment' Model Management

- Upon selecting the Blog "Comment" model, a list of comments on a post is displayed with the username, comment body, post title, status and created_on. Admin can select the comment and edit or delete its data.
- When a comment is submitted by a user, it requires approval from an admin in order to publish it on the comments section.

The admin site for comment model appears as shown [here]().

## Technologies Used

### Languages Used

* [HTML 5](https://en.wikipedia.org/wiki/HTML/)- Used to structure all the templates on the site
* [CSS 3](https://en.wikipedia.org/wiki/CSS)- to provide extra styling to the site
* [JavaScript](https://www.javascript.com/)- Minimum javascript was used to fade out alerts after a few seconds.
* [Python](https://www.python.org/)- To provide the functionality to the site. Packages used in the project can be found in requirements.txt

### Django Packages

* [Gunicorn](https://gunicorn.org/)- As the server for Heroku.
* [Cloudinary](https://cloudinary.com/)- Was used to host the static files and media for the site.
* [Dj_database_url](https://pypi.org/project/dj-database-url/)- To parse the database URL from the environment variables in Heroku.
* [Psycopg2](https://pypi.org/project/psycopg2/)- As an adaptor for Python and PostgreSQL databases.
* [Summernote](https://summernote.org/)- As a text editor.
* [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)- For authentication, registration, account management.
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)- To style the forms.

### Frameworks - Libraries - Programs Used

* [Django](https://www.djangoproject.com/) was used as the framework for the back-end logic of the project. Django enables rapid and secure development.
* [Bootstrap](https://getbootstrap.com/)- Used to style the website, add responsiveness and interactivity.
* [Git](https://git-scm.com/)- Used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub.
* [GitHub](https://github.com/)- Used to store the project's code after being pushed from Git.
* [Heroku](https://id.heroku.com)- Used to deploy the live project.
* [PostgreSQL](https://www.postgresql.org/)- Database used through heroku.
* [Balsamiq](https://balsamiq.com/)- To build the wireframes for the project.
* [Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) was used to inspect page elements, debug, troubleshoot and test features and adjust property values. Using the Lighthouse extension installed in Chrome Browser, the performance report was generated.
* [Google Fonts:](https://fonts.google.com/) used for the Poppins and Protest Guerrilla font
* [Font Awesome:](https://fontawesome.com/) was used to add icons for aesthetic and UX purposes.

## Testing

### Validation
I used the following validation tools to validate HTML, CSS, PYTHON codes. Below the link of TESTING.md file, which includes all validation results.  
- HTML using [W3C HTML validator](https://validator.w3.org/)
- CSS using [Jigsaw CSS validator](https://jigsaw.w3.org/css-validator/)
- Python via [PEP8 CI Python Linter](https://pep8ci.herokuapp.com/)

## Bugs

## Future Implementation

## Deployment

### 1. Creating the Django Project
* Go to the Code Institute Gitpod Full Template [Template](https://github.com/Code-Institute-Org/gitpod-full-template).
* Click on `Use This Template` button, then create new repository.
* Name our repository and click on `Create repository from template` button.
* Once the template is available in your repository click on `Gitpod` button.
* When the image for the template and the Gitpod are ready, open a new terminal to start a new Django App.
* Install Django and gunicorn: `pip3 install 'django<4' gunicorn`.
* Install supporting database libraries dj_database_url and psycopg2 library: `pip3 install dj_database_url==0.5.0 psycopg2`.
* Install Cloudinary libraries to manage static files: `pip install dj-3-cloudinary-storage`.
* Create file for requirements: `pip freeze --local > requirements.txt`.
* Create project:`django-admin startproject project_name .`.
* Create app: `python manage.py startapp app_name`.
* Add app to list of `installed apps` in settings.py file: `'app_name'`.
* Migrate changes: `python manage.py migrate`.
* Test server works locally: `python manage.py runserver`.
* If the app has been installed correctly the window will display- The install worked successfully! Congratulations!

### 2. Create your Heroku app
* Navigate to [Heroku](https://id.heroku.com).
* Create a Heroku account by entering your email address and a password (or login if you have one already).
* Activate the account through the authentication email sent to your email account.
* Click the **new button** on the top right corner of the screen and select create a new app from the dropdown menu.
* Enter a unique name for the application.
* Select the appropriate region for the application.
* Click create app.
* Click Reveal Config Vars and add a new record with `DATABASE_URL`.
* Click Reveal Config Vars and add a new record with `PORT`.
* Click Reveal Config Vars and add a new record with the `DISABLE_COLLECTSTATIC = 1`(note: this must be either removed or set to 0 for final deployment).
* Next, scroll down to the Buildpack section, click `Add Buildpack` select python and click Save Changes.

### 5. Heroku Deployment: 
* Click Deploy tab in Heroku.
* Select Github as the deployment method.
* Confirm you want to connect to GitHub.
* Search for the repository name and click the connect button to link the heroku app with the Github repository. The box will confirm that heroku is connected to the repository.
* Scroll to the bottom of the deploy page and select the preferred deployment type.
* Click either Enable Automatic Deploys for automatic deployment when you push updates to Github or To manually deploy click the button 'Deploy Branch'. The default 'main' option in the dropdown menu should be selected in both cases. When the app is deployed a message 'Your app was successfully deployed' will be shown. Click 'view' to see the deployed app in the browser.

### 6. Final Deployment
In the IDE:
* When development is complete change the debug setting to: `DEBUG = False` in `settings.py` 
* In Heroku settings config vars change the `DISABLE_COLLECTSTATIC` value to 0
* Because DEBUG must be switched to True for development and False for production it is recommended that only manual deployment is used in Heroku. 
* To manually deploy click the button 'Deploy Branch'. The default 'main' option in the dropdown menu should be selected in both cases. When the app is deployed a message 'Your app was successfully deployed' will be shown. Click 'view' to see the deployed app in the browser.

----

# Credits

## Code

## Learning Resources

## Content and Media

## Acknowledgement


[Back to top](<>)
   
