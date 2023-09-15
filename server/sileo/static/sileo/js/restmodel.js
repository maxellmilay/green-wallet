(function(root, declaration) {
    if (typeof define === 'function' && define.amd) {
        define(['stapes', 'promise'], declaration);
    } else {
        root.Sileo = declaration(root.Stapes, root.Promise);
    }
})(this, function(Stapes, Promise) {

    var ModelManager = Stapes.subclass({
        constructor: function(model) {
            this.model = model;
        },
        get: function(pk, extras) {
            var url = this.model.baseUrl + 'get/' + pk + '/';
            // extras are optional
            if (extras) {
                url += '?' + this._parseGetParams(extras);
            }
            return this._fetch('GET', url);
        },
        filter: function(filter, exclude) {
            var url = this.model.baseUrl + 'filter/';
            var filterArgs = this._parseGetParams(filter);
            if (filterArgs !== '') {
                url += '?' + filterArgs;
            }
            // exclude is optional
            if (exclude) {
                if (filterArgs === '') {
                    url += '?';
                }   else {
                    url += '&';
                }
                url += this._parseGetParams(exclude);
            }
            return this._fetch('GET', url);
        },
        form_dict: function(filter) {
            var url = this.model.baseUrl + 'form-info/';
            if (filter) {
                if (typeof filter !== 'object') {
                    filter = {'pk': filter};
                }
                var filterArgs = this._parseGetParams(filter);
                if (filterArgs !== '') {
                    url += '?' + filterArgs;
                }
            }
            return this._fetch('GET', url);
        },
        create: function(formdata, extras) {
            var url = this.model.baseUrl + 'create/';
            // extras are optional
            if (extras) {
                url += '?' + this._parseGetParams(extras);
            }
            return this._fetch('POST', url, formdata);
        },
        update: function(filter, formdata, extras) {
            if (typeof filter !== 'object') {
                filter = {'pk': filter};
            }
            var url = this.model.baseUrl + 'update/';
            var filterArgs = this._parseGetParams(filter);
            if (filterArgs !== '') {
                url += '?' + filterArgs;
            }
            // extras are optional
            if (extras) {
                if (filterArgs === '') {
                    url += '?';
                }   else {
                    url += '&';
                }
                url += this._parseGetParams(extras);
            }
            return this._fetch('POST', url, formdata);
        },
        delete: function(filter, extras) {
            if (typeof filter !== 'object') {
                filter = {'pk': filter};
            }
            var url = this.model.baseUrl + 'delete/';
            var filterArgs = this._parseGetParams(filter);
            if (filterArgs !== '') {
                url += '?' + filterArgs;
            }
            // extras are optional
            if (extras) {
                if (filterArgs === '') {
                    url += '?';
                }   else {
                    url += '&';
                }
                url += this._parseGetParams(extras);
            }
            return this._fetch('POST', url);
        },
        _fetch: function(method, url, data) {
            var _this = this;
            var xhr = null;
            var promise = new Promise(function(resolve, reject) {
                var req = new XMLHttpRequest();
                xhr = req;
                // somehow upload events dont fire unless
                // `req.upload` is accessed before connection is open
                req.upload.onprogress = function(){};
                req.open(method, url, true);
                req.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
                if (method === 'POST') {
                    req.setRequestHeader('X-CSRFToken', _this._getCSRFToken());
                }
                req.onreadystatechange = function() {
                    if (req.readyState === 4) {
                        if ((req.status === 200 || req.status === 201) &&
                        typeof resolve === 'function') {
                            _this.model.callback(resolve)(JSON.parse(req.responseText).data);
                        }   else if (req.status !== 200 &&
                        typeof reject === 'function') {
                            reject(req);
                        }
                    }
                };
                req.send(data ? getData(data) : null);
            });
            promise.xhr = xhr;
            return promise;
        },
        _parseGetParams: function(extras) {
            var exs = [];
            for (var key in extras) {
                if(extras.hasOwnProperty(key)) {
                    exs.push(key + '=' + extras[key]);
                }
            }
            return exs.join('&');
        },
        _getCSRFToken: function() {
            var pattern = new RegExp('(?:(?:^|.*;)\\s*'
                + encodeURIComponent('csrftoken').replace(/[\-\.\+\*]/g, '\\$&')
                + '\\s*\\=\\s*([^;]*).*$)|^.*$');
            var value = decodeURIComponent(
                document.cookie.replace(pattern, '$1'));
            return value || null;
        }
    });



    var utils = {
        extend: function(base) {
            Array.prototype.slice.call(arguments, 1).forEach(function(ext) {
                for (var key in ext) {
                    if (ext.hasOwnProperty(key)) {
                        base[key] = ext[key];
                    }
                }
            });
            return base;
        },

        flow: function(data, callbacks) {
            return callbacks.reduce(function(data, callback) {
                if (data instanceof Array) {
                    return data.map(callback);
                }
                return callback(data);
            }, data);
        }
    };

    var defaultOptions = { applyGlobalMiddlewares: true };
    var globalMiddlewares = [];

    var Model = Stapes.subclass({
        constructor: function(namespace, resource, middlewares, options) {
            this.baseUrl = '/api-sileo/' + namespace + '/' + resource + '/';
            this.middlewares = middlewares || [];
            this.options = utils.extend({}, defaultOptions, options);
            this.objects = new ModelManager(this);
        },

        callback: function(callback) {
            var model = this;
            return function(response) {
                if (model.options.applyGlobalMiddlewares) {
                    response = utils.flow(response, globalMiddlewares);
                }
                response = utils.flow(response, model.middlewares);
                window.wrapErrors(callback)(response);
            };
        }
    });

    Model.addGlobalMiddleware = function() {
        Array.prototype.forEach.call(arguments, function(middleware) {
            if (typeof middleware === 'function') {
                globalMiddlewares.push(middleware);
            }
        });
    };

    // wrapper function to log errors in async functions
    function wrapErrors(fn) {
        // don't wrap function more than once
        if (!fn.__wrapped__) {
            fn.__wrapped__ = function () {
                try {
                    return fn.apply(this, arguments);
                } catch (e) {
                    window.onerror(e);
                    throw e; // re-throw the error
                }
            };
        }
        return fn.__wrapped__;
    }

    function getData(data) {
        if (!data) {
            return null
        }
        if (data.constructor.name === 'Object') {
            var param = data;
            data = new FormData();
            for (var key in param) {
                data.append(key, param[key]);
            }
        }
        return data
    }

    window.wrapErrors = window.wrapErrors || wrapErrors;

    return {
        Model: Model,
        ModelManager: ModelManager
    };
});
