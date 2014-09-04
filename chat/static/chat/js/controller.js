conversationApp.controller('ConversationDetailCtrl', ['$scope', '$routeParams', 'ConversationFactory', 'CommentsFactory', 'CommentsListFactory', '$location',
    function ($scope, $routeParams, ConversationFactory, CommentsFactory, CommentsListFactory) {

        // callback for ng-click 'updateItem':
        $scope.scopeSet = function (id, position) {
            $scope.parentId = id;
            $scope.position = position;
            alert(position.id);
        };

        $scope.save = function () {
            ConversationFactory.update($scope.conversation);
        };

        $scope.destroy = function () {
            ConversationFactory.delete($scope.conversation);
        };

        // create a comment without a parent
        $scope.createNewComment = function () {
            $scope.comment.conversation = $scope.conversation.id;
            CommentsFactory.create($scope.comment, function(data){
                $scope.comments.push(data);
                $scope.comment = null;
                $scope.error = null;
            }, function(error) {
                $scope.error = error
            });
        };

        // create a comment nested under another comment and push to correct location
        $scope.createNewCommentReply = function () {
            var position = $scope.position;
                console.log(position);
            $scope.comment.conversation = $scope.conversation.id;
            $scope.comment.parent = $scope.parentId;
            CommentsFactory.create($scope.comment, function(data){
                data.children = [];
                $scope.position.children.push(data);
                $scope.comment = null;
                $scope.error = null;
            }, function(error) {
                $scope.error = error;
                console.log(error);
            });
        };

        $scope.refresh = function () {
            $scope.comments = CommentsListFactory.query({id: $routeParams.id});
            console.log($scope.comments);
        };

        $scope.comments = CommentsListFactory.query({id: $routeParams.id});
        $scope.conversation = ConversationFactory.show({id: $routeParams.id});

        $scope.spawn = function () {

        };
    }
]);

conversationApp.controller('ConversationCreationCtrl', ['$scope', 'ConversationsFactory', '$location',
    function ($scope, ConversationsFactory, $location) {

        // callback for ng-click 'createNewItem':
        $scope.createNewItem = function () {
            ConversationsFactory.create($scope.conversation);
            $location.path('/');
        }
    }]);

conversationApp.controller('ConversationListCtrl', ['$scope', 'ConversationsFactory', '$location',
    function ($scope, ConversationsFactory, $location) {

        $scope.conversations = ConversationsFactory.query();

            $scope.go = function (conversation) {
                var url = "/" + conversation.id;
                $location.path(url);
            };

        $scope.refresh = function () {
            $scope.conversations = ConversationsFactory.query();
        };

        $scope.createNewConversation = function () {
            ConversationsFactory.create($scope.conversation_form, function(data){
                $scope.conversations.unshift(data);
                $scope.conversation_form = null;
                $scope.form = null;
                $scope.error = null;
            }, function(error) {
                $scope.error = error;
                console.log(error);
            });
        };

    }]);

conversationApp.controller('CommentCreationCtrl', ['$scope', 'CommentsFactory', '$location',
    function ($scope, CommentsFactory, $location) {

        // callback for ng-click 'createNewItem':
        $scope.createNewItem = function () {
            CommentsFactory.create($scope.comment);
        }
    }]);