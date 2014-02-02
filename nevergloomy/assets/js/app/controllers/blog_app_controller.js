var appController = Blog.controller('AppController', function ($scope, $rootScope, $location, GlobalService) {
	var failureCb = function (status) {
		console.log(status);
	};
	$scope.globals = GlobalService;

	$scope.initialize = function (is_authenticated) {
		$scope.global.is_authenticated = is_authenticated;
	};
})
