function MainView(document) {
    this.presenter = null;

    $('#button-write-article').click('on', function() {
        var modalWriteArticle = $('#modal-write-article')
        modalWriteArticle.modal('open');

        $('#modal-publish-article').click(function() {
            var inputFieldTitle = $('#modal-article-title');
            var inputFieldContent = $('#modal-article-content');
            var articleTitle = inputFieldTitle.val();
            var articleContent = inputFieldContent.val();

            inputFieldTitle.val('');
            inputFieldContent.val('');


            console.log('publishArticle:', articleTitle, articleContent);
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
    }.bind(this));
};

MainView.prototype.appendArticle = function(article) {
    console.log('appendArticle:', article);
    var content = '<a href="/article.html?id=' + article['id'] + '" class="collection-item">' + article['title'] + '</a>'
    $("#articles-container .collection").append(content);
};
