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
            console.log('listArticles result:', result);
            this.view.showArticles(result['articles']);
        }.bind(this),
        function(error) {
            console.log('listArticles error:', error);
            console.log(error);
        });
};

MainPresenter.prototype.addArticle = function(title, content) {
    this.apiClient.addArticle(
        title, content,
        function(result) {
            console.log('addArticle result:', result);
            this.view.appendArticle(result);
        }.bind(this),
        function(error) {
            console.log('addArticle error:', error);
            console.log(error);
        }
    );
};
