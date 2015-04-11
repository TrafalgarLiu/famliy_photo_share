/**
 * Created by luffy on 15-4-11.
 */
define(['./services'], function (services) {
    'use strict';
    services.service('photoDisplayService', [
        '$rootScope',
        '$http',
        'ROOT_DOMAIN',
        function ($rootScope, $http, ROOT_DOMAIN) {
            this.get_upload_token = function() {
                return $http({
                    method: 'GET',
                    headers: {
                    },
                    url: [
                        ROOT_DOMAIN,
                        'upload',
                        'token'
                    ].join('/'),
                    data:{
                    }
                })
            };

        }])
});