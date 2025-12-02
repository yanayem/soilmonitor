# 🌱 SoilMonitor

A real‑time soil monitoring and analysis web application built during a **10‑hour hackathon** by a team of four passionate developers, led by **Yeasin Arafat Nayem**.  
The project combines **Python (Django)**, **JavaScript**, **HTML/CSS**, and a lightweight database to provide farmers and researchers with insights into soil conditions.

---

## 🚀 Project Overview
- **Goal:** Help farmers and agricultural researchers monitor soil conditions digitally.  
- **Hackathon Duration:** 10 hours of intense collaboration.  
- **Team Size:** 4 contributors.  
- **Leader:** Yeasin Arafat Nayem (Executive of participant engagement, technical lead).  

The app was designed to be **minimal, fast, and visually clear**, with a focus on accessibility and practical use in agricultural contexts.

---

## 🛠️ Tech Stack
- **Backend:** Django (Python)  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** SQLite (default Django setup)  
- **Environment Management:** `django-environ` for secure variable handling  
- **Templates:** Custom login/signup with 3D card flip UI  

---

## 📂 Project Structure
soilmonitor/    
├── account/                        # User account system (authentication, signup, login, forms)  
├── soilcore/                       # Main Django project (settings, URLs, core logic)   
├── static/                        # Static files (CSS, JS, images, icons)   
├── templates/                     # HTML templates (UI pages, layouts, components)   
├── db.sqlite3                      # Local SQLite database (development use)   
├── manage.py                        # Django command-line management utility  
├── LICENSE                          # MIT License file   
└── README.md                        # Project documentation  



---

## 🔑 Features
- **Custom Login/Signup UI:** 3D card flip design with separate forms.  
- **Signup Fields:** Full name, email, password, location, terms agreement.  
- **Dashboard:** Placeholder for soil data visualization and monitoring.  
- **Minimal Deployment:** Lean file setup for quick deployment.  

---

## 👥 Contributors
- **Yeasin Arafat Nayem** – Team Leader, backend setup, template design, deployment strategy.  
- **Contributor 2** – Frontend styling, JavaScript integration.  
- **Contributor 3** – Database structuring, form validation.  
- **Contributor 4** – Documentation, testing, and UI refinement.  

*(Replace Contributor 2–4 with actual names once finalized.)*

---

## ⚡ Getting Started
### Prerequisites
- Python 3.10+  
- Django 4.x  
- Virtual environment recommended  

### Installation
```bash
# Clone the repository
git clone https://github.com/yanayem/soilmonitor.git
cd soilmonitor

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver

```
📜 License
This project is licensed under the MIT License – free to use, modify, and distribute.

🌍 Future Scope
- Integration with IoT sensors for real‑time soil data.
- Data visualization dashboards (charts, graphs).
- Mobile‑friendly design.
- Expansion to regional soil datasets for Bangladesh and beyond.

