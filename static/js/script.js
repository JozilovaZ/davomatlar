// Search functionality for employees
document.addEventListener('DOMContentLoaded', function() {
    const searchEmployee = document.getElementById('searchEmployee');
    if (searchEmployee) {
        searchEmployee.addEventListener('input', function(e) {
            const searchTerm = e.target.value.toLowerCase();
            const rows = document.querySelectorAll('#employeeTable tr');
            rows.forEach(row => {
                const text = row.textContent.toLowerCase();
                row.style.display = text.includes(searchTerm) ? '' : 'none';
            });
        });
    }

    // Employee form submission
    const employeeForm = document.getElementById('employeeForm');
    if (employeeForm) {
        employeeForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(this);
            console.log('Employee Form Data:', Object.fromEntries(formData));
            // Replace with your API call, e.g., fetch('/api/xodimlar/', { method: 'POST', body: formData })
            bootstrap.Modal.getInstance(document.getElementById('addEmployeeModal')).hide();
        });
    }
    //update
     const employeeForm = document.getElementById('employeeForm');
    if (employeeForm) {
        employeeForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(this);
            console.log('Employee Form Data:', Object.fromEntries(formData));
            // Replace with your API call, e.g., fetch('/api/xodimlar/', { method: 'POST', body: formData })
            bootstrap.Modal.getInstance(document.getElementById('updateEmployeeModal')).hide();
        });
    }

    // Attendance form submission
    const attendanceForm = document.getElementById('attendanceForm');
    if (attendanceForm) {
        attendanceForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(this);
            console.log('Attendance Form Data:', Object.fromEntries(formData));
            // Replace with your API call, e.g., fetch('/api/davomat/', { method: 'POST', body: formData })
            bootstrap.Modal.getInstance(document.getElementById('addAttendanceModal')).hide();
        });
    }

    // Edit and Delete button handlers
    document.querySelectorAll('.edit-employee').forEach(button => {
        button.addEventListener('click', function() {
            const id = this.dataset.id;
            console.log('Edit employee ID:', id);
            // Replace with your API call to fetch and populate form
        });
    });

    document.querySelectorAll('.delete-employee').forEach(button => {
        button.addEventListener('click', function() {
            const id = this.dataset.id;
            if (confirm('Xodimni o\'chirishni xohlaysizmi?')) {
                console.log('Delete employee ID:', id);
                // Replace with your API call to delete
            }
        });
    });

    document.querySelectorAll('.edit-attendance').forEach(button => {
        button.addEventListener('click', function() {
            const id = this.dataset.id;
            console.log('Edit attendance ID:', id);
            // Replace with your API call to fetch and populate form
        });
    });

    document.querySelectorAll('.delete-attendance').forEach(button => {
        button.addEventListener('click', function() {
            const id = this.dataset.id;
            if (confirm('Davomatni o\'chirishni xohlaysizmi?')) {
                console.log('Delete attendance ID:', id);
                // Replace with your API call to delete
            }
        });
    });
});