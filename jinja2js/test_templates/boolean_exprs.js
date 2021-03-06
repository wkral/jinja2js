(function(__ns, _) {
var __this = {};
__this.test_and = function() {
    var __data = _.parse_args(arguments, ['a', 'b'], []);
    var __output = '';
    if (_.truth(__data.a) && _.truth(__data.b)) {
        __output += 'True';
    }
    return __output;
};

__this.test_or = function() {
    var __data = _.parse_args(arguments, ['a', 'b'], []);
    var __output = '';
    if (_.truth(__data.a) || _.truth(__data.b)) {
        __output += 'True';
    }
    return __output;
};

__this.test_xor = function() {
    var __data = _.parse_args(arguments, ['a', 'b'], []);
    var __output = '';
    if ((_.truth(__data.a) || _.truth(__data.b)) && !(_.truth(__data.a) && _.truth(__data.b))) {
        __output += 'True';
    }
    return __output;
};

__this.test_alt_xor = function() {
    var __data = _.parse_args(arguments, ['a', 'b'], []);
    var __output = '';
    if ((_.not(__data.a) && _.truth(__data.b)) || (_.truth(__data.a) && _.not(__data.b))) {
        __output += 'True';
    }
    return __output;
};
__ns['boolean_exprs'] = __this;
})(this.jinja2js = this.jinja2js || {}, jinja2support);
