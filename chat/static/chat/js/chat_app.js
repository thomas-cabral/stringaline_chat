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
        });

    //$locationProvider.html5Mode(true);
});

conversationApp.run( function run($http, $cookies ){
    // Grab the CSRF Token
    $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
});