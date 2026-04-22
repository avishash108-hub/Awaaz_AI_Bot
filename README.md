# Awaaz_AI_Bot
### Team Techie
> A Telegram-based support chatbot that provides immediate emotional assistance,
> legal awareness, and guidance to verified support resources for individuals
> affected by domestic violence, in a gender-neutral and inclusive manner.

# Problem Statement
Domestic violence and its consequences affect individuals across all genders,
ages, and social backgrounds. Beyond direct harm, it often leads to emotional,
mental, and physical distress, as well as child neglect and long-term trauma.
Many affected individuals struggle with:
- Seeking help anonymously
- Knowing their legal rights
- Finding reliable helplines or shelters
- Having a safe space to be heard without judgment

# Our Solution
"Awaaz AI bot" is designed as an inclusive, privacy-conscious first-response
support chatbot that:
- Provides empathetic and non-judgmental listening
- Supports users experiencing emotional, mental, physical, online, verbal or sexual abuse
- Addresses the impact of domestic violence on children, including neglect
- Shares general legal awareness and verified helpline and nearby shelter information
- Maintains complete user anonymity
The bot does not assume gender, role, or identity, ensuring inclusive and
respectful interaction for all users

# Privacy and Anonymity
- No personal user data is stored
- Conversations are not logged or persisted
- No authentication or identification is required
- Designed to allow users to speak freely and safely
User anonymity is a core design principle, not an afterthought

# System Flow
1. User interacts with the bot via Telegram
2. Telegram sends updates to the backend using a webhook
3. A Flask server (deployed on Render) processes the request
4. Messages are forwarded to Dialogflow ES for intent handling
5. The response is sent back to the user through the same pipeline

# Technical Setup
- Language: Python 3
- Backend Framework: Flask
- Deployment Platform: Render
- Messaging Platform: Telegram Bot API
- Intent Handling: Dialogflow ES
- Database: None (stateless architecture)

# Environment Variables
BOT_TOKEN = telegram_bot_token
GOOGLE_APPLICATION_CREDENTIALS_JSON
DIALOGFLOW_PROJECT_ID


# Design Principles
- Gender-neutral and inclusive communication
- Privacy-first and anonymous usage
- No storage of sensitive user data
- Emotion-first responses before informational guidance
- Safe handling of sensitive topics such as abuse and neglect
- Intent-based system in order to make sure the information provided to user is reliable and verified

# Disclaimer
~ This project was developed as part of a hackathon and is intended for
educational, awareness, and demonstration purposes only.
~ The bot does not replace professional counseling, legal advice, or emergency
services. Users are encouraged to reach out to official helplines or local
authorities in critical situations.

### Security
All API keys and credentials are managed via environment variables.
No secrets or private keys are committed to the repository.


# Team
Team Name: Team Techie
- Avisha Sharma : Backend / Research
- Bhuvi Gupta : NLP / Content

# Future Scope
- Multilingual and voice-based support to increase accessibility
- Improve emergency response of the bot
- Improve intents and responses
- Region-specific resources and shelters information (by integrating Google Map API)
- Improved child support

# License
This project is released under the MIT License as part of an open‑source hackathon submission.


