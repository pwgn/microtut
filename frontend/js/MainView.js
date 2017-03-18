function MainView(document) {
    this.presenter = null;

    $('#button-write-article').click('on', function() {
        $('#modal-write-article').modal('open');
    }.bind(this))

    $('.modal').modal();
}

MainView.prototype.setPresenter = function(presenter) {
    this.presenter = presenter;
};

MainView.prototype.showArticles = function(articles) {
    $.get('views/listArticlesView.mustache', function(view) {

	var renderedView = Mustache.render(view, {articles: [{title: 'hello'}]});

	$('#content-container-main').html(renderedView);

	this.progressBar = $('#progress-bar');

    }.bind(this));
}
