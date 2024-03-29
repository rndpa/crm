new Vue({
    el: '#admin',
    data: {
        reports: [],
    },
    created: function () {
        const vm = this;
        axios.get('/api/').then(function (response) {
            vm.reports = response.data
        })
    }
})