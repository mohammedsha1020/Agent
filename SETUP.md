# Setup Guide

This guide provides detailed instructions for setting up and configuring the Agent project.

## System Requirements

### Operating System
- Windows 10/11
- macOS 10.14 or later
- Linux (Ubuntu 18.04+ recommended)

### Software Requirements
- Python 3.8 or higher
- pip (Python package manager)
- Git
- Internet connection (for API calls)

## Step-by-Step Installation

### 1. Install Python

#### Windows
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer and check "Add Python to PATH"
3. Verify installation: `python --version`

#### macOS
```bash
# Using Homebrew (recommended)
brew install python3

# Or download from python.org
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### 2. Clone the Repository

```bash
git clone https://github.com/mohammedsha1020/Agent.git
cd Agent
```

### 3. Set Up Virtual Environment

Creating a virtual environment is strongly recommended to avoid dependency conflicts.

```bash
# Create virtual environment
python3 -m venv agent_env

# Activate virtual environment
# On Windows:
agent_env\Scripts\activate

# On macOS/Linux:
source agent_env/bin/activate
```

### 4. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Configure Environment Variables

#### Create .env file
```bash
cp .env.example .env
```

#### Edit .env file
Open `.env` in your preferred text editor and add your Google API key:

```bash
GOOGLE_API_KEY=your_actual_google_api_key_here
```

## Getting Google API Key

### Step 1: Access Google AI Studio
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account

### Step 2: Create API Key
1. Click "Create API key"
2. Select an existing project or create a new one
3. Copy the generated API key

### Step 3: Configure API Key
1. Open your `.env` file
2. Replace `your_google_api_key_here` with your actual API key
3. Save the file

## Verification

### Test Installation

#### Test Python Environment
```bash
python3 -c "import sys; print(f'Python {sys.version}')"
```

#### Test Dependencies
```bash
python3 -c "import crewai; print('CrewAI installed successfully')"
python3 -c "import dotenv; print('python-dotenv installed successfully')"
```

#### Test API Configuration
```bash
python3 -c "
from dotenv import load_dotenv
import os
load_dotenv()
key = os.environ.get('GOOGLE_API_KEY')
print('API key configured' if key and key != 'your_google_api_key_here' else 'API key not configured')
"
```

### Quick Test Run

#### Test Research Agent
```bash
python Single_Agent.py
# Enter a simple topic like "Python programming" when prompted
```

#### Test Website Development (Optional)
```bash
python Website_Developer_Using_CrewAi.py
# Enter a simple description like "simple landing page" when prompted
# Note: This may take several minutes and use API quota
```

## Troubleshooting

### Common Issues

#### Issue: "ModuleNotFoundError: No module named 'crewai'"
**Solution:**
```bash
# Ensure virtual environment is activated
source agent_env/bin/activate  # macOS/Linux
# or
agent_env\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

#### Issue: "API key not configured" or authentication errors
**Solution:**
1. Verify `.env` file exists and contains your API key
2. Ensure no extra spaces around the API key
3. Restart your terminal/command prompt
4. Check API key validity at Google AI Studio

#### Issue: "Permission denied" on Linux/macOS
**Solution:**
```bash
# Make scripts executable
chmod +x Single_Agent.py
chmod +x Website_Developer_Using_CrewAi.py
```

#### Issue: Slow performance or timeouts
**Solution:**
1. Check internet connection
2. Verify Google API quota limits
3. Consider reducing temperature settings in scripts (lower values = faster responses)

### Performance Optimization

#### Reduce API Usage
- Use lower temperature values (0.1-0.3) for faster, more focused responses
- Limit the scope of research topics
- Cache results when possible

#### Speed Up Development
- Use smaller project descriptions for website development
- Test with simple requirements first
- Monitor API usage in Google Cloud Console

## Advanced Configuration

### Custom LLM Settings

You can modify LLM parameters in the Python files:

```python
llm = LLM(
    model="gemini/gemini-1.5-flash",
    temperature=0.3,  # Lower = more focused, Higher = more creative
    api_key=os.environ.get("GOOGLE_API_KEY"),
    max_tokens=2048   # Adjust based on needs
)
```

### Environment Variables

Additional environment variables you can set in `.env`:

```bash
# Google API Key (required)
GOOGLE_API_KEY=your_api_key

# Optional: Custom model settings
LLM_TEMPERATURE=0.3
LLM_MAX_TOKENS=2048

# Optional: Output directories
OUTPUT_DIR=./generated_projects
```

## Development Setup

If you plan to contribute or modify the code:

### Install Development Dependencies
```bash
pip install black flake8 pytest
```

### Code Formatting
```bash
black *.py
```

### Code Linting
```bash
flake8 *.py
```

## Next Steps

After successful setup:

1. Read the main [README.md](README.md) for usage overview
2. Check [EXAMPLES.md](EXAMPLES.md) for detailed usage examples
3. Start with simple research topics to test the system
4. Gradually explore more complex website development projects

## Support

If you encounter issues not covered here:

1. Check the [main README](README.md) for basic usage
2. Review [EXAMPLES.md](EXAMPLES.md) for working examples
3. Open an issue on GitHub with:
   - Your operating system
   - Python version
   - Error messages
   - Steps to reproduce the issue