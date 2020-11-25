# Import necessary libraries
import os
from flask import Flask, render_template, request

# Initialize application object as an instance of class Flask
app = Flask(__name__)

# Show the index page of the Flask application whether the user types '/' or 'index'
@app.route('/')
@app.route('/index')
def index():
    # Render index.html from the templates folder
    return render_template("index.html")

@app.route('/phrase', methods = ['POST', 'GET'])
def phrase():

    # Prevent the possibility that the user visits the /phrase page straight from the web browser without inputting a phrase in the /index page.
    if request.method == 'GET':
        return f"Sorry, this action is prohibited. Please revisit '/' or '/index' for a smooth experience."
    
    # Show /prhase page if user has inputted a phrase in /index. Retrieve the phrase, edit it accordignly and show it.
    if request.method == 'POST':
        
        # Select the input phrase from the form in index.html
        phrase = request.form['phrase_context']

        # Initialize company list 
        company_list = ['Oracle', 'Google', 'Microsoft', 'Amazon', 'Deloitte']
        for company in company_list:

            # Check whether the company's name is on the list.
            # Define cases in which the company's cloud platform is mentioned. In these cases, the '©' symbol must be added after the full name.
            if company in phrase:

                # Google and Oracle case
                if company + ' Cloud Platform' in phrase:
                    phrase = phrase.replace(company + ' Cloud Platform', company + ' Cloud Platform©')

                # Google and Oracle case (shortened)
                elif company + ' Cloud' in phrase:
                    phrase = phrase.replace(company + ' Cloud', company + ' Cloud©')

                # Microsoft case
                elif company + ' Azure' in phrase:
                    phrase = phrase.replace(company + ' Azure', company + ' Azure©')

                # Amazon case
                elif company + ' Web Services' in phrase:
                    phrase = phrase.replace(company + ' Web Services', company + ' Web Services©')

                # Case in which none of the platforms are mentioned
                else:
                    phrase = phrase.replace(company, company + '©')
        
        # Render phrase.html from the templates folder with the edited phrase as an argument
        return render_template("phrase.html", phrase = phrase)

if __name__ == "__main__":
    # Define a host and a port for the application. Setting the debug variable to True will print out error messages to the page in case there is an error.
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 1234)))