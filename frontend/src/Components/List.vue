<template>
  <div>
    <h2>List of Items</h2>
    <table class="table">
      <thead>
        <tr>
          <th>ID</th>
          <th>Char Field</th>
          <th>Date Field</th>
          <th>Email Field</th>
          <th>Integer Field</th>
          <th>Edit</th>
          <th>Delete</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in items" :key="item.id">
          <td>{{ item.id }}</td>
          <td>{{ item.char_field }}</td>
          <td>{{ item.date_field }}</td>
          <td>{{ item.email_field }}</td>
          <td>{{ item.integer_field }}</td>
          <td>
            <edit-component :item="item" :unique-id="item.id" @item-edited="updateItem" />
          </td>
          <td>
            <button class="btn btn-danger" @click="deleteItem(item.id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
  
<script>
import EditComponent from './Edit.vue';

export default {
  components: {
    EditComponent
  },
  props: {
    items: Array
  },
  data() {
    return {
      selectedItem: null
    };
  },
  methods: {
    editItem(item) {
      this.selectedItem = item;
    },
    updateItem(updatedItem) {
      this.$emit('update-items', updatedItem);
    },
    deleteItem(itemId) {
      this.$emit('delete-item', itemId);
    }
  }
};
</script>