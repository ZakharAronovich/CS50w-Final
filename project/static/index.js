// Datetime selector properties
flatpickr("input[type=datetime-local]", 
    {
        enableTime: true,
        dateFormat: "Y-m-d H:i",
        altInput: true,
        altFormat: "F j, Y (h:S K)",
        defaultDate: Date.now(),
        minDate: Date.now(),
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
        if (!dialogWrapper.contains(e.target)) {
            taskDialog.close();
        }
    })
}


// Toggle sections open & closed dependant on each other's state
function toggleElements(prevElPointer, nextElPointer) {
    const prevEl = document.querySelector(prevElPointer);
    const nextEl = document.querySelector(nextElPointer);

    prevEl.style.display = "none";
    nextEl.style.display = "flex";
}


// Navigate through the course form
function courseFormNavigation(event) {
    const navButton = event.target.parentNode;
    const submitButton = document.getElementById("course-form-button");

    if (navButton.id == "form-nav-button-1") {
        toggleElements(".course-form-title", ".course-form-description");

    } else if (navButton.id == "form-nav-button-2") {
        toggleElements(".course-form-description", ".course-form-image");

    } else if (navButton.id == "form-nav-button-3") {
        toggleElements(".course-form-image", ".course-form-tags");

        // At the last section, show the submit button
        submitButton.style.display = "flex";
    }

}