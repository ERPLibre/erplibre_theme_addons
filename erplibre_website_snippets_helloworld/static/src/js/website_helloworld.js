odoo.define('website_helloworld', function (require) {
    'use strict';

    var sAnimation = require('website.content.snippets.animation');
    sAnimation.registry.helloworld = sAnimation.Class.extend({
        selector: '.website_helloworld',
        xmlDependencies: [],
        events: {},
        read_events: {
        },

        /**
         * @override
         */
        start: function () {
            var def = this._rpc({route: '/website_helloworld/get_message/'}).then(function (data) {
                if (data.error) {
                    return;
                }

                if (_.isEmpty(data)) {
                    return;
                }

                document.getElementById("message").innerHTML = data.message;
            });

            return $.when(this._super.apply(this, arguments), def);
        },
    });
});