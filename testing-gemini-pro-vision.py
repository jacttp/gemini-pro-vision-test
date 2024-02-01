import os
import google.generativeai as genai 

os.environ['GOOGLE_API_KEY'] = "YOUR_GOOGLE_API_KEY"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

import PIL

#1. We ask it to describe the image.
query1 = "Explain the picture in spanish?"
print(f"USER::: {query1}")

image = PIL.Image.open('assets/sample_image.jpg')
vision_model = genai.GenerativeModel('gemini-pro-vision')
response = vision_model.generate_content([query1, image])
print(response.text)
print("\n\n\n")

# # 2. We ask it to write a story
query2 = "Write a story from the picture in spanish"
print(f"USER:::: {query2}")

image = PIL.Image.open('assets/sample_image2.jpg')
vision_model = genai.GenerativeModel('gemini-pro-vision')
response = vision_model.generate_content([query2,image])
print(response.text)
print("\n\n\n")

# 3. We ask it to count the objects from an image, the response in json format. 
query3 = "Generate a json of ingredients, with their count present in the image"
print(f"USER::: {query3}")
image = PIL.Image.open('assets/sample_image3.jpg')
vision_model = genai.GenerativeModel('gemini-pro-vision')
response = vision_model.generate_content([query3,image])
print(response.text)

#We ask it for my homework

# image = PIL.Image.open('assets/sample_image3.jpg')
# vision_model = genai.GenerativeModel('gemini-pro-vision')
# response = vision_model.generate_content(['What Bussiness Inteligence information can I get with multiple tickets like that?', image])
# print(response.text)