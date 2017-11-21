(function () {
    'use strict';

    angular.module('scrumboard.demo', ['ngRoute'])
        .controller('ScrumboardController', ['$scope', '$http', ScrumboardController]);

    function ScrumboardController($scope, $http) {
        $scope.list_add = function (board, title) {
            var card = {
                board: board.id,
                title : title
            }
            $http.post('/scrumboard/cards/', card)
            .then(function(response){
                 board.cards.push(response.data);
            },
            function() {
                alert('Could not create card');
            });

        };       

        $scope.data = [];
        $http.get('/scrumboard/boards/').then(function(response){
            $scope.data = response.data;
        })

        $scope.login = function() {
            $http.post('/auth_api/login/',
                {username:'hopeaz', password: 'babygirlh13'});
        }

    }
}());