## PyGUIimport

### GUI
 - PyGUIimport operates by editing text or spreadhseet files formated in columns in rows, cropping to important data and allowing you to save a new edited data text file or load cropped data in to a python application.
 - Currently the app functions by naming your file ET.csv. The app will then save your output file at VT.csv.

	- ![](https://raw.githubusercontent.com/aulloa/pyGUIimport/master/Before.JPG)

	- - ![](https://raw.githubusercontent.com/aulloa/pyGUIimport/master/Click.JPG)

    - ![](https://raw.githubusercontent.com/aulloa/pyGUIimport/master/After.JPG)

 - Start Row allows you to enter the row number you wish to start at, which crops out all above rows.
 - Columns allows you to enter in any colums you want to include in your new data set.

### Code
 - PyGUIimport is built on the Kivy framework
 - It also uses numpy to load and save data

### Future Work
 - The goal of this UI is to make the process as interactive as possible. I'm working on a way to automatically display the new data in real-time on the UI view.