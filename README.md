

---

# PyBot - Your Friendly Coding Assistant 🤖

**PyBot** is an intelligent and friendly coding assistant chatbot built to help programmers of all skill levels. It can answer coding questions, provide explanations, offer encouragement, and even recall past conversations to make each interaction more personalized. With OpenAI's GPT-3 integration, PyBot brings advanced conversational AI to coding assistance.

## 🌟 Features

- **GPT-3 Powered**: Uses OpenAI's GPT-3 API to provide intelligent responses to coding questions.
- **Memory**: Remembers previous questions and answers to offer continuity in conversations.
- **Skill Adaptation**: Adjusts guidance based on user’s skill level (beginner, intermediate, advanced).
- **Motivational & Friendly**: Offers motivational and encouraging messages to keep coders inspired.
- **Context-Aware Responses**: Personalized greetings based on the time of day and remembers your name.
  
## 📸 Preview

> *Example Interaction*  
> **User**: "What is a Python dictionary?"  
> **PyBot**: "A dictionary in Python is a collection of key-value pairs. Each key is unique and maps to a value. It's useful for storing data that has a meaningful relationship, like name-age pairs."

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- OpenAI API Key (for GPT-3 functionality)
- [OpenAI Python Library](https://pypi.org/project/openai/) (Install using `pip install openai`)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/pybot.git
   cd pybot
   ```

2. **Install required libraries**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key**:
   - Sign up at [OpenAI](https://beta.openai.com/signup/) if you don’t already have an account.
   - Generate an API key and replace `"your-api-key-here"` in the code with your OpenAI API key.

### Running PyBot

Run the following command in your terminal:

```bash
python pybot.py
```

Once running, PyBot will guide you through initial setup and then be ready to answer your coding questions!

## 📋 Usage

- **Ask Coding Questions**: Just type any coding question, and PyBot will provide an answer.
- **Motivational Support**: PyBot can offer friendly encouragement when needed.
- **Goodbye Message**: Type `exit`, `quit`, or `bye` to end the conversation.

## 🛠️ Customization

You can easily modify PyBot by adjusting:

- **Response Templates**: Modify responses in the `self.responses` dictionary to personalize PyBot’s tone and answers.
- **Knowledge Base**: Expand PyBot’s memory by adding frequently asked questions directly to the code for instant recall.

## 🤖 Contributing

Contributions are welcome! If you have ideas for new features or enhancements, feel free to open an issue or submit a pull request.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 💡 Future Enhancements

Some features to consider for future versions:

- **Extended Knowledge Base**: Pre-load answers for common questions to reduce GPT-3 API calls.
- **GUI Support**: Create a graphical interface for more user-friendly interactions.
- **Advanced Memory**: Enable multi-session memory to recall user interactions across sessions.

---
📝 Version Notes

v1.0.0 - Initial Release
Core Features:
GPT-3 Integration: Provides intelligent, conversational responses to coding questions.
Personalized User Interaction: Asks for the user's name and coding skill level to tailor responses.
Memory System: Remembers questions and answers within a single session.
Supportive & Motivational Responses: Offers encouragement and motivation to keep users engaged.
Simple Command Interface: Users can exit by typing "exit", "quit", or "bye".
Planned Features
Enhanced Memory Matching: Improved recall for similar questions across sessions.
Customizable Responses: Options for users to adjust PyBot’s responses and tone.
UI Enhancements: Adding colored output for a more user-friendly experience.
