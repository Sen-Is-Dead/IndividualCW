<template>
    <div>
        <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#addModal">
            Add New Item
        </button>

        <div class="modal fade" id="addModal" tabindex="-1" ref="addModal" aria-labelledby="addModalLabel"
            aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="addModalLabel">Add New Item</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form @submit.prevent="submitForm">
                            <div class="mb-3">
                                <label for="charField" class="form-label">Char Field</label>
                                <input type="text" class="form-control" id="charField" v-model="newItem.char_field"
                                    required>
                            </div>
                            <div class="mb-3">
                                <label for="dateField" class="form-label">Date Field</label>
                                <input type="date" class="form-control" id="dateField" v-model="newItem.date_field"
                                    required>
                            </div>
                            <div class="mb-3">
                                <label for="emailField" class="form-label">Email Field</label>
                                <input type="email" class="form-control" id="emailField" v-model="newItem.email_field"
                                    required>
                            </div>
                            <div class="mb-3">
                                <label for="integerField" class="form-label">Integer Field</label>
                                <input type="number" class="form-control" id="integerField" v-model="newItem.integer_field"
                                    required>
                            </div>
                            <button type="submit" class="btn btn-primary">Submit</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
export default {
    data() {
        return {
            newItem: {
                char_field: '',
                date_field: '',
                email_field: '',
                integer_field: null
            }
        };
    },
    methods: {
        async submitForm() {
            try {
                const response = await fetch('http://localhost:8000/api/mymodel/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(this.newItem)
                });
                if (response.ok) {
                    const data = await response.json();
                    this.$emit('item-added', data);
                    this.resetForm();
                    // Close the modal using Bootstrap's JavaScript
                    this.closeModal();
                } else {
                    console.error('Error adding item:', response.statusText);
                }
            } catch (error) {
                console.error('Error:', error);
            }
        },
        resetForm() {
            // Reset the newItem object to clear the form fields
            this.newItem = { char_field: '', date_field: '', email_field: '', integer_field: null };
        },
        closeModal() {
            // Use Bootstrap's modal method to hide the modal
            const addModalElement = this.$refs.addModal;
            const addModal = bootstrap.Modal.getInstance(addModalElement);
            if (addModal) {
                addModal.hide();
            }
            // Remove the modal backdrop if it exists
            const backdrop = document.querySelector('.modal-backdrop');
            if (backdrop) {
                backdrop.remove();
            }
        }
    }
}

</script>
  