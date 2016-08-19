(function () {
    angular.module('app')
        .factory('DataFactory', ['$http', function ($http) {
            return {
                images: function () {
                    return $http.get('/static/data/galleryData.json');
                },
                projects: function () {
                    return $http.get('/api/projects');
                },
                getProject: function (index) {
                    return $http.get('/api/projects/'+index);
                },
                teams: function () {
                    return $http.get('/api/teams');
                },
                getTeam: function (index) {
                    return $http.get('/api/teams/'+index);
                }
            }
        }]);
})();
