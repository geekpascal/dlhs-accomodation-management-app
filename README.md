# DLHS Accommodation Management App

This project is a full-stack accommodation management application originally built for the DLHS program, which ran from March 28th to April 2nd, 2024. The app was deployed and used at a massive scale, with close to 4000 participants registering and managing their accommodation through the platform.

## Project Context

- **Purpose:** The app was designed to help organizers efficiently manage accommodation logistics for thousands of attendees during the five-day event.
- **Database:** Initially, the app used a remote PostgreSQL database. Since the program has ended and all data has been retrieved by the organizers, the app now uses SQLite for local testing and demonstration purposes.
- **Reference:** This repository is maintained for reference only. You can run the app locally to see how it worked during the event.
- **Note:** This was my first full-stack application and my first deployed app used at scale.

## Features

- Registration and accommodation management for attendees
- Admin views for managing hostel assignments
- Export functionality for participant data

## Running Locally

1. **Clone the repository:**
	```powershell
	git clone <repo-url>
	cd dlhs-accomodation-management-app-main
	```
2. **Install dependencies:**
	```powershell
	pip install -r requirements.txt
	```
3. **Run the application:**
	```powershell
	python index.py
	```
4. **Access the app:**
	Open your browser and go to `http://localhost:5000`.

## Notes

- The app now uses SQLite, so no remote database setup is required.
- All original event data has already been retrieved by the organizers.
- This repository is for demonstration and reference only.


