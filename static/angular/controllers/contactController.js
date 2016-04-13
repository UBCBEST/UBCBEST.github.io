(function () {
    angular.module('main')
        .controller('contactController', ['$http', '$scope', function ($http, $scope) {
            $scope.message = {};
            $scope.sent = false;

            $scope.sendMail = function () {
                $http.post('/api/email', $scope.message)
                    .then(function () {
                        $scope.sent = true;
                    });
                $scope.contactForm.$setPristine();
                $scope.contactForm.$setUntouched();
                $scope.message = {};

            }
        }]);
})();