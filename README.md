# Introductions
Welcome to G1T5'5 IS212 SBRP project. A web-based application that serve as a platform to facilitate job postings within a company and ease of applications for aemployees according to skills matchiing and thair career aspirations. This coursework aims to demonstrate web development, database management, and user experience design skills while engaging in the scrum project development framework.

### Getting Started 
Run the following instructions provided for setup.
1. Clone the repo
   ```sh
   git clone https://github.com/faithangg/is212-project
   ```
2. Install NPM packages
   ```sh
   npm install
   ```
3. Compiles and minifies for production
   ```js
   npm run build
   ```
4. Compiles and hot-reloads for development
    ```
    npm run serve
    ```
5. Import database
   Start up WAMP or MAMP
   Download 'sbrp_database.sql' and import into local db
   
6.Run backend
   ```
   cd backend
   ```
   Change directory to internal file 'backend'
   ```
   python app.py
   ```
   Run in terminal




## Built with
The following were utilised:

  Front End
  * HTML
  * Vuetify
  * Javascript
  * CSS
    
  Backend
  * Python
    
  Testing
  * Selenium
  * Python Unittest

## Files
A brief overview of file contents 
  * `backend` - blueprints, controllers which handles the logic for each API, models representing database structure and also files for creating the Flask application.
  * `database` - SQL files for database schema and sample file, `sbrp_database.sql` main database and `test_database.sql` for testing
  * `src` - main Vue.js application, media assets (icons and images), components, routing and views.
  * `public` - main HTML file for the Vue application
  * `test_files`- files for UI , integration and unit testing.

## Features
   **Applicant Management** : Efficiently manage applications, review candidate profile and their respective skillset.
   
   **Mobile Responsiveness**: The portal is responsive and accessible on mobile devices, ensuring that user access regardless of location.
   
   **Filtering and sorting mechanisms** : allows Users or HR the option of sorting and filtering based on desired criterias like recency of application and match percentage, or category and department.
   
   **Search bar** : robust search function to explicitly define search terms for finding roles or roles managed.
   
   **Easy Job Posting**: Simple and straightforward job posting process that integrates job role listings data from external system.
   
## Running tests
Populate the database test_database.sql

Change directory to folder containing test to be run
```
python <file name eg.selenium_test.py>
```
## Team
[@balveen01](https://github.com/balveen01) (backend)

[@faithangg](https://github.com/faithangg) (backend)

[@xinyitann](https://github.com/xinyitann) (frontend)

[@v1ghn35h](https://github.com/v1ghn35h) (frontend)

[@limpes](https://github.com/limpes) (frontend)

[@leeleetan88](https://github.com/leeleetan88) (frontend)

Link to git repo:https://github.com/faithangg/is212-project 

See [Configuration Reference](https://cli.vuejs.org/config/).
