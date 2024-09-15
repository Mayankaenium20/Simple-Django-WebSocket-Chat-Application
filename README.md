# Simple-Django-WebSocket-Chat-Application

This project is a basic real-time chat application built using **Django Channels**, **WebSockets**, and **Redis**. It allows users to exchange messages in real-time within a chat room.

## Features
- Real-time messaging using WebSockets.
- Handles multiple users in a chat room.
- Uses Django Channels for WebSocket management.

## Prerequisites

To run this project, you need to have the following installed:

1. Python (>=3.8)
2. Django (>=5.x)
3. Django Channels
4. Redis (for channel layer backend)

## Setup Instructions

### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/chat-app.git
cd chat-app
```

### Step 2: Create and activate a virtual environment

```bash
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

Ensure that `channels` and `channels-redis` are included in your `requirements.txt`.

### Step 4: Install and configure Redis

1. Install Redis (e.g., using Homebrew on macOS):
   ```bash
   brew install redis
   ```
2. Start Redis server:
   ```bash
   brew services start redis
   ```

   Alternatively, on Linux:
   ```bash
   sudo apt-get install redis-server
   sudo service redis-server start
   ```

### Step 5: Configure Django settings

Ensure `settings.py` includes the necessary Channels and Redis configurations:

```python
INSTALLED_APPS = [
    'channels',
    'chat',  # your app
    ...
]

ASGI_APPLICATION = 'mywebsite.asgi.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
```

### Step 6: Run Django Migrations

```bash
python manage.py migrate
```

### Step 7: Start the Django development server

Run both servers (Django and Daphne) in two separate terminals:

1. **Terminal 1** (Django server):
   ```bash
   python manage.py runserver
   ```
   
2. **Terminal 2** (Daphne server):
   ```bash
   daphne -b 127.0.0.1 -p 8001 mywebsite.asgi:application
   ```

### Step 8: Access the Chat Application

Open your browser and go to:
```
http://127.0.0.1:8000
```

### Usage

- Open multiple browser windows or tabs and enter a chat message in one. 
- The message will appear in real-time in all windows or tabs connected to the chat room.

## Folder Structure

```
mywebsite/
│
├── chat/
│   ├── __init__.py
│   ├── consumers.py         # WebSocket consumer logic
│   ├── routing.py           # WebSocket routing
│   ├── urls.py              # HTTP URL routing
│   └── views.py             # HTML view logic
│
├── mywebsite/
│   ├── __init__.py
│   ├── asgi.py              # ASGI configuration for WebSockets
│   └── settings.py          # Django settings
│
├── manage.py                # Django management script
└── requirements.txt         # Python package dependencies
```

## Example

Here's what the messages might look like in the chat room:
```
msg: Hi everyone!
msg: Hello!
```

## Chat Demo

![Chat Demo](path_to_video.mp4)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
