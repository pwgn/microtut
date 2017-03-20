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
    $.get('views/commentCardView.mustache', function(view) {
	var renderedView = Mustache.render(view, comment);
	$('#comments').append(renderedView);
    }.bind(this));
};

ArticleView.prototype._setupButtonListeners = function() {
    $('#button-send-comment').click(function() {
        var inputField = $('#input-field-new-comment');
        var message = inputField.val();
        inputField.val("");
        this.presenter.addComment(message);
    }.bind(this));
};
