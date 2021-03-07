# Find A Vaccine - OSDH

## What the script does:
**TLDR;** Scans the Oklahoma State Department of Health (OSDH) website to find covid vaccine sites, with available appointments, within a distance you're comfortable with travelling to receive one. 

The process (as of 3/5/2021) to get to a COVID-19 vaccine through the OSDH is a bit clunky to say the least:

1. You fill out the health questionaire on https://vaccinate.oklahoma.gov. You should recieve an email saying that you are registered.
2. If it is determined that you are eligible for the current phase, you will be allowed to search their map for locations that have available appointments within a range that you determine. 
3. You should recieve a second email, when you are eligible to recieve the vaccine, with a link that will take you back to the site where you enter your birthday and locate a site with an available appointment slot. 
4. You book the appointment at which ever location has an available slot. ** **IMPORTANT NOTE:** Before booking the slot, please take notice of whether the site offers the **first dose, second dose, or both** **

If you can not find an appointment site, you must return to the site at a later time to search again. Essentially, I got tired of searching manually, so I wrote this script. It can be scheduled to run. I ran it hourly until I found a site to book the appointment to receive my first dose. 

When the script runs is opens a Selenium browser that loads the https://vaccinate.oklahoma.gov site using the link from the second email mentioned above. It then enters the birthday, which you must set in the script. That will take the browser to the map screen where it will enter the location for the person and the distance you're willing to travel which defaults to 25 miles up to 400 miles. That will refresh the list of locations next to the map. The script parses that list and looks for the words "Book Appointment" which only shows on the locations that have slots available. Those locations will be emailed back to the given email address signaling that there is a vaccine location with available time/vaccine slots.

## What the script does NOT do:
This script is not designed and was not intended to automatically reserve an appointment for you. It is a notification tool designed to check the site and notify you of slots to get vaccinated

This script does not check third-party vendors that may have available slots or waitlists such as Walmart or Walgreens. They do not use the ODSH system and must be independently monitored.

The emails that you will recieve do not strip out the default URLs like "Book Appointment" or "Get Directions". You cannot visit the appointment booking page or get directions page directly from the email. Sorry, I didn't have a chance to strip those out. You can however, use the "Go to Vaccine Page" link to visit the original link that came from the second email in step number 3.

## IMPORTANT INFORMATION:
The set up for this is not for the faint of heart. In order to run this script, there are a number of things that must be installed an in place first. My recommendation is to enlist a techie/programmer friend to either help or run it for you. 

This process could be exploited! If you have someone run this script for you, you need to trust this person. In order for this script to check to see if you have an appointment slot near you, it requires the URL provided to you by the state in that second email. That link includes a unique identifier, which along with your birthdate, connects your information and would allow someone to book an appointment FOR you. **DO NOT UNDER ANY CIRCUMSTANCES PROVIDE THAT PERSONAL INFORMATION TO ANOTHER PERSON IF YOU DO NOT TRUST THEM TO KEEP IT SAFE AND THAT THEY WILL HELP YOU FIND A VACCINE LOCATION.**

Once an appointment is booked for the unique ID provided in the URL from the second email, the link is no longer valid. You will not be able to go back through the site. I have had the first shot only and my link is no longer valid. You may have to go back through the process starting at step 1 in order to book an appointment for your second link. See the IMPORTANT NOTE from step 4.

This script worked as of 3/1/2021. If the state modifies their site or the process, it may not continue working as written and would need to be updated. I do not intend on updating it as I have limited access to the system now that I've scheduled my first appointment (see above). 

## Required Software:
- Python 3.x
- - Python Modules:
- - - [ezgmail](https://github.com/asweigart/ezgmail) (to email results)
- - - [selenium](https://github.com/SeleniumHQ/selenium/) (to automate the loading and navigating of the site)
- - - [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) (to parse the contents)
- Selenium WebDriver (The script uses the Chrome WebDriver as is. I doubt changing it to use another would be terribly difficult.)
- A [GMail](https://gmail.com) account is required to use this script as is.

## Setup Software (for the most part, follow the recommended installation of the following):
- Python (https://www.python.org/downloads/)
- Selenium WebDriver (https://sites.google.com/a/chromium.org/chromedriver/)
- Setup notes:
- - Make sure the path to your Selenium WebDriver is included in your PATH environment variable
- - Create a virtual environment to install the required Python modules
- - You must follow the GMail setup as outlined in the ezgmail instructions in order for this to work as is. Further modifications may be made to work with other email systems.
- - Schedule the script to run. The instructions below are for a Windows 10 environment that I have admin access on. Your system may be different.

## Basically:
- Install Python
- Install Selenium
- git clone <repo> (at the command prompt where you want the directory created)
- Open the directory
- Run in command `python -m venv venv`
- Run in command `.\venv\activate.bat`
- Run in command `pip install -r requirements.txt`
- Modify the "run.bat" file with the correct paths to the Virtual Environment Activate script and the "app.py" script.
- Modify the app.py with your information
- - Line 18: The link (or list of links if you're running it for multiple people) from the second email. ex: https://vaccinate.oklahoma.gov/follow-up-vaccine/?id=<random string of letters and numbers>
- - Lines 30-34: Birth month, day, year, email address of the first link from the urls entered on line 18, address, and acceptable distance from the address provided (5, 10, 25, 50, 100, 400) in miles.
- - Lines 40-52: Uncomment the variables and elif statement for the next link (and so on) in your urls variable from line 18 if applicable.
- Schedule the "run.bat" command through Task Scheduler (or cron if running in linux)
- Make sure to leave your computer on during the times you have it scheduled to run.

I can not and will not provide any assurances or guarantees that this will run in your environment or work for you as it worked for me. I'm providing this script and instructions as educational information ONLY. It was a "quick and dirty" script that suited my needs and may be modified and improved freely. 
