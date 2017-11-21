angular.module('scrumboard.demo').directive('scrumboardCard', function() {
    return {
            templateUrl: '/static/html/card.html',
            restrict: 'E',
            controller: function($scope, $http) {
                var url = '/scrumboard/cards/' + $scope.card.id + '/';


                $scope.updateCard = function() {
                    $http.put(url, $scope.card);
                    $scope.edit = false;
                }

                $scope.deleteCard = function() {
                    $http.delete(url, $scope.card)
                        .then(function(){
                            var cards = $scope.board.cards;
                            cards.splice(cards.indexOf($scope.card,1)
                            );
                        });
                };
            }
     }
});

