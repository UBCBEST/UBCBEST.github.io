(function () {
    angular.module('app')
        .controller('applyController', function (DataFactory, $scope) {
            $scope.activeRecruitment = false;
            $scope.recruitmentMessage = null;
            $scope.events = null;

            DataFactory.recruitment()
                .success(function (data) {
                    var status = data.status;
                    $scope.links = data.links;

                    if (status.active) {
                        $scope.activeRecruitment = true;
                        $scope.recruitmentMessage = status.activeMessage;
                    } else {
                        $scope.activeRecruitment = false;
                        $scope.recruitmentMessage = status.inactiveMessage;
                    }
                });
        });
})();
