function ArticlePresenter(articleId, apiClient, view) {

    this.articleId = articleId
    this.apiClient = apiClient;
    this.view = view;
    this.view.setPresenter(this);
}

ArticlePresenter.prototype.start = function() {
    console.log('start');
    this.getArticle(this.articleId);
};

ArticlePresenter.prototype.getArticle = function(articleId) {
    console.log('getArticle:', articleId);
    this.view.showArticle();
};

ArticlePresenter.prototype.addComment = function(message) {

};
