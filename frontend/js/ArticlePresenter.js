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
    this.view.showArticle();
};

ArticlePresenter.prototype.addComment = function(message) {

};
