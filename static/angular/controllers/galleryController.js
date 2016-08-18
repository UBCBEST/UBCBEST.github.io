(function () {
    angular.module('app')
        .controller('galleryController', function (DataFactory, $scope) {
            $scope.tabG = 0;

            DataFactory.images()
                .success(function (data) {
                    $scope.images = data.data;
                });

            $scope.isTabG = function (tab) {
                return tab === $scope.tabG;
            };

            $scope.setTabG = function (tab) {
                $scope.tabG = tab;
            }
        });
})();
