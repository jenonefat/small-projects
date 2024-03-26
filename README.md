# small-projects

## General description: 
    These were some fun, simple programs I wrote to explore some Python packages that I was previously unfamiliar with. 
    I moreover wanted to consider how Python can be employed to automate practical, daily tasks. 
    I used the following tutorial as a guide for 'YT_video_download' & 'PDF_merger': https://www.youtube.com/watch?v=vEQ8CXFWLZU
    and this tutorial as a guide for 'weather_API': https://www.youtube.com/watch?v=Oz3W-LKfafE&t=2612s


### YouTube Video Download 
This program can be used to download a YouTube video to your device. It comes in handy if you want to be able to watch a particular video at a later time when you won't have 
internet access! 
I used the *pytube* library and created a YouTube object that requires a link to the video to be passed in as an arg. 
After getting the highest resolution stream for that video, I downloaded it to my 'Downloads' folder on my mac. 


### Weather API
This program returns the current general weather pattern and temperature (in Celsius) in a given city.
This project is a great way to be introduced to API requests! 
After making an account on the **Open Weather** site, I was able to get a free API key to access their data. 
I constructed a request URL using the Open Weather base URL, as well as my personal API key and the city name as query parameters.
I sent an API request to the weather site using the very useful *requests* Python library.
After verifying that there were no issues with the request, I converted the response format into JSON, which made it more convenient 
to grab weather and temperature data. 
When you run this program, you should see something like this: 
    'Enter city name:' 
    *After you enter a city name,* 
    'Weather: clear sky' 
    'Temperature: 16.29 Celsius' 


### Merging PDF files
This program merges/combines separate PDF files to create a new file ('combined.pdf'). 
I created a 'merger' object using the *PyPDF2* library.
The program iterates through the current working directory and appends only pdf files to the merger object.
The output file containing all merged PDFs is named 'combined.pdf' 
Each file name that was merged into the new output file is printed in the terminal-- this makes it easier for 
the user to verify that all the appropriate pdf files were merged into the aggregate file. 
    
