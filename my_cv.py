class Job:
    def __init__(self, company, location, role, start_date, end_date, responsibilities):
        self.company = company
        self.location = location
        self.role = role
        self.start_date = start_date
        self.end_date = end_date
        self.responsibilities = responsibilities

class Education:
    def __init__(self, institution, location, degree, start_date, end_date):
        self.institution = institution
        self.location = location
        self.degree = degree
        self.start_date = start_date
        self.end_date = end_date

class Project:
    def __init__(self, name, technologies, description, link=None):
        self.name = name
        self.technologies = technologies
        self.description = description
        self.link = link

class Developer:
    def __init__(self, name, contact_details, introduction, experience, education, skills, languages, projects):
        self.name = name
        self.contact_details = contact_details
        self.introduction = introduction
        self.experience = experience
        self.education = education
        self.skills = skills
        self.languages = languages
        self.projects = projects

    def introduce_yourself(self):
        introduction = f"Name: {self.name}"
        introduction += f"\nContact Details: {self.contact_details}"
        introduction += f"\nIntroduction: {self.introduction}"
        introduction += f"\nSkills: {', '.join(self.skills)}"
        introduction += f"\nLanguages: {', '.join(self.languages)}"
        introduction += f"\n\nExperience:"
        for job in self.experience:
            introduction += f"\n- {job.role} at {job.company} ({job.start_date} - {job.end_date})"
            for responsibility in job.responsibilities:
                introduction += f"\n  - {responsibility}"
        introduction += f"\n\nEducation:"
        for edu in self.education:
            introduction += f"\n- {edu.degree} at {edu.institution} ({edu.start_date} - {edu.end_date})"
        introduction += f"\n\nProjects:"
        for project in self.projects:
            introduction += f"\n- {project.name} ({', '.join(project.technologies)})"
            introduction += f"\n  - {project.description}"
            if project.link:
                introduction += f"\n  - Link: {project.link}"
        return introduction

# Job experiences
torilo_group = Job("Torilo Group of Companies", "England (Nigeria)", "Backend Engineering & Frontend Developer, Software Tester", "October 2020", "Present",)
credpal = Job("CredPal", "Lagos, Nigeria", "Backend Python Engineer", "March 2023", "Present")
lorek_database = Job("Lorek Database Management Agency", "England", "Wordpress Developer", "May 2019", "Sept 2020",)

# Education experiences
torilo_academy_software = Education("Torilo Academy", "Ikeja, Lagos Nigeria", "Software Engineering, Diploma", "October 2019", "December 2019")
torilo_academy_graphic = Education("Torilo Academy", "Ikeja, Lagos Nigeria", "Graphic design, Diploma", "October 2019", "December 2019")
torilo_academy_wordpress = Education("Torilo Academy", "Ikeja, Lagos Nigeria", "Wordpress Design, Diploma", "July 2019", "July 2019")
torilo_academy_product = Education("Torilo Academy", "Ikeja, Lagos Nigeria", "Product Design, Diploma", "March 2021", "March 2021")
yaba_college = Education("Yaba College of Technology", "Yaba, Lagos Nigeria", "Mechanical Engineering, OND", "November 2014", "Feb 2018")

# Projects
crm_project = Project("Customer Relation Management Software", ["Django", "Django Template", "Tailwind CSS"],)
bank_api_project = Project("Mini Bank Api", ["Django", "Django rest framework", "Swagger", "Simple JWT auth"],)
nft_website_project = Project("NFT website", ["Reactjs", "ThirdWeb", "Metamask"], "Various project details")
tinder_clone_project = Project("Tinder Clone", ["Reactjs", "Nodejs", "ExpressJs", "MongoDB"], "Various project details", "https://tinder-clone-8c518.firebaseapp.com/")

# Define Oluwaseyi
oluwaseyi = Developer("Oluwaloseyi Abiola-Alaka", 
                     "(234) 7025859196, alakaoluwaseyi@gmail.com, Github", 
                     "Innovative Software Developer with demonstrated Backend development...",
                     [torilo_group, credpal, lorek_database],
                     [torilo_academy_software, torilo_academy_graphic, torilo_academy_wordpress, torilo_academy_product, yaba_college],
                     ["Python", "Django", "Django Rest-Framework", "Manual Software testing", "Selenium", "Git", "PostgreSQL", "Swagger", "Agile Development", "Celery", "Docker", "Seleniumbase", "Deployment (Heroku, Render, AWS, GCP)", "CI/CD", "React Js", "Nodejs", "Express", "Mongoose", "MongoDB"],
                     ["English", "Yoruba"],
                     [crm_project, bank_api_project, nft_website_project, tinder_clone_project])

print(oluwaseyi.introduce_yourself())
