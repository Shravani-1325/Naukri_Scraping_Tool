# 🚀 **Naukri Scraping Tool**  
*A powerful web scraping and analysis tool for job listings on Naukri.com*  

---

## **📌 Project Overview**  
This project is designed to scrape job postings from **Naukri.com** based on user-defined roles and locations. The scraped data is processed, analyzed, and presented through a **Streamlit web application**. Users can explore job listings, extract key insights, and filter relevant roles efficiently.  

---

## **🛠 Features**  
✅ **Web Scraping with Selenium & BeautifulSoup** → Extract job details like title, company, location, experience, salary, skills, and description.  
✅ **Data Preprocessing & Cleaning** → Remove duplicates, extract structured data, and process missing values.  
✅ **Exploratory Data Analysis (EDA)** → Analyze salary trends, required skills, and experience levels using visualizations.  
✅ **Streamlit Web App** → Interactive UI to search and display job listings dynamically.  
✅ **Well-Structured Codebase** → Organized into separate modules for scraping, processing, and visualization.  

---

## **📂 Project Structure**  
```
📂 Naukri_Scraping_Tool
 ┣ 📂 data                   # Store all scraped CSV/Excel files
 ┃  ┣ 📄 scraped_jobs_YYYY-MM-DD.xlsx  # Raw scraped data
 ┃  ┣ 📄 cleaned_jobs_YYYY-MM-DD.csv   # Processed data
 ┣ 📂 notebooks              # Jupyter Notebooks for different tasks
 ┃  ┣ 📄 web_scraper.ipynb   # Web scraping script
 ┃  ┣ 📄 Machine_Learning_Preprocessing.ipynb   # Data preprocessing script
 ┣ 📂 streamlit_app          # Streamlit Web App
 ┃  ┣ 📄 app.py              # Streamlit UI Code
 ┣ 📄 requirements.txt       # Project dependencies
 ┣ 📄 README.md              # Project Documentation
 
```

---

## **🔧 Installation & Setup**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/Shravani-1325/Naukri_Scraping_Tool.git
cd Naukri-Scraping-Tool
```

### **2️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **3️⃣ Run the Scraper**  
To scrape job listings, update `web_scraper.ipynb` with your desired **job role** and **location**, then execute the script.  

---

## **📊 Running the Streamlit App**  
Once the data is scraped and preprocessed, launch the **Streamlit web app** to visualize results.  
Run the following command:  
```bash
streamlit run streamlit_app/app.py
```
Then, open **http://localhost:8501/** in your browser to explore job listings interactively.  

---

## **🎯 Real-World Impact**  
This tool helps job seekers, recruiters, and analysts by:  
✔️ **Identifying job trends & demand** for specific roles.  
✔️ **Filtering jobs based on experience, skills, and location.**  
✔️ **Saving time** by automating job search processes.  

---

## **📌 Future Enhancements**  
🔹 Expand scraping to multiple job platforms.  
🔹 Add AI-based salary prediction.  
🔹 Improve UI with filters and charts.  

---

