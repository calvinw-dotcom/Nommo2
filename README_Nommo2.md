
# Nommo2

**Nommo2** is a Django-based web application that provides a Text-to-Speech (TTS) service. Users can input text, and the system generates MP3 audio files from the text using backend logic. It features user authentication, a dashboard, and request tracking.

## Features

- User registration and login
- Upload or input text for TTS conversion
- Automatic generation of MP3 files
- Dashboard with request history
- Admin interface for managing requests
- Static frontend with basic styling

## Project Structure

```
Nommo2/
├── manage.py
├── db.sqlite3
├── media/
│   └── mp3_files/
├── nommo/               # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── tts/                 # Main app for TTS functionality
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── templates/
│   │   └── tts/
│   └── ...
├── Static/
│   ├── CSS/
│   └── js/
```

## Getting Started

### Prerequisites

- Python 3.10 or newer
- pip
- virtualenv (recommended)

### Installation

1. Clone or extract the project.
2. Navigate to the project directory:
   ```bash
   cd Nommo2
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt  # You may need to create this manually
   ```
5. Apply migrations:
   ```bash
   python manage.py migrate
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```

### Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

## Usage

1. Navigate to `http://127.0.0.1:8000/`
2. Register or log in.
3. Use the dashboard to submit text and generate MP3 files.
4. Download or play the audio files from the interface.

## Notes

- MP3 files are stored under `media/mp3_files/`
- Templates are located in `tts/templates/tts/`
- Static files are under `Static/`

## License

This project does not currently include a license file. Please add one to specify usage terms.
