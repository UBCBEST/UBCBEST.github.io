(function () {
    angular.module('ng-counter', [])
        .controller('counterController', ['$scope', '$interval', function ($scope, $interval) {
            const period = 150;
            $scope.value = 0;
            $scope.start = function () {
                var iterations = (1.0 * $scope.countTo) / $scope.step;
                $interval(function () {
                    $scope.value += $scope.step;
                    if ($scope.value >= $scope.countTo) {
                        $scope.value = $scope.countTo;
                    }
                }, period, iterations);
            };
        }])
        .directive('counter', ['$interval', function ($interval) {
            return {
                restrict: 'E',
                template: '<p>{[ value ]} {[ text ]}</p>',
                scope: {
                    countTo: '=',
                    step: '=',
                    text: '@'
                },
                controller: 'counterController',
                link: function (scope, element) {
                    var el = element[0];

                    var hack = $interval(function () {
                        $(window).scrollTop();
                    }, 100);
                    scope.isHit = function () {
                        return $(el).offset().top - 200 < $(window).scrollTop();
                    };

                    scope.$watch(scope.isHit, function (hit) {
                        if (hit) {
                            $interval.cancel(hack);
                            scope.start();
                        }
                    });
                }
            }
        }]);
})();
