function MainView(document) {
    this.presenter = null;

    $('#button-write-article').click('on', function() {
        var modalWriteArticle = $('#modal-write-article')
        modalWriteArticle.modal('open');

        $('#modal-publish-article').click(function() {
            var articleTitle = $('#modal-article-title').val();
            var articleContent = $('#modal-article-content').val();

            console.log(articleTitle, articleContent);
            this.presenter.addArticle(articleTitle, articleContent);

            modalWriteArticle.modal('close');
        }.bind(this));
    }.bind(this))

    $('.modal').modal();
}

MainView.prototype.setPresenter = function(presenter) {
    this.presenter = presenter;
};

MainView.prototype.showArticles = function(articles) {
    console.log('showArticles:', articles);

    $.get('views/listArticlesView.mustache', function(view) {
	var renderedView = Mustache.render(view, {articles: articles});

	$('#content-container-main').html(renderedView);

	this.progressBar = $('#progress-bar');

    }.bind(this));
}
