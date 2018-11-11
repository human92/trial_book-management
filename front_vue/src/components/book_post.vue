<template>
    <h2>
        Hello, World
            <p>
                {{ posts }}
            </p>
    </h2>
</template>

<script>
import axios from 'axios'

export default {
    name: 'BookIndex',
    data(){
        return{
            posts: null
        }
    },
    mounted (){
        axios
            .get('http://localhost:8000/api/posts/')
            .then(response => (this.posts = response.data))
    },
}
</script>
<style>
</style>