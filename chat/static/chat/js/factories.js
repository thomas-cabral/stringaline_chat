conversationApp.run( function run($http, $cookies ){

    // Grab the CSRF Token
    $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
});

conversationApp.factory('ConversationsFactory', function (djResource) {
    return djResource('/api/conversation/', {}, {
        query: { method: 'GET', isArray: true },
        create: { method: 'POST' }
    })
});

conversationApp.factory('ConversationFactory', function ($resource) {
    return $resource('/api/conversation/:id/', {}, {
        show: { method: 'GET' },
        update: { method: 'PUT', params: {id: '@id'} },
        delete: { method: 'DELETE', params: {id: '@id'} }
    })
});

conversationApp.factory('CommentsListFactory', function (djResource) {
    return djResource('/api/conversation/:id/comments/', {}, {
        query: { method: 'GET', isArray: true },
        create: { method: 'POST' }
    })
});

conversationApp.factory('CommentsFactory', function (djResource) {
    return djResource('/api/comment/', {}, {
        query: { method: 'GET', isArray: true },
        create: { method: 'POST' }
    })
});

conversationApp.factory('CommentFactory', function ($resource) {
    return $resource('/api/comment/:id/', {}, {
        show: { method: 'GET' },
        update: { method: 'PUT', params: {id: '@id'} },
        delete: { method: 'DELETE', params: {id: '@id'} }
    })
});