'use strict';

//(1)
var Blog = angular.module("Blog", ["ui.bootstrap", "ngCookies"], function ($interpolateProvider) {
		$interpolateProvider.startSymbol("{[{");
		$interpolateProvider.endSymbol("}]}");
	}
);

//(2)
Blog.run(function ($http, $cookies) {
	$http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
})

//(3)
Blog.config(function ($routerProvider) {
	$routeProvider
		.when("/", {
			templateUrl: "static/js/app/views/feed.html",
			controller: "FeedController",
			resolve: {
				posts: function (PostService) {
					return PostService.list();
				}
			}
		})
		.when("/post/:id", {
			templateUrl: "static/js/app/views/view.html",
			controller: "PostController",
			resolve: {
				post: function ($route, PostService) {
					var postId = $route.current.params.id
					return PostService.get(postId);
				}
			}
		})
		.otherwise({
			redirectTo: '/'
		})
})
