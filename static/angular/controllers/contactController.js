(function () {
    angular.module('main')
        .controller('contactController', ['$http', '$scope', function ($http, $scope) {
            $scope.msg = {};
            $scope.form = document.forms['contactForm'];
            $scope.sendMail = function(msg) {
                $scope.msg = msg;
                $scope.contactForm.$setPristine();
                $scope.form.reset();
                console.log ($scope.msg);
            }
        }]);
})();