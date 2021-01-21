const app = new Vue({
    el: '#app',
    data: {
        posts: []
    },
    created: function () {
        const vm = this
        axios.get('/blog/home/')
        .then(function (response){
            vm.posts = response.data;
        })
    }
})