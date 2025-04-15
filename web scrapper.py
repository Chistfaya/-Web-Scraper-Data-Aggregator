import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the job postings page
url = 'https://vacancymail.co.zw/jobs/'

# Send a GET request to the website
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all job listings
job_listings = soup.find_all('a', class_='job-listing')

# List to store job details
job_data = []

# Loop through each job listing
for job in job_listings:
    title = job.find('h3', class_='job-listing-title').text.strip() if job.find('h3', class_='job-listing-title') else ''
    company = job.find('h4', class_='job-listing-company').text.strip() if job.find('h4', class_='job-listing-company') else ''
    location = job.find('i', class_='icon-material-outline-location-on').find_next('li').text.strip() if job.find('i', class_='icon-material-outline-location-on') else ''
    expiration = job.find('i', class_='icon-material-outline-access-time').find_next('li').text.strip() if job.find('i', class_='icon-material-outline-access-time') else ''
    job_type = job.find('i', class_='icon-material-outline-business-center').find_next('li').text.strip() if job.find('i', class_='icon-material-outline-business-center') else ''
    salary = job.find('i', class_='icon-material-outline-account-balance-wallet').find_next('li').text.strip() if job.find('i', class_='icon-material-outline-account-balance-wallet') else ''
    
    job_data.append({
        'Job Title': title,
        'Company': company,
        'Location': location,
        'Expiration': expiration,
        'Job Type': job_type,
        'Salary': salary
    })

# Create a DataFrame and save to Excel
df = pd.DataFrame(job_data)
df.to_excel('job_listings.xlsx', index=False)

print("Job details have been saved to 'job_listings.xlsx'")


