function MainView(document) {
    this.presenter = null;

    this.loadViewContentMainView();
}

MainView.prototype.loadViewContentMainView = function() {

    $.get('views/contentMainView.mustache', function(view) {

	var renderedView = Mustache.render(view, {});

	$('#content-container-main').html(renderedView);

	this.progressBar = $('#progress-bar');

    }.bind(this));

};

MainView.prototype.setPresenter = function(presenter) {
    this.presenter = presenter;
};
