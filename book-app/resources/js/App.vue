<template>
  <div id="app" class="flex flex-wrap gap-6 p-4">
    <div class="flex-1 min-w-0 max-w-full bg-white p-4 rounded-lg shadow-md">
      <BookComponent />
    </div>
    <div class="flex-1 min-w-0 max-w-full bg-white p-4 rounded-lg shadow-md">
      <AuthorComponent />
    </div>
  </div>
</template>

<script>
import BookComponent from './components/BookComponent.vue';
import AuthorComponent from './components/AuthorComponent.vue';

export default {
  components: {
    BookComponent,
    AuthorComponent,
  },
};
</script>
