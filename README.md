# InteractiveImagePerspectiveTransformation

I happened to about 300 photos with my phone of a book I needed to read. 
After doing so, I wanted to use an application for perspective transformation and so I began searching for an application that would allow me to do so by selecting four corners of my quadrangle. 
I was unable to find a manual QUAD to QUAD image perception tranformation application for sets of images so in turn...

# I've created a rough project to allow you to:
1) Input a folder path filled with raw photo images 
2) Input a specified output path (path must already be created, it will not create folders)
3) Process each image manually by traversing through each image and allow you to choose four points of the page (click the "c" key to cancel early and keep processed images)
4) See what photos you have "fixed" in a small list in GUI
5) Use the specified output path to filter the images into a PDF File. (I have specified a width that happened to fit my photos in the page most appropriately, you may want to switch it to cater to your needs)
6) You may view the PDF by going to the main directory and opening "output.pdf"

# End points
I hope that this code can help someone else accomplish similiar tasks. Please continue to credit. I do know about using OpenCV's contouring and boundry boxes, but due to the fact that I was taking hundreds of photos quickly, the shape of each page became too distorted and skewed to rely on computer vision.

I continue to believe that taking photos of all the pages and creating this entire program has taken less time than it would have had I turned and scanned each individial page in the book in a flatbed scanner. 

![Preview](https://i.gyazo.com/85a54b300d834bef5dd7c7f5c1e860f6.png)
