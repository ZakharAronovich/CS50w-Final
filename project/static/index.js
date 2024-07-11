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
function courseFormNavigation(navButton) {
    const submitButton = document.getElementById("course-form-button");
    
    if (navButton.dataset.step == "1") {
        toggleElements(".course-form-title", ".course-form-description");

    } else if (navButton.dataset.step == "2") {
        toggleElements(".course-form-description", ".course-form-image");

    } else if (navButton.dataset.step == "3") {
        toggleElements(".course-form-image", ".course-form-tags");

        // At the last section, show the submit button
        submitButton.style.display = "flex";
    }

}


// Add and remove tags in the course form
function toggleTag(tagElement) {
    if (tagElement.className == "tag") {
        tagElement.className = "tag active";
    } else {
        tagElement.className = "tag";
    }
}