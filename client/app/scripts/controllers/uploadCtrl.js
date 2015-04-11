/**
 * Created by luffy on 15-4-11.
 */
define(['./controllers'], function (controllers) {
    "use strict";
    controllers.controller("uploadCtrl", [
        '$scope',
        'uploadService',

        function ($scope, uploadService) {
//            $scope.changes = function(){
//                console.log("adsf");
//                var formdata = new FormData();
//                var form = document.forms["uploadForm"];
//                console.log(form["filename"].files[0]);
//                $scope.none_use = form["filename"].files[0].name;
//            };
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