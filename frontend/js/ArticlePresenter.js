function ArticlePresenter(articleId, apiClient, view) {

    this.articleId = articleId
    this.apiClient = apiClient;
    this.view = view;
    this.view.setPresenter(this);
}

ArticlePresenter.prototype.start = function() {
    this.getArticle(this.articleId);
};

ArticlePresenter.prototype.getArticle = function(articleId) {
    console.log('getArticle:', articleId);

    this.apiClient.getArticle(
        articleId,
        function(result) {
            this.view.showArticle(result);
        }.bind(this),
        function(error) {
            console.log(error);
        });
};

ArticlePresenter.prototype.addComment = function(message) {
    console.log('addComment:', message);
    this.apiClient.addComment(
        this.articleId, message,
        function(result) {
            console.log('added comment:', result);
            this.view.appendComment(result['comment']);
        }.bind(this),
        function(error) {
            console.log(error);
        });
};
