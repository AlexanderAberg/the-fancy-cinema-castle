const editButtons = document.getElementsByClassName("btn-edit");
const bookText = document.getElementById("id_body");
const bookForm = document.getElementById("bookForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
 * Initializes edit functionality for the provided edit buttons.
 * 
 * For each button in the `editButtons` collection:
 * - Retrieves the associated bookings ID upon click.
 * - Fetches the content of the corresponding bookings.
 * - Populates the `bookText` input/textarea with the bookings content for editing.
 * - Updates the submit button's text to "Update".
 * - Sets the form's action attribute to the `edit_book/{bookId}` endpoint.
 */
for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let bookId = e.target.getAttribute("data-book_id");
        let bookContent = document.getElementById(`bookings${bookId}`).innerText;
        bookText.value = bookContent;
        submitButton.innerText = "Update";
        bookForm.setAttribute("action", `edit_book/${bookId}`);
    });
}

/**
 * Initializes deletion functionality for the provided delete buttons.
 * 
 * For each button in the `deleteButtons` collection:
 * - Retrieves the associated bookings ID upon click.
 * - Updates the `deleteConfirm` link's href to point to the 
 * deletion endpoint for the specific booking.
 * - Displays a confirmation modal (`deleteModal`) to prompt 
 * the user for confirmation before deletion.
 */
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let bookId = e.target.getAttribute("data-book_id");
        deleteConfirm.href = `delete_book/${bookId}`;
        deleteModal.show();
    });
}