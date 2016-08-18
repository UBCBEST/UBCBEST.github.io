(function () {
    angular.module('app')
        .factory('DataFactory', ['$http', function ($http) {
            return {
                images: function () {
                    return $http.get('/static/data/galleryData.json');
                },
                projects: function () {
                    return $http.get('/static/data/projectsData.json');
                },
                teams: function () {
                    return $http.get('/static/data/teamsData.json');
                }
            }
        }]);
})();
