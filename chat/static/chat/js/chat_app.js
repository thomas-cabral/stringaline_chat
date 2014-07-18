var conversationApp = angular.module('conversationApp', ['ngRoute', 'ngResource', 'ngAnimate', 'djangoRESTResources', 'ngCookies']);

conversationApp.config(function($routeProvider, $locationProvider, $httpProvider) {
    $routeProvider

    // Index
        .when('/', {
            templateUrl : '/angular/conversation-list/',
            controller : 'ConversationListCtrl'
        })

        .when('/new', {
            templateUrl : '/angular_new/',
            controller : 'ConversationCreationCtrl'
        })

        .when('/:id', {
            templateUrl : '/angular/conversation-detail/',
            controller : 'ConversationDetailCtrl'
        })

        .when('/:id/edit', {
            templateUrl : '/angular_edit',
            controller : 'ConversationDetailCtrl'
        });

    //$locationProvider.html5Mode(true);
    //$httpProvider.provider.defaults.headers.post["X-CSRFToken"] = getCookie('csrftoken');
});