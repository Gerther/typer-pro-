TyperPro

This project is a simple keyboard auto-presser tool with a graphical interface built on tkinter.
It allows users to select multiple keys, set custom press durations for each key, save/load key sequences to JSON files, and automatically press keys in a loop.

Current Features:
Add and remove keys dynamically.

Set individual press durations for each key.

Start/Stop the auto-presser.

Save key setups to a JSON file.

Load previously saved key setups from a JSON file.

Select a custom directory for saving settings.

Plans for the Future:
UI/UX Improvements:

Redesign the interface for a cleaner and more modern look.

Group related buttons (Start, Save, Load) into a toolbar.

Add status indicators (like "Running", "Stopped") on the window.

Make the window resizable and adaptive.

Feature Upgrades:

Add the ability to set an interval between entire key sequences (not just per key).

Allow setting a number of loops or a stop timer.

Implement a global hotkey (e.g., F8) to start/stop the presser without focusing the app.

Add a "Test" mode to simulate a single loop before actual starting.

Code Improvements:

Refactor global variables into a class for better organization.

Improve threading (e.g., add safe thread termination).

Add error handling for invalid inputs (e.g., non-numeric duration).

Advanced Ideas (maybe later):

Support mouse auto-clicking along with keyboard pressing.

Create profiles (different key setups saved under different names).

Add key recording: user presses a sequence once, and the app records it automatically.