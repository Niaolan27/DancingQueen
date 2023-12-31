# DancingQueen - KKB Dance

KKB Dance is an interactive game which combines elements of Just Dance and Osu. A player can select a song to dance to, and rectangles will spawn according to the beats of the song. The player earns points by using his wrists to destroy the rectangles. 

## Code Explanation
We utilized Object-Oriented Programming (OOP) for our game. We had 3 main classes: Game, Music and View. The Game class represented each instance of the game and contained parameters such as score and positions. The Music class contains information about the song selected, such as the filepath and title. The View class is responsible for opening up the webcam and drawing of shapes.

We used Librosa to detect the beats in the song. The speed of generating rectangles is determined by taking an integer k and dividing it by the BPM of the song. This generates the rectangles at a consistent beat in sync with the music.

We used Mediapipe for our pose estimation model to detect the positions of the wrists. To determine if there is a collision between the wrist and rectangles, we checked for dot-in-rectangle in our calculations. 

The frontend for the start/end pages of KKB Dance is developed using Tkinter. 

The drawing of rectangles and displaying of score onto the webcam canvas is done using OpenCV. 

## Instructions to run the code
### For Windows only (for now)
1. Git clone this repository
`git clone https://github.com/Niaolan27/DancingQueen.git`
2. Enter into the src/src/ folder. This is the folder containing all the code needed to run the game.
3. Pip install the necessary packages in the requirements.txt file.
`pip install -r requirements.txt`
4. Run the code by running main.py

