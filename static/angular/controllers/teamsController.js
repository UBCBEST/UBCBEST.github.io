(function () {
    angular.module('app')
        .controller('teamsController', function (DataFactory, $scope) {
            $scope.selectedT = null;

            $scope.selectT = function(member) {
                $scope.selectedT = member;
            };
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
