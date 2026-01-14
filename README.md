Mango Chat BOT
A persistent Telegram assistant integrated with OpenAI GPT models for automated natural language processing.

Project Overview
This application is a Python-based Telegram bot designed for high availability on cloud infrastructure. It utilizes asynchronous programming to manage concurrent user interactions and features an integrated health-check system to maintain 24/7 uptime on the Render platform.

Live Demo
The bot is active and can be tested here: t.me/YourBotUsername

Technical Implementation
Asynchronous Message Handling
The bot is built using aiogram 3.x, leveraging Python's asyncio library. This ensures non-blocking I/O operations, allowing the bot to process multiple user messages simultaneously without latency.

AI Integration
Natural language understanding is powered by the OpenAI API (GPT-3.5-turbo). The system is configured with specific system prompts to ensure concise and relevant responses.

Cloud Optimization and Uptime
To address the inactivity timeouts associated with free-tier cloud hosting (Render), the project includes a secondary Flask-based web server. A dedicated background thread executes a self-pinging routine every 10 minutes, ensuring the service remains active without manual intervention.

Security
All sensitive credentials, including the Telegram Bot Token and OpenAI API Key, are managed through environment variables. This prevents the exposure of secrets within the version control system.

Project Structure
main.py: Core application logic, Telegram polling, and API integration.
example.py: Flask web server and multi-threaded keep-alive logic.
requirements.txt: List of dependencies including aiogram, flask, and requests.
