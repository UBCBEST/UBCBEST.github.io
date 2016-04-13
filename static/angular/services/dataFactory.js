(function () {
    angular.module('main')
        .factory('DataFactory', ['$http', function ($http) {
            return {
                projects: function () {
                    return $http.get('/static/data/projectsData.json');
                },
                teams: function () {
                    return $http.get('/static/data/teamsData.json');
                }
            }
        }]);
})();
