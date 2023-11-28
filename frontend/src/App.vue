<template>
  <div class="container pt-3">
    <div class="h1 text-center border rounded bg-light p-2 mb-3">
      MyModel API Client
    </div>
    <!-- List Component -->
    <list-component :items="items" @update-items="handleUpdateItems" @delete-item="handleDeleteItem" />
    <!-- Add Component -->
    <add-component @item-added="addItem"></add-component>
  </div>
</template>

<script>
import ListComponent from './Components/List.vue';
import AddComponent from './Components/Add.vue';

export default {
  components: {
    ListComponent,
    AddComponent,
  },
  data() {
    return {
      items: [],
      selectedItem: null,
      showUpdateModal: false,
    };
  },
  async mounted() {
    await this.fetchItems();
  },
  methods: {
    async fetchItems() {
      try {
        const response = await fetch('http://localhost:8000/api/mymodel/');
        if (response.ok) {
          this.items = await response.json();
        } else {
          console.error('Error fetching items:', response.statusText);
        }
      } catch (error) {
        console.error('Error:', error);
      }
    },
    async addItem(newItem) {
      this.items.push(newItem);
      await this.fetchItems();
    },
    async handleUpdateItems(updatedItem) {
      const index = this.items.findIndex(item => item.id === updatedItem.id);
      if (index !== -1) {
        // Update the item in the array
        this.items[index] = updatedItem;
        // Replace the array to trigger reactivity
        this.items = [...this.items];
        await this.fetchItems();
      }
    },
    async handleDeleteItem(itemId) {
      // Ask for confirmation
      if (confirm('Are you sure you want to delete this item?')) {
        try {
          const response = await fetch(`http://localhost:8000/api/mymodel/${itemId}/`, {
            method: 'DELETE',
          });
          if (response.ok) {
            // Remove the item from the local array
            this.items = this.items.filter(item => item.id !== itemId);
          } else {
            console.error('Error deleting item:', response.statusText);
          }
        } catch (error) {
          console.error('Error:', error);
        }
      }
    }
  }
}
</script>