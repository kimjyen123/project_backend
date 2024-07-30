document.addEventListener('DOMContentLoaded', function() {
    // Fetch and display doctors
    fetch('/api/doctors/')
        .then(response => response.json())
        .then(data => {
            const doctorsList = document.getElementById('doctors-list');
            data.forEach(doctor => {
                const li = document.createElement('li');
                li.textContent = `${doctor.first_name} ${doctor.last_name} - ${doctor.hospital}`;
                doctorsList.appendChild(li);
            });
        });

    // Fetch and display meetings
    fetch('/api/meetings/')
        .then(response => response.json())
        .then(data => {
            const meetingsList = document.getElementById('meetings-list');
            data.forEach(meeting => {
                const li = document.createElement('li');
                li.textContent = `${meeting.first_name} ${meeting.last_name} - ${meeting.meeting_date} - ${meeting.instrument_name}`;
                meetingsList.appendChild(li);
            });
        });

    // Fetch and display customers
    fetch('/api/customers/')
        .then(response => response.json())
        .then(data => {
            const customersList = document.getElementById('customers-list');
            data.forEach(customer => {
                const li = document.createElement('li');
                li.textContent = `${customer.name} - ${customer.linkedin_info}`;
                customersList.appendChild(li);
            });
        });

    // Fetch and display devices
    fetch('/api/devices/')
        .then(response => response.json())
        .then(data => {
            const devicesList = document.getElementById('devices-list');
            data.forEach(device => {
                const li = document.createElement('li');
                li.textContent = `${device.device_name} - ${device.summary_of_recent_papers}`;
                devicesList.appendChild(li);
            });
        });

    // Fetch and display recordings
    fetch('/api/recordings/') // Add this part for recordings
        .then(response => response.json())
        .then(data => {
            const recordingsList = document.getElementById('recordings-list');
            data.forEach(recording => {
                const li = document.createElement('li');
                li.textContent = `ID: ${recording.id} - Text: ${recording.text}`;
                recordingsList.appendChild(li);
            });
        });
});
