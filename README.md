# qtCamFeed
The code simply displays your webcam feed. 
QtThreads are used for functionality of the GUI, camera and plotting together. 

The code currently starts the feed when START is pressed, and stops with STOP. After pressing STOP though, the START button no longer updates the plot. The camera feed does start again and will be blocked after the message queue transfering the images between the threads is filled. 

