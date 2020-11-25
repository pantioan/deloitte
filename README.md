# Deloitte - Cloud Engineer Assignment
This repository contains a solution for the Deloitte Cloud Engineer Assignment

The repository consists of the following files:
- main.py: The python file that describes the actions taking place in each page of the Flask application.
- requirements.txt: The text file containing the necessary libraries in order to run the application successfully.
- Dockerfile: Configuration file that builds the Docker image.
- templates/index.html: The index page of the Flask application, welcoming the user and requesting a phrase to edit.
- templates/phrase.html: The phrase page of the Flask application, presenting the edited phrase to the user and requesting whether the procedure should be repeated.

Notes for using the application:
The phrase is edited only if it contains the words 'Amazon', 'Deloitte', 'Google', 'Microsoft' and 'Oracle' by adding the © symbol right after each company.
Having in mind that this is a cloud engineering assignment, the application can understand whether the phrase contains one of the three major platforms; Amazon Web Services, Google Cloud Platform and Microsoft Azure (acronyms are not taken into consideration). If that is the case, © is added after the subphrases 'Cloud Platform', 'Cloud', 'Azure' and 'Web Services'. If the input phrase does not contain one of the 5 companies mentioned above, the phrase is returned unedited to the user. 
