#from keras.models import load_model


#Import CNN Model for character recognition
#char_model = load_model('CNN models/Arabic_OCR_model.h5')

#Import CNN Model for digit recognition
#digit_model = load_model('CNN models/Digit_OCR_model.h5')

output_string = ""


#make a dictionary for the Arabic Char from 0 - 27

output_file = open("outputfile.txt" , "w" )

# for loop over the folders with the name 0 to 18
# for loop over the images inside the folders

# Pre processing for each image
#img = cv2.imread('p7.png',1)

# Convert to Gray
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#convert to binary
#new= image > (150)
#new = new.reshape(1, 32, 32,1).astype('float32')

#check the image is all white and if yes put a " " in the output file

#y = loaded_model.predict_classes(new)
# map the y to the coressponding char
# in case of digit no need yo map

# Close opend file
output_file.close()