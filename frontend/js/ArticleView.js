function ArticleView(document) {
    this.presenter = null;
}

ArticleView.prototype.setPresenter = function(presenter) {
    this.presenter = presenter;
};

ArticleView.prototype.showArticle = function(article) {
    console.log('showArticle:', article);
    $.get('views/articleView.mustache', function(view) {
	var renderedView = Mustache.render(view, article);

	$('#content-container-main').html(renderedView);
    }.bind(this));
};

ArticleView.prototype.appendComment = function(article) {

};
