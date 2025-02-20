from flask import Flask, render_template
import os
import subprocess
import threading
import time

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Disable caching during development

def start_ngrok():
    # Wait for Flask to start
    time.sleep(3)
    # Start ngrok
    ngrok_process = subprocess.Popen(['ngrok', 'http', '5000'])
    print("\nNgrok started! Check the ngrok interface for your public URL")
    return ngrok_process

@app.route('/')
def home():
    return render_template('index.html', 
        name="Giri Rajendran",
        title="Project Manager at App Innovation Technologies",
        summary="""Project Manager and Professional Scrum Master (PSM I) with over 8 years of diverse experience 
                in IT project management, business analysis, and operations. Specializing in driving digital 
                transformation through effective collaboration and innovative problem-solving. Expert in leading 
                global teams to deliver high-quality mobile and web app solutions using Agile methodologies.""",
        skills=[
            "Project Management", "Scrum Master", "Agile Methodologies", "Business Analysis",
            "JIRA", "Team Leadership", "Stakeholder Management", "Risk Management",
            "Mobile App Development", "Web Development", "Operations Management",
            "Process Optimization", "Technical Documentation", "Client Relations"
        ],
        experience=[
            {
                "company": "App Innovation Technologies",
                "role": "Project Manager",
                "duration": "January 2022 - Present",
                "description": """• Leading multiple mobile and web projects including Social Networking Apps and AI/ML Projects
                • Managing projects using technologies like .Net, Flutter, React Native, iOS, Android, Laravel
                • Implementing and championing Agile methodologies across all projects
                • Leading sprint planning, daily stand-ups, and retrospectives
                • Facilitating communication between stakeholders and development teams
                • Monitoring project progress and providing timely updates to stakeholders"""
            },
            {
                "company": "App Innovation Technologies",
                "role": "Business Analyst",
                "duration": "August 2021 - December 2021",
                "description": """• Gathered and analyzed client requirements for mobile and web app development
                • Created detailed functional specifications and user stories
                • Conducted market research and competitor analysis
                • Collaborated with UI/UX designers for wireframes and prototypes"""
            },
            {
                "company": "Banyan Learning Solutions India Pvt. Ltd.",
                "role": "Assistant Operations Manager",
                "duration": "March 2018 - August 2021",
                "description": """• Led and managed a team of 20 individuals
                • Managed operations for over 150 schools in Tamil Nadu and Bangalore
                • Developed business architecture and conducted requirement analysis
                • Maintained client relationships and ensured customer satisfaction"""
            }
        ],
        education=[
            {
                "degree": "Master's degree in Computer Science and Information Technology",
                "school": "G.T.N. ARTS COLLEGE",
                "year": "2013 - 2015"
            },
            {
                "degree": "Bachelor's degree in Information Technology",
                "school": "G.T.N. ARTS COLLEGE",
                "year": "2010 - 2013"
            }
        ],
        certifications=[
            "Professional Scrum Master™ I (PSM I)",
            "Jira Fundamentals Badge",
            "Scrum Team Member (STM)",
            "Fundamentals of Agile Project Management",
            "SQL"
        ],
        contact={
            "location": "Tamil Nadu, India",
            "email": "girirajendran93@gmail.com",
            "phone": "+91 9894740408",
            "linkedin": "linkedin.com/in/girirajendran93",
            "github": "github.com/girirajendran"
        },
        languages=["English", "Tamil", "Telugu"]
    )

if __name__ == '__main__':
    # Start ngrok in a separate thread
    ngrok_thread = threading.Thread(target=start_ngrok)
    ngrok_thread.daemon = True
    ngrok_thread.start()
    
    # Run Flask app
    app.run(debug=False, port=5000) 