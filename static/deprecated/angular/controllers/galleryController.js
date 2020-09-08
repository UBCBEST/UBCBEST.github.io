(function () {
    angular.module('app')
        .controller('galleryController', function (DataFactory, $scope) {
            DataFactory.images()
                .success(function (data) {
                    $scope.images = data.data;
                });
        });
})();
