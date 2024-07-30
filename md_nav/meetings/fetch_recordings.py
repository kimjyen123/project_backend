"""
This script fetches recordings from a specified API endpoint using a curl command,
parses the JSON response to retrieve all recordings, and then identifies and prints
the most recent recording based on the 'posted_timestamp' field.

Dependencies:
- Python 3.x
- subprocess module
- json module
- datetime module
- dateutil.parser

Usage:
Run this script directly using Python:
    python fetch_most_recent_recording.py

The script will output the total number of recordings found and the details of the
most recent recording.
"""

import subprocess
import json
from datetime import datetime
from dateutil.parser import isoparse

def fetch_recordings():
    try:
        # Execute curl command to get recordings
        command = "curl -X GET \"http://mdnavenv2.eba-7c8mvb5g.us-east-2.elasticbeanstalk.com/api/recordings/\""
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        if result.returncode != 0:
            print("Failed to fetch recordings:", result.stderr)
            return []

        # Parse JSON response
        recordings = json.loads(result.stdout)
        return recordings
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def get_most_recent_recording(recordings):
    if not recordings:
        return None

    # Convert timestamps to datetime objects
    for recording in recordings:
        recording['posted_timestamp'] = isoparse(recording['posted_timestamp'])

    # Find the most recent recording
    most_recent = max(recordings, key=lambda x: x['posted_timestamp'])
    return most_recent

def main():
    recordings = fetch_recordings()
    total_recordings = len(recordings)
    print(f"Total recordings found: {total_recordings}")

    most_recent_recording = get_most_recent_recording(recordings)
    if most_recent_recording:
        print("Most recent recording:")
        print(f"ID: {most_recent_recording['id']}")
        print(f"Timestamp: {most_recent_recording['posted_timestamp']}")
        print(f"Details: {most_recent_recording}")
    else:
        print("No recordings found.")

if __name__ == "__main__":
    main()
