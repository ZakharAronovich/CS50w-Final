// Datetime selector properties
flatpickr("input[type=datetime-local]", 
    {
        enableTime: true,
        dateFormat: "Y-m-d H:i",
        altInput: true,
        altFormat: "F j, Y (h:S K)",
        defaultDate: "today", 
        static : true,       
    }
);

// Toggle the task creation form dialog
function toggleTaskDialog() {
    const taskDialog = document.querySelector(".task-form-dialog");
    const dialogWrapper = document.querySelector(".task-form-wrapper");
    
    // Show the dialog when the button is clicked
    taskDialog.showModal();

    // Close the dialog once anything rather than the dialog is clicked
    taskDialog.addEventListener("click", (e) => {
        if (!dialogWrapper.contains(e.target))  {
            taskDialog.close();
        }
    })
}
