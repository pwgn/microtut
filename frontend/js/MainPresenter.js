function MainPresenter(apiClient, view) {

    this.apiClient = apiClient;
    this.view = view;
    this.view.setPresenter(this);
}

MainPresenter.prototype.start = function() {
    console.log('start');
    this.listArticles();
};

MainPresenter.prototype.listArticles = function() {
    this.apiClient.listArticles(
        function(result) {
            console.log(result);
        },
        function(error) {
            console.log(error);
        });
}
