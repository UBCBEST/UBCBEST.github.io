(function () {
    angular.module('app')
        .controller('projectsController', function (DataFactory, $scope) {
            $scope.selectedP = null;
            $scope.tabP = 0;

            $scope.selectP = function (member) {
                $scope.selectedP = member;
            };

            DataFactory.projects()
                .success(function (data) {
                    $scope.projects = data.data;

                });

            $scope.isTabP = function (tab) {
                return tab === $scope.tabP;
            }
        });
})();
