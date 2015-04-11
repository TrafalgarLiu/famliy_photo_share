define([
	'angular',
	'angularRoute',
	"lodash",
	'factories/index',
	'controllers/index',
//	'directives/index',
	'filters/index',
	'services/index'
],
function(ng) {
	'use strict';
	return ng.module('app', [
		'ngRoute',
		'app.factories',
		'app.services',
		'app.controllers',
		'app.filters'
//		'app.directives'
	]);
});
