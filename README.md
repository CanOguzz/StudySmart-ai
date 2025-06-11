# StudySmart-ai

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

An intelligent study schedule generator powered by Google's Gemini AI. **StudySmart-ai** helps you create personalized study plans based on your topics, self-assessed knowledge levels, and timeframe—so you can study smarter, not harder.

---

## 🚀 Features

- **Multiple Topics**: Add as many study topics as you need.
- **Knowledge Assessment**: Rate your familiarity with each topic (1-5 scale).
- **Custom Schedule Length**: Specify your available study days.
- **Notes & Requirements**: Add extra notes or requirements for your schedule.
- **AI-Powered Planning**: Uses Google Gemini AI to intelligently generate your study plan.
- **Simple UI**: Clean, intuitive web interface built with Streamlit.

---

## 🖥️ Demo

*Coming soon!* (You can add screenshots or a link to a deployed version here.)

---

## 🏁 Quick Start

### 1. Prerequisites

- Python 3.8 or higher
- Google Gemini API key

### 2. Installation

```bash
git clone https://github.com/CanOguzz/StudySmart-ai.git
cd StudySmart-ai
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure API Key

Create a `.streamlit/secrets.toml` file and add your Gemini API key:

```toml
GOOGLE_API_KEY = "your-api-key-here"
```

### 4. Run the App

```bash
streamlit run src/app.py
```

Open your browser to the provided local URL (usually http://localhost:8501).

---

## 📝 Usage

1. Enter the number of study days, your topics, and knowledge scores.
2. Optionally, provide any notes or special requirements.
3. Click **Generate Schedule** to receive a custom plan.
4. Follow the generated schedule to optimize your study sessions!

---

## 📁 Project Structure

```
StudySmart-ai/
├── .streamlit/
│   └── secrets.toml
├── src/
│   └── app.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork this repo
2. Create a new branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Describe your feature'`)
4. Push to your branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [Google Gemini AI](https://ai.google/) for the intelligence behind planning
- [Streamlit](https://streamlit.io/) for the effortless web interface

---

## 🌟 Show Your Support

If you find this project helpful, please consider giving it a ⭐️ on [GitHub](https://github.com/CanOguzz/StudySmart-ai)!
