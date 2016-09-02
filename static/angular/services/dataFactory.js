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
                teams: function () {
                    return $http.get('/api/teams');
                },
                recruitment: function () {
                    return $http.get('/static/data/recruitmentData.json')
                }
            }
        }]);
})();
