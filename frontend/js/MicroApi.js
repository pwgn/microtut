DEFAULT_HOST = '127.0.0.1';
DEFAULT_PORT = '6101'

function MicroApi(host, port) {

    this.host = host | DEFAULT_HOST;
    this.port = port | DEFAULT_PORT;

    this.url = 'http://' + this.host + ':' + this.port;

}

MicroApi.prototype.listArticles = function(successCallback, errorCallback) {
    var endpoint = this.url + '/api/articles';
    $.ajax({
        url: endpoint,
        type: 'GET',
        success: successCallback,
        error: errorCallback
    });
};

MicroApi.prototype.getArticle = function(articleId) {

};

MicroApi.prototype.addArticle = function(title, content) {

};

MicroApi.prototype.addComment = function(articleId, message) {

};
