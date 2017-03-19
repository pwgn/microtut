function ArticlePresenter(apiClient, view) {

    this.apiClient = apiClient;
    this.view = view;
    this.view.setPresenter(this);
}

ArticlePresenter.prototype.start = function() {
    console.log('start');
    this.getArticle();
};

ArticlePresenter.prototype.getArticle = function(articleId) {
    this.view.showArticle();
};

ArticlePresenter.prototype.addComment = function(message) {

};
