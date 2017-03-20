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

        this._setupButtonListeners();
    }.bind(this));
};

ArticleView.prototype.appendComment = function(comment) {
    console.log('appendComment:', comment);
};

ArticleView.prototype._setupButtonListeners = function() {
    $('#button-send-comment').click(function() {
        var message = $('#input-field-new-comment').val();
        this.presenter.addComment(message);
    }.bind(this));
};
