<template>
    <div>
        <button class="btn btn-primary" data-bs-toggle="modal" :data-bs-target="'#editModal' + item.id">
            Edit
        </button>
        <div class="modal fade" :id="'editModal' + item.id" tabindex="-1" ref="editModal" aria-labelledby="editModalLabel"
            aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="editModalLabel">Edit Item</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form @submit.prevent="submitEditForm">
                            <div class="mb-3">
                                <label for="editCharField" class="form-label">Char Field</label>
                                <input type="text" class="form-control" id="editCharField" v-model="editableItem.char_field"
                                    required>
                            </div>
                            <div class="mb-3">
                                <label for="editDateField" class="form-label">Date Field</label>
                                <input type="date" class="form-control" id="editDateField" v-model="editableItem.date_field"
                                    required>
                            </div>
                            <div class="mb-3">
                                <label for="editEmailField" class="form-label">Email Field</label>
                                <input type="email" class="form-control" id="editEmailField"
                                    v-model="editableItem.email_field" required>
                            </div>
                            <div class="mb-3">
                                <label for="editIntegerField" class="form-label">Integer Field</label>
                                <input type="number" class="form-control" id="editIntegerField"
                                    v-model="editableItem.integer_field" required>
                            </div>
                            <button type="submit" class="btn btn-primary">Save changes</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        item: Object,
        uniqueId: {
            type: [String, Number],
            required: true
        }
    },
    data() {
        return {
            editableItem: {},
        };
    },
    watch: {
        item: {
            immediate: true,
            handler(newValue) {
                this.editableItem = { ...newValue };
            }
        }
    },
    methods: {
        async submitEditForm() {
            if (!this.editableItem.id) {
                console.error('Error: No ID provided for editable item');
                return;
            }
            try {
                const response = await fetch(`http://localhost:8000/api/mymodel/${this.editableItem.id}/`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(this.editableItem),
                });
                if (response.ok) {
                    const data = await response.json();
                    this.$emit('item-edited', { ...data, id: this.editableItem.id });
                    const editModalId = 'editModal' + this.editableItem.id;
                    const editModal = bootstrap.Modal.getInstance(document.getElementById(editModalId));
                    if (editModal) {
                        editModal.hide();
                    }
                    document.querySelectorAll('.modal-backdrop').forEach(backdrop => backdrop.remove());
                } else {
                    console.error('Error updating item:', response.statusText);
                }
            } catch (error) {
                console.error('Error:', error);
            }
        },
    },
};
</script>
