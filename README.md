# LLM

Gemini Function Calling Quickstart (Python)
This project shows you how to make Google's Gemini AI model "call" a function in your Python code. We'll build a simple program where you can ask for the weather, and Gemini will tell your code to fetch it!

What You'll Learn: 
  How to get your Gemini API key from Gemini AI Studio.
  How to set up your Python environment.
  How to run a simple Gemini app that uses "function calling."
  
1. Get Your Gemini API Key
This key lets your program talk to Google's Gemini AI.

Go to Gemini AI Studio and sign in with your Google account.
In the left sidebar, click on "Get API key".
Click "Create API key in new project" (or use an existing one if you have it).
Copy the API key that appears. Keep this key secret! Never share it or put it directly in your code.
2. Set Up Your Project
Let's prepare your computer for the code.

Create a Project Folder:
Open your command prompt (or terminal) and type:

Bash/cmd

mkdir gemini-weather-app
cd gemini-weather-app
Create a Virtual Environment:
This keeps your project's Python libraries separate.

Bash/cmd

python -m venv venv
Activate Your Virtual Environment:

Windows:
Bash/cmd

.\venv\Scripts\activate
macOS / Linux:
Bash/cmd

source venv/bin/activate
(You'll see (venv) appear before your command prompt, meaning it's active.)

Install Python Libraries:

Bash/cmd

pip install google-generativeai python-dotenv
3. Store Your API Key Safely
We'll use a .env file to keep your API key secure.

Create a .env file:
In your gemini-weather-app folder, create a new file named .env (that's a dot then "env").

Add Your Key to .env:
Open the .env file and add this line, replacing YOUR_GEMINI_API_KEY_HERE with the actual key you copied earlier:

GOOGLE_API_KEY=YOUR_GEMINI_API_KEY_HERE
Example: GOOGLE_API_KEY=AIzaSyBwZrK6Vvhi0mjVtkHdqVokIDjhMlAJ1uo (this is just an example, use your key).

Important for GitHub: If you plan to put this project on GitHub, create another file called .gitignore in the same folder and add this line to it:

.env
This prevents you from accidentally sharing your secret key!
