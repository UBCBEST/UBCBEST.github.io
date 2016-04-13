(function () {
    angular.module('main')
        .controller('projectsController', function (DataFactory, $scope) {

            DataFactory.projects()
                .success(function(data) {
                    $scope.donated = data.donated;
                    $scope.idea_emr = data.idea_emr;
                    $scope.m2m = data.m2m;
                    $scope.ptm = data.ptm;
                    $scope.rrm = data.rrm;
                    $scope.femur = data.femur;
                    $scope.phone_holder = data.phone_holder;
                });

        });
})();
