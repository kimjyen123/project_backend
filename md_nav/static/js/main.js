document.addEventListener('DOMContentLoaded', function() {
    fetch('http://127.0.0.1:8000/api/doctors/')
        .then(response => response.json())
        .then(data => {
            const doctorsList = document.getElementById('doctors-list');
            data.forEach(doctor => {
                const li = document.createElement('li');
                li.textContent = `${doctor.first_name} ${doctor.last_name}  - ${doctor.hospital}`;
                doctorsList.appendChild(li);
            });
        });

    fetch('http://127.0.0.1:8000/api/meetings/')
        .then(response => response.json())
        .then(data => {
            const meetingsList = document.getElementById('meetings-list');
            meetingsList.innerHTML = '';  // Clear existing content if needed
    
            data.forEach(meeting => {
                const li = document.createElement('li');
                li.textContent = `${meeting.first_name} ${meeting.last_name}, ${meeting.doctor_hospital} - ${meeting.meeting_date} - ${meeting.instrument_name}`;
                meetingsList.appendChild(li);
            });
        })
        .catch(error => console.error('Error fetching meetings:', error));
    

    fetch('http://127.0.0.1:8000/api/customers/')
        .then(response => response.json())
        .then(data => {
            const customersList = document.getElementById('customers-list');
            data.forEach(customer => {
                const li = document.createElement('li');
                li.textContent = `${customer.name} - ${customer.linkedin_info}`;
                customersList.appendChild(li);
            });
        });

    fetch('http://127.0.0.1:8000/api/devices/')
        .then(response => response.json())
        .then(data => {
            const devicesList = document.getElementById('devices-list');
            data.forEach(device => {
                const li = document.createElement('li');
                li.textContent = `${device.device_name} - ${device.summary_of_recent_papers}`;
                devicesList.appendChild(li);
            });
        });
});
