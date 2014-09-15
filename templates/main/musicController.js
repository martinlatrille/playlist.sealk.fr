var main = angular.module('mainApp', []);

main.controller('MusicPlayerController', ['$scope', function() {
		$scope.adress = "https://www.youtube.com/watch?v=HMUDVMiITOU";
		
		$scope.getAdress = function() {
			return $scope.adress;
		};
		
		$scope.changeAdress = function(addr) {
			$scope.adress = addr;
		};
	}]);