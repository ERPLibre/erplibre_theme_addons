odoo.define('erplibre_website_snippets.animation', function (require) {
  'use strict';

  var sAnimation = require('website.content.snippets.animation');

  sAnimation.registry.erplibre_website_snippets = sAnimation.Class.extend({
    selector: '.o_cards_extend',
    read_events: {
      'click .o_card_extend': '_toggleExtend',
    },

    //--------------------------------------------------------------------------
    // Handlers
    //--------------------------------------------------------------------------

    /**
     * @private
     */
    _toggleExtend: function (ev) {
      var card = ev.currentTarget;
      var className = "extended";
      if (card.classList.contains(className)) {
        card.classList.remove(className);
      }
      else {
          card.classList.add(className);
      }
    },
  })
});
