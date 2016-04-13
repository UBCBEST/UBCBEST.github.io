(function () {
    angular.module('app')
        .controller('counterController', function ($scope) {
            $scope.lines_of_code = 50000;
            $scope.prototypes_built = 5;
            $scope.people_reached = 160;
        });
})();
