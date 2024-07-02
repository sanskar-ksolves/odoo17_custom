odoo.define('my_module.custom_action', function(require) {
    "use strict";
    
    var core = require('web.core');
    var AbstractAction = require('web.AbstractAction');
    
    var CustomAction = AbstractAction.extend({
        template: 'CustomActionTemplate',
        
        start: function() {
            this.$el.append('<div>Hello, this is a custom client action!</div>');
            return this._super();
        },
    });
    
    core.action_registry.add('custom_action', CustomAction);
});
