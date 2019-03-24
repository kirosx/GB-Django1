var config = {
    selectors:{
        add: '.addstuff',
        delete: '.delstuff',
        quantity:'.basketquantity'
    },
    urls:{
        add:'/basket/add/',
        update:'/basket/update/',
        delete:'/basket/remove/',

    }
};

$(document).ready(function () {
    $(config.selectors.add).on('click',function () {
        var item_id = $(this).data('id');
        var item_url = config.urls.add + item_id + '/';
        var parent_item = $(this).parents()[0];
        var counter = $(parent_item).find(config.selectors.quantity);

        $.ajax({
            url: item_url,
            success: function (data) {
                counter.text(data.quantity)
            }
        })
    });
    $(config.selectors.delete).on('click',function () {
        var item_id = $(this).data('id');
        var item_url = config.urls.delete + item_id + '/';
        var parent_item = $(this).parents()[0];
        var counter = $(parent_item).find(config.selectors.quantity);

        $.ajax({
            url: item_url,
            success: function (data) {
                counter.text(data.quantity)
            }
        })
    });

});