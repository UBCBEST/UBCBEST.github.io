(function () {
    angular.module('app')
        .controller('applyController', function (DataFactory, $scope) {
            $scope.recruitmentMessage = null;
            $scope.events = null;

            DataFactory.recruitment()
                .success(function (data) {
                    var status = data.status;
                    if (status.active) {
                        $scope.recruitmentMessage = status.activeMessage;
                    } else {
                        $scope.recruitmentMessage = status.inactiveMessage;
                    }
                });
        });
})();
