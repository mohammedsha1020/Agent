# API Reference

This document provides detailed API reference for the Agent repository functions and classes.

## Table of Contents

- [Single Agent API](#single-agent-api)
- [Website Development API](#website-development-api)
- [Configuration Classes](#configuration-classes)
- [Utility Functions](#utility-functions)
- [Error Handling](#error-handling)

## Single Agent API

### Research Agent

The main research agent functionality from `Single_Agent.py`.

#### Agent Configuration

```python
Research_agent = Agent(
    role="Research Agent",
    goal="Conduct research on a given topic and provide a detailed report.",
    backstory="you are a highly skilled researcher in Artificial Intelligence.",
    verbose=True,
    llm=llm
)
```

**Parameters:**
- `role` (str): The role identifier for the agent
- `goal` (str): The primary objective of the agent
- `backstory` (str): Background context that shapes agent behavior
- `verbose` (bool): Enable detailed logging output
- `llm` (LLM): Language model instance to use

#### Task Creation

```python
research_task = Task(
    description=f"Research the topic: '''{topic}'''",
    agent=Research_agent,
    expected_output='give a clear explanation in given topic'
)
```

**Parameters:**
- `description` (str): Detailed description of the research task
- `agent` (Agent): The agent responsible for executing the task
- `expected_output` (str): Description of expected output format

#### Crew Execution

```python
crew = Crew(
    agents=[Research_agent],
    tasks=[research_task], 
    verbose=True
)
result = crew.kickoff()
```

**Parameters:**
- `agents` (List[Agent]): List of agents participating in the crew
- `tasks` (List[Task]): List of tasks to be executed
- `verbose` (bool): Enable detailed execution logging

**Returns:**
- `result` (str): Research report and analysis

## Website Development API

### Main Functions

#### create_professional_website()

Creates a professional website using the 8-agent development team.

```python
def create_professional_website(user_prompt: str) -> str
```

**Parameters:**
- `user_prompt` (str): Description of the website requirements

**Returns:**
- `result` (str): Complete development output including all agent contributions

**Example:**
```python
result = create_professional_website(
    "Create a modern portfolio website for a graphic designer"
)
```

#### save_professional_website()

Processes and saves the generated website files.

```python
def save_professional_website(
    result: str, 
    project_name: str = "professional_website"
) -> str
```

**Parameters:**
- `result` (str): Output from `create_professional_website()`
- `project_name` (str, optional): Name for the project directory

**Returns:**
- `project_dir` (str): Path to the created project directory

**Example:**
```python
project_dir = save_professional_website(
    result, 
    "my_portfolio_site"
)
```

#### create_additional_files()

Creates supplementary project files (README, package.json).

```python
def create_additional_files(project_dir: str) -> None
```

**Parameters:**
- `project_dir` (str): Path to the project directory

**Side Effects:**
- Creates `README.md` with project documentation
- Creates `package.json` with project metadata
- Prints creation confirmation messages

### Agent Definitions

#### Project Manager Agent

```python
project_manager = Agent(
    role="Senior Project Manager",
    goal="Analyze requirements, create project specifications, and coordinate the entire development process",
    backstory="You are a senior project manager with 10+ years of experience leading web development projects.",
    verbose=True,
    llm=llm
)
```

#### Business Analyst Agent

```python
business_analyst = Agent(
    role="Business Analyst", 
    goal="Define user requirements, create user stories, and ensure the website meets business objectives",
    backstory="You are an experienced business analyst who specializes in translating business needs into technical requirements.",
    verbose=True,
    llm=llm
)
```

#### UI/UX Designer Agent

```python
ui_ux_designer = Agent(
    role="Senior UI/UX Designer",
    goal="Create modern, user-friendly, and accessible design systems with professional aesthetics",
    backstory="You are a senior UI/UX designer with expertise in modern design trends, accessibility standards, and user psychology.",
    verbose=True,
    llm=llm
)
```

#### Frontend Architect Agent

```python
frontend_architect = Agent(
    role="Frontend Architect",
    goal="Design scalable frontend architecture using modern best practices and performance optimization",
    backstory="You are a frontend architect with deep knowledge of modern JavaScript, CSS methodologies, performance optimization, and web standards.",
    verbose=True,
    llm=llm
)
```

#### Content Strategist Agent

```python
content_strategist = Agent(
    role="Content Strategist",
    goal="Create compelling, SEO-optimized content that engages users and drives conversions",
    backstory="You are a content strategist who understands copywriting, brand voice, and conversion optimization.",
    verbose=True,
    llm=llm
)
```

#### SEO Specialist Agent

```python
seo_specialist = Agent(
    role="SEO Specialist",
    goal="Optimize website structure and content for search engines and performance",
    backstory="You are an SEO expert who understands technical SEO, page speed optimization, and search engine algorithms.",
    verbose=True,
    llm=llm
)
```

#### Frontend Developer Agent

```python
frontend_developer = Agent(
    role="Senior Frontend Developer",
    goal="Implement pixel-perfect, responsive, and interactive web interfaces using cutting-edge technologies",
    backstory="You are a senior frontend developer with expertise in HTML5, CSS3, JavaScript ES6+, and modern frameworks.",
    verbose=True,
    llm=llm
)
```

#### QA Engineer Agent

```python
qa_engineer = Agent(
    role="Quality Assurance Engineer",
    goal="Test website functionality, accessibility, and cross-browser compatibility", 
    backstory="You are a QA engineer who ensures websites work flawlessly across all devices and browsers.",
    verbose=True,
    llm=llm
)
```

### Task Definitions

#### Planning Task

```python
planning_task = Task(
    description=f"""
    Analyze this website requirement: '{user_prompt}'
    
    Create a comprehensive project plan including:
    1. Project scope and objectives
    2. Target audience analysis
    3. Technical requirements
    4. Feature list and priorities
    5. Technology stack recommendations
    6. Project timeline and milestones
    7. Success metrics and KPIs
    """,
    agent=project_manager,
    expected_output="Comprehensive project specification with scope, requirements, and technical recommendations"
)
```

#### Development Task

```python
development_task = Task(
    description=f"""
    Implement the complete website for: '{user_prompt}'
    Using ALL previous specifications: architecture, design, content, and SEO requirements,
    
    Create production-ready code including:
    1. Semantic HTML5 with proper structure
    2. Modern CSS3 with custom properties and grid/flexbox
    3. Vanilla JavaScript with ES6+ features
    4. Responsive design with mobile-first approach
    5. Accessibility features (ARIA, keyboard navigation)
    6. Performance optimizations (lazy loading, minification)
    7. SEO-friendly structure with meta tags
    8. Progressive enhancement
    9. Cross-browser compatibility
    10. Clean, documented, and maintainable code
    """,
    agent=frontend_developer,
    expected_output="Complete, production-ready HTML, CSS, and JavaScript code with professional quality",
    context=[planning_task, business_analysis_task, design_task, architecture_task, content_task, seo_task]
)
```

## Configuration Classes

### LLM Configuration

```python
llm = LLM(
    model="gemini/gemini-1.5-flash",
    temperature=0.3,
    api_key=os.environ.get("GOOGLE_API_KEY"),
    max_tokens=2048
)
```

**Parameters:**
- `model` (str): LLM model identifier
- `temperature` (float): Response creativity level (0.0-1.0)
- `api_key` (str): Authentication key for the LLM service
- `max_tokens` (int): Maximum response length

### Environment Configuration

Required environment variables:

```bash
GOOGLE_API_KEY=your_google_api_key_here
```

**Optional environment variables:**
```bash
LLM_TEMPERATURE=0.3
LLM_MAX_TOKENS=2048
OUTPUT_DIR=./generated_projects
```

## Utility Functions

### File Extraction Functions

The system includes internal functions for extracting code from agent responses:

#### extract_html()
```python
html_matches = re.findall(r'```html(.*?)```', result_text, re.DOTALL | re.IGNORECASE)
```

#### extract_css()
```python
css_matches = re.findall(r'```css(.*?)```', result_text, re.DOTALL | re.IGNORECASE)
```

#### extract_javascript()
```python
js_matches = re.findall(r'```javascript(.*?)```', result_text, re.DOTALL | re.IGNORECASE)
```

### Directory Management

```python
import os
os.makedirs(project_dir, exist_ok=True)
```

Creates project directories with proper error handling.

### File Writing

```python
with open(f"{project_dir}/index.html", "w", encoding="utf-8") as f:
    f.write(html_content)
```

Writes extracted code to appropriate files with UTF-8 encoding.

## Error Handling

### Common Exceptions

#### API Key Missing
```python
KeyError: 'GOOGLE_API_KEY'
```
**Cause:** Environment variable not set
**Solution:** Configure `.env` file with valid API key

#### Model Access Errors
```python
AuthenticationError: Invalid API key
```
**Cause:** Invalid or expired API key
**Solution:** Verify API key in Google Cloud Console

#### File System Errors
```python
PermissionError: [Errno 13] Permission denied
```
**Cause:** Insufficient file system permissions
**Solution:** Check directory permissions and disk space

#### Network Errors
```python
ConnectionError: Failed to establish connection
```
**Cause:** Network connectivity issues
**Solution:** Check internet connection and API service status

### Error Handling Patterns

#### Safe Environment Variable Loading
```python
api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable not set")
```

#### Safe File Operations
```python
try:
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ File saved: {filename}")
except IOError as e:
    print(f"❌ Error saving file {filename}: {e}")
```

#### API Call Error Handling
```python
try:
    result = crew.kickoff()
except Exception as e:
    print(f"❌ Error during crew execution: {e}")
    raise
```

## Rate Limiting and Quotas

### API Usage Considerations

- **Rate Limits:** Google API has rate limits per minute/hour
- **Quota Management:** Monitor usage in Google Cloud Console
- **Cost Optimization:** Each agent interaction consumes tokens
- **Batch Processing:** Consider grouping similar requests

### Best Practices

1. **Monitor Usage:**
   ```python
   import time
   
   def rate_limited_call(func, delay=1):
       result = func()
       time.sleep(delay)
       return result
   ```

2. **Implement Retry Logic:**
   ```python
   import time
   from functools import wraps
   
   def retry_on_failure(max_retries=3):
       def decorator(func):
           @wraps(func)
           def wrapper(*args, **kwargs):
               for attempt in range(max_retries):
                   try:
                       return func(*args, **kwargs)
                   except Exception as e:
                       if attempt == max_retries - 1:
                           raise
                       time.sleep(2 ** attempt)
               return wrapper
           return decorator
   ```

3. **Cache Results:**
   ```python
   import json
   import hashlib
   
   def cache_result(func):
       cache = {}
       def wrapper(*args, **kwargs):
           key = hashlib.md5(str(args + tuple(kwargs.items())).encode()).hexdigest()
           if key not in cache:
               cache[key] = func(*args, **kwargs)
           return cache[key]
       return wrapper
   ```

## Testing and Validation

### Unit Testing Examples

```python
import unittest
from unittest.mock import patch, MagicMock

class TestAgentFunctionality(unittest.TestCase):
    
    @patch('os.environ.get')
    def test_llm_configuration(self, mock_env):
        mock_env.return_value = 'test_api_key'
        # Test LLM initialization
        
    def test_file_extraction(self):
        sample_output = "```html<html><body>Test</body></html>```"
        # Test HTML extraction regex
        
    def test_project_directory_creation(self):
        # Test directory creation and cleanup
        pass
```

### Integration Testing

```python
def test_full_workflow():
    """Test complete website generation workflow"""
    test_prompt = "Simple landing page for testing"
    result = create_professional_website(test_prompt)
    project_dir = save_professional_website(result, "test_project")
    
    # Verify files were created
    assert os.path.exists(f"{project_dir}/index.html")
    assert os.path.exists(f"{project_dir}/styles.css")
    assert os.path.exists(f"{project_dir}/script.js")
```

## Performance Optimization

### Memory Management

```python
import gc

def optimize_memory_usage():
    """Clean up memory after large operations"""
    gc.collect()
```

### Parallel Processing

```python
from concurrent.futures import ThreadPoolExecutor

def parallel_agent_execution(tasks):
    """Execute multiple agents in parallel where possible"""
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(task.execute) for task in tasks]
        results = [future.result() for future in futures]
    return results
```

This API reference provides comprehensive documentation for integrating and extending the Agent repository functionality.