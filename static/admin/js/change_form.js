/*global showAddAnotherPopup, showRelatedObjectLookupPopup showRelatedObjectPopup updateRelatedObjectLinks*/

(function($) {
    'use strict';
    $(document).ready(function() {
        var modelName = $('#django-admin-form-add-constants').data('modelName');
        $('body').on('click', '.add-another', function(e) {
            e.preventDefault();
            var event = $.Event('django:add-another-related');
            $(this).trigger(event);
            if (!event.isDefaultPrevented()) {
                showAddAnotherPopup(this);
            }
        });

        if (modelName) {
            $('form#' + modelName + '_form :input:visible:enabled:first').focus();
        }

        /* Show custom type only if type is "other" */
        $('.field-other_type').hide();
        $("select#id_type").change(function(){
            var selected_type = $(this).children("option:selected").val();
            if (selected_type != 'OT'){
               $('.field-other_type').hide();
            } else {
              $('.field-other_type').show();
            }
        });
    });
})(django.jQuery);
