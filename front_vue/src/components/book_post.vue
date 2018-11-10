<template>
    <h2>
        Hello, World
            <ul>
                {{posts}}
            </ul>
    </h2>
</template>

<script>
import axios from 'axios'

export default {
    name: 'BookIndex',
    data(){
        return{
            posts: [],
        }
    },
    methods: {
        fetchData () {
            axios.get('http://localhost:8000/api/posts/').then(response => {
                // console.log(response)
                (this.posts = response.data.results)
            })
        },
    },
    mounted () {
        this.fetchData()
    },
}
</script>
<style>
</style>