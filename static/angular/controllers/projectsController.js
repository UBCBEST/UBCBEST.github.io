(function () {
    angular.module('app')
        .controller('projectsController', function (DataFactory, $scope) {
            $scope.selectedP = null;
            $scope.tabP = 0;

            function getProject(tabP) {
                DataFactory.getProject(tabP)
                    .success(function (data) {
                        $scope.project = data;
                    });
            }

            DataFactory.projects()
                .success(function (data) {
                    $scope.projects = data.data;
                });

            $scope.selectP = function (member) {
                $scope.selectedP = member;
            };

            $scope.isTabP = function (tab) {
                return tab === $scope.tabP;
            };

            $scope.setTabP = function (tab) {
                $scope.tabP = tab;
                getProject(tab);
            };

            getProject($scope.tabP);
        });
})();
