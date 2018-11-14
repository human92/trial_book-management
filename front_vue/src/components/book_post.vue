<template>
    <v-app>
        <h1>Test REST API
            <ul id='post_list'>
                <li v-for="post in posts" :key="post.title">
                    {{post.title}}
                    {{post.category}}
                    {{post.createdDate}}
                </li>
            </ul>
        </h1>
    </v-app>
</template>

<script>
import axios from 'axios'

export default {
    name: 'BookIndex',
    data(){
        return{
            posts: []
        }
    },
    mounted (){
        axios
            .get('http://localhost:8000/api/posts/')
            .then(response => (this.posts = response.data))
            .catch(error => {
                console.log(error)
                this.errored = true
            })
            .finally(() => this.loading = false)
    },
}
</script>
<style>
</style>