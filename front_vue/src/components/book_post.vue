<template>
    <v-app>
        <v-container fluid>
            <v-layout justify-center>
                <v-flex md6 xs12>
                    <v-card>
                        <v-card-title class="font-weight-bold headline">New Post</v-card-title>
                    </v-card>
                        <div class='postform'>
                            <v-text-field
                            v-model="title"
                            :counter="200"
                            label="title"
                            required
                            ></v-text-field>
                            <v-select
                            v-bind:items="book_category"
                            label="book category"
                            item-value="id"
                            item-text="cName"
                            required
                            ></v-select>
                            <v-textarea
                            box
                            name="text"
                            label="text"
                            value=""
                            ></v-textarea>
                            <v-text-field
                            label="Created date"
                            v-model="p_date"
                            prepend-icon="event"
                            disabled
                            ></v-text-field>
                            <v-menu
                            ref="menu"
                            :close-on-content-click="false"
                            v-model="menu"
                            :nudge-right="40"
                            :return-value.sync="p_date"
                            lazy
                            transition="scale-transition"
                            offset-y
                            full-width
                            min-width="290px"
                            >
                            <v-text-field
                            slot="activator"
                            v-model="p_date"
                            label="Published date"
                            prepend-icon="event"
                            readonly
                            ></v-text-field>
                            <v-date-picker v-model="p_date" no-title scrollable>
                            <v-spacer></v-spacer>
                                <v-btn flat color="primary" @click="menu = false">Cancel</v-btn>
                                <v-btn flat color="primary" @click="$refs.menu.save(p_date)">OK</v-btn>
                            </v-date-picker>
                            </v-menu>
                            <div class='image'>
                                <v-text-field 
                                label="Image Name" 
                                :counter="50"
                                prepend-icon='attach_file'
                                ></v-text-field>
                                <v-text-field 
                                label="Select Image" 
                                v-model='imageName' 
                                prepend-icon='attach_file'
                                ></v-text-field>
                            </div>
                            <v-spacer></v-spacer>
                            <v-btn large color="#BDBDBD">Cancell</v-btn>
                            <v-btn large color="primary">Post</v-btn>
                        </div>
                </v-flex>
            </v-layout>
        </v-container>
    </v-app>
</template>

<script>
import axios from 'axios'
// import moment from 'moment'

export default {
    name: 'BookCategory',
    data(){
        return{
            book_category: [],
            p_date: new Date().toISOString().substr(0, 10),
            today: [],
            menu: false
        }
    },
    mounted (){
        axios
            .get('http://localhost:8000/api/book_category/')
            .then(response => (this.book_category = response.data))
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