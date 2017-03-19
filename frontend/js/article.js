
(function() {

    var apiClient = new MicroApi();

    var articleView = new ArticleView(document);
    var articlePresenter = new ArticlePresenter(apiClient, articleView);
    articlePresenter.start();

})();
