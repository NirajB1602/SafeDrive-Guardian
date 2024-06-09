# SafeDrive Guardian

SafeDrive Guardian is a comprehensive safety application designed to prevent accidents caused by driver drowsiness and distractions. It integrates various technologies such as machine learning, navigation, and real-time tracking to enhance driver safety and promote responsible driving habits.

## Features:

### Drowsiness Detection using Machine Learning:
The application employs a machine learning model to detect driver drowsiness by analyzing eye movements and facial expressions. Camera frames captured at regular intervals are processed to determine the driver's alertness level.

### Navigation using OSRM API:
SafeDrive Guardian offers navigation functionality powered by the Open Source Routing Machine (OSRM) API. Users can access real-time navigation instructions to reach their destination safely and efficiently. Note that although Google Maps' API could be used for navigation, we opted for an open-source solution to avoid dependency on a paid API.

### Frontend developed in React Native:
The frontend of the application is built using React Native, a popular framework for developing cross-platform mobile applications. This ensures a responsive and user-friendly interface across different devices and operating systems.

### Backend powered by Node.js and Flask:
SafeDrive Guardian's backend infrastructure is implemented using Node.js for handling user authentication, data processing, and API requests. Flask, a lightweight web framework, is utilized to integrate the machine learning model into the application.

### Database managed with MongoDB:
MongoDB serves as the database solution for SafeDrive Guardian, enabling efficient storage and retrieval of user data, driving history, and application settings.

### Speed tracking using Expo Location API:
The application leverages the Expo Location API for real-time tracking of vehicle speed. This feature provides users with accurate feedback on their driving speed and encourages adherence to speed limits.

## Usage:

### Starting the Servers:
To use the SafeDrive Guardian application, follow these steps:

1. Start the React frontend server:
    ```bash
    cd frontend
    npm start
    ```

2. Start the Node.js backend server:
    ```bash
    cd backend
    npm start
    ```

3. Start the Flask server:
    ```bash
    cd backend
    python app.py
    ```

## Flow of Project:

### User Authentication:
Users are required to log in to the application using their credentials before accessing its features. Authentication mechanisms ensure secure access to user-specific data and functionalities.

### Frame Capture:
Camera frames are captured at predefined intervals, typically every 5 seconds, using the device's camera. These frames serve as input data for the drowsiness detection model.

### Data Transmission:
Captured frames are converted into form data and transmitted to the Flask server via a custom API endpoint. The Flask server receives and processes the incoming data for further analysis.

### Data Processing:
At the Flask server, the received form data is preprocessed and formatted to meet the requirements of the machine learning model. Data transformation tasks include image resizing, normalization, and feature extraction.

### Drowsiness Detection:
The preprocessed data is fed into the machine learning model, which predicts the driver's drowsiness level based on eye movements and facial expressions. The model outputs a score indicating the likelihood of drowsiness (0 for closed eyes, 1 for open eyes).

### Score Monitoring:
The React server continuously monitors the drowsiness score received from the Flask server. If the score exceeds a predefined threshold, an alarm is triggered to alert the driver and prompt them to take corrective action.

## Future Work:

### Driving Mode Module:
A future enhancement for SafeDrive Guardian includes the development of a driving mode module. This module aims to further enhance driver safety by implementing features to limit or restrict user actions on the mobile device while driving. Possible functionalities may include disabling certain app features, blocking incoming notifications, or providing voice-based controls.

## Contributors:

- [Niraj Bansal](https://github.com/NirajB1602)

Feel free to fork, contribute, and share this project with others interested in improving driver safety through technology!
