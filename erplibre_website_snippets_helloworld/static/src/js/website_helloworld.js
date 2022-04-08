function showdate() {
    "use strict";
    var def = this._rpc({route: '/website_helloworld/get_message'}).then(function (data) {

                if (data.error) {
                    // $donationError.append(qweb.render('website.Error', {data: data}));
                    return;
                }

                if (_.isEmpty(data)) {
                    return;
                }

                document.getElementById("message").innerHTML = data.message;

            });

            return $.when(this._super.apply(this, arguments), def);
}

