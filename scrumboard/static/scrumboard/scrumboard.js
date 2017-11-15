(function () {
    'use strict';

    angular.module('scrumboard.demo', [])
        .controller('ScrumboardController', ['$scope', ScrumboardController]);

    function ScrumboardController($scope) {
        $scope.list_add = function (list, title) {
            var card = {
                title : title
            }
            list.cards.push(card);
        };       
        
        $scope.data = [{
                name: 'Django Demo',
                cards: [{
                        title: 'Create Models'
                    },
                    {
                        title: 'create View'
                    },
                    {
                        title: 'Create Database'
                    }
                ]
            },
            {
                name: 'Angular Demo',
                cards: [{
                        title: 'Write HTML'
                    },
                    {
                        title: 'Write JavaScript'
                    }
                ]
            }
        ];
    }
}());