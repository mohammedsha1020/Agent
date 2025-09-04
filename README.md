# Agent

AI-powered automation agents using CrewAI framework for research and professional website development.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Components](#components)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Overview

This repository contains two powerful AI automation tools built with the CrewAI framework:

1. **Single Research Agent** - An AI research assistant that can investigate any topic and provide detailed reports
2. **Professional Website Development Team** - A collaborative team of 8 specialized AI agents that work together to create professional websites

Both tools leverage Google's Gemini LLM to provide intelligent, automated solutions for research and web development tasks.

## Features

### Single Research Agent (`Single_Agent.py`)
- 🔍 Intelligent topic research and analysis
- 📊 Detailed reporting with AI-generated insights
- 🤖 Powered by Google Gemini LLM
- 💬 Interactive command-line interface

### Professional Website Development Team (`Website_Developer_Using_CrewAi.py`)
- 👥 8 specialized AI agents working collaboratively:
  - Project Manager - Planning and coordination
  - Business Analyst - Requirements and user stories
  - UI/UX Designer - Design systems and user experience
  - Frontend Architect - Technical architecture
  - Content Strategist - SEO-optimized copywriting
  - SEO Specialist - Search optimization
  - Frontend Developer - Code implementation
  - QA Engineer - Quality assurance and testing
- 🌐 Generates complete, production-ready websites
- 📱 Mobile-first responsive design
- ♿ WCAG 2.1 AA accessibility compliance
- 🚀 Performance optimized with Core Web Vitals
- 📈 SEO-friendly structure and content

## Components

### File Structure
```
Agent/
├── Single_Agent.py                    # Research agent script
├── Website_Developer_Using_CrewAi.py  # Website development team
├── requirements.txt                   # Python dependencies
├── .env.example                      # Environment variables template
├── README.md                         # This documentation
├── SETUP.md                          # Detailed setup instructions
└── EXAMPLES.md                       # Usage examples
```

## Prerequisites

- Python 3.8 or higher
- Google API key for Gemini LLM
- Git (for cloning the repository)

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/mohammedsha1020/Agent.git
cd Agent
```

2. **Create a virtual environment (recommended)**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env and add your Google API key
```

## Configuration

### Environment Variables

Create a `.env` file in the root directory with:

```bash
GOOGLE_API_KEY=your_google_api_key_here
```

### Getting a Google API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the key to your `.env` file

## Usage

### Research Agent

```bash
python Single_Agent.py
```

The agent will prompt you to enter a research topic and provide a detailed analysis.

### Website Development Team

```bash
python Website_Developer_Using_CrewAi.py
```

Follow the prompts to describe your website requirements. The team will create a complete website with:
- HTML, CSS, and JavaScript files
- Project documentation
- README and package.json
- Professional development process logs

### Generated Output

Website development creates a structured project:
```
generated_app/your_project_name/
├── index.html              # Main website file
├── styles.css              # Stylesheet
├── script.js              # JavaScript functionality
├── README.md              # Project documentation
├── package.json           # Project metadata
└── project_documentation.md # Complete development log
```

## Examples

### Research Agent Example
```bash
python Single_Agent.py
# Input: "Artificial Intelligence in Healthcare"
# Output: Comprehensive research report on AI applications in healthcare
```

### Website Development Example
```bash
python Website_Developer_Using_CrewAi.py
# Input: "Create a modern portfolio website for a freelance graphic designer"
# Output: Complete responsive website with portfolio showcase, contact forms, and professional design
```

For more detailed examples and use cases, see [EXAMPLES.md](EXAMPLES.md).

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Mohammed Sha (mohammedsha1020)

---

## Support

If you encounter any issues or have questions:
1. Check the [SETUP.md](SETUP.md) for detailed installation instructions
2. Review [EXAMPLES.md](EXAMPLES.md) for usage examples
3. Open an issue on GitHub for bug reports or feature requests

## Acknowledgments

- Built with [CrewAI](https://crewai.com/) framework
- Powered by Google Gemini LLM
- Inspired by collaborative AI development practices
