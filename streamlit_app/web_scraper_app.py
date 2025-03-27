import streamlit as st
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Function
def scrape_jobs(job_role, location, max_jobs=10):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new") 
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=chrome_options)
    base_url = f"https://www.naukri.com/{job_role.replace(' ', '%20')}-jobs-in-{location.replace(' ', '%20')}?k={job_role.replace(' ', '%20')}&l={location.replace(' ', '%20')}"

    driver.get(base_url)
    time.sleep(5)
    
    job_lists = []
    job_count = 0
    max_page = 5 # Scraping up to 5 pages
    
    for page in range(1, max_page+1):
        jobs= driver.find_elements(By.CLASS_NAME, "srp-jobtuple-wrapper")
        
        for job in jobs:
            if job_count >= max_jobs:
                break
            
            try:
                title = job.find_element(By.CLASS_NAME, "title").text
                company = job.find_element(By.CLASS_NAME, "comp-name").text
                location = job.find_element(By.CLASS_NAME, "loc").text
                experience = job.find_element(By.CLASS_NAME, "exp").text if job.find_elements(By.CLASS_NAME, "exp") else "Not Specified"
                job_link = job.find_element(By.CLASS_NAME, "title").get_attribute("href")
                
                #Visiting the each job page directly to get particularr info
                driver.execute_script("window.open();")  # Open new tab
                driver.switch_to.window(driver.window_handles[1])  # Switch to new tab
                driver.get(job_link)  # Go to job link
                time.sleep(5)


                try:                    
                    salary = driver.find_element(By.CLASS_NAME, "styles_jhc__salary__jdfEC").text
                except:
                    salary = "Not Specified"
                    
                try:
                    skills_container = driver.find_element(By.CLASS_NAME,"styles_key-skill__GIPn_")
                    skills = [skill.text for skill in skills_container.find_elements(By.TAG_NAME,"span")]
                except:
                    skills = ["Not Specified"]
                    
                driver.close()
                driver.switch_to.window(driver.window_handles[0])

                    
                # Appending the job elements in list
                job_lists.append([title, company, location, experience, job_link,salary,skills])
                job_count +=1
                    
            except Exception as e:
                print("Skipping the Job due to error: ",e)   

        if job_count >= max_jobs:
            break
        
        try:
            next_page = driver.find_element(By.XPATH, f"//a[text()='{page + 1}']")  # Select the next page button
            driver.execute_script("arguments[0].click();", next_page)  # Click using JavaScript
            time.sleep(5)  # Wait for the next page to load
        except Exception as e:
            print("No more pages found or error:", e)
            break  # Stoping the scraping if no more pages are available

        print("✅ Scraping completed!")
            
    driver.quit()
    return pd.DataFrame(job_lists, columns = ["Job Title", "Company", "Location", "Experience", "Job Link", "Salary", "Skills"])

# Streamlit UI 
st.title("👩‍💻 Naukri Job Scraper 📈🚀")
st.markdown("_Welcome to Naukri Job Scaper! On one click, you will get every piece of information about various jobs posted on Naukri.com._")
st.write("Enter the Job details and click 'Search' to find jobs")

#Initializing session state for clearing inputs
if "job_role" not in st.session_state:
    st.session_state.job_role = ""
if "location" not in st.session_state:
    st.session_state.location = ""
 
# Input Fields
job_roles = st.text_input("Enter Job Role (e.g. Machine Learning Engineer): ")
location = st.text_input("Enter the Location (e.g. Bangalore): ")
max_jobs = st.slider("Select Number of Jobs to Fetch: ",5,50,10)

# search Button
if st.button("🔍 Search Jobs"):
    with st.spinner("Fetching jobs....."):
        df=scrape_jobs(job_roles, location, max_jobs)
        st.success("✅ Job Search Completed!")
        st.dataframe(df)
        st.download_button("📥 Download the CSV file", df.to_csv(index=False), f"{job_roles}_Naukri.csv", "text/csv")
                       
#Clear Button
if st.button("❌ Clear"):
    st.session_state.job_role = ""
    st.session_state.location = ""
    st.rerun()  # Reload the page to reset fields   
    
st.write("Created By: Shravani More ✨")             
                
# Custom Css
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://img.freepik.com/free-photo/dark-green-wall-shadow-background-with-flower_53876-119873.jpg?t=st=1742925567~exp=1742929167~hmac=d16f87b11fea346480bcbe70fde336b0760cf96c24186a6398738e92b61fc105&w=1380");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    /* Title Styling */
    .title {
        text-shadow: 2px 2px 5px black;
    }

    /* Buttons */
    .st-emotion-cache-b0y9n5 {
        background-color: rgb(22, 74, 76);
    }

    /* Header */
    .st-emotion-cache-h4xjwg {
        position: fixed;
        top: 0px;
        left: 0px;
        right: 0px;
        height: 3.75rem;
        background: rgb(7 51 51);
        z-index: 999990;
    }

    /* Sidebar background */
    .st-b7 {
        background-color: rgb(16, 67, 65);
    }
    </style>
    """,
    unsafe_allow_html=True
    
)
