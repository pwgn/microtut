function MainPresenter(apiClient, view) {

    this.apiClient = apiClient;
    this.view = view;
    this.view.setPresenter(this);
}

MainPresenter.prototype.start = function() {
    this.listArticles();
};

MainPresenter.prototype.listArticles = function() {
    this.apiClient.listArticles(
        function(result) {
            this.view.showArticles(result['articles']);
        }.bind(this),
        function(error) {
            console.log(error);
        });
};

MainPresenter.prototype.addArticle = function(title, content) {
    this.apiClient.addArticle(
        title, content,
        function(result) {
            this.view.appendArticle(result);
        }.bind(this),
        function(error) {
            console.log(error);
        }
    );
};
