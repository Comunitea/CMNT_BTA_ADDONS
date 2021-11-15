odoo.define('website_rgpd_custom.payment_form', function (require) {
    "use strict";
    require("web.dom_ready")
    
    var core = require('web.core');
    var PaymentForm = require('payment.payment_form');

    PaymentForm.include({
        events: _.extend({
            "click #checkbox_rgpd_acceptance": "toggleDisplayStatus"
        }, PaymentForm.prototype.events),

        init: function (parent, action) {
            this._super.apply(this, arguments);
            this.checkRgpd();
        },

        willStart: function () {
            var self = this;
            return this._super();
        },

        checkRgpd: function () {
            var self = this;
            setTimeout( function() {
                if ($('#checkbox_rgpd_acceptance').length == 0) {
                    $('#o_payment_form_pay').attr('disabled', false);
                }
            }, 300);
        },

        toggleDisplayStatus: function (ev) {
            var self = this;
            var input = ev.target;
            console.log("input => ", input);
            if ($(input).is(":checked") && $('#o_payment_form_pay').is(':disabled')) {
                $('#o_payment_form_pay').attr('disabled', false);
            } else if (!$(input).is(":checked") && !$('#o_payment_form_pay').is(':disabled')){
                $('#o_payment_form_pay').attr('disabled', true);
            }
        },
    });
});