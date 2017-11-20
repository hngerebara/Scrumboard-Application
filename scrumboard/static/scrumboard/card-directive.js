 (function () {
    'use strict';

    angular.module('scrumboard.demo',)
        .directive('scrumboardCard', cardDirective);

    function cardDirective() {
        return {
            templateUrl: '/templates/scrumboard/card.html',
            restrict: 'E'
        }
    }
})();