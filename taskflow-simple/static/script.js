document.addEventListener("DOMContentLoaded", () => {
    const taskForm = document.querySelector("form");
  
    if (taskForm) {
      taskForm.addEventListener("submit", (e) => {
        const title = document.querySelector('input[name="title"]').value.trim();
        const description = document.querySelector('input[name="description"]').value.trim();
        const assignee = document.querySelector('input[name="assignee"]').value.trim();
        const dueDate = document.querySelector('input[name="due_date"]').value;
  
        if (!title || !description || !assignee || !dueDate) {
          e.preventDefault();
          alert("Please fill in all task fields.");
        }
      });
    }
  });
  