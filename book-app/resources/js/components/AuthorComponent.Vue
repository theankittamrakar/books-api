<template>
  <div class="p-4">
    <h1 class="text-3xl font-bold mb-6">Authors</h1>

    <div v-if="successMessage" class="bg-green-100 border border-green-400 text-green-700 p-4 rounded mb-4">
      {{ successMessage }}
    </div>

    <div v-if="errors.length" class="bg-red-100 border border-red-400 text-red-700 p-4 rounded mb-4">
      <ul>
        <li v-for="error in errors" :key="error">{{ error }}</li>
      </ul>
    </div>

    <form @submit.prevent="saveAuthor" class="mb-6 space-y-4">
      <input v-model="author.firstname" placeholder="First Name" class="border border-gray-300 p-2 rounded-md w-full"/>
      <input v-model="author.middlename" placeholder="Middle Name" class="border border-gray-300 p-2 rounded-md w-full"/>
      <input v-model="author.lastname" placeholder="Last Name" class="border border-gray-300 p-2 rounded-md w-full"/>
      <button type="submit" class="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">
        {{ author.id ? 'Update' : 'Add' }} Author
      </button>
    </form>

    <div class="bg-white shadow-md rounded-lg p-4">
      <h2 class="text-xl font-semibold mb-4">Author List</h2>
      <ul class="space-y-2">
        <li v-for="author in authors" :key="author.id"
            class="border-b border-gray-200 py-2 flex items-center justify-between">
          <span>{{ author.firstname }} {{ author.lastname }}</span>
          <div>
            <button @click="editAuthor(author)"
                    class="bg-yellow-500 text-white px-3 py-1 rounded-md hover:bg-yellow-600 mr-2">Edit
            </button>
            <button @click="deleteAuthor(author.id)"
                    class="bg-red-600 text-white px-3 py-1 rounded-md hover:bg-red-700">Delete
            </button>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from '../axios';

export default {
  data() {
    return {
      authors: [],
      author: {
        id: null,
        firstname: '',
        middlename: '',
        lastname: '',
      },
      errors: [],
      successMessage: '',
    };
  },
  created() {
    this.fetchAuthors();
  },
  methods: {
    async fetchAuthors() {
      try {
        const response = await axios.get('/authors');
        this.authors = response.data.data;
      } catch (error) {
        console.error('Failed to fetch authors:', error);
      }
    },
    async saveAuthor() {
      this.errors = [];
      this.successMessage = '';
      try {
        if (this.author.id) {
          await axios.post(`/authors/${this.author.id}`, this.author);
          this.successMessage = 'Author updated successfully!';
        } else {
          await axios.post('/authors', this.author);
          this.successMessage = 'Author added successfully!';
        }
        this.author = {id: null, firstname: '', middlename: '', lastname: ''};
        this.fetchAuthors();
      } catch (error) {
        if (error.response && error.response.data.errors) {
          this.errors = Object.values(error.response.data.errors).flat();
        } else {
          console.error('Failed to save author:', error);
        }
      }
    },
    async deleteAuthor(id) {
      try {
        await axios.delete(`/authors/${id}`);
        this.successMessage = 'Author deleted successfully!';
        this.fetchAuthors();
      } catch (error) {
        console.error('Failed to delete author:', error);
      }
    },
    editAuthor(author) {
      this.author = {...author};
    },
  },
};
</script>


