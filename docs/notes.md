# Development Notes

<br>

## Day 1 - 09/10/2026 *(4h)*

### Work Done
Implemented part of the core application logic and created a reuseable text rendering function for the UI. Prepared the main loop for handling events, updating the application, and rendering each frame.

Also implemented a system that keeps the canvas resolution independent of the actual window size, allowing the window to be resized without changing the logical resolution.

### Problems & Dicisions
Seperated event handling, updates, and rendering into distinct steps to keep the main loop organized and make future extensions easier to implement.

One of the first challenges was creating a stable and reuseable text renderer. I decided to implment it as a function rather than a class top keep the design simple and avoid unnecessary complexity.

### Result & Next Steps
Completed the initinal foundation of the application. Next, I plan to implement the menu system and it's UI elements.

<br>

## Day 2 - 10/10/2026 *(6h)*

### Work Done
Added a documentation explaining the rules of Conway's Game of Life. Implemented a scene managment system for switching between scenes and handling transitions. Also started developing the main menu and it's buttons.

### Problems & Dicisions
Decided to seperate scene managment from invdividual scenes to keep the application structure modular. This makes it easier to add new scenes and handle transition without putting everything into the main loop.

Also started organizing the menu elements into reuseable components to avoid duplicating UI logic.

### Result & Next Steps
Finished the basic structure for scene switching and continued building the main menu. Next, I plan to improve UI with animations and more polished feedback.

<br>

## Day 3 - 11/10/2026 *(5h)*

### Work Done
Implemented an animation system for UI elements, allowing interface components to animate instead of changing instantly. Also reorginized the folder structure to make the project easier to navigate and maintain.

### Problems & Dicisions
Focused on making UI animations reuseable so that different elements can use the same logic rather thann requiring separate implementations.

Continued seperating responsibilities across modules to keep the code organized and make future features easier to integrate.

### Result & Next Steps
Improved the foundation of the UI system and made the project structure more maintainable. Next, I plan to finish polishing the main menu, refine the button animations, and prepare other menus and the actual Game of Life functionality.

<br>

## Day 4 - 12/10/2026 *(break)*

Decided to take a break on this day due to school.

<br>

## Day 5 - 13/10/2026 *(4h)*

### Work Done
Implemented the grid representation and camera movement. Added cell placement and removal, as well as some first UI elements to the hotbar, including back, run/pause, and other controls. Implemented alive cell rendering and the actual Game of Life simulation logic.

### Problems & Dicisions
Getting the positioning to work correctly with the camera was challenging because I had only worked with centered coordinate systems in the past. Especially making the zoom focus on the center of the screen rather than the top left corner was difficult. To find a solution, I experiemented with several approaches. I also asked a friend to compose a menu theme for the project, since I have no experience in music composition TvT

### Result & Next Steps
The core simulation is now working, including camera controls, cell interaction, rendering, and the basic Game of Life rules. Next, I plan to expand the editor functionality by adding features such as holding the mouse button to continuously place or remove cells, copying and pasting patterns, and improving some other stuff.

## Day 6 - 14/10/2026 *(break)*

Decided to take another break to think about some ideas.

<br>

## Day 7 - 15/10/2026 *(4h)*

### Work Done
Added a world border to the grid, integraded the music theme into the editor, and implemented undo and redo.

### Problems & Dicisions
I decided to implement a world border first because I'm currently looking for ways to improve the performance when handling a large number of cells. I'm thinking about implementing a chunk system, but I want to reasearch how Conway's Game of Life implementations handle large grids before deciding on a approach.

For now, I also decided to keep the editor simple and keep out features such as copy-paste and continuous cell placement. The copy-paste could benefit from the chunk system, so I want to make a stable grid architecture before adding some advanced editing features.

### Result & Next Steps
The editor now has a defined world boundary, includes the music theme, and allows users to undo and redo changes. Next I will focus on my other projects for a while before continuing work on this one.