# AI Photo Organiser

## Image Processing Server
**Problem statement** : 
Create an AI based solution that separates duplicates, blur photos from a given set of photos and logically organizes photos based on location, date etc. This can help create photo albums automatically based on different attributes from the huge number of photos available.

**Overview** : 
The Image Processing Server is a web application that allows users to upload images, process them, and download the processed results. The server performs various image processing tasks, including duplicate removal, blur detection, and location-based sorting.

**Features**
1. Image Upload: Users can upload images through a web interface.
2. Duplicate Removal: The server identifies and removes duplicate images from the uploaded files.
3. Blur Detection: Images are scanned for blur, and blurry images are identified and separated.
4. Location-based Sorting: Images are sorted into folders based on their geographical location, if available in the image metadata.
5. Output Zip Creation: The processed images are packaged into a zip file for easy download by the user.
6. Clean-up: After processing, the server clears uploaded images and processed results to conserve disk space.


**Usage**
1. Navigate to the upload page on the web interface.
2. Select one or more images to upload.
3. Submit the upload form to start image processing.
4. After processing, the server will generate a zip file containing the processed images.
5. Download the zip file from the provided link.
6. The server will automatically clean up uploaded images and processed results to maintain disk space.


**Dependencies**
1. Node.js
2. Express.js
3. Multer
4. Archiver
5. Python (with required libraries for image processing)

