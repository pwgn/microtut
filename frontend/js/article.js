
function getId(subString) {
    var keyValues = subString.split('?');
    return keyValues[0].split('=')[1];
};

(function() {

    var articleId = getId(window.location.search.substring(1));

    var apiClient = new MicroApi();

    var articleView = new ArticleView(document);
    var articlePresenter = new ArticlePresenter(articleId, apiClient, articleView);
    articlePresenter.start();

})();
