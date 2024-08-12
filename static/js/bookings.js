const editButtons = document.getElementsByClassName("btn-edit");
const bookForm = document.getElementById("bookForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

// Edit Button
document.addEventListener('DOMContentLoaded', function () {
    const editButtons = document.querySelectorAll('.btn-edit');
    editButtons.forEach(button => {
        button.addEventListener('click', function () {
            const url = button.getAttribute('data-action-url');
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    document.querySelector('#editModal #id_session_type').value = data.session_type;
                    document.querySelector('#editModal #id_amount').value = data.amount;
                    document.querySelector('#editModal #id_options').value = data.options;
                    document.querySelector('#editModal #id_wishes').value = data.wishes;
                    document.querySelector('#editModal #id_date').value = data.date;
                    document.querySelector('#editModal #id_book_id').value = data.id;
                    document.querySelector('#editBookingForm').action = url;
                })
                .catch(error => console.error('Error:', error));
        });
    });
    document.querySelector('#editBookingForm').addEventListener('submit', function (event) {
        event.preventDefault();
        const form = event.target;
        const formData = new FormData(form);
        fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': form.querySelector('[name=csrfmiddlewaretoken]').value
            }
        })
        .then(response => {
            if (response.ok) {
                // Reload the page to make changes visible
                location.reload();
            } else {
                return response.text().then(text => alert('Error: ' + text));
            }
        })
        .catch(error => console.error('Error:', error));
    });
});

// Delete Button
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let bookId = e.target.getAttribute("data-book_id");
        deleteConfirm.href = `delete_book/${bookId}`;
        deleteModal.show();
    });
}