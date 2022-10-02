# PrintPlusPlus
The intent behind this project was just a fun way to learn more about the Python programming language and see the output from playing with different python functions/features in a custom made GUI as oppose to the console window.  
![Animation showing the ability to change the theme and palette used in PrintPlusPlus](gifs/themes-and-palettes-demo.gif "Look and feel functions in Print++")
## Latest Changes (Sunday, October 2, 2022)
- Top buttons now reflect the "Actions" available in Print++ (i.e. Exporting is now exclusive to the menu bar).
- Removed text from buttons for a cleaner look.
- Add "Themes" option in menu bar allowing the user to change the feel of the app using one of many built-in themes.
- The "Palettes" option in the menu bar allows the user to change the UI colors from a set of pre-made options.
## Latest Changes (Sunday, September 18, 2022)
- A menu bar is now available to access all Print++ functions along with documentation on the app's capabilities.
- It is now possible to append text from a text file into the app's text area from the file menu in the menu bar.
- Small refactor to icons used more than once which are now stored in global variables.
## Latest Changes (Sunday, September 11, 2022)
- An edit button is now available allowing you use the software as a basic text editor but also allows you to edit content output from clicking "Run".
- Output from clicking "Run" now appends text to the text area instead of overwriting it.
- Closing the app by clicking the 'X', pressing the 'Quit' button, or pressing the ESC key now saves text content to a temporary text file.
- The app now starts loading text from the user's last open session.
## Latest Changes (Sunday July 17, 2022)
- A vertical scrollbar is now available to make seeing text in the output area easier.
## Latest Changes (Sunday July 10, 2022)
- Clicking on the newly added "Export" button allows you to export the content in the text area as a .txt file.
## service.py
The service.py module is meant to be used to contain any desired logic. The return value of the *run* function is what is seen in the Text widget when the "Run" button is clicked.
