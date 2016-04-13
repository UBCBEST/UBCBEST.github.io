(function () {
    angular.module('app')
        .controller('teamsController', function (DataFactory, $scope) {

            DataFactory.teams()
                .success(function(data) {
                    $scope.exec = data.exec;
                    $scope.man = data.man;
                    $scope.bus = data.bus;
                    $scope.bod = data.bod;
                    $scope.alum = data.alum;
                    $scope.spc = data.spc;
                });

        });
})();
