/**
 * Created by luffy on 15-4-11.
 */
define(['./controllers'], function (controllers) {
    "use strict";
    controllers.controller("photoDisplayCtrl", [
        '$scope',
        'uploadService',

        function ($scope, uploadService) {
            var promise = uploadService.get_upload_token();
            $scope.upload_obj = {
                remark: '',
                tags: 'sssss',
                token: null,
                key: null
            };
            promise.then(
                function(response){
                    $scope.upload_obj.key = response.data.key;
                    $scope.upload_obj.token = response.data.token;
                },
                function(e){
                }
            );
        }])
});