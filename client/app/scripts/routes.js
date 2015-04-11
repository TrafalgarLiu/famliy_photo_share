/**
 * Top level routes definition
 */
define(['app'], function(app) {
	'use strict';
	return app.config(['$locationProvider', '$routeProvider',
		function($locationProvider, $routeProvider) {
			$locationProvider.html5Mode(false);
			$routeProvider
				.when("/", {
					controller: "indexCtrl",
					templateUrl: "views/index.html"
				}).when("/upload", {
                    controller: "uploadCtrl",
                    templateUrl: "views/upload.html"
                })
				.otherwise({
					redirectTo: '/'
				});
		}
	]);
});