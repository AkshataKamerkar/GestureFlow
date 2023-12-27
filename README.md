
# GestureFlow 

This Python-based project enables interactive control of presentation slides through hand gestures captured via a webcam. Using OpenCV and CVZone libraries, the application recognizes specific gestures to navigate slides and perform annotations in real-time. It's designed to provide an engaging and hands-free experience for presentations.


## Description 


The project offers an intuitive interface, allowing users to control presentation slides through recognized hand gestures captured in real-time via a webcam. With this system, presenters can effortlessly transition between slides, draw annotations, and use their finger as a pointer during presentations.
## Key Features 


* **Gesture Control** - Navigate slides with left and right hand gestures, mimicking page flipping for seamless transitions.

* **Annotation** - Draw on slides using hand gestures, enabling on-the-fly illustrations or emphasis during presentations.

* **Pointer Mode** - Use the index finger as a virtual pointer, enhancing interaction and engagement with specific elements on slides.

* **Clear Annotations** - Instantly clear drawn annotations with a specific gesture, ensuring a clean canvas for further interactions.


## Technologies Used 

* **Python :** The project's core language for developing the application's functionalities and logic.
* **OpenCV (cv2) :** Handles webcam access, image manipulation, and gesture recognition to control slide navigation and annotations.
* **NumPy :** Assists in efficient handling and manipulation of image data for gesture recognition and processing.
* **CVZone :** Provides specialized tools and functions for precise hand tracking and gesture-based interactions within the presentation slides.
## Requirements and Configurations 

**Requirements -**

* Python 3.x
* Webcam


**Configurations -**

* Adjust webcam resolution via width and height variables.
* Modify FolderPath to the directory containing presentation slides in main.py file.
* Fine-tune gestureThreshold, button_delay, and other parameters as needed.
## Deployment

Accessing the project involves a few steps:

**Step 1 :** Clone the Repository : 

```bash
  git clone https://github.com/AkshataKamerkar/GestureFlow.git
```

**Step 2 :** Set Up Environment and Dependencies
* **Install Python :**  Ensure Python (preferably Python 3.x) is installed on your system.

* **Install Required Libraries :** Navigate to the project directory and install the necessary Python libraries by running -

```bash
  pip install -r requirements.txt

```
If there's a requirements.txt file in the project, this command installs all the dependencies needed for the project to run.

**Step 3 :** Configure and Run the Project

* **Place Presentation Slides :** Follow the project's instructions to place the presentation slides in the designated folder (ppt or as specified).

* **Adjust Configuration (if required) :** Modify any configuration parameters in the code if needed, such as webcam resolution or folder paths.

* **Run the Script :** Execute the Python script that controls the presentation slides - 

```bash
  python main.py

```

* **Interact with the Presentation :** Use the hand gestures as specified in the project's README to control and interact with the presentation slides via the webcam.


**Step 4 :** Quitting the Application
Press the specified keyboard key 'q' to exit or close the application when done.

## Conclusion

The system offers a convenient gesture-based command to swiftly clear annotations. With a specific gesture, presenters can reset the slide, removing any drawn annotations instantly. This functionality ensures a clean slate for new annotations or a clear view of the original slide content.
## Contributors

* ak_639
* shubham-murtadak
* ItachiUchiha08
