python -m venv venv

Call of Duty League Stats Scraper Setup (Windows Environment)



--- 1. Create the Project Folder and Navigate into it ---



We'll call the project directory 'cdl-scraper'



mkdir cdl-scraper

cd cdl-scraper



--- 2. Create the Virtual Environment (venv) ---



This creates an isolated environment named 'venv' inside your project folder.



This keeps project dependencies separate from your main Python installation.



python -m venv venv



--- 3. Activate the Virtual Environment ---



This step is critical. Once activated, all 'pip install' and 'python' commands



will only affect this specific project environment.



Note: This path is standard for Windows PowerShell/CMD.



.\\venv\\Scripts\\activate



--- 4. Install Dependencies ("The Goodies") ---



We need three specific libraries:



1\. requests: To fetch the raw HTML content from the URL.



2\. pandas: The primary data analysis library for reading the HTML table and converting it to a CSV.



3\. lxml: A fast HTML parser that pandas requires for efficient web scraping (the 'flavor' used in the script).



pip install pandas requests lxml



--- 5. Save the Python Script ---



At this point, you should save the code below into a file named 'scrape\_stats.py'



inside the 'cdl-scraper' folder.



--- 6. Run the Script ---



Once the environment is active and the script is saved, run it with this command:



python scrape\_stats.py



--- 7. Deactivate the Environment (When done working) ---



When you are finished with your session, run this to exit the isolated environment.



deactivate

