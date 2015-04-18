define(["./controllers"], function(controllers) {
	"use strict";
	controllers.controller("indexCtrl", [
		"$scope",
		function($scope) {
            $scope.totalItems = 64;
            $scope.currentPage = 4;
            $scope.maxSize = 8;

            $scope.photos = [
                {
                    full_url: '#/upload',
                    thumbnail_url: 'http://7xidjv.com1.z0.glb.clouddn.com/girl.jpg?imageView2/1/w/245/h/200',
                    name: 'girl'
                },
                {
                    full_url: '#/upload',
                    thumbnail_url: 'http://7xidjv.com1.z0.glb.clouddn.com/girl.jpg?imageView2/1/w/245/h/200',
                    name: 'girl'
                },
                {
                    full_url: '#/upload',
                    thumbnail_url: 'http://7xidjv.com1.z0.glb.clouddn.com/girl.jpg?imageView2/1/w/245/h/200',
                    name: 'girl'
                },
                {
                    full_url: '#/upload',
                    thumbnail_url: 'http://7xidjv.com1.z0.glb.clouddn.com/girl.jpg?imageView2/1/w/245/h/200',
                    name: 'girl'
                }
            ];
		}
	]);
});