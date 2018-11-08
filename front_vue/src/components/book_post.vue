<template>
    <h2>
        Hello, world!!
        <p>
            I wiil develop this html
        </p>
    </h2>
</template>

<script>
import axios from 'axios'

export default {
    name: 'BookIndex',
    methods: {
        fetchData () {
            axios.get('http://localhost:8000/api/posts/').then(res => {
                console.log(res)
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