# DraftManager

A simple and scalable web app on Azure for creating and managing pods of players for a card game draft.

## Overview

This web app allows a user to run a card game draft night with multiple rounds and pods of players. The app does not store any data on the server, but the user can export the data as a CSV file. The app allows the user to specify the number of players in each pod, and randomly assigns players to pods for each round. The app also handles the cases when the total number of players changes, or when there are not enough players to fill every pod. The app shows a countdown timer for each round, and allows the user to pause, resume, or end the process.

## Features

- Web app hosted on Azure App Service
- Python code for the backend logic
- No data storage on the server
- User can export data as CSV file
- User can specify number of players in each pod
- Random assignment of players to pods for each round
- Handling of incomplete pods and extra players
- Countdown timer for each round
- Pause, resume, and end functions
