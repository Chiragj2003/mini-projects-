# 🐍 Python Mini Projects Collection

A collection of beginner-friendly to intermediate Python projects organized in separate folders. Each project is self-contained with its own code and documentation.

## 📁 Projects List

### 🔐 Security & Utilities
- **[password-manager/](password-manager/)** - Secure password manager with encryption
- **[chatbot/](chatbot/)** - AI chatbot using OpenAI's GPT-3.5 Turbo
- **[qr-code-generator/](qr-code-generator/)** - Generate QR codes from text/URLs

### 💰 Finance & Productivity
- **[expense-tracker/](expense-tracker/)** - Track daily expenses with charts and reports
- **[pomodoro-timer/](pomodoro-timer/)** - Productivity timer based on Pomodoro Technique
- **[file-organizer/](file-organizer/)** - Auto-organize files into categorized folders
- **[currency-converter/](currency-converter/)** - Real-time currency converter with 150+ currencies

### 🌐 Web & API Projects
- **[weather-detection/](weather-detection/)** - Real-time weather information with GUI
- **[internet-speed-test/](internet-speed-test/)** - Test your internet connection speed
- **[language-translator/](language-translator/)** - Translate text between languages

### 🎮 Games & Entertainment
- **[rock-paper-scissors/](rock-paper-scissors/)** - Classic game against computer
- **[tic-tac-toe/](tic-tac-toe/)** - Tic-tac-toe with GUI
- **[mini-games/](mini-games/)** - Blackjack and Caesar Cipher games

### 📝 Productivity Tools
- **[text-editor/](text-editor/)** - Simple text editor with save functionality
- **[typing-speed-test/](typing-speed-test/)** - Test your typing speed and accuracy
- **[youtube-video-manager/](youtube-video-manager/)** - Manage YouTube video lists
- **[time-greeting/](time-greeting/)** - Time-based greeting system

### 🎵 Media
- **[music-player/](music-player/)** - GUI-based MP3 music player
- **[morse-code-translator/](morse-code-translator/)** - Encode/decode Morse code

## 🚀 Getting Started

Each project has its own folder with:
- Python script(s)
- README.md (where applicable)
- Requirements (if any)

Navigate to any project folder and run:
```bash
python <project_name>.py
```

## 📦 Common Dependencies

Some projects may require:
```bash
pip install tkinter pygame cryptography requests openai qrcode translate speedtest-cli
```

---

## 📖 Featured Projects

### 🔐 Password Manager
Secure command-line password manager with military-grade encryption. Store, retrieve, and manage passwords safely with master password protection.

### 💰 Expense Tracker
Track your daily expenses with detailed reports and beautiful visualizations. Features monthly summaries, category-based filtering, and multiple chart types for analyzing spending patterns.

### 🍅 Pomodoro Timer
Beautiful productivity timer with GUI based on the Pomodoro Technique. Features 25-minute work sessions, automatic breaks, sound notifications, and daily statistics tracking.

### 📁 File Organizer
Automatically organize messy folders by categorizing files into 12+ predefined categories. Features dry run mode, undo functionality, statistics, and detailed logging.

### 💱 Currency Converter
Real-time currency converter with beautiful GUI supporting 150+ world currencies. Features smart caching, conversion history, offline mode, and quick access to popular currency rates.


# Speed Test Code 
Imagine a program that lets you test your internet speed with just a click
! This Python script builds a basic screen with a "Start Test" button. Once 
you click it, the program uses a tool called "speedtest" to measure how fast your
internet uploads and downloads data, and how long it takes to connect to websites. 
It then displays the results on the screen, showing you download speed (for things like streaming videos)
, upload speed (for sending emails or photos), and even the 
response time (how long it takes to talk to websites). It's like having a mini 
internet speedometer for your computer!
While this program works well, it can be improved by removing unnecessary 
windows and organizing the code more neatly. But overall, it's a cool example of using Python to create a simple and helpful tool!

# Typing speed and accuracy test 
This Python script conducts a typing speed and accuracy test. It randomly selects a sentence from a predefined list, prompts the user to type it, measures the time taken, and calculates typing speed and accuracy. The program showcases random sentence generation, input handling, and basic performance metrics. Users receive feedback on their typing speed, accuracy, and overall performance after completing the test.


# Language Translation Using Tkinter 

This Python script implements a simple language translation application using Tkinter and the `translate` library. The application provides a user-friendly interface for translating text from one language to another.

# youtube video manager 
This Python script manages YouTube videos with functionalities to list, add, update, and delete videos stored in a JSON file. It provides a text-based menu for user interaction, allowing seamless video management and updates while maintaining data integrity by saving changes to the file.

## Features
- **Language Selection:** Users can choose both the input language and the target language from a list of available options, including Hindi, English, French, German, and Spanish.
- **Text Input and Output:** Enter the text to be translated in the "Enter Text" field, and the translated output will be displayed in the "Output Text" field. Tkinter StringVar variables are used to dynamically link input and output fields.
- **Translation Functionality:** The translation is performed using the `translate` function from the `translate` library. The translation function is triggered when the user clicks the "Translate" button.
- **Graphical User Interface:** The Tkinter library is utilized to create a basic graphical user interface with labels, entry fields, drop-down menus, and a translation button.

## Dependencies

- Tkinter
- `translate`

## Further Customization

Feel free to customize the code or expand the application by adding more features, error handling, or enhancing the user interface.

## Conclusion

This language translation application serves as a practical example for beginners interested in building graphical applications for language processing tasks. Explore the code, experiment with different languages, and adapt it to your specific needs.


