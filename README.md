# ai-bot

This repository hosts the source code for a simple Flask based AI bot.

## Deploying to a VPS

Follow these steps to set up the project on a virtual private server and run it in a production setting:

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/ai-bot.git
   cd ai-bot
   ```

2. **Create and activate a Python virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Run the Flask app with a production server**

   Install `gunicorn` if it is not already installed and run it behind `nginx`:

   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 127.0.0.1:8000 app:app
   ```

   Then configure `nginx` to proxy requests to `http://127.0.0.1:8000`.

4. **Configure environment variables**

   Store API keys and other sensitive settings as environment variables. A typical approach is to create a `.env` file and load it before starting the server:

   ```bash
   export OPENAI_API_KEY=your_api_key_here
   export OTHER_SETTING=value
   ```

   Tools like `dotenv` can be used to automatically load these variables on startup.

