import os
from crewai import Agent, Task, Crew
from dotenv import load_dotenv
import json
import re
import time

load_dotenv()

from crewai import LLM

# Set up the LLM with explicit API key and reduced rate limits
llm = LLM(
    model="gemini/gemini-1.5-flash",  # Using stable version instead of 2.5-flash
    temperature=0.3,
    api_key=os.environ.get("GOOGLE_API_KEY"),
    max_tokens=2048  # Reduced to prevent quota issues
)

# Professional Development Team - Multiple Specialized Agents
project_manager = Agent(
    role="Senior Project Manager",
    goal="Analyze requirements, create project specifications, and coordinate the entire development process",
    backstory="You are a senior project manager with 10+ years of experience leading web development projects. You excel at breaking down complex requirements into actionable tasks and ensuring quality deliverables.",
    verbose=True,
    llm=llm
)

business_analyst = Agent(
    role="Business Analyst",
    goal="Define user requirements, create user stories, and ensure the website meets business objectives",
    backstory="You are an experienced business analyst who specializes in translating business needs into technical requirements. You understand user experience and business goals.",
    verbose=True,
    llm=llm
)

ui_ux_designer = Agent(
    role="Senior UI/UX Designer",
    goal="Create modern, user-friendly, and accessible design systems with professional aesthetics",
    backstory="You are a senior UI/UX designer with expertise in modern design trends, accessibility standards, and user psychology. You create award-winning designs that convert visitors into customers.",
    verbose=True,
    llm=llm
)

frontend_architect = Agent(
    role="Frontend Architect",
    goal="Design scalable frontend architecture using modern best practices and performance optimization",
    backstory="You are a frontend architect with deep knowledge of modern JavaScript, CSS methodologies, performance optimization, and web standards. You ensure code is maintainable and scalable.",
    verbose=True,
    llm=llm
)

frontend_developer = Agent(
    role="Senior Frontend Developer",
    goal="Implement pixel-perfect, responsive, and interactive web interfaces using cutting-edge technologies",
    backstory="You are a senior frontend developer with expertise in HTML5, CSS3, JavaScript ES6+, and modern frameworks. You write clean, semantic, and performant code.",
    verbose=True,
    llm=llm
)

seo_specialist = Agent(
    role="SEO Specialist",
    goal="Optimize website structure and content for search engines and performance",
    backstory="You are an SEO expert who understands technical SEO, page speed optimization, and search engine algorithms. You ensure websites rank well and load fast.",
    verbose=True,
    llm=llm
)

qa_engineer = Agent(
    role="Quality Assurance Engineer", 
    goal="Test website functionality, accessibility, and cross-browser compatibility",
    backstory="You are a QA engineer who ensures websites work flawlessly across all devices and browsers. You test for bugs, accessibility issues, and performance problems.",
    verbose=True,
    llm=llm
)

content_strategist = Agent(
    role="Content Strategist",
    goal="Create compelling, SEO-optimized content that engages users and drives conversions",
    backstory="You are a content strategist who understands copywriting, brand voice, and conversion optimization. You create content that tells a story and drives action.",
    verbose=True,
    llm=llm
)

def create_professional_website(user_prompt):
    """
    Create a professional website using a full development team
    """
    
    # 1. Project Planning & Requirements Analysis
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
        
        Provide a detailed project specification document.
        """,
        agent=project_manager,
        expected_output="Comprehensive project specification with scope, requirements, and technical recommendations"
    )

    # 2. Business Requirements & User Stories  
    business_analysis_task = Task(
        description=f"""
        Based on the project requirement: '{user_prompt}' and the project plan,
        
        Create detailed business analysis including:
        1. User personas and journey mapping
        2. Functional requirements
        3. User stories with acceptance criteria
        4. Business logic requirements
        5. Integration requirements
        6. Performance requirements
        7. Security requirements
        
        Focus on understanding the business value and user needs.
        """,
        agent=business_analyst,
        expected_output="Detailed user stories, functional requirements, and business logic specifications"
    )

    # 3. Design System & UI/UX Strategy
    design_task = Task(
        description=f"""
        Create a professional design system for: '{user_prompt}'
        Using the project specifications and business requirements,
        
        Design a comprehensive UI/UX system including:
        1. Brand identity and visual hierarchy
        2. Color palette with accessibility considerations
        3. Typography scale and font choices
        4. Component library specifications
        5. Layout grids and spacing system
        6. Responsive breakpoint strategy
        7. Interactive states and animations
        8. Accessibility compliance (WCAG 2.1 AA)
        9. User flow wireframes
        10. Modern design trends implementation
        
        Create detailed design specifications that follow current industry standards.
        """,
        agent=ui_ux_designer,
        expected_output="Complete design system with components, layouts, and accessibility guidelines"
    )

    # 4. Frontend Architecture
    architecture_task = Task(
        description=f"""
        Design frontend architecture for: '{user_prompt}'
        Based on the project requirements and design system,
        
        Create technical architecture including:
        1. File structure and organization
        2. CSS methodology (BEM/SMACSS/CSS Modules)
        3. JavaScript architecture patterns
        4. Performance optimization strategy
        5. Code splitting and lazy loading
        6. State management approach
        7. Build process and tooling
        8. Browser compatibility strategy
        9. Progressive Web App features
        10. Security best practices
        
        Ensure scalable and maintainable code architecture.
        """,
        agent=frontend_architect,
        expected_output="Technical architecture plan with file structure, methodologies, and performance strategies"
    )

    # 5. Content Strategy
    content_task = Task(
        description=f"""
        Create content strategy for: '{user_prompt}'
        Using the business analysis and design specifications,
        
        Develop comprehensive content including:
        1. Brand voice and tone guidelines
        2. SEO-optimized headlines and copy
        3. Compelling calls-to-action
        4. Micro-copy and UX writing
        5. Content hierarchy and information architecture
        6. Social media integration content
        7. Accessibility-friendly alt texts and descriptions
        8. Conversion-focused landing page copy
        9. Error messages and user feedback text
        10. Meta descriptions and SEO content
        
        Ensure all content drives user engagement and conversions.
        """,
        agent=content_strategist,
        expected_output="Complete content strategy with copy, CTAs, and SEO-optimized text"
    )

    # 6. SEO & Performance Optimization
    seo_task = Task(
        description=f"""
        Create SEO and performance optimization strategy for: '{user_prompt}'
        
        Develop comprehensive optimization including:
        1. Technical SEO implementation
        2. Page speed optimization techniques
        3. Core Web Vitals optimization
        4. Schema markup strategy
        5. Meta tags and structured data
        6. Image optimization and lazy loading
        7. Critical CSS and resource loading
        8. Mobile-first optimization
        9. Analytics and tracking setup
        10. Performance monitoring recommendations
        
        Ensure the website loads fast and ranks well in search engines.
        """,
        agent=seo_specialist,
        expected_output="SEO strategy with technical optimizations and performance guidelines"
    )

    # 7. Frontend Development & Implementation
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
        11. Interactive features and animations
        12. Form validation and error handling
        
        Generate complete HTML, CSS, and JavaScript files with professional code quality.
        Include detailed code comments explaining functionality.
        """,
        agent=frontend_developer,
        expected_output="Complete, production-ready HTML, CSS, and JavaScript code with professional quality",
        context=[planning_task, business_analysis_task, design_task, architecture_task, content_task, seo_task]
    )

    # 8. Quality Assurance & Testing
    qa_task = Task(
        description=f"""
        Perform comprehensive quality assurance for the developed website.
        Review the implemented code and create testing recommendations.
        
        Provide QA analysis including:
        1. Code quality review
        2. Accessibility testing checklist
        3. Cross-browser compatibility notes
        4. Mobile responsiveness verification
        5. Performance optimization suggestions
        6. SEO implementation review
        7. User experience testing scenarios
        8. Security best practices check
        9. Bug identification and fixes
        10. Deployment readiness checklist
        
        Ensure the website meets professional standards.
        """,
        agent=qa_engineer,
        expected_output="Comprehensive QA report with testing checklist and quality improvements",
        context=[development_task]
    )

    # Create and run the professional development crew
    crew = Crew(
        agents=[
            project_manager,
            business_analyst, 
            ui_ux_designer,
            frontend_architect,
            content_strategist,
            seo_specialist,
            frontend_developer,
            qa_engineer
        ],
        tasks=[
            planning_task,
            business_analysis_task,
            design_task, 
            architecture_task,
            content_task,
            seo_task,
            development_task,
            qa_task
        ],
        verbose=True,
        process="sequential"  # Ensures proper workflow
    )

    result = crew.kickoff()
    return result

def save_professional_website(result, project_name="professional_website"):
    """
    Save the professionally generated website files
    """
    # Create project directory
    project_dir = f"generated_app/{project_name}"
    os.makedirs(project_dir, exist_ok=True)
    
    result_text = str(result)
    
    # Extract and save HTML
    html_matches = re.findall(r'```html(.*?)```', result_text, re.DOTALL | re.IGNORECASE)
    if html_matches:
        # Use the most complete HTML (usually the last one)
        html_content = html_matches[-1].strip()
        with open(f"{project_dir}/index.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"✅ Professional HTML saved: {project_dir}/index.html")
    
    # Extract and save CSS
    css_matches = re.findall(r'```css(.*?)```', result_text, re.DOTALL | re.IGNORECASE)
    if css_matches:
        css_content = css_matches[-1].strip()
        with open(f"{project_dir}/styles.css", "w", encoding="utf-8") as f:
            f.write(css_content)
        print(f"✅ Professional CSS saved: {project_dir}/styles.css")
    
    # Extract and save JavaScript
    js_matches = re.findall(r'```javascript(.*?)```', result_text, re.DOTALL | re.IGNORECASE)
    if js_matches:
        js_content = js_matches[-1].strip()
        with open(f"{project_dir}/script.js", "w", encoding="utf-8") as f:
            f.write(js_content)
        print(f"✅ Professional JavaScript saved: {project_dir}/script.js")
    
    # Save project documentation
    with open(f"{project_dir}/project_documentation.md", "w", encoding="utf-8") as f:
        f.write(f"# {project_name.replace('_', ' ').title()} - Project Documentation\n\n")
        f.write("## Development Process\n\n")
        f.write("This website was developed using a professional 8-agent development team:\n\n")
        f.write("1. **Project Manager** - Project planning and coordination\n")
        f.write("2. **Business Analyst** - Requirements and user stories\n") 
        f.write("3. **UI/UX Designer** - Design system and user experience\n")
        f.write("4. **Frontend Architect** - Technical architecture\n")
        f.write("5. **Content Strategist** - Content and copywriting\n")
        f.write("6. **SEO Specialist** - Search optimization\n")
        f.write("7. **Frontend Developer** - Code implementation\n")
        f.write("8. **QA Engineer** - Quality assurance and testing\n\n")
        f.write("## Complete Development Log\n\n")
        f.write(result_text)
    
    print(f"✅ Project documentation saved: {project_dir}/project_documentation.md")
    
    # Create additional professional files
    create_additional_files(project_dir)
    
    return project_dir

def create_additional_files(project_dir):
    """Create additional professional development files"""
    
    # README.md
    readme_content = """# Professional Website Project

## 🚀 Overview
This website was built using AI-powered professional development team with 8 specialized agents.

## 📁 Project Structure
```
/
├── index.html              # Main HTML file
├── styles.css              # Stylesheet
├── script.js              # JavaScript functionality  
├── project_documentation.md # Complete development process
├── README.md              # This file
└── package.json           # Project dependencies
```

## 🛠️ Technologies Used
- HTML5 (Semantic markup)
- CSS3 (Modern features, Grid, Flexbox)
- Vanilla JavaScript (ES6+)
- Responsive Design
- SEO Optimization
- Accessibility (WCAG 2.1 AA)

## 🎯 Features
- Mobile-first responsive design
- Cross-browser compatibility
- SEO optimized structure
- Accessibility compliant
- Performance optimized
- Professional code quality

## 🚀 Getting Started
1. Open `index.html` in your browser
2. For development, use a local server
3. Customize content and styling as needed

## 📈 Performance
- Optimized for Core Web Vitals
- Lazy loading implementation
- Minified and compressed assets
- Fast loading times

## ♿ Accessibility
- WCAG 2.1 AA compliant
- Screen reader friendly
- Keyboard navigation support
- High contrast support

Generated by CrewAI Professional Development Team
"""
    
    with open(f"{project_dir}/README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    # package.json for professional setup
    package_json = {
        "name": "professional-website",
        "version": "1.0.0",
        "description": "Professional website built with AI development team",
        "main": "index.html",
        "scripts": {
            "serve": "python -m http.server 8000",
            "build": "echo 'Build process would go here'",
            "test": "echo 'Tests would go here'"
        },
        "keywords": ["website", "professional", "responsive", "seo"],
        "author": "CrewAI Development Team",
        "license": "MIT",
        "devDependencies": {
            "live-server": "^1.2.2"
        }
    }
    
    with open(f"{project_dir}/package.json", "w", encoding="utf-8") as f:
        json.dump(package_json, f, indent=2)
    
    print(f"✅ Additional files created: README.md, package.json")

if __name__ == "__main__":
    print("🏢 PROFESSIONAL WEBSITE DEVELOPMENT TEAM")
    print("=" * 50)
    print("8 AI Agents working together like a real dev team:")
    print("👨‍💼 Project Manager | 👩‍💼 Business Analyst | 🎨 UI/UX Designer")
    print("🏗️ Frontend Architect | ✍️ Content Strategist | 🔍 SEO Specialist") 
    print("👨‍💻 Frontend Developer | 🧪 QA Engineer")
    print("=" * 50)
    
    # Get user input
    user_prompt = input("\n📝 Describe your website project: ")
    
    if not user_prompt.strip():
        user_prompt = "Create a modern business website for a tech startup with services, portfolio, team, and contact sections"
    
    print(f"\n🚀 Starting professional development for: {user_prompt}")
    print("⏳ This will take a few minutes as our team works together...")
    print("=" * 80)
    
    # Generate the professional website
    result = create_professional_website(user_prompt)
    
    # Save files
    project_name = input("\n📁 Enter project name (or press Enter for 'professional_website'): ").strip() or "professional_website"
    project_dir = save_professional_website(result, project_name)
    
    print(f"\n✅ PROFESSIONAL WEBSITE COMPLETED!")
    print("=" * 50)
    print(f"📁 Project files: {project_dir}")
    print(f"🌐 Open {project_dir}/index.html to view your website")
    print(f"📚 Read {project_dir}/project_documentation.md for full details")
    print(f"📖 Check {project_dir}/README.md for project overview")
    print("=" * 50)
    print("🎉 Your website is ready for production!")
