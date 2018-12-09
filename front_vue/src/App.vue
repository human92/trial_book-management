<template>
  <v-app>
    <v-toolbar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>BOOK MANAGEMENT by Django</span>
        <!-- <span class="font-weight-light">MATERIAL DESIGN</span> -->
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        flat
        href="/new_post"
        target="_blank"
      >
        <span class="mr-2">New Post</span>
      </v-btn>
    </v-toolbar>

    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
// import HelloWorld from './components/HelloWorld'
// import booklist from './components/book_list'

// export default {
//   name: 'App',
//   components: {
//     HelloWorld
//   },
//   data () {
//     return {
//       //
//     }
//   }
// }

// export default {
//   name: 'Book',
//   components: {
//     booklist
//   },
//   data () {
//     return {
//       //
//     }
//   }
// }
</script>

<style>
</style>
