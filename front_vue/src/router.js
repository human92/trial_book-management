import Vue from 'vue'
import Router from 'vue-router'
import booklist from './components/book_list'
import bookpost from './components/book_post'


Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'booklist',
      component: booklist
    },
    {
      path: '/new_post',
      name: 'bookpost',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: bookpost
    }
  ]
})
