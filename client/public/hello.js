angular.module('demo', [])
.controller('Hello', function ($scope, $http) {
    //$http.get('http://rest-service.guides.spring.io/greeting').
    $http.get('http://127.0.0.1:5000/greeting').
        then(function (response) {
            $scope.greeting = response.data;
        });
});
