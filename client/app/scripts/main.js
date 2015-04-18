/**
 * Configure RequireJS
 */
require.config({
	baseUrl: 'scripts',
	paths: {
		angular: '../vendors/angular/angular',
		domReady: '../vendors/requirejs-domready/domReady',
		angularRoute: '../vendors/angular-route/angular-route',
		agCharts: '../vendors/angular-charts/dist/angular-charts',
		lodash: "../vendors/lodash/dist/lodash",
		fontAwesome: '../vendors/font-awesome/css/font-awesome',
		angularBootstrap: '../vendors/angular-bootstrap/ui-bootstrap-tpls',
		main_style:'../style/main',
		bootstrap_css: '../vendors/bootstrap/dist/css/bootstrap.min'
	},
	shim: {
		// Angular does not support AMD out of the box, put it in a shim
		angular: {
			exports: 'angular'
		},
		angularRoute: {
			deps: ['angular',]
		},
		angularBootstrap: {
			deps: ['angular', 'css!bootstrap_css']
		}
	},
	map: {
		'*': {
			// The path to require-css is. [Plugin for requirejs to load css sheet]
			'css': '../vendors/require-css/css'
//			'less':'../vendors/require-less/less'
		}
	},
	// This is NOT twitter's bootstrap library,it's sctipts/bootstrap.js
	deps: ['css!fontAwesome', 'css!main_style', 'bootstrap', ]
});