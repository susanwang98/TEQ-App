# Code Review

Within Team 10, code reviews are typically informal. However, given the requirements in Deliverable 4, documentation of our code review is provided. The video for the November 8 code review is found [here](https://drive.google.com/file/d/1QWhTOe7yiAyrI3t_L7N8U35C5dqXjaRP/view).

## Review Strategy

Within our team agreement (which can be found [here](../deliverable_1)) there exists a section called "Submission". In this section, a buddy/infinite linked list system is in place. Analogously, the system is in place where "A->B" means A reviews B's work:

`Dann -> Philip -> Riaz -> Susan -> David -> Dann`

The general strategy is to pick out any code that does "stink" off of scripts that are typically 100 to 200 lines of code. Examples of such include:

* Duplicate code
* Long methods
* Big ("God") classes
* Long list of switch/if statements
* Lots of checking for null objects
* Unencapsulated fields/methods
* Dead code
* Hardcoded code

Note that the stinks above is not limited to the above as members are able to make professional judgement on other's code. Positive feedback is also encouraged.

## Code Review Summary (November 8, 2018)

### Dann to Philip
* Noticed that there is at least some injection within the "AggregateValueChecker"; it's great that there is because Philip can make mock objects off of abstract classes.
* Found a potential "stink" in his code where he checks a column name like a "postal code". It can be possible that he could expand this list of if statements; the tradeoff is that he may potentially duplicate code.
    * I recommended Philip to research on the concept of reflection; the idea that you can call methods or instantiate objects with strings (this goes into functional programming territory).
* I recommended a "hard coded" list of constants at the top of his class for checking column names. If someone were to revisit his code, that person would easily know which column names are "aggregated".
* This was not discussed in the video, but I noticed that there was an unencapsulated method in his class. Just a small reminder that a single underscore means "private".

### Philip to Riaz
* Code is easy to follow and understand, also by Riaz's design, it makes things easier when working with the GUI
* Since MissingValueChecker and the function (DataAggregator) I was working on are similar, we have to agree and unify our ideas on how the methods should function
* Only concern about his MissingValueChecker is that, it returns a list of tuples, but it is probably better to return the DataFrame object instead

### Riaz to Susan
* Code is well seperated into classes and imports are clear making it easy to trace code
* Biggest concern was that Observer pattern wasn't implemented, this means changes to button functionality not relating to the view requires changing the view page for the button
	* but I refactored this, this also makes the code easier to follow as button functionality is in its own class and makes adding functionality to buttons easier

### Susan to David
* Code that retrieves information from the database in method send() should be separate from the class PasswordForgettingEmailer
* The SQL command for checking if an email is in the database does not need to include the Type of the user, having just Name is sufficient
* In PasswordForgettingEmailer, there does not need to be a method to check whether the email was sent, this can be done externally after validating whether the email exists in the database or not

### David to Dann
* Noticed that in is_dropdown_value_mandatory for the true template handler, there are two dummy variables that are being used in order to take up all indexes of a tuple. Instead only the first index should be returned in order to be more efficient.
* In the same function, is_dropdown_value_mandatory, I mentioned that there is a conversion of a string into an integer and then into a boolean right after. Python allows 0's and 1's to act as booleans so the second conversion can be removed so I suggested to just keep it as an integer for conditional statements.
* In handle_template, there is a hardcoded True value returned which is taking memory unnecessarily.
* Otherwise, the rest of the quality of code is sufficient and no further comments could be made.

## Code Review Summary (November 15, 2018)

### Dann to Philip
* For Custom Query, noticed that the user cannot select the name of the csv to export to, so it would be better if the user has the option to
* For the Data Viewer Page, it should run the data frame checkers (Data Aggregator and MissingValChecker) after the generate table button is hit
    * data_viewer_page should not contain both table viewer and data viewer class
* In the table_viewer, there should be a method to upload the data to the database once the user hits the back button
    * Make sure the format of the dataframe or modified dataframe is matching  in format
* For Custom Query, the user should have a back button if the user doesn't want to handle any commands, or mistakenly clicked into this page

### Philip to Riaz
* Missing Value Checker contains too many comments, could reduce some of the unnecessary ones, but the code is easy to understand. In both the execute and  parse_columns method.
* There are variables that are not clear, for example empty_fields should be code and all the variable (var1, var2.. etc) should be code variable instead.
    * Not clean code, properly need to reformat the layout of your code.
### Riaz to Susan
* beautiful_uploader:
    * Code is well organized and clear
    * Not sure if the class is getting "too long" but it is justified regardless
* Dispensables; Duplicate Code
    * all methods start with the same few lines of code, this can be separated
    * this means if this part of the code has to be changed, it only has to be changed once
* Symbolic Constant
    * the magic number 2 used for indexing should be replaced with a symbolic constant
    * this would also help remove the need for comments relating to it

### Susan to David
* In client_db_functions, it would be better to call execute_query from database_methods and return cur to get rid of all of the redundant code which creates a new connection each time
* Add more error messages when the user enters bad input for account creation
* Fix creating another account with the same username saying "success" but nothing actually happens

### David to Dann
* Code Review for Dann was conducted on 18 as he did not have much on the 15th
* DuplicateRowChecker was not needed since one line from pandas was called
* We also talked about the tradeoffs as to why DuplicateRowChecker is is a command rather than something to be called when tying it together.
* Excellent idea of "Screener", following the template design pattern
    * The screener is used to determine if the user is uploading the right thing based off of the selected iCare templates

## Code Review Summary (November 24, 2018)

### Dann to Philip
* There were minor bugs in multiple pages (custom query, table viewer, etc) that will crash or raise error if we try to break the program.
  Should put restrictions on those so that those crashs and error raises can be minimized
* The format of the dataframe in when uploading to the database using beautiful uploader is not set, need to fix that when user gets to view data
  or when the data gets passed through from the file upload page to the data/table viewer page. But the data gets displayed well.
	- Where index 0 of the dataframe are all blank spaces, index 1 contains the column names, and from index 2 to n, it contains the data
* Custom Query error handling caused the exception, where the error message cannot be displayed when invalid SQL Commands were inputted, suggested
  to remove the true error message (from system) and just display "Invalid SQL Command"
* For client summary reports, there are a few minor bugs that needs to be fixed, and handled, and make sure to have an GUI for these reports.
* When file gets uploaded, there needs to be more parameters passed in for beautiful uploader as well as other pages that links to these viewers.
### Philip to Riaz
* The graphs that he made, Histogram, Scatter plot and Line graph should be refactored to be line graph,histogram and pie graph because we couldn't find usage of scatter plot and pie graph is better for comparison.
    * Some of the variables in the parameters were not needed, so they are removed during the refactoring
### Riaz to Susan
* Some docstring requirements don't match parameters
* graph
    * Dispensables; Comments
    * A few unnecessary comments, code is clear without them
* pie_graph
* Symbolic Constant
    * Good to seperate symbolic constants from code into variables
    * Symbolic constants should be all caps
* graph subtypes
* Dispensables; Duplicate Code
    * display has diplicate code between the subtypes
    * this can be moved up to the abstract class's display method

### Susan to David
* A TEQ account should not have the authority to delete other TEQ accounts
* In client_db_functions, there should be a "check duplicate field" which would return whether or not the field exists in order to prevent rollbacks from happening every time a duplicate value is attempted to be inserted into to the database

### David to Dann
* Dann showed me his branch for "Predicitve Analysis"
* Used the template model
* Used inheritance appropriately
* One potential smell is the get_model() method as there are optional parameters. I warned Dann to be cautious about this.
