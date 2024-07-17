<template>
  <div class="p-4">
    <h1 class="text-3xl font-bold mb-6">Books</h1>

    <div v-if="successMessage" class="bg-green-100 border border-green-400 text-green-700 p-4 rounded mb-4">
      {{ successMessage }}
    </div>

    <div v-if="errors.length" class="bg-red-100 border border-red-400 text-red-700 p-4 rounded mb-4">
      <ul>
        <li v-for="error in errors" :key="error">{{ error }}</li>
      </ul>
    </div>

    <form @submit.prevent="saveBook" class="mb-6 space-y-4">
      <input v-model="book.title" placeholder="Title" class="border border-gray-300 p-2 rounded-md w-full"/>
      <input v-model="book.slug" placeholder="Slug" class="border border-gray-300 p-2 rounded-md w-full"/>
      <input v-model="book.price" type="number" placeholder="Price" class="border border-gray-300 p-2 rounded-md w-full"/>
      <button type="submit" class="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">
        {{ book.id ? 'Update' : 'Add' }} Book
      </button>
    </form>

    <div class="bg-white shadow-md rounded-lg p-4">
      <h2 class="text-xl font-semibold mb-4">Book List</h2>
      <ul class="space-y-2">
        <li v-for="book in books" :key="book.id" class="border-b border-gray-200 py-2 flex items-center justify-between">
          <span>{{ book.title }} - Rs.{{ book.price }}</span>
          <div>
            <button @click="editBook(book)" class="bg-yellow-500 text-white px-3 py-1 rounded-md hover:bg-yellow-600 mr-2">Edit</button>
            <button @click="deleteBook(book.id)" class="bg-red-600 text-white px-3 py-1 rounded-md hover:bg-red-700">Delete</button>
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
      books: [],
      book: {
        id: null,
        title: '',
        slug: '',
        price: '',
      },
      errors: [],
      successMessage: '',
    };
  },
  created() {
    this.fetchBooks();
  },
  methods: {
    async fetchBooks() {
      try {
        const response = await axios.get('/books');
        this.books = response.data.data;
      } catch (error) {
        console.error('Failed to fetch books:', error);
      }
    },
    async saveBook() {
      this.errors = [];
      this.successMessage = '';
      try {
        if (this.book.id) {
          await axios.post(`/books/${this.book.id}`, this.book);
          this.successMessage = 'Book updated successfully!';
        } else {
          await axios.post('/books', this.book);
          this.successMessage = 'Book added successfully!';
        }
        this.book = { id: null, title: '', slug: '', price: '' };
        this.fetchBooks();
      } catch (error) {
        if (error.response && error.response.data.errors) {
          this.errors = Object.values(error.response.data.errors).flat();
        } else {
          console.error('Failed to save book:', error);
        }
      }
    },
    async deleteBook(id) {
      try {
        await axios.delete(`/books/${id}`);
        this.successMessage = 'Book deleted successfully!';
        this.fetchBooks();
      } catch (error) {
        console.error('Failed to delete book:', error);
      }
    },
    editBook(book) {
      this.book = {...book};
    },
  },
};
</script>

