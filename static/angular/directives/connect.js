(function () {
    angular.module('app')
        .directive('connect', function () {
            return {
                restrict: 'E',
                templateUrl: '/static/angular/templates/footer.html',
                controller: 'contactController',
                controllerAs: 'contactCtrl'
            };
        });
})();
