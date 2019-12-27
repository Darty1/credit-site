new Vue(
    {
        el: '#search_products',
        data: {
            products: []
        },
        created: function () {
            const vm=this;
            axios.get('/search/')
            .then(function (response) {
                console.log(response.data)
            })
        }
    }
)