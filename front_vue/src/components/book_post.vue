<template>
    <v-app>
        <h1>Test REST API</h1>
            <div id='post_list'>
                    <v-flex xs6  v-for="post in posts" :key="post.id">
                        <h2>{{post.title}}</h2>
                            <div calss='post_detai'>
                                <p>Category: {{post.category.cName}}</p>
                                <p>Detail: {{post.text}}</p>
                            </div>
                            <div class="date">
                                <p>First published: {{ post.publishedDate|printDate }}</p>
                                <p>Last updated: {{ post.lastUpdatedDate|printDate }}</p>
                            </div>
                    </v-flex>
            </div>
    </v-app>
</template>

<script>
import axios from 'axios'
import moment from 'moment'

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
    filters: {
        printDate (val){
            return moment(val).locale('ja').format('YYYY年MM月DD日(ddd)')
        },
    },
}
</script>
<style>
</style>