# 🎬 NextFlix Movie Recommendation System

A **movie recommendation web application** inspired by Netflix that suggests movies using **Association Rule Mining (Apriori Algorithm)**.  
The system analyzes relationships between movies and provides recommendations along with explanation metrics like **Support, Confidence, and Lift**.

---

## 🔗 Project Links

- **Live Demo:** [https://your-deployment-link](https://nextflix-recommendation-system.onrender.com/)
- **Portfolio:** [https://your-portfolio-link](https://anmolpatel20.github.io/Anmol_Portfolio/)
- **Certificate:** [https://your-certificate-link](https://unstop.com/certificate-preview/4345a3ef-85cf-458a-9bb5-b7097d374f09)

---

## 🚀 Project Overview

NextFlix is a web-based recommendation system where users can:

- Get **Top movie recommendations** based on a selected movie.
- Analyze the **relationship between two movies**.
- Understand *why* a movie is recommended using **Apriori rule metrics**.

The system is built using:

- **Flask** for backend
- **HTML + CSS** for frontend
- **Python** for recommendation logic
- **Apriori rules dataset** for movie relationships

---

## 🧠 Recommendation Logic

The system uses **Association Rule Mining (Apriori Algorithm)** to discover patterns in movie watching behavior.

Key metrics used:

| Metric | Meaning |
|------|------|
| **Support** | Frequency of two movies appearing together |
| **Confidence** | Likelihood that Movie2 is watched when Movie1 is watched |
| **Lift** | Strength of association between movies |

Example rule:

```
Movie1 → Movie2
Support: 0.02
Confidence: 0.45
Lift: 3.2
```

A **higher Lift value** indicates a stronger recommendation.

---

## 🏗 System Architecture


```
User Interface (HTML + CSS)
↓
Flask Backend (app.py)
↓
Recommendation Engine (recommender.py)
↓
Apriori Rules Dataset (movie_rules.csv)
↓
Recommendations / Relationship Analysis
↓
Rendered Results (index.html)
```

---

## 📊 Workflow

1. User selects **Movie1 (required)** and optionally **Movie2**.
2. The frontend sends a **POST request** to Flask.
3. Flask backend processes the request.
4. The **MovieRecommender class** analyzes Apriori rules.
5. The system returns:
   - Top movie recommendations
   - OR relationship analysis between two movies.
6. Results are rendered in the UI.

---

## 📁 Project Structure

```
NextFlix_Recommendation_System
│
├── app.py
├── requirements.txt
├── movie_rules.csv
├── netflix_data.csv
│
├── model
│   └── recommender.py
│
├── templates
│   └── index.html
│
├── static
│   ├── css
│   │   └── style.css
│   └── images
│
└── README.md
```

---

## 🌐 Deployment

The project is deployed using **Render**.

## 🖥 Features

✔ Movie recommendation based on association rules  
✔ Relationship analysis between two movies  
✔ Apriori rule metrics explanation  
✔ Clean Flask web interface  
✔ Lightweight dataset-based recommendation engine  

---

## 📷 Workflow Diagram

![Workflow Diagram](https://raw.githubusercontent.com/AnmolPatel20/NextFlix_Recommendation_System/main/static/images/NextFlix_Workflow.png)
---

## 🛠 Technologies Used

- Python
- Flask
- Pandas
- Apriori Algorithm
- HTML
- CSS
- Git
- Render (Deployment)

---

## 👨‍💻 Author

**Anmol Patel**

- Data Science & Machine Learning Enthusiast
- Python Developer

---
⭐ If you found this project useful, consider **starring the repository**!
