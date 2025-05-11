# AI Quiz Scheduler

An intelligent study schedule generator that uses Google's Gemini AI to create personalized study plans based on your topics and knowledge levels.

## Features

- Input multiple study topics
- Rate your knowledge level for each topic (1-5 scale)
- Specify the number of days for your study schedule
- Add additional notes and requirements
- AI-powered schedule generation using Google Gemini
- Clean and intuitive user interface

## Prerequisites

- Python 3.8 or higher
- Google Gemini API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-quiz-scheduler.git
cd ai-quiz-scheduler
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Set up your Google Gemini API key:
   - Create a `.streamlit/secrets.toml` file
   - Add your API key:
   ```toml
   GOOGLE_API_KEY = "your-api-key-here"
   ```

## Usage

1. Start the Streamlit app:
```bash
streamlit run src/app.py
```

2. Open your web browser and navigate to the provided local URL (usually http://localhost:8501)

3. Enter your study parameters:
   - Number of days
   - Topics (comma-separated)
   - Knowledge scores for each topic
   - Any additional notes

4. Click "Generate Schedule" to create your personalized study plan

## Project Structure

```
ai-quiz-scheduler/
├── .streamlit/
│   └── secrets.toml
├── src/
│   └── app.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google Gemini AI for the scheduling intelligence
- Streamlit for the web interface framework 