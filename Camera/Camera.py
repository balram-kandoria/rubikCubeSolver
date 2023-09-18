import os
import cv2
from PIL import Image
import natsort

class Camera():
    def __init__(self):

        self.ImageDirectory = "/home/pi1/Desktop/Rubik/rubikCubeSolver/Camera/Images/"
        self.Resolution = "1920x1080"
        self.delay = "0.5"
        self.skip = "30"
        self.frameReference = "5"
        self.OutputDirectory = "/home/pi1/Desktop/Rubik/rubikCubeSolver/Solution"
        print("=====================Camera Init===================================")
        print("Camera Initiated: TBI")
        print("Future Installation Site")
        print("===================================================================")
    
    def takeImage(self, ImageNumber):

        imageFrameName = self.ImageDirectory + "output" + str(ImageNumber) + ".png"
        os.system(f"fswebcam -r {self.Resolution} -pMJPEG -S {self.skip} -D {self.delay} -F {self.frameReference} -q --save {imageFrameName}")

    def createVideo(self):
        # Checking the current directory path
        print(os.getcwd())

        # Folder which contains all the images
        # from which video is to be generated
        os.chdir(self.ImageDirectory)
        path = self.ImageDirectory

        mean_height = 0
        mean_width = 0

        num_of_images = len(os.listdir('.'))
        print(num_of_images)

        for file in os.listdir('.'):
            if file.find(".png") != -1:
                im = Image.open(os.path.join(path, file))
                width, height = im.size
                mean_width += width
                mean_height += height
            # im.show()   # uncomment this for displaying the image

        # Finding the mean height and width of all images.
        # This is required because the video frame needs
        # to be set with same width and height. Otherwise
        # images not equal to that width height will not get
        # embedded into the video
        mean_width = int(mean_width / num_of_images)
        mean_height = int(mean_height / num_of_images)

        # print(mean_height)
        # print(mean_width)

        # Resizing of the images to give
        # them same width and height
        for file in os.listdir('.'):
            if file.endswith("png"):
                # opening image using PIL Image
                im = Image.open(os.path.join(path, file))

                # im.size includes the height and width of image
                width, height = im.size
                print(width, height)

                # resizing
                imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
                # imResize.save(file, 'JPEG', quality=95)  # setting quality
                # printing each resized image name
                print(im.filename.split('\\')[-1], " is resized")

        # Video Generating function

        def generate_video(self):
            # image_folder = self.OutputDirectory  # make sure to use your folder
            video_name = 'mygeneratedvideo.avi'
            os.chdir(self.OutputDirectory)

            images = [img for img in os.listdir(self.ImageDirectory)
                    if img.endswith("png")]

            # Array images should only consider
            # the image files ignoring others if any

            images = natsort.natsorted(images, reverse=False)
            print(images)

            frame = cv2.imread(os.path.join(self.ImageDirectory, images[0]))

            # setting the frame width, height width
            # the width, height of first image
            height, width, layers = frame.shape

            video = cv2.VideoWriter(video_name, 0, 1, (width, height))

            # Appending the images to the video one by one
            for image in images:
                video.write(cv2.imread(os.path.join(self.ImageDirectory, image)))

            # Deallocating memories taken for window creation
            cv2.destroyAllWindows()
            video.release()  # releasing the video generated

        # Calling the generate_video function
        generate_video(self)
            

