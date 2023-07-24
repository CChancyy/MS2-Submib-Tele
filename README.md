# Table of Contents

1. [Ideation](#ideation) 
2. [Getting Started](#getting-started)
3. [System Overview](#system-overview)
4. [Testing](#testing)

## Ideation
### 1.1 Problem Defined
Students residing in school hostels often face many problems due to inefficiencies in the laundry service. 

1) Students have to physically visit the laundry room to check for available washing machines. Therefore, they may often find themselves carrying bulky laundry bags downstairs only to discover that all the washing machines are already occupied. This leaves them with no choice but to wait for the machines to become available, which can take a long time, especially if the previous user is out for class.

2) Students have to manually keep track of the finishing time by setting alarms to remind themselves. However, many students find this process troublesome and does not want their alarm to disrupt them during classes or meetings.

3) Many students also face the problem that they lost/found a piece of clothes but do not know where to report it. 

Since no existing solutions address all of these problems, we are motivated to create a Telegram Bot accompanied by a website to tackle these issues. 

The website will present users the availability of washing machines and dryers, enabling residents to check their vacancies before heading down to the laundry rooms. 

Users can notify our Telegram Bot when they start a washing machine or dryer, and the bot will record the starting time and send reminders when the laundry is about to finish and when it is finished. This feature allows users to easily find out when their laundry will be done and plan their time better.

### 1.2 Aim
Our project's primary focus is on enhancing the laundry experience for students living in school hostels. Our aim is to improve the efficiency of washing clothes for them.

### 1.3 User Story
1. As a student who wish to avoid wasting time checking for washing machine vacancies in person, I want to be able to effortlessly check the availability of washing machines before making my way down. This can be down through platforms such as Telegram Bot and website as I am more familar with them.

2. As a student who feels it is troublesome to set alarms for laundry reminders and wish to avoid disturbances during class or meetings, I want to be able to receive a notification once the laundry is done. 

3. As a student who wants to better cope with situations like clothes accidentally left in the washing machine by the previous user, I wish to be able to contact the previous user and resolve any lost-and-found laundry items.

### 1.4 Planned Procedure
![image](https://github.com/CChancyy/MS3-Tele/assets/110718225/f8c7f16c-2f6d-4872-9483-c74cf7216f78)
(a) The machine will generate a QR code after the user selects a washing machine or dryer and completes the payment.

(b) The user scans the QR code and it will redirect them to our built Telegram Bot. The bot will recognise the user's account,  associating it with the selected dryer, for instance, the account with the handle @John123 will be linked to Dryer 1.

(c) At the same time, the Web will be updated with the availability status of each washing machine. This allows users to conveniently check the availability before heading to the laundry room.

(d)As the washing machine nears completion (e.g., approximately 5 minutes before finishing), the bot will send a reminder message to the user, prompting them to come down and collect their laundry.

(e) Once the washing machine finishes its cycle (e.g., Dryer 1 completes), the bot will promptly notify the user (e.g., @John123) that their laundry is ready.

(f) If users find clothes that do not belong to them, they can utilize the contact-previous-user function to contact the previous user and resolve lost-and-found laundry items efficiently. 

### 1.5 Features built
#### 1.5.1 Telegram Bot
1. **Selecting locations and machines**
- The bot utilizes Telegram's Keyboard Reply function to offer users a user-friendly interface for selecting their desired location and laundry machines.

2. **Timer function for laundry reminders**
- The bot  incorporates a timer function that sends reminders after 25 minutes. Once the laundry is completed, another message notifies the user.

3. **Updating Firebase on the availability of each machine**
- For real-time tracking of laundry machine availability, the bot integrates with Firebase as its backend. When a user selects a machine, the Firebase database is promptly updated to mark it as "unavailable".

4. **Recording and updating the user's laundry collection status**
- The bot efficiently maintains and updates the user's laundry collection status. Once the user collects their laundry, this status is promptly updated in the Firestore database.

5. **Reward system for timely laundry collection**
- To incentivize timely laundry collection, the bot implements a reward system. Users who collect their laundry within 5 minutes are rewarded with 5 points.

6. **Displaying top 5 users with the most points**
= The bot shows a leaderboard featuring the Telegram handles of the five users with the highest points earned through timely laundry collection.

7. **Contacting the previous user**
- For seamless communication between users, the bot offers a convenient feature to contact the previous user of a laundry machine. If the user wants to contact the previous user of the machine, the bot can help to forward the message from the current user to the previous user. This facilitates effective communication or timely information exchange, such as prompting the previous user to collected their laundry or helping to resolve lost-and-found items.

#### 1.5.2 Website
1. **Login page**
- The website  incorporates a login page, allowing users to access their accounts  using their email credentials if they already have an existing account.

2. **Sign up page**
- For new users, they can register one with their email on the "Sign Up" page. Once they registered, their email credentials will be uploaded to the Firestore database, ensuring a seamless account creation process.

3. **Edit profile page"**
- To personalize their experience, the website features an "Edit Profile" page. Users can modify their default location, with Location 1 as the default setting. Any changes made will be promptly updated in the Firestore database. The website will remember their default location and automatically select the location upon successful login.

4. **Leaderboard**
- The website showcases a leaderboard page, displaying the top 5 users with the highest points earned through timely laundry collection. This leaderboard feature adds an element of competition and recognition for users who consistently collect their laundry in a timely manner.
...
![Web structure](https://github.com/CChancyy/MS3-Tele/assets/110718225/11ee4ea4-41ac-422a-ad96-fad73f47fea2)



### 1.6 Tech Stack
Front end: react <br>
Backend: Firebase

## Getting Started
### 2.1 Prerequisites
- Cloud Firebase
- Visual Studio Code 
- Node.js
- Codesandbox 
- Github

### 2.2 Installation
#### 2.2.1 Telegram Bot 
1. Download the zip file from https://github.com/CChancyy/MS2-Submib-Tele.git 
2. Install by running the following in the directory <br>
   `pip install python-telegram-bot` <br>
   `pip install nest_asyncio` <br>
   `pip install firebase_admin`<br>
3. Change the path to the path to service account in your own laptop
![image](https://github.com/CChancyy/MS3-Tele/assets/110718225/27c8237c-fd02-417b-8087-f3263264bd1f)

#### 2.2.2 Website
1. Download the zip file from https://github.com/z-wenqing/MS3-website/tree/master
2. Install by running the following in the directory `npm install`
3. Install Firebase by running `npm install firebase`
4. Start the app by running `npm start`
5. Open https://localhost:3000 with your browser to see the website <br>
**Note**:
1. every time the user declares the usage in the Telegram Bot, the website has to be refreshed to view the updated availability (may need to wait for about 1 second).
2. if the user updates on the Telegram Bot after he logged into the website, he has to manually select location when he refreshed the page. (need to solve)



### 2.3 File Structure
#### Folders
- `components` folder contains all our react components like `WelcomeBanner.js`
- `config` folder contains configuration files for the firestore database

#### Files
- `App` contains routing of our website
- `gitignore` contains files and folders to be ignored when pushing to github
- `styles.css``home.css``navigation.css` are configuration files for the website

...

## System Overview
The system comprises three components: the Telegram Bot, Firestone Database, and the website. The Firestone Database serves as a core platform to connect the Telegram Bot and the website. The Telegram Bot updates the availability of the machines stored in the Firestore Database once the users declare their use in the Bot. The website can read from the database and update the website accordingly.
![image](https://github.com/CChancyy/MS3-Tele/assets/110718225/1db68e42-17f4-4750-8d37-f012ca221b04)

### 3.1 System Design
Originaly, we planned to use a MySQL Database for connecting the Telegram Bot and the website, as depicted in the following diagram. 
![image](https://github.com/CChancyy/MS3-Tele/assets/110718225/822585bf-daf3-474a-b79e-e8a0243d8306)
However, after conducting thorough research and analysis, we found the manual setup of this connection to be extremely complex and challenging. As a result, we decided to switch to Cloud Firestore, and the new database diagram is shown in the second diagram. Cloud Firestore can offer several advantages, such as easier setup and scalability, which can significantly simplify the process of connecting our Telegram Bot and website to the database. It allows us to store and retrieve data for our Telegram Bot and website more efficiently.


## Testing
1. **Test Case**: I am a student who wants to check the availability of the machines before I head to laundry rooms so that I can plan my time better.

**Expected Output**: when there is a change in the availability status in Firestore Database, the website is updated accordingly.

**Actual Output**:
When a user indicates that he is using Dryer 1 in Block E on the Telegram Bot, the website is updated correctly.
![image](https://github.com/CChancyy/MS3-Tele/assets/110718225/1293a806-8368-4043-9c3f-1a235acb4f31)


2. **Test case**
I am a student who wants to have personalised website page so that I can select my default address, eliminating the need to manually select the location every time I log in.

**Expected Outcome**: I am able to select my default location and the location will be automatically selected when I log in.

**Actual Output**: 
When the default location is updated to 2 in the profile, the location "RVRC Block F" would be automatically selected once the user logs in.
![image](https://github.com/CChancyy/MS3-Tele/assets/110718225/1733215b-b87a-463b-8f94-0216c249e1f6)

3. **Test case**: 
I am a student who wants to be reminded to collect my laundry so that I can collect laundry in time and others can use the machine.

**Expected Outcome**: Reminder message to be sent after 25 minutes and when the laundry is done.

**Actual Outcome**: 
![image](https://github.com/CChancyy/MS3-Tele/assets/110718225/601ad8f1-e763-4f54-abe8-e58c5d1ca45f)

4. **Test case**: 
I am a student who wants to be awarded points when I have collected my laundry in a timely manner so that I will be more incentivised to collect my laundry in time.

**Expected Outcome**:  The user will be awarded points when they collect their laundry in a timely manner. They can also check their points as well as the leaderboard.

**Actual Outcome**: 
![image](https://github.com/CChancyy/MS3-Tele/assets/110718225/aaabb4fd-1c52-4099-a7d3-5505bffe90d1)
Message is sent after the user indicate that he has collected laundry and his point is also displayed.

### 4.1 Unit testing
We split the whole process into small sections and test the connection between each section.

#### 4.1.1 Testing the Connection between Web and Cloud Firestore
Change the availability of machine manually on Cloud Firestore, and refresh the page to see whether the web is updated corrected. If it is updated accordingly, we know that web and firebase is connected.
![image](https://github.com/CChancyy/MS3-Tele/assets/110718225/5825a0da-d24c-4589-a9bc-331f374f9d70)

#### 4.1.2 Testing the connection between Python and Cloud Firestore
Run a simplified file to test the connection between Python and Cloud Firestore.
![image](https://github.com/CChancyy/MS3-Tele/assets/110718225/92187fbf-7536-4fa5-a335-780403489d2c)

### 4.3 User testing
We conducted testing with 10 NUS students to evaluate the Telegram Bot and website. After engaging with the telegram bot and making commands, we sought their feedback on their experience using both the Telegram Bot and the web platform. The outcome is evident that 80% of them agreed that the laundry system significantly improves the efficiency of the laudnry process. This positive feedback reflects the effectiveness of the platform in streamlining laundry management and enhancing the overall user experience. We also take their suggestions into consideration and incorporate their valuable suggestions to enhance the platform. 




