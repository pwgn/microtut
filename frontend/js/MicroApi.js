DEFAULT_HOST = '127.0.0.1';
DEFAULT_PORT = '6101'

function MicroApi(host, port) {

    this.host = host || DEFAULT_HOST;
    this.port = port || DEFAULT_PORT;
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

MicroApi.prototype.getArticle = function(articleId, successCallback, errorCallback) {
    var endpoint = this.url + '/web/api/articles/' + articleId;
    $.ajax({
        url: endpoint,
        type: 'GET',
        success: successCallback,
        error: errorCallback
    });
};

MicroApi.prototype.addArticle = function(title, content,
                                         successCallback, errorCallback) {
    var data = {
        title: title,
        content: content
    };

    var endpoint = this.url + '/api/articles';
    $.ajax({
        url: endpoint,
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(data),
        success: successCallback,
        error: errorCallback
    });

};

MicroApi.prototype.addComment = function(articleId, message,
                                         successCallback, errorCallback) {
    var data = {
        message: message
    };

    var endpoint = this.url + '/api/comments/' + articleId;
    $.ajax({
        url: endpoint,
        type: 'PUT',
        contentType: 'application/json',
        data: JSON.stringify(data),
        success: successCallback,
        error: errorCallback
    });
};
