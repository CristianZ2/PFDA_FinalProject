# Project Title: Road Kill

**Repository:** `https://github.com/CristianZ2/PFDA_FinalProject.git`

# Video Presentation

**Youtube Link:** https://youtu.be/o8m5OGQTGDw?si=bk3z2dQSPan75g-j

# About the Project

- The project is inspired by the classic game "Frogger," the concept of the game "Road Kill," is for the player to get to the ocean by avoiding getting hit by the cars. This project was done using three main feature (collusion, score, and player and enemy movement). 

# Project Descrption

- **Font:** I added different types of font in the game to give it a different design. I went online and downloaded two types of font for the win and lose prompt and the score font. 

- **Image Render:** In this project I imported image assests to create the player character, enemy character and the win bound. By doing this I used the pygame.image.render to help render each of these images that in the project. Once I imported the images, I will than use the pygame.transform to scale the image and placed them to a certain coordinate on the screen. I would also use the same function to rotate the image and flip them to face the opposite direction as well. 

- **Collusion:** In order to have the game end or have the player win, I needed to add collusion for the player, car, and the win bound. In the player class and class I added "self.rect," to create a collusion box over the player, car, and the win area. It will activate when the player collides with the car which will end the game and reset it. Also when the player collides with the win area they will get a win prompt and a point for making it. 

- **Scoring System:** The scoring system helps keep up with the player progress in the game. Everytime the player avoids the car and gets to the win area they recieve a point. However, anytime they collide with the car they lose and the game resets their score.

# Cites
- https://courses.nelsonlim.com/courses/take/PFDA/lessons/49598389-intro-to-pillow

- https://www.pygame.org/docs/

- https://youtu.be/Vose-mfhtiY?si=GBQ1sGlYqXHGswEU

- https://youtu.be/tK-r89FYF-M?si=pXEiSLygdB_izGE6

- https://cs50.ai/

