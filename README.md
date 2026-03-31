# ️ PollPoint – DevOps-Based College Voting System

##  Project Overview
**PollPoint** is a web-based college voting system developed using **Django** and deployed using a complete **DevOps pipeline on AWS**.

This project demonstrates how modern DevOps practices like **CI/CD, cloud deployment, and automated testing** can be integrated to build a **secure, scalable, and efficient voting system**.

---

##  Objectives
- Build a secure online voting system for students  
- Replace manual paper-based voting  
- Ensure transparency and fairness  
- Automate deployment using CI/CD pipeline  

---

##  Key Features

###  Admin
- Add / Edit / Delete positions  
- Manage candidates  
- View live voting results  

###  Student
- Secure login system  
- Cast vote (only once)  
- Anonymous voting system  

---

## ️ Tech Stack

| Category | Technology |
|--------|-----------|
| Backend | Python, Django |
| Cloud | AWS Cloud9, AWS Elastic Beanstalk |
| CI/CD | GitHub Actions |
| Version Control | GitHub |
| Code Quality | Pylint |
| Security | SonarQube |

---

##  Deployment

- Developed on **AWS Cloud9**
- Deployed using **AWS Elastic Beanstalk**
- CI/CD automated using **GitHub Actions**

 **Live Application**  
http://poll-point.us-east-1.elasticbeanstalk.com/

---

##  CI/CD Pipeline

The pipeline is triggered on every push to GitHub:

1. Build application  
2. Run Pylint (code quality check)  
3. Execute Django tests  
4. Perform SonarQube security analysis  
5. Deploy to AWS Elastic Beanstalk  

This ensures **automated, reliable, and error-free deployment**.

---

##  Testing

- Django test suite implemented  
- All test cases passed successfully  
- Ensures system reliability  

---
## Project Structure
```
my-devops-project/
|── .github/workflows/    # CI/CD pipeline (GitHub Actions)
|── voting/               # Main Django app
|── templates/            # HTML templates
|── static/               # CSS, JS, images
|── db.sqlite3            # Database (default)
|── manage.py             # Django entry point
|── requirements.txt      # Project dependencies
|── django.yml            # CI/CD configuration
|── README.md             # Project documentation
```



---

##  Key URLs

| Function | URL |
|--------|-----|
| Home Page | / |
| Admin Login | /admin/ |
| Student Login | /login/ |
| Signup | /signup/ |
| Logout | /logout/ |
| Add Position (Admin) | /adminadd/ |
| Update Position | /update/<id> |
| Delete Position | /delete/<id> |
| Voting Page | /vote/<position_id>/ |
| Submit Vote | /submit_vote/ |

 **Live Application**  
http://poll-point.us-east-1.elasticbeanstalk.com/



---

## CRUD Operations

- Create → Add positions & candidates  
- Read → View elections & results  
- Update → Modify records  
- Delete → Remove unused entries  

---

##  Learning

- CI/CD pipeline implementation  
- AWS cloud deployment  
- Secure coding practices  
- Version control using GitHub  
- Code quality & vulnerability analysis  

---

##  Conclusion

This project shows how **DevOps + Cloud + Django** can be combined to build a **real-world scalable application** with automation, security, and efficiency.

---

##  Author

**Manirathnam Gajula**  
DevOps Project – College Voting System  

---

## How to Run Locally

```bash
# Clone the repository
git clone https://github.com/manirathnam21/my-devops-project.git

# Navigate to project
cd my-devops-project

# Install dependencies
pip install -r requirements.txt

# Run server
python manage.py runserver